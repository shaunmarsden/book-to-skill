# Book to Skill

<p>
  <img alt="Status: Illustrative examples" src="https://img.shields.io/badge/status-illustrative%20examples-2563eb">
  <a href="LICENSE"><img alt="Licence: MIT" src="https://img.shields.io/badge/licence-MIT-lightgrey"></a>
</p>

Turn source text into reference files for an AI assistant: a short index plus one file per chapter or section. The instructions cover books, training courses and internal policies. Use only material you have permission to process this way.

## Why

Loading a whole book puts text into the AI's working context that a particular question may not need. These instructions ask for a short index and separate chapter files, so relevant material can be supplied on its own.

Creating files does not make an AI load them selectively. That depends on the tool and how you supply the files. In an ordinary chat, you can provide the index and then the relevant chapter yourself. This repository has no measured token-saving result or logged model test; the examples show the intended format, not verified performance.

[![A source book, course or policy becoming structured skill files.](assets/diagrams/10-book-to-skill.svg)](SKILL.md)

**Not what you need?** This turns a book, course or policy document you already have into skill files, chapter by chapter. If you have a different task you repeat and want a skill with clear limits built from a plain description, you probably want [Skill Author](https://github.com/shaunmarsden/skill-author).

## Use It

Copy [SKILL.md](SKILL.md) and paste it into any AI chat. Then paste in source text you have permission to use, a chapter at a time for a long book. The instructions ask for:

- an index file with the book's argument in one paragraph, a chapter list, and where to find the glossary and techniques document, short enough to load every time
- one file per chapter, setting out its ideas and techniques rather than copying the original prose
- a techniques and patterns document listing every named method in the book, with the chapter it came from
- a glossary of terms the book uses in its own way

<details>
<summary><strong>See the requested file structure</strong></summary>

1. A short index file: the book's argument in one paragraph, a chapter list, and pointers to the glossary and techniques document
2. One structured file per chapter, with ideas and techniques rather than a copy of the prose
3. A techniques and patterns document and a glossary, each built once and reused across chapters
4. For a policy or course, any contradiction between sections flagged in the index, not quietly resolved

</details>

You don't need to install anything, set up a project or write code to try it once. For repeated use, a tool that supports saved reference files may help. Uploading files alone does not guarantee that only the relevant chapter enters the AI's working context. Compatibility has not been logged for individual AI tools here.

[The book example](example/) shows the intended structure using ideas from three chapters of *The Art of War*. It is an illustration, not a logged test. The repository does not identify a source edition or translation, so it does not establish rights or source fidelity for a particular edition.

[The policy example](example-two/) shows an index recording a later update that explicitly replaces an earlier rule for eligible roles only. It illustrates a scoped update, not a test of how the AI handles an unresolved contradiction. Books, courses and policies can all contain conflicting information.

Go through [the review checklist](checks/checklist.md) before you rely on the files it builds.

## Before You Use It

Owning or borrowing a copy does not establish permission for every use of its contents. Check that you may process the source in your chosen AI tool. For work material, check your organisation's approval and confidentiality rules too. The output is for your own private use. Don't publish, sell or share the chapter files, the techniques document or the glossary. [UK copyright guidance](https://www.gov.uk/using-somebody-elses-intellectual-property/copyright) explains permissions and exceptions; this tool does not determine which apply to your source.

The instruction file, [SKILL.md](SKILL.md), contains no book text. Running it requires source text that you supply. Pasting or uploading that text sends it to your chosen AI service, subject to that service's data policies. This repository does not provide a private processing environment or verify the rights to a source or translation.

## Licence

MIT. Use, adapt or share the tool freely. This licence does not grant rights to books, courses or policies you supply.

## Feedback

Tried it on a real book? [Start a discussion](https://github.com/shaunmarsden/book-to-skill/discussions) if something didn't work as you expected, or if the output could be better.

## Part of a Family

This was the first of a growing set of free tools. The rest take [practical-ai-sales-workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows) patterns beyond sales. See [sibling-projects](https://github.com/shaunmarsden/sibling-projects) for the list, or use [the router](https://github.com/shaunmarsden/sibling-projects/blob/main/ROUTER.md) if you're not sure which one fits.
