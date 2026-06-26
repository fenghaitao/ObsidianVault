---
title: "OSSInAgeOfClankers"
type: concept
tags: [open-source, agents, community, ai-ethics]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
"OSS in the age of clankers" describes the phenomenon of AI agents ("clankers") overwhelming open-source projects with low-quality, automated issues and pull requests. Mario Zechner documented this as a systemic threat to open-source maintainers' sanity and project health.

## Key Information
- "Clankers" = AI agents that automatically file issues and PRs on open-source repositories
- Till Draw closed their issue and PR tracker entirely due to clanker spam
- Open Claw's tracker was similarly overwhelmed
- Half of Pi's issue tracker was Open Claw instances posting garbage
- Mario's defenses:
  - Auto-close PRs with a comment asking for a human-written issue (no longer than a screen of text)
  - If a human responds, their account gets whitelisted ("vouch" system)
  - Clankers don't read the comment and never come back — perfect filter
  - Mitchell Hashimoto turned this into a tool called "vouch"
  - Label Open Claw interactions to deprioritize issues
  - Embed issue/PR texts in 3D space to spot clusters
  - "OS certification": close the tracker whenever you want to get your life back
- "Does this work? Yes, sort of." — not a complete solution

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[MarioZechner]] — originator of the term and defenses
- [[TillDraw]] — project that closed its tracker
- [[OpenClaw]] — source of many clanker submissions
- [[Pi (coding agent)]] — project affected by clankers
- [[MitchellHashimoto]] — created vouch tool based on Mario's approach
- [[Ghosty]] — Mitchell's project
