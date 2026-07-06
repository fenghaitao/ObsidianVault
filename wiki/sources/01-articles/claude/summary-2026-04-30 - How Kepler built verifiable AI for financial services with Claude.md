---
title: "summary-2026-04-30 - How Kepler built verifiable AI for financial services with Claude"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-30 - How Kepler built verifiable AI for financial services with Claude.md"]
last_updated: 2026-07-04
---

## Core Summary

This "How startups build with Claude" article profiles [[Kepler]], a research platform for financial services founded by Vinoo Ganesh and John McRaven (both ex-Palantir, building data systems for defense, energy, and financial firms). Kepler's core insight — drawn from conversations with 147 financial firms (private equity, hedge funds, investment banks) — is that firms want AI for research but don't trust its output because it can't be audited. Kepler's answer is to separate the *reasoning* stage (handled by Claude) from the *computation/verification* stage (handled by deterministic infrastructure Kepler built itself), so every number in an answer can be traced back to an exact filing, page, and line item. Claude serves as the interpretation and planning layer — decomposing plain-English analyst questions into multi-step plans, resolving ambiguous financial terminology, and flagging cases needing human judgment — while Kepler's proprietary ontology, deterministic execution environments, and access-control layer handle anything that must be provably correct (ratios, fiscal-period resolution, formula computation). The team uses a multi-stage pipeline with different Claude models per stage (Opus 4.7 for complex reasoning/decomposition/planning, Sonnet 4.6 for higher-throughput constrained stages), plus their own specialized recall models (some Claude-based, some proprietary) reaching 94% accuracy on financial-statement-label-to-taxonomy-code mapping versus 38-46% for other models. The platform indexes 26M+ SEC filings, 50M+ public documents, and 1M+ private documents across 14,000+ companies and 27 global markets, and pulls verified figures into an Excel template where analysts can trace any number back to its highlighted source line item with one click. Kepler benchmarked all frontier models and found Claude uniquely held long, multi-step plans together without dropping constraints and proactively stopped to ask analysts to disambiguate terms rather than silently guessing — a behavior the founders say matters more than raw benchmark scores in finance, where one wrong early assumption breaks all downstream analysis. The company has SOC 2 Type II certification (ISO 27001 underway), full audit logging, siloed customer environments, and end-to-end data provenance, and frames finance as a deliberately chosen hard first vertical for a domain-agnostic architecture it plans to extend to healthcare (clinical trial reconciliation) and legal (precedent tracing) use cases.

## Key Points

- **Founders**: Vinoo Ganesh and John McRaven, both spent years at Palantir building data systems for defense, energy, and financial firms before founding [[Kepler]].
- **Market research**: spoke with 147 financial firms (private equity, hedge funds, investment banks); near-universal finding — everyone wants AI for research, nobody trusts the output. Quote from a managing director: "How am I supposed to trust something I can't audit?"
- **Product**: Kepler Finance — a research platform where analysts ask plain-English questions and get instantly verifiable answers, each number traceable to exact filing/page/line item.
- **Architecture split**: Claude = reasoning/interpretation/planning layer; Kepler's deterministic infrastructure = computation/verification layer. "In finance, the model can't be the whole system. We treat it as one stage in a pipeline whose job is to hand the model exactly what it needs to succeed at exactly that stage" — McRaven. "Prompt engineering optimizes a call while content engineering optimizes the system around it."
- **Model benchmarking**: tested all frontier models; on simple queries performance was comparable across models, but on long multi-step plans with interdependencies, all models except Claude started taking shortcuts or dropping constraints by step 4-5. "On our workloads, Claude was the model that consistently held the plan together" — Ganesh. "Other models would start strong and then quietly drop a constraint by step five."
- **Ambiguity handling as differentiator**: when a term has multiple meanings, other models silently picked one and continued; Claude stopped and asked the analyst to disambiguate. "That behavior matters more than any benchmark score. One wrong assumption early in a financial analysis breaks everything downstream." — Ganesh.
- **Deterministic execution environments**: built for every operation needing provable correctness (e.g., computing a ratio, resolving a fiscal period).
- **Proprietary ontology**: maps financial concepts to precise definitions/formulas, customizable per use case.
- **Security**: access-control restrictions enforced at every step, governing which data sources each user can query.
- **Reusable skills**: built for common workflows, e.g. enterprise value calculations across complex capital structures (preferred shares, convertibles, minority interests) and segment revenue waterfall reconciliation across reporting-period changes. These skills coordinate deterministic and nondeterministic stages and are idempotent by design (same input always yields same output).
- **Multi-model pipeline**: Opus 4.7 for complex reasoning (intent decomposition, ambiguity resolution, structured execution plans); Sonnet 4.6 for higher-throughput, more constrained stages.
- **Specialized recall models**: trained in-house (some built on Claude, some fully proprietary), reaching 94% accuracy mapping financial statement labels to standardized taxonomy codes, vs. 38-46% accuracy for other models on the same task.
- **Evaluation rigor**: every prompt change, model upgrade, and context modification tested against thousands of cases before production release; automated pipelines compare Claude's output to known-correct answers at every stage (both structured plan and final computed result); failures are traced to reasoning, context, or downstream execution. New Anthropic model versions are benchmarked "within hours" of release.
- **Scale**: 26M+ SEC filings, 50M+ public documents, 1M+ private documents, 14,000+ companies, 27 global markets.
- **Output**: retrieval layer pulls verified figures from SEC filings, computes results, assembles them into the analyst's Excel template; one click traces any number back to its highlighted line item in the source document.
- **Org efficiency claim**: separating Claude's reasoning from Kepler's deterministic infrastructure lets a small team operate at this scale — new capabilities that would take a large team months can ship in weeks because the modular architecture allows improving one pipeline stage without touching the rest.
- **Compliance posture**: full audit logging, siloed customer environments, end-to-end provenance; SOC 2 Type II certified, ISO 27001 certification underway.
- **Future direction**: platform is designed to be domain-agnostic; finance was chosen deliberately as one of the hardest environments (dense data, overloaded terminology, complex calculations, zero error tolerance). Founders cite healthcare (reconciling clinical trial data against treatment protocols) and legal (tracing precedent across case law) as future extensions of the same pattern: "Claude reasons about the question and infrastructure guarantees the answer." Quote from Ganesh: "Kepler Finance is our first product. It won't be the last."
- **Article metadata**: published by Anthropic, dated 2026-04-30, part of the "How startups build with Claude" series; source URL https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude.
- **Anomaly**: none detected — no prompt-injection-style text found embedded in the raw source; the article is standard first-party Anthropic marketing/case-study copy.

## Related

- [[Kepler]] — subject company profiled in this article
- [[FinancialServicesAI]] — broader concept this case study exemplifies
- [[Hebbia]] — comparable financial-services AI platform built on Claude
- [[Claude4.7Opus]] — model used for complex reasoning/planning stages
- [[Claude4.6Sonnet]] — model used for higher-throughput constrained stages
- [[ToolUse]] — underlying agentic capability enabling multi-step plan execution
