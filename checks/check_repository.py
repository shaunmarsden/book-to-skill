"""Offline documentation checks. These do not evaluate model behaviour."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


FORBIDDEN = set("\u2013\u2014\u2018\u2019\u201c\u201d")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for name, value in attrs
                         if name in ("href", "src") and value)


def links(text):
    """Handle the inline Markdown and HTML link forms used in this repo."""
    parser = Links()
    parser.feed(text)
    return re.findall(r"\]\(([^\s)]+)\)", text) + parser.urls


def anchors(text):
    seen = {}
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug if not count else f"{slug}-{count}")
    return result


def check(root, names):
    root = Path(root).resolve()
    errors = []
    markdown = relative = svg = 0
    for name in sorted(names):
        path = root / name
        if path.suffix == ".svg":
            svg += 1
            try:
                ET.parse(path)
            except (ET.ParseError, OSError) as error:
                errors.append(f"{name}: invalid SVG XML: {error}")
        if path.suffix != ".md":
            continue
        markdown += 1
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), 1):
            if FORBIDDEN.intersection(line):
                errors.append(f"{name}:{number}: non-ASCII dash or smart quote")
        for url in links(text):
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            relative += 1
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not target.is_relative_to(root):
                errors.append(f"{name}: link escapes repository: {url}")
            elif not target.exists():
                errors.append(f"{name}: missing relative link: {url}")
            elif parts.fragment and target.is_file() and target.suffix == ".md":
                if unquote(parts.fragment) not in anchors(target.read_text(encoding="utf-8")):
                    errors.append(f"{name}: missing heading anchor: {url}")
    return errors, (markdown, relative, svg)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    names = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=args.root
    ).decode("utf-8").strip("\0").split("\0")
    errors, (markdown, relative, svg) = check(args.root, filter(None, names))
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {markdown} Markdown files, {relative} relative links and {svg} SVG files.")
    print(f"Errors: {len(errors)}. External links and model behaviour were not tested.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
