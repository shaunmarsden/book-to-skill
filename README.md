# Book to Skill

<p>
  <img alt="Status: Working tool" src="https://img.shields.io/badge/status-working%20tool-2563eb">
  <a href="LICENSE"><img alt="Licence: MIT" src="https://img.shields.io/badge/licence-MIT-lightgrey"></a>
</p>

Turn a book you already own into a Claude skill: a short index plus one file per chapter. An AI assistant can then look things up chapter by chapter instead of holding the whole book in context every time. It also works for a training course or an internal policy document.

## Why

Loading a whole 400-page book can cost hundreds of thousands of tokens before you've asked a single question. Most of them go unused, since any one answer usually needs only a chapter or two. This tool sets a book out the way any other AI skill is set out: a short file that always loads, and deeper material that opens only when a step needs it.

[![A source book, course or policy becoming structured skill files.](assets/diagrams/10-book-to-skill.svg)](SKILL.md)

**Not what you need?** This turns a book, course or policy document you already have into skill files, chapter by chapter. If you have a different task you repeat and want a skill with clear limits built from a plain description, you probably want [Skill Author](https://github.com/shaunmarsden/skill-author).

## Use It

Copy [SKILL.md](SKILL.md) and paste it into your AI tool (ChatGPT, Claude, Gemini or similar). Then paste in the book's text, a chapter at a time for a long book. It builds:

- an index file with the book's argument in one paragraph, a chapter list, and where to find the glossary and techniques document, short enough to load every time
- one file per chapter, setting out its ideas and techniques rather than copying the original prose
- a techniques and patterns document listing every named method in the book, with the chapter it came from
- a glossary of terms the book uses in its own way

<details>
<summary><strong>See exactly what it produces</strong></summary>

1. A short index file: the book's argument in one paragraph, a chapter list, and pointers to the glossary and techniques document
2. One structured file per chapter, with ideas and techniques rather than a copy of the prose
3. A techniques and patterns document and a glossary, each built once and reused across chapters
4. For a policy or course, any contradiction between sections flagged in the index, not quietly resolved

</details>

You don't need to install anything, set up a project or write code to try it once. If you use the same book often, a Claude Project, a Custom GPT or a Gemini Gem is easiest, because you can attach the files once and reuse them.

[The worked example](example/) shows what it produces: three chapters of *The Art of War*, which I chose because it's old enough to be public domain everywhere.

[The second worked example](example-two/) shows the one real difference when the source is a policy rather than a book. A policy can contradict itself between sections in a way a book rarely does, and the index needs to flag that rather than quietly pick a side.

Go through [the review checklist](checks/checklist.md) before you rely on the files it builds.

## Before You Use It

Only use a book you have the legal right to read: one you bought, borrowed properly, or that's in the public domain. The output is for your own private use. Don't publish, sell or share the chapter files, the techniques document or the glossary.

The tool itself, [SKILL.md](SKILL.md), never contains, ships or needs any book content. You supply that from a copy you have the right to read, and the output stays with you. The one exception is the worked example folder, which uses a public-domain text on purpose so the demonstration carries no copyright risk.

## Licence

MIT. Use, adapt or share the tool freely. It never contains anyone's copyrighted book content, only the method for structuring your own.

## Feedback

Tried it on a real book? [Start a discussion](https://github.com/shaunmarsden/book-to-skill/discussions) if something didn't work as you expected, or if the output could be better.

## Part of a Family

This was the first of a growing set of free tools. The rest take [practical-ai-sales-workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows) patterns beyond sales. See [sibling-projects](https://github.com/shaunmarsden/sibling-projects) for the list, or use [the router](https://github.com/shaunmarsden/sibling-projects/blob/main/ROUTER.md) if you're not sure which one fits.
