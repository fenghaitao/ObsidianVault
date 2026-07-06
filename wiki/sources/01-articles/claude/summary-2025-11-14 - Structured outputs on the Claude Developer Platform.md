---
title: "summary-2025-11-14 - Structured outputs on the Claude Developer Platform"
type: source
tags: [source, structured-outputs, api, json-schema]
sources: ["raw/01-articles/claude/2025-11-14 - Structured outputs on the Claude Developer Platform.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic launched structured outputs on the Claude Developer Platform (public beta, Claude Sonnet 4.5 and Opus 4.1), guaranteeing API responses conform exactly to a supplied JSON schema or tool definition — eliminating schema-related parsing errors and failed tool calls without impacting model performance. [[OpenRouter]] is cited as an early adopter praising the reliability gain for agentic workflows.

## Key Points

- Two usage modes: supply a JSON schema directly, or define tool specifications and have Claude's tool-call output automatically conform to them.
- Eliminates the need for failover logic and complex error-handling/retry code in production applications and agents (data extraction from images, agent orchestration, external API integration).
- OpenRouter COO Chris Clark: structured outputs "close a real gap for developers" in the agentic AI stack, since agents constantly ingest and produce structured data.
- **Rollout timeline** (per in-article updates): public beta launch for Sonnet 4.5/Opus 4.1 (Nov 14, 2025) → Haiku 4.5 support added on the Claude Developer Platform and Microsoft Foundry (Dec 4, 2025) → general availability natively on the Claude Developer Platform and Amazon Bedrock for Sonnet 4.5, Opus 4.5, and Haiku 4.5, adding support for more complex schemas (Feb 4, 2026).

## Related

- [[StructuredOutputs]] — the feature this article announces
- [[OpenRouter]] — cited early-adopter customer
- [[AmazonBedrock]] — platform structured outputs reached GA on
