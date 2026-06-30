---
title: "Domain Expert as Oracle"
type: concept
tags: [domain-expertise, ai-quality, organizational-design, oracle, prompt-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs.md"]
last_updated: 2026-06-30
---

## Definition
The Domain Expert as Oracle is the first of three models in Chris Lovejoy's framework for incorporating domain expertise into AI organizations. In this model, the domain expert directly embeds their expertise into the actual application by both assessing AI outputs AND making improvements themselves — handling both sides of the assess→improve loop.

## Key Information
- **Dual role**: The domain expert both assesses outputs (looking at traces, playing with the product) and makes improvements (tweaking prompts, adding documents, tools)
- **Core mechanism**: Direct human review and prompt engineering — the domain expert is the primary gatekeeper of AI quality
- **Best when**: Quality is subjective (taste matters more than objective metrics), or at small scale where one person can handle the volume
- **When not to use**: When quality can be objectively measured and you want to scale beyond one person's capacity
- **Decentralized Oracle variant**: When one person isn't enough, hire multiple domain experts who each own a subset (specialty, geography, use case)
- **Common starting point**: Most organizations begin here, especially startups at small scale
- **Required skills**: Relevant domain expertise (direct use case experience), prompting/content engineering, attention to detail, customer communication

### Case Studies
- **[[Granola]]**: Joe (writer/journalist) as primary gatekeeper — writes all prompts, does user research, directly iterates. Works because no objectively perfect meeting note exists.
- **[[Tandem]]**: Started with Roy (medical doctor) as single Oracle, evolved to decentralized Oracle with doctors across specialties/countries handling long-tail prompt customizations.
- **[[Anterior]]**: [[ChrisLovejoy]] started as Oracle reviewing prior authorization outputs and updating prompts/code before evolving to Evaluator and Architect.

## Related
- [[Domain Expert as Evaluator]] — next model (defines metrics, engineers improve)
- [[Domain Expert as Architect]] — final model (self-improving systems)
- [[Domain Expertise]] — the core capability
- [[Domain Native AI Organization]] — the organizational philosophy
- [[Principal Domain Expert]] — recommended organizational role
- [[Prompt Engineering]] — core mechanism in Oracle model
- [[AI Quality]] — what the Oracle assesses
- [[Granola]] — Oracle model case study
- [[Tandem]] — decentralized Oracle case study
- [[Anterior]] — started as Oracle before evolving
- [[ChrisLovejoy]] — framework creator
- [[summary-20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs]] — source talk
