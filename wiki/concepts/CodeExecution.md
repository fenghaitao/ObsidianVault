---
title: "CodeExecution"
type: concept
tags: [agents, code-execution, sandboxing, security]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260325 - Armin Ronacher Leaning In To Find Out - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Code execution is the paradigm of giving AI agents the ability to write and run code as their primary mode of interacting with the world, rather than calling individual tools. Also called "code mode" (Cloudflare) or "programmatic tool calling" (Anthropic). It sits between simple tool calling and full computer use on the control-capability spectrum.

## Key Information

### Why It Works

- LLMs are strongly trained on code — coding sessions dominate RL training data because they produce measurable reward signals (tests pass, code committed)
- Code is a general-purpose expression medium: agents can accomplish non-coding tasks (data analysis, presentations, research) by writing code
- A single "run code" tool replaces dozens of individual tools, reducing context overhead
- REPL-style execution (stateful, iterative) matches how models were trained

### The Spectrum

Samuel Colvin's continuum from control to capability:
1. **Tool calling** — LLM returns JSON with function name and arguments (most controlled, least capable)
2. **Monty** — minimal secure interpreter, white-list capabilities
3. **Sandboxing services** — full VMs with restrictions (Daytona, E2B, Modal)
4. **Coding agents** — Claude Code, Codex, Copilot (less controlled, more capable)
5. **Full computer use** — unrestricted access (most capable, least controlled)

### Security Considerations

- Running code on the host is dangerous — agents can access everything
- Sandboxing services are expensive at scale and problematic for enterprises
- From-scratch interpreters (Monty, QuickJS) offer a middle ground: start with nothing, add capabilities
- White-list approach is safer than blacklisting from a full VM

## Related

- [[Monty]] — Pydantic's secure Python interpreter
- [[Sandboxing]] — the security approach
- [[ToolUse]] — the simpler alternative
- [[CodingAgents]] — the broader agent category
- [[ArminRonacher]] — analyzed why code execution works
- [[SamuelColvin]] — built Monty for this paradigm
