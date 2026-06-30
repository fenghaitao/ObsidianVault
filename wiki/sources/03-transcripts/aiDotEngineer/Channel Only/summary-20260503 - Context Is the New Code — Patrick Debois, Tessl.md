---
title: "Context Is the New Code — Patrick Debois, Tessl"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"
date: 2026-05-03
ingested: 2026-06-29
tags: [context, context-engineering, devops, context-development-life-cycle, skills, evals, agent-observability, security]
---

## Core Thesis
Patrick Debois proposes that context is the new code — as AI coding agents become the primary interface for software development, the scarce resource shifts from writing code to crafting, testing, distributing, and observing context. He draws a parallel to the DevOps movement (which he helped pioneer in 2009) and introduces the "Context Development Life Cycle" (CDLC): Generate → Test → Distribute → Observe → Adapt.

## Key Topics
- **Context as the New Code**: Debois observes he barely touches code anymore — he tells the AI to do things. Context (prompts, instructions, skills, documentation) is what's being authored, and code is what's being generated from it.
- **Code Transforming Back into Context**: Large pieces of code are being turned into skills — reusable workflows that solve more problems than hardcoded logic ever could. Example: an onboarding skill that figures out the user's package manager, ecosystem, and guides them through steps.
- **The DevOps Parallel**: In 2009, Debois asked "what if ops looked more like dev?" which sparked the DevOps movement. Now he asks "what if context is the code?" — applying software engineering rigor to context management.
- **Context Development Life Cycle (CDLC)**: An infinity loop with five phases:
  - **Generate**: Creating context through prompting, reusable instructions (agent.md/Claude.md), pulling in library documentation, fetching context from MCP servers (GitLab, GitHub, Slack), and spec-driven development.
  - **Test**: Validating context through linting (format validation), Grammarly-like comprehension checks, LLM-as-judge evaluations (e.g., "does the generated code prefix URLs with /awesome?"), and end-to-end agent tests in sandboxes.
  - **Distribute**: Sharing context via repo check-ins, packaging context as libraries (skills), registries for discovery (e.g., Tessl registry), dependency management, and security scanning (Snyk for context, AI SBOM).
  - **Observe**: Getting feedback from agent logs, PR reviews, and production instrumentation. If agents consistently miss something, surface it and create context for it.
  - **Adapt**: Using feedback to optimize and regenerate context, running evals in CI/CD with error budgets (since LLM outputs are non-deterministic).
- **Non-deterministic Testing**: Unlike traditional tests, LLM evals are non-deterministic. Run them 5 times and measure success rate. Use error budgets — some tests can fail occasionally, others must pass consistently.
- **Context Packaging and Registries**: Skills are becoming a standard package format. Registries like Tessl's marketplace allow discovery, but 99.9% of skills are low quality. Organizations will want their own private registries.
- **Context Dependency Hell**: Just like code dependencies, context packages will have conflicts (e.g., frontend context conflicting with React context).
- **Context Security**: Snyk scans context for credential exposure and third-party risks. AI SBOM (Software Bill of Materials) tracks what model built a skill and how it was constructed. Context filters act like web application firewalls, filtering prompt injections and malicious patterns before they reach the agent.
- **Context Filter**: A "web application firewall for context" that filters out prompt injections and malicious patterns before they enter the agent's context. Necessary because agents load agent.md and skills.md without restrictions.
- **The Flywheel**: Individual solo model (crafting personal context) → Team model (making context improvement a reflex) → Organizational model (cross-team context reuse flywheel).
- **LLMs Are Just the Engine**: The LLM is the engine; context is the fuel. You can't change the LLM, but you can optimize your context. The message: engineer context rather than copy-pasting and hoping for the best.

## Entities
- [[PatrickDebois]] — speaker, pioneer of DevOps, now at Tessl
- [[Tessl]] — company building context development lifecycle tooling, implementing pieces of the CDLC
- [[Snyk]] — security scanning for context (credential handling, third-party exposure)
- [[AIDevCon]] — AI developer conference curated by Debois in London (June 1-2)
- [[aiDotEngineer]] — the AI Engineer conference where this talk was given

## Concepts
- [[ContextDevelopmentLifeCycle]] — the CDLC infinity loop: Generate → Test → Distribute → Observe → Adapt
- [[ContextAsCode]] — the paradigm shift from writing code to crafting context
- [[ContextTesting]] — validating context through linting, comprehension checks, LLM-as-judge, and end-to-end tests
- [[ContextDistribution]] — sharing context via repos, packages, registries, and dependency management
- [[ContextObservability]] — getting feedback on context from agent logs, PR reviews, and production
- [[ContextFilter]] — a WAF-like filter for prompt injections and malicious context patterns
- [[ContextPackageRegistry]] — registries for discovering and distributing context packages (skills)
- [[ContextDependencyHell]] — version conflicts between context packages
- [[AISBOM]] — AI Software Bill of Materials tracking how skills were built
- [[NonDeterministicTesting]] — testing LLM outputs requires statistical approaches (run N times, measure success rate)
- [[ErrorBudgetsForContext]] — allowing some context tests to fail occasionally due to non-determinism
- [[ContextFeedbackLoop]] — using agent logs, PR feedback, and production data to improve context
- [[ContextSecurity]] — scanning context for credentials, prompt injections, and supply chain risks
- [[ContextOptimization]] — using test feedback to iteratively improve context quality

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — harness engineering as a related paradigm
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — context engineering
- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — skills replacing code
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — skills as package format
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — eval challenges
