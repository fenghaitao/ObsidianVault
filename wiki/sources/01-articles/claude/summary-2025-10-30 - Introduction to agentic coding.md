---
title: "summary-2025-10-30 - Introduction to agentic coding"
type: source
tags: [source, agentic-coding, claude-code, rakuten]
sources: ["raw/01-articles/claude/2025-10-30 - Introduction to agentic coding.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic defines agentic coding by contrasting three generations of AI coding assistance: IDE autocomplete (predicts the next fragment from visible context), conversational tools like [[Claude.ai]] (chat-based guidance on pasted snippets, but manual orchestration across files), and agentic systems like [[ClaudeCode]] (read entire codebases, plan multi-step approaches, execute changes across files, run tests, and iterate until a goal is met). [[Rakuten]] is cited implementing a full activation-vector extraction method in the 12.5M-line vLLM codebase in seven hours of autonomous work.

## Key Points

- **Autocomplete tools**: limited to the current file or a few nearby files; good for boilerplate and established patterns, but can't trace cross-service data flow.
- **Conversational tools** ([[Claude.ai]]): good for analysis and guidance (optimization suggestions, trade-off analysis, troubleshooting) via iterative back-and-forth, but orchestrating multi-file changes remains manual — copy each file in, track needed updates, copy results back.
- **Agentic systems** ([[ClaudeCode]]): operate at the project level — read config/test files to understand setup and conventions, trace imports to map dependencies, form an adaptive plan, then implement across multiple files (route handlers, middleware, schemas, docs, tests) while requesting approval by default before modifying files. Transforms the workflow from "write code, run tests, read errors, fix code, repeat" into "define goal, review proposed changes, approve implementation."
- [[Rakuten]]'s engineering team had Claude Code implement a specific activation-vector extraction method in vLLM (12.5M lines, Python/C++/CUDA) in seven hours of sustained autonomous work with only occasional guidance, achieving 99.9% numerical accuracy versus the reference method. Quote from Yusuke Kaji (GM of AI for Business): "You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."

## Related

- [[AgenticCoding]] — the concept this article defines by contrast with autocomplete and conversational tools
- [[ClaudeCode]] — the agentic coding tool profiled
- [[Claude.ai]] — the conversational-tier tool contrasted with agentic coding
- [[Rakuten]] — customer example cited
