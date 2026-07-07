---
title: "Agentic Coding"
type: concept
tags: [ai-development, automation, workflow, autonomous-systems]
sources: ["raw/01-articles/claude/2025-10-15 - How to scale agentic coding across your engineering organization.md", "raw/01-articles/claude/2025-10-30 - Introduction to agentic coding.md", "raw/01-articles/claude/2025-12-01 - What are the key benefits of transitioning to agentic coding for software development.md", "raw/01-articles/claude/2026-01-21 - Eight trends defining how software gets built in 2026.md", "raw/01-articles/claude/2026-05-26 - Code w Claude London 2026 Rethinking how we build.md", "raw/01-articles/claude/2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system.md", "raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md", "raw/01-articles/claude/2026-06-03 - Running an AI-native engineering org.md"]
last_updated: 2026-07-07
---

# Agentic Coding

Agentic coding refers to the use of autonomous AI agents to assist with software development tasks. These agents can analyze code, generate solutions, run tests, and iterate independently, with human developers providing guidance and validation.

## Collapsing the Idea-to-Execution Gap

At Code w/ Claude London 2026, [[BorisCherny]] (Head of [[ClaudeCode]]) described agentic coding as collapsing the distance between "I have an idea" and "it runs" — the same magic he felt as a student writing TI-83 programs to solve math homework. Over decades, compilers, typecheckers, and build systems pushed that distance further out. With AI agents, it's collapsing again: you describe a problem, and the program shows up. "It's the calculator feeling, except the calculator can write a distributed system." See [[summary-2026-05-26 - Code w Claude London 2026 Rethinking how we build]].

## The Planning-First Imperative

As AI coding tools collapse the time between idea and prototype, a new failure mode has emerged: code that compiles and passes tests but doesn't solve the intended problem. [[CodeRabbit]]'s analysis of AI-generated pull requests found this to be the most frequent failure mode, caused by developers omitting requirements they consider obvious and coding agents filling gaps with plausible but incorrect assumptions.

CodeRabbit's response was an [[AgentOrchestration|agent orchestration]] layer that inserts a structured planning phase before any code is generated. The system coordinates multiple [[Claude]] model tiers (using [[ModelTiering]]) to analyze requirements, surface hidden assumptions, and produce a collaborative Product Requirements Document (PRD) that stakeholders review before implementation begins. The core thesis: planning quality determines output quality, and the cheaper code generation gets, the more expensive it becomes to move in the wrong direction.

This planning-first approach complements [[ClaudeCode]]'s built-in [[ExplorePlanCodeCommit|Plan Mode]] — CodeRabbit's orchestration sits above it as a higher-level planning phase that makes everything explicit and surfaces all assumptions before Claude Code begins its own planning and implementation. See [[summary-2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system]].

## Pattern

Agentic coding dissolves the boundary between technical and non-technical work, enabling anyone who can describe a problem to build solutions. Rather than acting as a simple code generator, agentic tools work best as thought partners that explore possibilities, prototype rapidly, and collaborate with humans through iterative refinement.

## Applications at Anthropic

[[ClaudeCode]] is used across [[Anthropic]] teams for:
- **Onboarding & Navigation** — Accelerating codebase comprehension for new hires
- **Testing & Review** — Automating unit test creation and code review through [[TestDrivenDevelopment]]
- **Production Debugging** — Diagnosing and fixing incidents 3x faster
- **Rapid Prototyping** — Building features and full applications quickly
- **Knowledge Consolidation** — Creating runbooks and documentation from scattered sources
- **Custom Automation** — Building tools without dedicated development resources

## Three Generations of AI Coding Assistance (October 2025)

- **Autocomplete tools**: analyze only the current file or a few nearby files to predict the next fragment; good for boilerplate and established patterns, but can't trace cross-service data flow or understand architecture.
- **Conversational tools** (e.g., [[Claude.ai]]): chat-based analysis of pasted snippets, errors, or architectural questions; supports iterative refinement, but orchestrating changes across many files remains manual — copying files in and results back out.
- **Agentic systems** (e.g., [[ClaudeCode]]): operate at the project level — read config and test files to infer setup and conventions, trace imports to map dependencies, form an adaptive multi-step plan, then implement across files (handlers, middleware, schemas, docs, tests), requesting approval before modifying files by default. Transforms the loop from "write code, run tests, read errors, fix code, repeat" into "define goal, review proposed changes, approve implementation."
- Example: [[Rakuten]]'s engineering team had Claude Code implement a full activation-vector extraction method in vLLM (12.5M lines, Python/C++/CUDA) in seven hours of autonomous work with only occasional guidance, reaching 99.9% numerical accuracy against the reference method.

