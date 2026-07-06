---
title: "Kepler"
type: entity
tags: [company, financial-services, ai-agents, verification, claude, startup]
sources: ["raw/01-articles/claude/2026-04-30 - How Kepler built verifiable AI for financial services with Claude.md"]
last_updated: 2026-07-04
---

# Kepler

[[Kepler]] is a startup building a trust-and-verification layer for AI in financial services, founded by Vinoo Ganesh and John McRaven (both formerly at Palantir, building data systems for defense, energy, and financial firms). Its flagship product, Kepler Finance, is a research platform where analysts ask plain-English questions and receive answers with every number traceable to the exact SEC filing, page, and line item it came from.

## Overview

- **Founders**: Vinoo Ganesh and John McRaven — ex-Palantir, defense/energy/financial data systems background.
- **Founding insight**: after speaking with 147 financial firms (private equity, hedge funds, investment banks), the team found near-universal demand for AI research tools paired with near-universal distrust of AI output that can't be audited. Quote from a managing director: "How am I supposed to trust something I can't audit?"
- **Core architecture**: separates Claude (reasoning/interpretation/planning) from Kepler's own deterministic infrastructure (computation/verification), so results are provably correct rather than model-generated. "In finance, the model can't be the whole system. We treat it as one stage in a pipeline whose job is to hand the model exactly what it needs to succeed at exactly that stage" — McRaven.
- **Scale**: indexes 26M+ SEC filings, 50M+ public documents, 1M+ private documents, across 14,000+ companies and 27 global markets.

## How It Uses Claude

- **Model benchmarking**: tested all frontier models; found that on long, multi-step plans with interdependencies, only [[Claude]] consistently held the plan together without dropping constraints by step four or five. Ganesh: "On our workloads, Claude was the model that consistently held the plan together."
- **Ambiguity handling**: unlike other models, which silently pick one interpretation of an ambiguous term and continue, Claude stops and asks the analyst to disambiguate — a behavior Ganesh says "matters more than any benchmark score."
- **Multi-model pipeline**: [[Claude4.7Opus]] handles complex reasoning (intent decomposition, ambiguity resolution, structured execution plans); [[Claude4.6Sonnet]] handles higher-throughput, more constrained stages.
- **Specialized recall models**: Kepler trained its own models (some Claude-based, some proprietary) for recall tasks, reaching 94% accuracy mapping financial statement labels to standardized taxonomy codes, versus 38-46% for other models.
- **Deterministic layer**: proprietary financial ontology, deterministic execution environments for any operation requiring provable correctness (ratios, fiscal-period resolution), per-user access controls, and idempotent, reusable "skills" for common workflows (e.g., enterprise value calculations across complex capital structures, segment revenue waterfall reconciliation).
- **Evaluation pipeline**: every prompt change, model upgrade, and context modification is tested against thousands of cases before production; automated pipelines compare Claude's output against known-correct answers at every stage, and new Anthropic model releases are benchmarked within hours.

## Compliance and Trust

- Full audit logging, siloed customer environments, end-to-end data provenance.
- SOC 2 Type II certified; ISO 27001 certification underway.
- Output is assembled into an analyst's Excel template, where a single click traces any number back to its highlighted line item in the source document.

## Future Direction

Kepler's architecture is designed to be domain-agnostic. Finance was chosen deliberately as one of the most demanding proving grounds (dense data, overloaded terminology, complex calculations, zero error tolerance). Founders cite healthcare (reconciling clinical trial data against treatment protocols) and legal (tracing precedent across case law) as likely future extensions of the same pattern. Ganesh: "Kepler Finance is our first product. It won't be the last."

## Related

- [[FinancialServicesAI]] — broader concept this case study exemplifies
- [[Hebbia]] — comparable financial-services AI platform built on Claude
- [[Claude4.7Opus]] — model used for complex reasoning/planning stages
- [[Claude4.6Sonnet]] — model used for higher-throughput constrained stages
- [[ToolUse]] — underlying agentic capability enabling multi-step plan execution
- [[summary-2026-04-30 - How Kepler built verifiable AI for financial services with Claude]] — source article
