---
title: "summary-20260507 - Samuel Colvin - Controlling the wild： from tool calling to computer use - PyAI London at AIE 2026"
type: source
tags: [source, pydantic, pyai-london, monty, code-execution]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260507 - Samuel Colvin - Controlling the wild： from tool calling to computer use - PyAI London at AIE 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Samuel Colvin's PyAI London talk on Monty, largely overlapping with his PyAI Conf 2026 talk. Covers the continuum from tool calling to full computer use, Monty's architecture as a from-scratch secure Python interpreter in Rust, the callback system for external functions, snapshotting for durable execution, and the REPL mode needed because LLMs are trained to expect stateful code execution. Additional detail on the "Python is the truth, but not the whole truth" design philosophy.

## Key Points

- Monty is not a CPython alternative — it's a deliberately limited subset for AI-written code
- Golden rule: "Python is the truth. We speak nothing but the truth, but we are not claiming to speak the whole truth"
- White-list approach: start with nothing, add capabilities — safer than blacklisting from a full VM
- External function callbacks enable DuckDB queries, Matplotlib plotting, and any host functionality
- REPL mode essential: LLMs assume variables and functions persist across executions
- Monty built largely with AI assistance — would not have been possible without leading models
- Other projects in the space: Just Bash (Vercel), BashKit, QuickJS — all share the from-scratch philosophy
- Goal: reach confidence level where Monty is no longer "experimental" and can be trusted for untrusted code

## Related

- [[Monty]] — the secure Python interpreter
- [[SamuelColvin]] — creator
- [[CodeExecution]] — the paradigm
- [[Sandboxing]] — the security approach
