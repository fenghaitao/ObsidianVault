---
title: "Monty"
type: entity
tags: [python, interpreter, sandbox, code-execution, rust, pydantic]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260507 - Samuel Colvin - Controlling the wild： from tool calling to computer use - PyAI London at AIE 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260325 - Armin Ronacher Leaning In To Find Out - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Monty is a minimal secure Python interpreter written from scratch in Rust, designed specifically for running code written by AI agents. Created by Samuel Colvin at Pydantic. It sits between simple tool calling and full sandbox VMs on the control-capability spectrum.

## Key Information

### Architecture

- Built entirely from scratch in Rust — not a CPython fork
- Uses Astral's Ruff AST parser for parsing Python source
- No file system access, no environment variables, no networking, no third-party packages by default
- White-list approach: start with nothing, add capabilities explicitly
- "Python is the truth. We speak nothing but the truth, but we are not claiming to speak the whole truth"

### Key Features

- **Callback system**: external functions suspend execution and return to host like tool calling; host controls what gets called and what values are returned
- **Runtime snapshotting**: serialize entire interpreter state to binary for durable execution — store in database, resume later
- **~1 microsecond startup latency** vs ~1 second for sandbox VMs (6 orders of magnitude faster)
- **Built-in TY type checker** from Astral with custom type stubs to enforce what code can/can't do
- **REPL mode**: LLMs are strongly trained to expect stateful REPL behavior; Monty supports this natively
- **Cross-platform**: runs anywhere Rust runs; SDKs exist for Python, JavaScript, Dart, Go, Kotlin

### Limitations

- Small subset of Python — no classes (as of mid-2026), limited stdlib, no third-party packages
- Not designed to run existing Python code — designed for AI-generated code specifically
- Anthropic Opus/Sonnet 4.6 perform poorly at REPL coding; 4.5 models work better

### Use Cases

- Data analysis with external functions (DuckDB, Matplotlib via callbacks)
- Safe code execution in production agent workflows
- Enterprise environments where external sandbox services aren't viable
- Constrained environments (e.g., in-vehicle agents)

## Related

- [[SamuelColvin]] — creator
- [[Pydantic]] — parent company
- [[CodeExecution]] — the paradigm
- [[Sandboxing]] — the security approach
- [[ArminRonacher]] — referenced Monty in his talk
