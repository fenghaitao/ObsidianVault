---
title: "Meta"
type: entity
tags: [company, social-media, developer-experience, measurement]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md"]
last_updated: 2026-06-26
---

## Definition
Meta (formerly Facebook) is a large technology company with what Joel Becker describes as "probably the best infrastructure for quantitative measurement of developer experience in the world."

## Key Information
- Presented at the Developer Community Engineering Summit about their quantitative measurement of developer experience
- Can measure how much actual human time effort it takes to make a PR (called "diffs" at Meta)
- Found a J-curve when giving developers AI agents: developers initially slowed down, then after 3-6 months began speeding up
- This J-curve finding contrasts with METR's RCT results, though Becker notes the contexts differ (enterprise vs. open source)
- Foundation model provider available through Amazon Bedrock alongside Anthropic, AI21 Labs, Cohere, Mistral, Stability AI, and Amazon Titan
- Had an internal token usage leaderboard where engineers' token counts were visible; taken down after an article made them look bad, but token maxing continues
- Token count is used as one data point in performance evaluations — can be "weaponized" (low performer + low tokens = "not even trying"; high performer + high tokens = "innovating")
- Engineers token max by asking agents to summarize docs instead of reading them, or running autonomous agents to build junk to increase token count
- Building internal AI infra alongside Uber, Airbnb, Intercom, and Microsoft

## Related
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[JCurveFamiliarityEffect]] — concept observed in Meta's data
- [[JoelBecker]] — referenced Meta's developer experience research
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source (Meta as Bedrock model provider)
- [[summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer]] — source (token maxing, leaderboard)
- [[TokenMaxing]] — phenomenon observed at Meta
- [[DeveloperProductivityMeasurement]] — broader context
- [[InternalAIPlatform]] — building custom AI infra
