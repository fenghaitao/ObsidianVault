---
name: query
description: Answer questions by searching the local wiki knowledge base. Triggered by /query <question>, or natural-language questions about "my notes", "my knowledge base", "what do I know about X", "what did I record about Y". Always reads wiki/index.md first to locate relevant pages, then deep-reads them, then answers with [[wikilink]] citations. Forbidden from answering purely from model memory when wiki content exists. If the wiki has no relevant content, must explicitly state "no local match — answering from general knowledge".
user-invocable: true
---

# query skill

## Goal

Turn the user's question into a deep search of the local wiki. Surface the relevant material, synthesize an answer with explicit `[[wikilink]]` citations, and — when the answer is high-value — offer to save it back to the wiki as a synthesis page.

## Trigger scenarios

- `/query <question>`
- Natural-language: "what do my notes say about X", "what did I conclude about Y", "find Z in my wiki", "search my knowledge base for…"
- Mentions of "wiki", "knowledge base", "my notes", "my records" in question form.

## Fallback policy

If the question is purely general knowledge (e.g. "how many planets in the solar system") and `wiki/index.md` has no relevant page, respond:

> No local match in the wiki — answering from general knowledge: [direct answer]

This makes the source of every answer explicit.

---

## Search & synthesis pipeline

### Step 1: Read the global index

**Always the first action.** Read `wiki/index.md` in full.

In the index, locate any pages relevant to the question across:
- Sources
- Entities
- Concepts
- Syntheses

Build a candidate list. Don't skip the index — it's the cheap, structured filter that prevents you from reading irrelevant pages.

### Step 2: Deep-read the candidates

For each candidate page from Step 1, read the full content. Pay attention to:
- The page body (definitions, key information).
- The frontmatter `sources` field — this lists the original `raw/` files, which you may also read if the wiki page summary isn't enough.
- The `## Related` section — follow links to adjacent pages if they're relevant.
- Any `## Knowledge Conflicts` section — surface these in your answer when relevant.

### Step 3: Synthesize the answer

Compose a clear answer. Format depends on the question:
- Factual lookup → direct answer + citation.
- Comparison → table or side-by-side analysis.
- Historical/decision question → chronological narrative.
- Open-ended exploration → structured analysis with sub-sections.

**Citation format:**
- Inline: when referencing a wiki page, use `[[Page Name]]` in the prose. The first mention of a page in a paragraph cites it; don't litter every sentence.
- Direct quotation: use markdown blockquote `> quoted text` followed by `— [[Page Name]]`.
- Multiple-page synthesis: cite at the end of the section: `Sources: [[PageA]], [[PageB]], [[PageC]]`.

If two wiki pages contradict each other, **call out the contradiction explicitly** rather than picking one arbitrarily. This is a feature, not a bug — it's how the user discovers gaps in their own knowledge.

### Step 4: Offer to save high-value answers

**Default behavior: `/query` answers the question and stops. Saving a synthesis is opt-in and ALWAYS requires an explicit, per-synthesis "yes" from the user.** Do not save unless the user clearly confirms *for that specific synthesis*. A general "run these queries" is not save-approval — answer first, then ask.

If the answer meets any of these criteria:
- More than 2 substantive paragraphs.
- Comparative or analytical (not just lookup).
- Synthesizes information from 3+ wiki pages.

…ask the user (once per candidate synthesis, naming it):

> This answer is a substantive synthesis. Would you like me to save it to `wiki/syntheses/` as a permanent wiki page? (It becomes part of the knowledge base, not just a one-off answer.)

If — and only if — they agree, create `wiki/syntheses/{slug}.md` (kebab-case slug derived from the question or topic):

```markdown
---
title: "{slug}"
type: synthesis
tags: [analysis, comparison, etc.]
sources: [raw/path/file.md, ...]   # raw files referenced via the wiki pages used
last_updated: YYYY-MM-DD
---

# {Question or Topic}

[Full synthesis content, with the same [[wikilink]] citations as the answer.]

## Related

- [[PageA]] — primary source for X
- [[PageB]] — primary source for Y
```

### Step 4b: Close the backlink loop (REQUIRED when saving)

A synthesis that nothing links *to* is an orphan — `/lint` will flag it, and `/query` will rarely rediscover it (queries navigate by following links from the index and hub pages). **After saving a synthesis, add a backlink to it from the `## Related` section of the 1–3 most central pages it draws from.** Example: a synthesis on RAG strategy gets a backlink from `[[RetrievalAugmentedGeneration]]`'s Related section. This is what makes the wiki compound — without it, syntheses are write-only dead ends.

Then update `wiki/index.md` under the `## Syntheses` section.

### Step 5: Log the operation

After every query (saved or not), append to `wiki/log.md`:

```markdown
## [YYYY-MM-DD] query | <one-line summary of the question>
- **Output**: saved to [[synthesis-slug]] (or: "answered inline; not saved")
- **Pages consulted**: [[PageA]], [[PageB]], [[PageC]]
```

---

## Hard rules

- **Always read `wiki/index.md` first.** Don't guess which pages exist.
- **Default to answer-only.** `/query` is a Q&A tool first. Saving a synthesis is a separate, explicit opt-in — never save without a per-synthesis "yes" (see Step 4). A batch instruction like "run these queries" authorizes *answering*, not *saving*.
- **When you do save, close the backlink loop** (Step 4b) so the synthesis isn't born an orphan.
- **Don't answer from model memory** if relevant wiki content exists. The user built this wiki precisely to anchor answers to their own curated material.
- **Cite every claim** with `[[wikilink]]` to the source page.
- **Don't over-cite.** Once per paragraph for the same page is enough.
- **Don't silently fabricate.** If a wiki page doesn't say what you want it to say, don't paraphrase it as if it did. Either say "the wiki doesn't directly address this" or read more pages.
- **Surface contradictions** — don't smooth them over.
- **Use the real current date** for any `last_updated` field and log entry — read it from the injected current-date context or run `date +%F`. Never copy the `YYYY-MM-DD` placeholder literally.

## Related

- [[wiki/index.md]] — global index entry point
- [[wiki/log.md]] — operation log
- [[CLAUDE.md]] — wiki schema and rules
