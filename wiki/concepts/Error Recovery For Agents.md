---
title: "Error Recovery For Agents"
type: concept
tags: [agents, error-handling, resilience, self-healing, agent-interface]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Error Recovery For Agents is a spectrum of techniques for making agent interfaces resilient, ranging from useful error messages to proactive detours to diagnostic playbooks. The goal is to enable agent self-healing — every time an agent encounters an error, it costs tokens in retries and understanding.

## Key Information
- Presented by Michael Hablich as a three-layer spectrum:
  1. **Useful Error Messages**: Error messages should suggest next steps, enabling agents to self-heal. Example: adding "last navigation entry not found — try navigating forward first" to a history navigation error enabled self-recovery.
  2. **Proactive Detours**: Counteract model training biases by steering agents toward the correct tool. Example: detouring agents from Lighthouse audit to start performance trace for performance profiling.
  3. **Diagnostic Playbooks**: Troubleshooting skills that kick in when agents encounter common setup issues. Chrome DevTools MCP has a troubleshooting skill for MCP server configuration problems.
- "Efficiency is useless if your agent gets stuck"
- All three layers increase the resilience of the agent harness
- Enables self-healing without human intervention
- Contrasts with [[ErrorsAsPrompts]] (Jeremiah Lowin) which focuses on making error messages informative — Hablich extends this to proactive detours and playbooks

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Proactive Detours]] — layer 2 technique
- [[Diagnostic Playbooks]] — layer 3 technique
- [[ErrorsAsPrompts]] — complementary concept from Jeremiah Lowin
- [[Agent Skills]] — mechanism for diagnostic playbooks
- [[Chrome DevTools MCP]] — practical implementation
