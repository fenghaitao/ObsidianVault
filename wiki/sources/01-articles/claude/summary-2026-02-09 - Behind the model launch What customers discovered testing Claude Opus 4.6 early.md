---
title: "summary-2026-02-09 - Behind the model launch What customers discovered testing Claude Opus 4.6 early"
type: source
tags: [source, claude-opus-4.6, early-access, customer-testing]
sources: ["raw/01-articles/claude/2026-02-09 - Behind the model launch What customers discovered testing Claude Opus 4.6 early.md"]
last_updated: 2026-07-04
---

## Core Summary

A behind-the-scenes look at four customers' ([[Harvey]], [[BoltNew|bolt.new]], [[Shopify]], [[Lovable]]) pre-launch testing of [[Claude4.6Opus|Claude Opus 4.6]], combining structured benchmarks with qualitative "vibe checks" — their candid feedback on both strengths and gaps directly shapes the shipped model.

## Key Points

- **[[Harvey]]**: brought in experienced lawyers to test legal tasks against BigLaw Bench; Opus 4.6 scored 90.2% (first Anthropic model over 90%, 40% of tasks perfect) — with lawyers separately noting the output felt "smart and analytical, like it's actually thinking."
- **[[BoltNew|bolt.new]]**: ran a dedicated Slack channel with deliberately unbiased separate impressions, combining an automated eval platform (build quality, bug fixing, codebase understanding, design aesthetics) with hands-on stress testing; Opus 4.6 diagnosed on the first try a waterfall-graph bug that had failed five-plus attempts with the previous model, finding 8 parallel HubSpot API calls bypassing rate-limit protection via raw fetch calls.
- **[[Shopify]]**: fed the model into existing iterative planning loops; Staff Engineer Paulo Arruda described giving a vague instruction and getting back more than asked for, anticipating his next request; Staff Engineer Ben Lafferty had it port a large TypeScript library to Ruby in one shot (creating a test shim first) with "one of the first early access periods where I haven't had substantial feedback to give."
- **[[Lovable]]**: ran structured design benchmarks and complex-task evals alongside engineer "vibe checks"; a subway-mapping/itinerary side project that had stalled on previous models pushed further with max effort turned up; noted a broader autonomy shift from the model's ability to browse and self-test.
- Common theme across all four: the model increasingly feels like "a true collaborator" with a growing time horizon of tasks safely delegable, per Shopify's Ben Lafferty.
- Candid negative feedback is treated as equally valuable — Anthropic frames early testers as development partners, not passive testers.

## Related

- [[Claude4.6Opus]] — the model under early access test
- [[Harvey]] — profiled early-access customer
- [[BoltNew]] — profiled early-access customer
- [[Shopify]] — profiled early-access customer
- [[Lovable]] — profiled early-access customer
