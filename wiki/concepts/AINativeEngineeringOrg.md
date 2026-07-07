---
title: "AI-Native Engineering Org"
type: concept
tags: [engineering-management, org-design, agentic-coding, ai-native]
sources: ["raw/01-articles/claude/2026-06-03 - Running an AI-native engineering org.md"]
last_updated: 2026-07-07
---

## Definition

An AI-native engineering org is one that has restructured its processes, team composition, and norms around the reality that agentic coding has eliminated traditional coding throughput as the primary bottleneck. Rather than letting obsolete processes persist, the org actively rewrites norms around planning, code ownership, review, and team structure to match the new constraint landscape where verification, code review, and security are the scarce resources.

## Key Information

### Bottleneck Shift

In a pre-AI engineering org, coding bandwidth was the expensive resource, driving heavy pre-planning (waterfall, then agile). In an AI-native org, coding, testing, and refactoring are rarely the slow part. New bottlenecks emerge:

- **Verification** — Is the generated code correct? How is it maintained?
- **Code review bandwidth** — How do humans keep up with reviewing AI-assisted code?
- **Security** — Higher throughput means more surface area and new ways to break things.
- **Cross-functional partners** — Product, design, and legal must keep pace with engineering speed.

### Planning: Just-in-Time (JIT)

Traditional roadmaps (e.g., six-month plans) become stale within months because the development speed itself accelerates change. The AI-native approach is [[JustInTimePlanning]] — doing just the right amount of planning at the right time, shifting away from design docs toward discussions in PRs and prototypes. The principle: "building is cheap, arguing is expensive."

### Code Ownership

Since all PRs are assisted by AI, "who made this change" is no longer a sufficient question. The AI-native norm is to reframe ownership questions around what you actually need to know — regression cause, expert lookup, or context on a decision — and ask AI first, with more data and context.

### Human-in-the-Loop Boundaries

AI handles style, linting, PR feedback, bug fixes, and test authoring via tools like [[CodeReview]]. Humans remain essential for:

- **Legal review** — risk tolerance decisions
- **Security-sensitive code** — trust boundaries and domain expertise
- **Product sense and taste** — PMs and designers

The right balance of trust vs. verify keeps changing as models improve, requiring continual re-evaluation.

### Team Composition

AI-native orgs index on two profiles rather than raw coding throughput:

- **Creative builders with product sense** — deeply curious about shipping products that solve problems
- **Engineers with deep systems expertise** — distributed systems, platform infrastructure

Roles blur across traditional boundaries: PMs code, engineers do content and design, nontraditional coders do engineering.

### Org Structure

- Flat orgs with pod-level autonomy within a small set of non-negotiable core principles.
- Pods choose how to use AI for triage, planning rituals, standups, and which workflows to automate first.
- Every manager starts as an individual contributor.

### Metrics

Track onboarding ramp-up time, PR cycle time, and share of AI-assisted commits — alongside product outcomes, not just raw throughput. Throughput is a metric, not the goal.

### Workflow Auditing

A core practice: regularly audit the noisiest (most expensive or dreaded) workflow, ask whether it still serves its original purpose, and either automate it or drop it entirely.

## Related

- [[summary-2026-06-03 - Running an AI-native engineering org]] — the blog article source
- [[summary-13 - Running an AI-native engineering org]] — the San Francisco transcript version
- [[summary-03 - Running an AI-native engineering org]] — the London transcript version
- [[FionaFung]] — Director of Engineering who articulated these principles
- [[JustInTimePlanning]] — the planning methodology
- [[AgenticCoding]] — the paradigm shift driving these org changes
- [[CodeReview]] — the automated review tool that handles routine review
- [[ClaudeCode]] — the product whose team exemplifies these principles
- [[Anthropic]] — the company
- [[AINativeStartup]] — the startup-level analogue for AI-native organizational design
- [[ClaudeCodeRoutines]] — automation practice for replacing manual rituals
- [[ExplorePlanCodeCommit]] — the workflow whose planning phase was transformed by JIT planning
