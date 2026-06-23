---
title: "The Expanding Toolkit"
type: source
tags: [tool-use, context-management, code-execution, computer-use, model-capabilities]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/19 - The expanding toolkit.md]
last_updated: 2026-06-23
---

## Core Summary

Lucas from Anthropic's research team presents the thesis that scaffolding previously built around models now ships with the model itself. The talk covers four capability areas with before/after comparisons: tool use (routers and retries now handled by the model), context management (1M context window + server-side compaction replaces RAG and chunking), code execution (server-side sandbox eliminates VM management), and computer use (native 1440p resolution eliminates scaling math). A demo shows Claude Code using the Claude in Chrome extension to test a project management dashboard, reproduce bugs, fix code, and verify fixes — closing the loop between development and QA. The core rule: code compensating for model unreliability has a half-life of months; code connecting the model to your world compounds.

## Key Points

- **Tool use evolution:** Tool routers (string matching, heuristics) are now worse than letting Claude search and select tools itself. Claude recovers from tool errors autonomously.
- **Tool tip:** Include output schema in tool descriptions so Claude knows what to expect, saving round trips.
- **Context management evolution:** 1M context at flat pricing + server-side compaction + context editing replaces RAG, chunking, and manual cache breakpoints.
- **Context tip:** Clear stale tool results (screenshots, search results, file reads) every N turns while keeping the decisions they informed.
- **Code execution evolution:** Server-side sandbox replaces VM provisioning, code transfer, traceback parsing, and retry loops — all in a single API turn.
- **Code execution mental model:** Claude gets its own computer (stateless compute, data analysis, custom libraries) separate from local bash (repo, Python env).
- **Computer use evolution:** Native 1440p resolution eliminates scaling math. OS World score improved from <50% to 78% in under 12 months.
- **Computer use tip:** Test different resolutions and image formats (JPEG, PNG, WebP) for your specific UI automation use case.
- **Claude in Chrome extension:** Claude Code can leverage the user's Chrome browser session for testing and debugging web apps directly.
- **Demo:** Claude reproduced a card creation bug, fixed the code, then discovered and fixed a drag-and-drop bug — all autonomously through browser interaction.
- **Core rule:** Code compensating for model unreliability has a half-life of months (leave to Anthropic). Code connecting model to your world compounds (your competitive advantage).

## Related

- [[ClaudeCode]] — the tool used in the demo
- [[ClaudeFable5]] — Opus 4.7 enabling native resolution computer use
- [[ContextWindow]] — context management techniques
- [[ModelContextProtocol]] — tool integration standard
