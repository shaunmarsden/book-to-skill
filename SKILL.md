---
name: book-to-skill
description: Turn a book you already own into a structured Claude skill, a short index plus one file per chapter, loaded only when needed, instead of holding the whole book in context at once. Use when you want an AI assistant to consult a specific book repeatedly without paying the token cost of the whole book every time. Do not use this to reproduce or share a book's content publicly; the output is for your own private use, built from a copy you already have the right to read.
---

# Turn a Book Into a Skill

You do not need to install anything to try this once: copy this whole file, paste it as your first message in any AI chat tool, then paste in the book's text, a chapter at a time works best for a long book.

A full book loaded into context costs tokens whether or not a given answer actually needs it. This restructures a book the same way any other AI skill is structured: a short index that loads every time, and separate per-chapter files that only open when a specific question actually needs that chapter.

## Before You Start

- Only use a book you have the legal right to read: one you bought, borrowed properly, or that is in the public domain.
- This output is for your own private use. Do not publish, resell, or redistribute the chapter files, the techniques document, or the glossary; that would be redistributing someone else's copyrighted work, not a tool.
- Work from your own copy's text, not a pirated or scraped source.

## Gather the Inputs

- The book's title, author, and table of contents, if available
- The text of each chapter, pasted in one at a time for a long book, or the whole book at once for a short one
- What you actually want to use the book for, so the index highlights what matters most to you rather than everything equally

## Build the Structure

### 1. The Index File

One short file that stays loaded every time: the book's title and author, a one-paragraph summary of what it actually argues or teaches, a chapter list with a one-line description of each, and where the glossary and techniques document live. Keep this under roughly 100 lines; it is the only file that loads on every use, so it must earn its place.

### 2. One File Per Chapter

For each chapter, a separate file containing the chapter's actual content structured as concepts, techniques, patterns, or arguments, not a copy of the original prose. Use a few direct short quotations only where the original wording genuinely matters and cannot be paraphrased without losing meaning. End with a one-line note on where this chapter sits in the book's overall argument.

### 3. The Techniques and Patterns Document

One document, separate from the chapter files, listing every named technique, pattern, framework, or step-by-step method the book describes, with the chapter it came from, so a specific method can be found without opening every chapter file to look for it.

### 4. The Glossary

One file defining every term the book uses in a specific or non-obvious way, so a later question can check a definition without reloading a whole chapter.

## Apply the Guardrails

- Paraphrase and structure the book's ideas; do not reproduce long passages of the original text
- Never treat this output as something to share, publish, or sell; it is a private reading aid built from a book you already have the right to read
- If a chapter's actual content is thin or repetitive, say so rather than padding the file to look complete
- Keep the index short; if it is creeping past 100 lines, move detail into a chapter file instead

## Stop When the Task Is Unsafe

Do not produce this output when:

- The book's text was not provided by someone with the right to read it
- The stated purpose is to publish, sell, or otherwise redistribute the resulting files
- The request is to reproduce the book's text word for word rather than structure its ideas

## Require Human Review

Skim each chapter file once against the original before relying on it for something that matters. A structuring pass can still misread emphasis or drop a qualifier the original chapter actually included.
