---
title: "ARIA"
type: entity
tags: [hackathon, industrial-maintenance, claude-code, managed-agents, predictive-maintenance, multi-agent]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

ARIA (Adaptive Runtime Intelligence) is an AI system that continuously monitors factory machines and generates custom diagnostics and repair plans the moment trouble appears. It won the Best Use of Claude Managed Agents prize in the Built with Opus 4.7 hackathon. It turns an experienced maintenance engineer's instincts into an affordable, fast-to-set-up AI system.

## Key Information

- **Creators**: Idriss Benguezzou (French industrial-software engineer with a Master's in data/AI) and Adam Hnaien (self-taught engineering student experienced with Claude Code and multi-agent workflows). Both have on-the-floor industrial experience and met in the hackathon's teammate-finding Discord channel.
- **How it works**: A maintenance engineer uploads a manufacturer's PDF, answers four plain-language calibration questions, and within 15 minutes the plant is profiled. From there, five agents watch live signals. If an agent detects a failure or predicts one is imminent, it produces a work order analyzing component, failure mode, urgency, parts, and intervention window.
- **Development approach**: Spent all of the hackathon's second day in planning mode with a GitHub Project board, scoping every milestone, issue, and acceptance criterion before writing the first line of code. Claude Code wrote ~80% of the raw lines while the builders made domain logic and design decisions by hand.
- **Division of labor**: Idriss handled threshold evaluation, KB schema, and anomaly detection (domain expertise). Adam took on UX, visual language, and ARIA's constellation concept (design taste).
- **Managed Agents role**: "Without Claude Managed Agents, we'd have spent the week building infrastructure that Anthropic already hosts: a sandboxed Python environment, secure execution, session persistence, MCP dispatching. Instead, we spent that week building the product around that infrastructure."
- **Post-hackathon**: Companies working on industrial maintenance reached out about the project. Idriss will fold ARIA's agent architecture into his own industrial IoT platform.

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — development environment
- [[ClaudeManagedAgents]] — agent infrastructure (Best Use prize)
- [[Claude4.7Opus]] — model used
- [[MultiAgentSystem]] — five-agent monitoring architecture
- [[SpecFirstDevelopment]] — planning-first methodology
