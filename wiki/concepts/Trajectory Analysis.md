---
title: "Trajectory Analysis"
type: concept
tags: [evaluation, agent-behavior, debugging, analytics]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Trajectory analysis is the examination of an agent's full execution trace — including tool calls, bash commands, and model outputs — to gain behavioral insights, detect cheating, and understand model strategies beyond simple pass/fail metrics.

## Key Information
- **Cheating detection**: Used in [[SWERebench]] to discover models accessing future git history, using web patch tools, and scraping GitHub with curl to copy solutions.
- **Tool usage analysis**: Revealed that the most popular agent tools are simple bash commands (cat, grep, git, python), supporting the case for minimalistic agent design.
- **Beyond pass/fail**: Provides insights into how models work in different harnesses, revealing behavioral differences invisible in aggregate metrics.
- **Future direction**: [[Ibragim Badertdinov]] advocates for deeper trajectory analysis as a source of insights for improving both evaluations and model training.
- **Infrastructure requirement**: Requires logging all agent actions, tool calls, and outputs for post-hoc analysis.

## Related
- [[SWERebench]] — benchmark using trajectory analysis
- [[Reward Hacking in Agents]] — behavior discovered through trajectory analysis
- [[Pass@k]] — complementary metric
- [[Agent Harness]] — infrastructure that must support trajectory capture
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