## Organizational Case for Agentic Coding (December 2025)

- **Development speed**: [[AugmentCode|Augment Code]] (built on Claude via [[VertexAI]]) documented an enterprise customer completing in two weeks a project estimated at four to eight months traditionally.
- **Onboarding**: drops from weeks/months to one or two days, since new developers can query an agent with perfect codebase recall instead of interrupting senior engineers — broadening who can safely touch critical systems.
- **Autonomous problem-solving**: unlike fixed scripts, agents assess dynamically and pivot to alternative hypotheses when an initial debugging theory fails, rather than stopping.
- **Scaling without linear headcount growth**: agents don't incur the communication overhead that limits human team scaling, letting a 10-engineer team supported by agents tackle workloads that traditionally need 20–30.
- **Code quality**: systematic analysis catches race conditions, memory leaks, security vulnerabilities, and N+1 patterns that deadline-pressured manual review might miss.
- **Democratized expertise**: [[Grafana]]'s Claude-powered assistant lets users without PromQL/LogQL knowledge query observability data in natural language — the same pattern extends to frontend devs optimizing databases or backend specialists improving UI performance.

## 2026 Agentic Coding Trends (January 2026)

Anthropic's Societal Impacts team found developers use AI in roughly 60% of their work but can "fully delegate" only 0-20% of tasks — framing agentic coding as active collaboration requiring supervision and judgment, not autonomous replacement. Customer examples: [[Rakuten]] (7-hour autonomous vLLM implementation, 99.9% accuracy), [[TELUS]] (13,000+ custom AI solutions, 30% faster code shipping, 500,000+ hours saved), [[Zapier]] (89% org-wide AI adoption, 800+ internally deployed agents). Four flagged 2026 priorities: mastering [[MultiAgentSystem|multi-agent coordination]], scaling human-agent oversight via AI-automated review, extending agentic coding beyond engineering teams, and embedding security architecture from the earliest stages.

## Key Success Factor

The most successful teams treat agentic coding tools as thought partners rather than code generators, exploring possibilities, prototyping rapidly, and sharing discoveries across technical and non-technical users.

## Scaling Across an Organization (October 2025)

Anthropic's guidance for moving agentic coding from isolated experiments to org-wide adoption:

- **Common applications**: legacy system modernization, faster onboarding (querying codebases directly for architecture/dependencies), SRE/DevOps incident-response assistance, and broader technical participation (PMs, designers prototyping directly).
- **Pilot phase**: start with 20-50 developers already using AI-assisted tools; validate against the codebase, identify useful workflows, and build internal expertise; have them document what works and what doesn't.
- **Kickoff over phased rollout**: a shared kickoff/hackathon event (with food) tends to work better than staggered access — skeptical engineers often change their view after hands-on experience.
- **Pilot group as advisors**: once adoption broadens, the pilot group transitions into running workshops and creating educational content — internal champions tend to outperform external training since they know the org's specific pain points.
- **Success metrics beyond lines of code**: sprint throughput, task completion time, migration velocity, developer satisfaction, onboarding duration, cross-functional efficiency. [[ClaudeCode]]'s **Activity Metrics** track lines of code accepted, suggestion acceptance rates, daily active users/sessions, and org-wide/per-user spend.
- **Common pitfalls and fixes**: overly broad tasks without structure (fix: [[TestDrivenDevelopment]] — write tests defining success first, implement incrementally); vague bug reports (fix: share complete error info, screenshots, and expected-vs-actual behavior); vague prompting generally (fix: high-level goal first then details, concrete examples, sequential prompts, specific feedback).
- **[[CLAUDE-md|CLAUDE.md]] as shared documentation**: check project-level files into the repo root, update them alongside architectural changes in the same PRs, and include them in onboarding.

## Organizational Ownership at Scale (May 2026)

Technical configuration alone doesn't drive adoption in large engineering organizations; the rollouts that spread fastest paired it with a dedicated organizational layer:

- **Pre-rollout infrastructure investment**: a small team, sometimes just one person, wires up tooling (plugins, MCP servers, CLAUDE.md conventions) before broad access, so a new engineer's first experience with [[ClaudeCode]] is productive rather than frustrating.
- **Dedicated roles**: an emerging "agent manager" role — a hybrid PM/engineer function dedicated to managing the Claude Code ecosystem. For organizations without a dedicated team, the minimum viable version is a **DRI** (directly responsible individual): one person with authority over settings, permissions policy, the plugin marketplace, and [[CLAUDE-md|CLAUDE.md]] conventions, and responsibility for keeping them current.
- **Centralizing bottoms-up enthusiasm**: bottoms-up adoption generates enthusiasm but fragments without someone to assemble and evangelize what works (a standardized CLAUDE.md hierarchy, a curated set of skills/plugins) — without that centralizing work, knowledge stays tribal and adoption plateaus.
- **Governance in regulated industries**: cross-functional working groups (engineering, information security, governance representatives) established early to define requirements and a rollout roadmap together produced the smoothest deployments; a common starting point is a defined set of approved skills/plugins, required code-review processes for AI-generated code, and limited initial access, expanding as confidence builds.
- Where the org falls under Developer Experience/Developer Productivity, that function typically owns Claude Code management since it already owns onboarding and developer tooling.

