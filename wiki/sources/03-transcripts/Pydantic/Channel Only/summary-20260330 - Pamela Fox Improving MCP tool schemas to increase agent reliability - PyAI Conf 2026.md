---
title: "summary-20260330 - Pamela Fox Improving MCP tool schemas to increase agent reliability - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, mcp, evals, schemas]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260330 - Pamela Fox Improving MCP tool schemas to increase agent reliability - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Pamela Fox (Microsoft/GitHub) presents empirical research on whether stricter MCP tool schemas improve agent reliability. Tests multiple schema variants (bare strings, descriptions, enums, literals, regex patterns) across GPT-4.1 mini, GPT-4o, GPT-5.3 Codex, and GPT-5.4. Key finding: modern LLMs are good enough that schema strictness matters less than expected for reliability, but structured schemas still provide type safety, IDE autocompletion, and validation benefits. Date fields worked perfectly across all schema variants because LLMs default to ISO 8601.

## Key Points

- Adding descriptions to tool parameters is essential — without them, agents may refuse to call the tool
- Enums + descriptions improve category matching but increase schema size (tradeoff)
- Date fields: all schema variants (bare string, description, Python date type, regex) produced identical results — LLMs default to ISO 8601
- Different models disagree on ambiguous categories (e.g., "spa treatment" — health or beauty?)
- GPT-5.3 Codex reasoning level: "low" performed best for category matching; higher reasoning levels overthought and disagreed with ground truth
- PydanticAI and GitHub Copilot SDK produced identical results on the same evals — agentic loops are similar
- FastMCP had to inline JSON Schema enums because Opus models couldn't handle schema references
- Recommendation: do evals for your specific use case; results vary by model and task

## Related

- [[ModelContextProtocol]] — the protocol for tool schemas
- [[PamelaFox]] — speaker, Microsoft/GitHub
- [[FastMCP]] — Jeremiah Lowin's MCP server framework
- [[AgentEvaluation]] — the practice of measuring agent reliability
- [[PydanticAI]] — agent framework used for evals
