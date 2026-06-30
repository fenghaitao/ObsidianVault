---
title: "Anterior"
type: entity
tags: [company, healthcare, ai, prior-authorization, startup, us-healthcare]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs.md"]
last_updated: 2026-06-30
---

## Definition
Anterior is a Square Back startup that performs prior authorization in the US healthcare system. Prior authorization is the process where insurance companies have nurses and doctors determine whether a requested treatment (e.g., MRI) should be approved based on medical evidence.

## Key Information
- **Product**: AI for prior authorization — determines whether treatments should be approved or escalated for clinician review
- **First technical employee**: [[ChrisLovejoy]], who built the initial product (prompts and code)
- **Domain expert evolution**: Progressed through Oracle → Evaluator → Architect models
  - **Oracle**: Chris reviewed outputs clinically, updated prompts and code
  - **Evaluator**: Defined metrics and failure modes, built review dashboard, hired clinicians for reviews, collaborated with engineering
  - **Architect**: Designed methods for automated improvement because manual iteration couldn't scale across organizational variations in policy interpretation
- **Why measurable**: AI output is either approval or escalation — clearly correct or incorrect based on medical evidence
- **Key challenge**: Large variation in how different organizations interpret prior authorization rules and policies
- **Architect approach**: System that adapts dynamically and learns from usage at the edge

## Related
- [[ChrisLovejoy]] — first technical employee, built initial product
- [[Tandem]] — another clinical AI company Chris worked with
- [[Domain Expert as Oracle]] — starting model at Anterior
- [[Domain Expert as Evaluator]] — second model at Anterior
- [[Domain Expert as Architect]] — final model at Anterior
- [[summary-20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs]] — source talk
