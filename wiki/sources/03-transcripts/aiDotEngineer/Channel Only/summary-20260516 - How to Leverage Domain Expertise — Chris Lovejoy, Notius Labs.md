---
title: "How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs.md"
date: 2026-05-16
ingested: 2026-06-30
tags: [talk, domain-expertise, vertical-ai, oracle-evaluator-architect, ai-quality, organizational-design, domain-expert, domain-native-ai]
---

## Core Thesis
Chris Lovejoy argues that winning in vertical AI is fundamentally an organizational problem, not a model problem. The system for incorporating domain insights is more important than the sophistication of your models or pipelines. He presents the Oracle-Evaluator-Architect framework: three models for how organizations bake domain expertise into AI products, with guidance on which model fits different use cases and scales.

## Key Points

### Why Domain Expertise Matters
- ~50% of generative AI projects were abandoned last year (per Gartner)
- A core reason: building AI products without deep understanding of the workflows being automated
- Front-end models are good enough — the gap is how organizations operationalize expert judgment around them
- Appraising AI quality requires judgment, and the best judgment involves domain expertise
- Domain expertise can be formal (doctors, lawyers) or informal (writers, journalists)

### The Three Common Mistakes
1. Not hiring domain experts, or hiring them too late
2. Hiring the wrong kind of domain expert (not granular enough — need direct experience of the specific use case, not just general domain)
3. Not fitting domain experts into the organization appropriately — not leveraging them correctly

### The Oracle-Evaluator-Architect Framework

**Oracle Model**: The domain expert directly embeds their expertise into the actual application. They assess AI outputs (looking at traces, playing with the product) AND make improvements themselves (tweaking prompts, adding documents/tools). Both sides of the assess→improve loop are done by the same person. Best when: quality is subjective (taste matters more than metrics), or at small scale where one person can handle it.

**Evaluator Model**: The domain expert defines how to measure quality — what metrics matter, what you're optimizing for. They build a measurement system (user metrics, hired reviewer teams, LLM-as-judge) that produces performance data. Engineers then make the improvements based on that data. Best when: quality can be measured objectively, and manual iteration by engineers is fast enough.

**Architect Model**: The domain expert designs a system that automatically improves itself — minimal human-in-the-loop. The system learns from usage and user interactions to self-improve. Best when: manual iteration is too slow, you have large variation in how rules/policies are interpreted, and you can identify methods to automate improvements.

### Decision Framework for Choosing a Model
1. **Can you measure performance in metrics?** If no → Oracle (is one person enough, or do you need multiple/decentralized?)
2. If yes, **is manual iteration fast enough?** If yes → Evaluator
3. If no → Architect (automated improvement systems)

### Organizational Evolution Over Time
- Common starting point: Oracle (especially for startups at small scale)
- Can progress to Evaluator if objective metrics exist
- Can progress to Architect if manual iteration becomes too slow
- Each progression requires the domain expert to have adjacent skills beyond pure domain expertise

### Case Studies

**Granola (Oracle)**: Joe (first employee, writer/journalist background) wrote all prompts, did extensive user research, and serves as primary gatekeeper of AI quality. Makes sense because: no objectively perfect meeting note (taste matters), and the core output is amenable to direct human review even at scale.

**Tandem (Decentralized Oracle)**: Medical AI scribe. Started with one doctor (Roy) as oracle reviewing medical notes and updating prompts. Scaled to decentralized oracle: hired many doctors across specialties/countries to handle long-tail prompt customizations. Makes sense because: medical expertise needed, subjectivity in notes, many customizations across specialties and geographies.

**Anterior (Oracle → Evaluator → Architect)**: Prior authorization product. Chris (first technical employee, medical doctor) started as oracle reviewing outputs and updating prompts/code. Progressed to evaluator: defined metrics and failure modes, built review dashboard, hired clinicians for reviews. Then to architect: designed systems for automated improvement because manual iteration couldn't keep up with variation in how different organizations interpret policies. Makes sense because: AI quality is clearly measurable (correct/incorrect decision), clinical reasoning needed, large variation in rule interpretation.

### Skills Required by Role
- **Oracle**: Relevant domain expertise (direct use case experience), prompting/content engineering, attention to detail, customer communication
- **Evaluator**: Domain expertise + data science intuition, statistical skills, industry connections (for hiring review teams), leadership, product management
- **Architect**: Domain expertise + experience working on LLM-powered products, engineering skills, all previous skills are relevant

### Three Principles for Leveraging Domain Experts
1. **Define a Principal Domain Expert**: A single individual ultimately accountable for AI quality, avoiding consensus-by-committee. Gives them time and space to deeply understand AI performance.
2. **Give Them Ownership**: Don't treat them as consultants — put them in the room for decisions. Failure mode: two senior clinicians with ambiguous authority, treated as advisory, leading to slow progress and eventual departure.
3. **Hire for Breadth**: Domain expertise is the base requirement, but hire for as many adjacent skills as possible. Pair with complementary people (e.g., statistician) if gaps exist. Someone who evolves from Oracle through Evaluator to Architect is extremely valuable because they have deep insight into how the AI performs.

## Entities
- [[ChrisLovejoy]] — speaker, medical doctor, founder of Notius Labs
- [[Notius Labs]] — Chris Lovejoy's company
- [[Granola]] — AI meeting notes company, Oracle model example
- [[Tandem]] — clinical AI product provider (UK), decentralized Oracle example
- [[Anterior]] — prior authorization AI startup, Oracle→Evaluator→Architect example
- [[McKinsey]] — Roy (Tandem's first domain expert) worked here before Tandem
- [[University of Cambridge]] — Chris Lovejoy's medical training
- [[NHS]] — UK National Health Service, where Chris worked as a doctor
- [[Bessemer]] — VC firm, noted vertical AI opportunity

## Concepts
- [[Domain Expertise]] — specialized or informal knowledge of a domain's workflows and nuances
- [[Domain Native AI Organization]] — organizational design that bakes domain expertise into AI product development
- [[Domain Expert as Oracle]] — domain expert directly embeds expertise into the application
- [[Domain Expert as Evaluator]] — domain expert defines quality metrics and measurement systems
- [[Domain Expert as Architect]] — domain expert designs self-improving AI systems
- [[Vertical AI]] — AI for specific industries/domains
- [[Last Mile Problem]] — challenge of getting AI products to understand specific workflow nuances
- [[Principal Domain Expert]] — single individual accountable for AI quality
- [[AI Quality]] — assessing and measuring the quality of AI outputs
- [[Last Mile Problem (AI)]] — AI's difficulty capturing domain-specific workflow nuances

## Related
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — vertical AI, domain-specific interfaces
- [[summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola]] — Granola's product approach
