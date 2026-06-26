---
title: "DataScienceAIGap"
type: concept
tags: [ai, data-science, enterprise, limitations, tacit-knowledge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md"]
last_updated: 2026-06-26
---

## Definition
The Data Science AI Gap is the observation that AI systems struggle significantly more with real-world corporate data science tasks than with software engineering tasks, due to messy, contradictory data environments and heavy reliance on undocumented tacit knowledge.

## Key Information
- Corporate data environments contain contradictory facts: field names and formats change over time without documentation
- Example: a "time started" field might contain only a date until November, then only a month, then seconds — with no record of these cut-off dates
- LinkedIn has 5,000 tables with the name "impressions," making it extremely difficult for AI to determine which data source to use
- Data scientists must know undocumented magic to determine when deployments started and ended, which PRs were in each deployment, and where team hierarchy data lives
- Complex tasks like "give me the P90 of time between deployments broken down by team hierarchy" require stitching together data from multiple systems (deployment system, GitHub API) that AI cannot currently navigate
- AI is good at writing SQL or Pandas code but "fails completely on complex tasks"
- Most ML engineering work is actually data work (feature curation, data cleaning), so improving AI for data science could have outsized impact on ML progress
- The problem is not just AI capability but also the state of underlying data infrastructure — data specs "really really matter"
- Joel Becker expressed interest in studying this domain as a way to triangulate AI capabilities

## Related
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[LinkedIn]] — example of extreme data complexity
- [[CapitalOne]] — enterprise with similar data challenges
- [[GenBI]] — related concept: AI for business intelligence
- [[MetadataEnrichment]] — potential mitigation approach
- [[JoelBecker]] — expressed interest in studying this gap
