---
title: "Agent Development Environment"
type: concept
tags: [ai, agents, engineering, skills, workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition
The Agent Development Environment is Vincent Koc's system for managing and iterating on AI agent skills. It treats skills as versioned, improvable artifacts — similar to how developers manage dotfiles. The process involves using skills with agents, reviewing session logs to identify improvements, refining the skills, and deploying them. This creates a feedback loop where agent performance continuously improves through structured skill management.

## Key Information

- **Origin**: Vincent Koc's personal workflow, described in his 2026 dark factory talk
- **Components**:
  - **".skills"**: Like dotfiles — a collection of skill definitions stored in version control, available open source on GitHub
  - **Session log review**: Using a skill to read Codex session logs and identify improvements
  - **Iteration loop**: Use skill → review logs → make improvements → deploy updated skill
  - **Distribution**: Uses vercel.skills.sh as a mechanism to distribute and discover skills
- **Skill types**: Technical documentation writing, agent workflow management, and other engineering practices
- **Privacy**: Some skills are private; public ones are available on GitHub
- **Tools**: Can use a skills management tool (like Geppetto, which Vincent contributes to) or just "Go Codex"
- **Philosophy**: Skills are not static — they improve through use, similar to how agents themselves improve
- **Relationship to dark factory**: The Agent Development Environment is the tooling layer that makes the dark factory sustainable — it's the engineering process behind the velocity

## Related
- [[summary-20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — originator
- [[Agent Skills]] — the general concept of agent skills
- [[Skills]] — skill definitions and management
- [[Skills Flywheel]] — the feedback loop concept
- [[Skills Versioning]] — version management for skills
- [[Dark Factory]] — the overarching concept this supports
- [[Swim Lanes]] — the parallel workflow pattern
- [[Codex]] — the agent tool used in this environment
- [[OpenClaw]] — the project context
