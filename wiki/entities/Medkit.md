---
title: "Medkit"
type: entity
tags: [hackathon, medical-training, claude-code, managed-agents, simulation]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Medkit is a gamified medical training tool built by Bedirhan Keskin using Claude Managed Agents. It simulates real-life patient encounters for medical residents and junior doctors, allowing them to practice diagnosis and treatment in a safe, simulated environment before facing real patients.

## Key Information

- **Creator**: Bedirhan Keskin, an Istanbul-based physician-turned-software engineer.
- **Purpose**: Addresses the gap between medical school training and real emergency department practice, where junior doctors often encounter cases they never practiced.
- **Workflow**: Students take medical history, order labs, read imaging, diagnose, and prescribe treatment for simulated patients. An agentic grader then assesses the full encounter against published clinical guidelines that a board examiner would use.
- **Architecture**: Built across four separate Claude Code sessions — voice engine, content generation, 3D game layer, and core app — keeping each context clean and progressing on all at once.
- **Development approach**: "Talk, don't type" — Bedirhan worked almost entirely by voice.
- **Adoption**: Three medical faculties and a pharma company in Istanbul are set to start running pilots.

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — development environment
- [[ClaudeManagedAgents]] — infrastructure for agentic grading
- [[Claude4.7Opus]] — model used
- [[HealthcareAI]] — broader healthcare AI context