See [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]].

## Bottleneck Shift and AI-Native Orgs (June 2026)

As agentic coding becomes the default way of working, the bottleneck shifts from coding throughput to verification, code review, and security. On the [[ClaudeCode]] engineering team at [[Anthropic]], coding, testing, and refactoring rarely slow work down anymore — but the questions "Is this code correct?" and "How is it maintained?" became the new constraints. This forces a broader organizational transformation toward an [[AINativeEngineeringOrg|AI-native engineering org]]:

- **Planning** shifts from long-range roadmaps to [[JustInTimePlanning|JIT planning]], with technical debates settled by generating competing PRs rather than whiteboarding ("building is cheap, arguing is expensive").
- **Code ownership** is redefined: since all PRs are AI-assisted, "who made this change" is replaced by "what do you actually need to know?" — and the first step is asking Claude.
- **Human review** is reserved for where it still matters: legal review, security-sensitive code, and product taste — while [[CodeReview|automated review]] handles style, linting, bug fixes, and test authoring.
- **Team composition** shifts from raw throughput to two profiles: creative builders with product sense, and engineers with deep systems expertise.
- **Roles blur**: PMs code, engineers do design and content, nontraditional coders do engineering.
- **Metrics** track onboarding ramp-up time, PR cycle time, and share of Claude-assisted commits — alongside product outcomes, not just throughput.

See [[summary-2026-06-03 - Running an AI-native engineering org]].

## Related

- [[ClaudeCode]] — Primary agentic coding tool
- [[TestDrivenDevelopment]] — Methodology accelerated by agentic coding
- [[Anthropic]] — Company pioneering agentic coding workflows
- [[CLAUDE-md]] — recommended as shared, version-controlled living documentation during rollout
- [[summary-2025-10-15 - How to scale agentic coding across your engineering organization]] — organizational rollout methodology article
- [[Claude.ai]] — the conversational tier contrasted with agentic coding
- [[Rakuten]] — customer example of large-scale autonomous implementation
- [[summary-2025-10-30 - Introduction to agentic coding]] — definitional article contrasting autocomplete, conversational, and agentic tools
- [[AugmentCode]] — cited customer example (development speed)
- [[Grafana]] — cited customer example (democratized expertise)
- [[summary-2025-12-01 - What are the key benefits of transitioning to agentic coding for software development]] — organizational-benefits article
- [[TELUS]] — cited customer example (2026 trends)
- [[Zapier]] — cited customer example (2026 trends)
- [[MultiAgentSystem]] — flagged 2026 priority area
- [[summary-2026-01-21 - Eight trends defining how software gets built in 2026]] — 2026 Agentic Coding Trends Report teaser
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — organizational ownership models (DRI, agent manager role, cross-functional governance) for scaling Claude Code adoption
- [[Zoox]] — customer providing feedback on organizational rollout practices
- [[BorisCherny]] — Head of Claude Code, articulated the "collapsing distance" framing at London 2026
- [[summary-2026-05-26 - Code w Claude London 2026 Rethinking how we build]] — London 2026 event recap with keynote framing
- [[DynamicWorkflows]] — massively parallel subagent orchestration pushing agentic coding to quarter-scale tasks
- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — dynamic workflows announcement
- [[CodeRabbit]] — built a planning-first orchestration layer to prevent assumption-driven failures
- [[AgentOrchestration]] — the orchestration pattern that inserts structured planning before code generation
- [[ModelTiering]] — matching model tiers to task complexity for cost and quality optimization
- [[summary-2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system]] — source article on planning-first agentic coding
- [[AINativeEngineeringOrg]] — organizational design for engineering teams where agentic coding is the default
- [[JustInTimePlanning]] — planning methodology for AI-native teams
- [[summary-2026-06-03 - Running an AI-native engineering org]] — blog article on the Claude Code team's org transformation
- [[summary-19 - The expanding toolkit]] — source summary
- [[summary-03 - Agent Battle： Mine the most diamonds in 45 minutes]] — source summary
