---
title: "StructuredOutputs"
type: concept
tags: [api, json-schema, tool-use, reliability]
sources: ["raw/01-articles/claude/2025-11-14 - Structured outputs on the Claude Developer Platform.md"]
last_updated: 2026-07-04
---

## Definition

Structured outputs is a Claude Developer Platform feature that guarantees API responses conform exactly to a supplied JSON schema or tool definition, eliminating schema-related parsing errors and failed tool calls in production applications and agents.

## Key Information

- **Two usage modes**: supply a JSON schema directly in the API request, or define tool specifications and have Claude's tool-call output automatically conform to them.
- **Guarantee, not just guidance**: responses always match the exact structure defined, without impact to model performance or requiring failover/retry logic for malformed output.
- **Use cases**: data extraction from images, agent orchestration, integration with external APIs — any workflow where a single formatting error can cascade into failure.
- **Timeline**: public beta for Claude Sonnet 4.5 and Opus 4.1 (November 14, 2025) → Haiku 4.5 support added on the Claude Developer Platform and Microsoft Foundry (December 4, 2025) → general availability natively on the Claude Developer Platform and [[AmazonBedrock]] for Sonnet 4.5, Opus 4.5, and Haiku 4.5, adding support for more complex schemas (February 4, 2026).
- Customer example: [[OpenRouter]] cites structured outputs as closing "a real gap for developers" in the agentic AI stack, since agents constantly ingest and produce structured data.

## Related

- [[OpenRouter]] — cited early-adopter customer
- [[AmazonBedrock]] — platform structured outputs reached GA on
- [[ToolUse]] — the tool-definition conformance mode of structured outputs
- [[summary-2025-11-14 - Structured outputs on the Claude Developer Platform]] — source article
