---
title: "Skills Sharing"
type: concept
tags: [ai, skills, sharing, collaboration, teams]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Skills Sharing is the challenge of distributing AI agent skills across individuals and teams. Current methods (GitHub repos, zip files, submodules, plugin marketplaces) are all inadequate, creating friction for adoption and collaboration.

## Key Information
- Current sharing methods and their problems:
  - MPX skills: requires a separate GitHub repository per skill (heavyweight for 50 skills)
  - Direct file sharing: sending skill files or zip files is primitive and doesn't handle updates
  - Git submodules: complex dependency management for skills folders
  - Plugin marketplaces: version the plugin, not the skills within it
- Additional complexity: if someone contributes to your skill, do you want their changes? Are changes local or global? This depends on the skill and the contributor
- "Do you run a backlog for each skill where you have tickets to improve the skills?" — unsolved organizational question
- Chris Parsons is building AirSkills to address this: package skills as manageable units, create skill bundles, create skill sets for different teams, automatic versioning and updates
- Parsons shared his Ralph loop skill during the workshop via an AirSkills command
- "I can't imagine non-coders using that" — current sharing methods have too much friction for non-technical users

## Related
- [[Skills Versioning]] — related problem
- [[Skills Governance]] — organizational scale
- [[AirSkills]] — Parsons' solution
- [[ChrisParsons]] — his approach
- [[Skills]] — what's being shared
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
