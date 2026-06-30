---
title: "Nick Nisi"
type: entity
tags: [person, speaker, workos, developer-experience, skills]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - Full Walkthrough： Writing & Using Skills — Nick Nisi and Zack Proser.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-29
---

## Definition
Nick Nisi is a Developer Experience (DX) engineer at WorkOS on the applied AI team. He co-presented a workshop on writing and using AI agent skills at scale at the AI Engineer Summit (aiDotEngineer).

## Key Information
- **Role**: Developer Experience Engineer at WorkOS, applied AI team
- **Notable Work**: Built the AI installer for WorkOS that automates auth setup; created the ideation plugin (an open-source skill for iterative planning with confidence scoring); built the WorkOS CLI powered by Claude Agent SDK and skills; built Case, an internal agent harness with five agents and state machine gates
- **Skills Philosophy**: Keeps Claude.md extremely small (terseness preference, Obsidian vault path); uses skills for everything else to avoid context bloat; discovered that skills can actively hurt performance — deleted 95% of skills (10,000+ lines → 553 lines of gotchas) and got better results
- **Agentic Philosophy**: Enforce don't instruct (use code/state machines not prompts), guide don't prescribe (gotchas not comprehensive docs), measure don't assume (evals are essential), replace trust with evidence (make agents prove their work)
- **Evals**: Wrote a custom eval framework for skills before Claude shipped one — runs tasks with and without skills, grades both, requires 80%+ improvement; discovered a skill that achieved 77% accuracy vs 97% without it
- **Tools**: Uses WhisperFlow for voice dictation, Obsidian for knowledge management, git worktrees for parallel work, Pi for agent harness, TypeScript state machines for enforcement
- **Speaking**: Presented at AI Engineer Summit (aiDotEngineer) on skills at scale and on deleting 95% of agent skills

## Related
- [[summary-20260506 - Full Walkthrough： Writing & Using Skills — Nick Nisi and Zack Proser]] — source
- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[WorkOS]] — employer
- [[ZackProser]] — co-presenter
- [[Case]] — internal agent harness
- [[WorkOS CLI]] — public-facing CLI tool
- [[AuthKit]] — WorkOS auth product
- [[Skills]] — workshop topic
- [[Gotchas]] — alternative to comprehensive skills
- [[Evidence-Based Verification]] — core philosophy
- [[State Machine Gates]] — architectural pattern in Case
- [[Harness Engineering]] — discipline Case embodies
- [[WhisperFlow]] — dictation tool
- [[Obsidian]] — knowledge management tool
