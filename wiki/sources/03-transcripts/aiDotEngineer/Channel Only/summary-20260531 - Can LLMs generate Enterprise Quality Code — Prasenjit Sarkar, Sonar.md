---
title: "summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar"
type: source
tags: [source, transcript, llm-code-quality, enterprise-code, code-security, code-maintainability, sonar, code-evaluation, llm-leaderboard, agentic-development]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Core Summary
Prasenjit Sarkar (Sonar) presents Sonar's evaluation framework that assesses LLM-generated code beyond functional correctness — measuring bugs, security issues, complexity (cyclomatic and cognitive), and verbosity across 4,444+ Java programming assignments. The findings show that even top-performing models on SWE-bench (Gemini 3.1 Pro High at 84.17% pass rate) generate code with significant quality problems: hundreds of security issues and bugs per million lines of code, wildly varying verbosity (from 250K to 1.2M LOC for the same tasks), and increasingly subtle bugs that are harder for humans to detect. Sonar proposes the ACDC (Agent-Centric Development Cycle) framework — Guide, Verify, Solve — to embed code quality checks throughout the AI-assisted development lifecycle, including pre-commit analysis, context augmentation, and automated remediation.

## Key Points

### The Shift to Agentic Coding
- Adnan Qureshi declared that English is now the new programming language — developers give instructions to agents
- Pragmatic Engineer Survey (March 2026): 55% of developers now regularly use AI agents
- The question: do you trust the code? Is it maintainable, secure, readable?

### What LLM Benchmarks Miss
- LLM leaderboards (HumanEval, MBPP, SWE-bench) measure functional correctness on test cases
- Missing dimensions: security, real-world reliability, engineering/architectural problems, engineering discipline, code maintainability, tech debt generation, and context-aware analysis
- High pass rates (80%+) obscure serious quality issues

### Sonar's Evaluation Findings (4,444+ Java assignments)
- **Gemini 3.1 Pro High**: 84.17% SWE-bench pass rate, 307K LOC, 234 cyclomatic complexity, 614 bugs/M LOC, 210 security issues/M LOC
- **Claude Sonnet 4.6**: 627K LOC, ~300 security issues/M LOC — highest security risk
- **GPT 5.4 / GPT 5.4 Pro High**: 1.2M LOC — highest verbosity (4x more code than Gemini)
- Newer models generate increasingly more lines of code but also higher complexity
- As models mature via reinforcement learning, they fix known issues but introduce subtler, harder-to-detect bugs
- Total vulnerabilities per model are decreasing but shifting to different categories

### Root Causes of Poor Code Quality from LLMs
- **Mixed quality training data**: open source and other sources contain insecure code examples alongside good ones
- **Built-in security flaws**: datasets used for training contain inherent vulnerabilities that models learn
- **Hidden bugs in training data**: subtle logic errors that cause models to produce failing code
- **LLM probabilistic nature**: same prompt to same model on different days produces different code
- **Limited context**: models don't understand company-specific codebases, data, or architecture
- **Not explainable**: hard to diagnose and improve when generation goes wrong

### Sonar Leaderboard
- Publicly available at sonar.com/leaderboard
- 53+ models evaluated across multiple dimensions
- Provides pass rates, issue density, lines of code, cyclomatic complexity, cognitive complexity
- Enables informed model selection based on organizational architecture needs

### Cyclomatic vs Cognitive Complexity
- **Cyclomatic complexity**: measures branches — if/else, for loops, while loops, switch statements
- **Cognitive complexity**: Sonar proprietary metric — how difficult code is for a human to read, understand, and maintain

### ACDC Framework (Agent-Centric Development Cycle)
Three stages with inner and outer loops:

**Guide Phase:**
- **Sonar Sweep** (private beta): treats/trains data to prevent problematic code generation at the source
- **Sonar Context Augmentation**: pushes full codebase context into the LLM

**Verify Phase:**
- **SonarQube Agentic Analysis** (open beta): analyzes code at runtime before commit — 1-5 seconds vs 1-5 minutes for CI
- Agent receives analysis, fixes issues before commit, then PR analysis runs

**Solve Phase:**
- **SonarQube Remediation Agent** (open beta): fixes slipped-through issues post-PR
- Creates one PR per issue with fix, re-runs analysis and compilation, discards regressions
- Can bulk-fix tech debt from the SonarQube dashboard

### Sonar's Product Portfolio
- 40+ programming languages and frameworks supported
- All DevOps integrations, IDE marketplace presence
- Partnerships across the ecosystem

## Related
- [[Prasenjit Sarkar]] — speaker
- [[Sonar]] — company
- [[SonarQube]] — code quality platform
- [[Enterprise Quality Code]] — core concept
- [[LLM Code Quality Evaluation]] — Sonar's evaluation framework
- [[Cyclomatic Complexity]] — complexity metric
- [[Cognitive Complexity]] — Sonar proprietary complexity metric
- [[ACDC Framework]] — Agent-Centric Development Cycle
- [[Sonar Leaderboard]] — public model quality leaderboard
- [[Mixed Quality Training Data]] — root cause of quality issues
- [[Code Verbosity]] — lines of code generation trends
- [[Gemini 3.1 Pro]] — top-performing model in evaluation
- [[Claude Sonnet 4.6]] — highest security risk model
- [[GPT 5.4]] — highest verbosity model
- [[GPT 5.2]] — referenced for verbosity comparison
- [[SWEBench]] — benchmark measuring functional correctness only
- [[Adnan Qureshi]] — quoted on English as the new programming language
- [[PragmaticEngineer]] — March 2026 survey cited
- [[aiDotEngineer]] — conference
