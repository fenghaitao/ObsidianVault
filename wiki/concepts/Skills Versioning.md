---
title: "Skills Versioning"
type: concept
tags: [ai, skills, versioning, git, management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Skills Versioning is the practice of tracking and managing changes to AI agent skills over time. Current approaches (GitHub, submodules) are inadequate, and better tooling is needed for both individual and team use.

## Key Information
- Chris Parsons currently uses GitHub to version his ~50 skills
- He treats skills as "quite important code" and versions them accordingly
- Challenges: putting a single skill on GitHub requires its own repository (heavyweight for 50 skills); submodules create complex dependency management
- "I don't think Git is the right skills format for this long-term. I think we need a new thing."
- Parsons is building AirSkills to solve this — automatic versioning and updates without requiring Git knowledge
- Skills contain IP (both personal and customer), so not all skills are shared publicly
- The skill itself is the prompt — versioning the skill means versioning the prompt
- Parsons gets Claude to write and update his skills, then versions the output
- Question from audience: how do you know if a skill version is actually better? Parsons acknowledges this is subjective and difficult to measure objectively given AI non-determinism

## Related
- [[Skills Sharing]] — related problem
- [[Skills Governance]] — organizational scale
- [[AirSkills]] — Parsons' solution
- [[ChrisParsons]] — his approach
- [[Skills]] — what's being versioned
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
