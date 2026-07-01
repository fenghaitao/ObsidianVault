---
title: "Diagnostic Playbooks"
type: concept
tags: [agents, error-recovery, skills, self-healing, troubleshooting]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Diagnostic Playbooks are troubleshooting skills embedded in an MCP server or agent harness that activate when agents encounter common issues, enabling self-healing without human intervention. They are the third layer of the Error Recovery For Agents spectrum.

## Key Information
- Layer 3 of the Error Recovery For Agents spectrum
- Implemented as skills within the agent's tool ecosystem
- Chrome DevTools MCP has a troubleshooting skill that helps agents and humans fix MCP server setup issues
- Enable agent self-healing — the agent can resolve problems without escalating to a human
- Part of the broader skills ecosystem: "skills supercharge discoverability but are not free lunch"
- Trade-off: adding too many skills shifts the problem — agents call skills when they shouldn't, context window grows
- Contrast with [[Proactive Detours]] (preventing mistakes) — diagnostic playbooks fix problems that already occurred

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Error Recovery For Agents]] — parent concept
- [[Proactive Detours]] — complementary technique (prevention vs. cure)
- [[Agent Skills]] — implementation mechanism
- [[Chrome DevTools MCP]] — practical implementation
