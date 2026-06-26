---
title: "ToolsVsBashVsCodeGen"
type: concept
tags: [agents, tools, bash, code-generation, design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
Tools vs. bash vs. code generation is the three-way taxonomy of action modalities available to agents in the Claude Agent SDK. Each has distinct trade-offs in structure, composability, context usage, latency, and reliability.

## Key Information
- **Tools**: Extremely structured and reliable. Fastest output, minimal errors, minimal retries. Cons: high context usage (50-100 tools confuse the model), not discoverable, not composable. Best for atomic actions needing control (write file, send email, irreversible changes).
- **Bash**: Highly composable via Unix primitives. Low context usage (discovery via --help). Slightly higher latency due to discovery time. Slightly lower call reliability. Best for composable actions (searching folders, GitHub CLI, linting, memory operations).
- **Code Generation**: Highly composable, dynamic scripts. Longest execution time (needs linting, compilation). API design becomes critical. Best for highly dynamic logic, composing APIs, data analysis, deep research, reusing patterns.
- Traditional agent builders tend to only think about tools; the call to action is to think more broadly
- The three modalities can be blended — for example, programmatic tool calling and code mode bridge tools and code generation
- General principle: keep tools for atomic actions needing guarantees, use bash for composable operations, use code generation for dynamic multi-step logic

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[BashTool]] — the bash modality
- [[CodeGenerationForNonCoding]] — the code generation modality
- [[AgentLoop]] — where these modalities are used
