---
title: "Spec-Driven Development: Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro"
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"
date: 2026-01-09
author: "Al Harris"
organization: "Amazon"
type: transcript
---

# Spec-Driven Development: Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro

## Core Thesis

Amazon Kiro implements spec-driven development as a structured SDLC workflow (requirements → design → tasks → execution) that uses EARS-format structured natural language requirements and property-based testing to deliver reproducible, high-confidence software at FAANG scale, moving beyond pure LLM-driven approaches toward neurosymbolic reasoning for quality assurance.

## Key Takeaways

1. **Kiro is an agentic IDE from Amazon**: Launched GA in November 2025, built by a small team of 3-4 people, purposefully distinct from Amazon Q Developer. Focuses on scaling AI dev to complex problems, improving agent control, and enhancing code quality and reliability.
2. **Spec-driven development compresses the SDLC**: Requirements discovery and design feedback happen in a tight inner loop. The spec becomes a living set of artifacts representing system state at a point in time, a structured workflow, and a set of tools for reproducible results.
3. **EARS format for requirements**: EARS (Easy Approach to Requirement Syntax) provides structured natural language ("when X then Y shall Z") that enables deterministic parsing by non-LLM systems, enabling property-based testing and automated reasoning.
4. **Property-based testing integration**: EARS requirements are translated into system invariants (properties). Property-based testing attempts to falsify these invariants; if no counterexample is found, there is high confidence the system meets requirements.
5. **Neurosymbolic reasoning strategy**: Kiro's backend may use non-LLM systems (classic automated reasoning techniques) alongside LLMs, with the goal of using LLMs less over time for quality-critical operations.
6. **MCP integration across all spec phases**: MCP servers can be used during requirements generation, design, and implementation. Examples include pulling tasks from Asana, fetching product examples from the web, and using AWS documentation MCP for research.
7. **Customizable artifacts**: Users can add wireframes, UI mocks, explicit test cases, and other content to any spec artifact because they are natural language documents. The agent can translate these into whatever format is needed.
8. **Steering as persistent memory**: Kiro's steering feature (analogous to Cursor rules) persists preferences like commit style, code coverage minimums, and deployment procedures across sessions.
9. **Spec as living documentation**: Specs are not one-off plans but living documents that are mutated over time. Kiro discovers existing specs and amends them rather than creating duplicates. Design doc reviews at Amazon have been replaced by spec reviews.
10. **Live demo: Dad joke generator**: Harris demoed "Gramps," a dad joke generator deployed to AWS Agent Core via CDK, using spec-driven development to add session persistence. The demo illustrated bias in initial prompts (S3 assumption) and the value of challenging the agent to research alternatives.
11. **Brownfield codebase strategy**: Kiro starts by reading the working tree. Success depends on separation of concerns and module cohesion. Well-structured codebases with good tests perform much better than monolithic ones with tech debt.
12. **Session management**: Kiro currently has no incremental pruning or summarization (as of talk date). Focus is on prompt caching hit rate (90-95% typical), which keeps interactions fast. Summarization feature exists but is slow (~30-45 seconds) and being improved.

## Entities

- [[AlHarris]] — Principal Engineer at Amazon, working on Kiro
- [[AmazonKiro]] — Amazon's agentic IDE for spec-driven development
- [[Amazon]] — Parent company of Kiro and AWS
- [[AgentCore]] — AWS service for deploying AI agents, used in the demo
- [[Asana]] — Task tracker used by the Kiro team, integrated via MCP
- [[AmazonS3]] — AWS object storage, used as a persistence backend in the demo
- [[AmazonDynamoDB]] — AWS NoSQL database, mentioned as an alternative to S3
- [[CodeOSS]] — The open-source VS Code base that Kiro is forked from
- [[Tessle]] — Company doing specs for knowledge bases, hosted a conference earlier that week
- [[Sonnet]] — Anthropic's Claude model family, referenced as a backend LLM for Kiro

## Concepts

- [[EARS]] — Easy Approach to Requirement Syntax: structured natural language format for requirements
- [[PropertyBasedTesting]] — Testing approach that attempts to falsify system invariants to prove correctness
- [[NeurosymbolicReasoning]] — Combining neural (LLM) and symbolic (classic automated reasoning) approaches
- [[Steering]] — Persistent agent memory/rules (like Cursor rules) for consistent behavior across sessions
- [[PromptCaching]] — Technique achieving 90-95% cache hit rate to keep agent interactions fast
- [[SpecAsLivingDocumentation]] — Specs that are mutated over time rather than created as one-off plans
- [[IncrementalDisclosure]] — Agent discovers context progressively rather than loading everything upfront
- [[AgentHooks]] — Event-driven extension points that fire at specific moments in the agent loop for deterministic verification

## Related

- [[SpecificationDrivenDevelopment]] — the broader paradigm Kiro implements
- [[VibeCoding]] — the approach Kiro aims to improve upon with structure
- [[MCP]] — protocol used extensively across all spec phases
- [[LangGraph]] — agent framework used in the demo project
- [[AWS]] — cloud provider for Kiro's deployment target
- [[Anthropic]] — provider of the Sonnet models powering Kiro
- [[ProgressiveContextDisclosure]] — related to Kiro's context management approach
- [[Hooks]] — related to Kiro's agent hooks for deterministic verification
