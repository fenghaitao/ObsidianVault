---
title: "InternalTools"
type: concept
tags: [software-category, brian-casel, custom-software]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260622 - How to build your own CRM (start to finish).md, raw/03-transcripts/Brian Casel/Channel Only/20260518 - You don't need to learn to code anymore.md, raw/03-transcripts/Brian Casel/Channel Only/20260512 - How I build agents that work the night shift.md]
last_updated: 2026-06-22
---

## Definition

Internal tools are custom-built software applications designed for a single business or individual's specific workflow, as opposed to commercial SaaS built for mass markets. In the AI era, building internal tools has become accessible to non-developers through spec-driven development with AI coding agents.

## Key Information

### Why Build Internal Tools

- Commercial SaaS is bloated for everyone and perfect for no one — you pay for features you never use while the few you need are buried.
- Internal tools match your exact workflow, not a generic one.
- For internal tools, you can hard-code business-specific details (pipeline stages, custom fields) rather than building complex configuration UIs — a major simplification.
- Building your own means no monthly subscriptions, no feature requests to vendors, no compromises.

### Brian Casel's Internal Tools

- **CRM**: simple contact/deal management with Kanban pipeline, activity log, to-dos.
- **Invoicing app**: invoice creation, Stripe checkout, email reminders, API for agents.
- **[[SparkDrop]]**: content pipeline (sparks → flames → scheduled).
- **[[BrainDown]]**: markdown editor/viewer integrated with Dropbox.
- **[[ResonanceRadar]]**: content idea curation from internal and external sources.
- **Tasks dashboard**: dispatch and schedule recurring agent tasks.
- **SEO dashboard**: manage meta titles/descriptions with API for agent access.

### The Dual-Access Pattern

Most of Brian's internal tools have both a UI (for him) and an API (for his agents), enabling the [[NightShiftModel]] where agents can read/write data automatically.

### Distribution

Brian releases many of his internal tools as [[StarterKit]] build kits for Builder Methods Pro members, allowing others to build their own versions.

## Related

- [[BrianCasel]] — primary builder
- [[NightShiftModel]] — the pattern they enable
- [[SpecDrivenDevelopment]] — how they're built
- [[StarterKit]] — how they're shared
- [[SparkDrop]] — example tool
- [[BrainDown]] — example tool
- [[BuildNew]] — the starter template
