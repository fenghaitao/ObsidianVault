---
title: "AI-Generated Security Reports"
type: concept
tags: [security, ai, open-source, maintenance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
last_updated: 2026-06-26
---

## Definition
AI-generated security reports are vulnerability advisories created by AI agents rather than human security researchers. They represent a growing burden on open-source maintainers who must triage large volumes of often low-quality or impractical reports.

## Key Information
- OpenClaw received 1,142 security advisories (~16.6/day), most of which were AI-generated — roughly double the rate of the Linux kernel and curl
- Peter Steinberger's rule: "the higher they're screaming how critical they are, the more likely it's slop"
- Signs of AI-generated reports: "anytime the report is too nice or someone apologizes, that's very likely AI because usually people in security don't apologize"
- Reports rarely come with fixes; if they do, "it's usually a very bad fix"
- Rushing fixes when overloaded "will very certainly break your product"
- AI tools are getting so good at identifying multi-chained exploits that "we're going to break all the software that exists"
- The security industry treats findings as "credits" — the more issues found, the more they're seen — incentivizing volume over quality
- "Hundreds of people firing up their clankers trying to break OpenClaw"
- Other open-source projects (like FFmpeg) are also publicly complaining about this phenomenon
- Humans still need to read each report because "we're not at the point where you can fully trust that the agent will figure it out"
- This is "a huge burden on time" and "something that I see more and more open source projects complaining about or breaking"

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source
- [[OpenClaw]] — project most affected
- [[PeterSteinberger]] — maintainer dealing with the flood
- [[FFmpeg]] — another project publicly complaining
- [[Slop]] — related concept (low-quality AI output)
- [[CVSS]] — scoring system that doesn't account for AI-generated report quality
