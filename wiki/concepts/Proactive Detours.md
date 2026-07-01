---
title: "Proactive Detours"
type: concept
tags: [agents, error-recovery, tool-design, agent-interface]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Proactive Detours are a technique for counteracting model training biases by explicitly steering agents toward the correct tool for a given task. When a model's training data might lead it to use the wrong tool, proactive detours provide corrective guidance in the tool description or system prompt.

## Key Information
- Layer 2 of the Error Recovery For Agents spectrum
- Beneath each agent there is a model trained on certain data — sometimes you need to counteract that training
- Example from Chrome DevTools MCP: detouring agents from Lighthouse audit to start performance trace for performance profiling, because models are more familiar with Lighthouse but it's not the right tool for the task
- Implemented through tool descriptions, usage guidelines, and system prompt reinforcement
- Part of the discoverability strategy — preventing mistakes rather than just recovering from them
- Works alongside [[Diagnostic Playbooks]] (troubleshooting skills) and useful error messages

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Error Recovery For Agents]] — parent concept
- [[Diagnostic Playbooks]] — complementary technique
- [[Agent Discoverability]] — related discoverability strategy
- [[Tool Description]] — implementation mechanism
- [[Chrome DevTools MCP]] — practical implementation
