---
title: "summary-20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, monty, code-execution, sandboxing]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Samuel Colvin introduces Monty, Pydantic's minimal secure Python interpreter written from scratch in Rust for running AI-generated code. Monty sits between tool calling and full sandbox VMs on the control-capability spectrum. Built from scratch (not a CPython fork), it has no file system, network, or environment variable access by default. Uses a callback system where external functions are exposed as tool-like calls. Supports snapshotting the entire runtime for durable execution. Includes Astral's TY type checker built-in.

## Key Points

- Monty is a from-scratch Python interpreter in Rust, not a CPython fork — no `open()`, `socket()`, or env var access exists in the codebase
- Callback system: external functions suspend execution and return to host like tool calling; host controls what gets called
- Runtime snapshotting: serialize the entire interpreter state to a database for durable execution across hours/days
- ~1 microsecond startup latency vs ~1 second for sandbox VMs (6 orders of magnitude faster)
- Built-in TY type checker with custom type stubs to enforce what code can/can't do at type-check time
- REPL mode: LLMs are strongly trained to expect REPL behavior (variables persist across executions)
- Monty is a small subset of Python — no classes (yet), limited stdlib, no third-party packages; designed for AI-written code, not porting existing apps
- Demo: investigating a PydanticAI download spike using DuckDB queries and Matplotlib plots via external functions
- Anthropic Opus/Sonnet 4.6 perform poorly at REPL coding; 4.5 models work better — possible overtraining on specific code execution environments

## Related

- [[Monty]] — the secure Python interpreter
- [[SamuelColvin]] — creator
- [[PydanticAI]] — agent framework Monty integrates with
- [[CodeExecution]] — the paradigm Monty enables
- [[Sandboxing]] — the security approach
