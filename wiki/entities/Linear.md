---
title: "Linear"
type: entity
tags: [tool, ticketing, project-management, quality, design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer.md"]
last_updated: 2026-06-26
---

## Definition
Linear is a modern ticketing and project management system for software teams, renowned for its exceptional design quality and performance. In agentic workflows, Linear tickets serve as a source of requirements that AI agents can read and validate against implementations. Linear is also known for its engineering culture that prioritizes taste, craft, and quality above shipping speed.

## Key Information
- Used in Baz's spec reviewer as one of the ticketing systems from which requirements are collected.
- Referenced alongside Jira as an example of ticketing system integration for agentic workflows.
- The spec reviewer reads ticket descriptions to understand what a developer was tasked with implementing.
- **Quality Wednesdays**: Every Wednesday, the full engineering team (~25 engineers, fully remote) gathers for 30 minutes. Each engineer presents one quality fix they found themselves. Started when CTO Tuomas Artman found 35 problems in a single small UI menu. To date, 2,500-3,000 small quality details have been fixed.
- **Zero Bug Policy**: Every reported bug is assigned immediately and becomes the assignee's highest priority. Bugs are typically fixed within 2-3 hours. Linear spent three weeks fixing all bugs to reach zero, then enforced immediate fixing going forward.
- **AI for bug fixing**: 10% of bugs are automatically fixed by single-shot AI — an agent creates a PR and lands it without engineer involvement. Tuomas Artman foresees this approaching 100%.
- **Customer proximity**: Slack channels with all big customers are open to any engineer. Every customer meeting is recorded and tagged. Engineers are exposed to a "fire hose" of customer feedback.
- **Hiring**: Full-week paid trial where candidates build a greenfield project from start to finish. Very few hiring misses.
- **Feature request philosophy**: Linear rarely ships feature requests as-is. Instead, they talk to customers, group requests, find root causes, and design a single perfect solution.
- **Design details**: Every highlight must be instantaneous on hover; every fade-out must be 150ms. These micro-interactions are enforced across the entire application.
- CTO Tuomas Artman is a former Uber engineer who brought lessons from hypergrowth to Linear's quality-focused culture.

## Related
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source
- [[summary-20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer]] — source
- [[Baz]] — company using Linear in spec reviewer
- [[Jira]] — alternative ticketing system
- [[TuomasArtman]] — CTO of Linear
- [[QualityWednesdays]] — weekly practice at Linear
- [[ZeroBugPolicy]] — policy at Linear
- [[CustomerProximity]] — practice at Linear
- [[AIAndTaste]] — concept discussed in context of Linear's approach
