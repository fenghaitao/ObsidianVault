---
title: "summary-20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom"
type: source
tags: [source, transcript, ai, engineering-throughput, claude-code, agent-skills, code-review, developer-productivity, intercom, organizational-change]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom.md"]
last_updated: 2026-06-30
---

## Core Summary
Brian Scanlan, Senior Principal Engineer at Intercom, presents how Intercom's "2x" project achieved doubling engineering throughput (measured as code changes per R&D person) in under a year. The strategy: go all-in on Claude Code as a unified AI coding platform, build a flywheel of high-quality durable skills, drive organizational change through clear executive guidance and full-time staffing, and automate code review. Key principles include giving agents problems not tasks, treating all engineering work as agent-first, and practicing continuous improvement on skills through backtesting and feedback loops.

## Key Points

### The 2x Project
- Intercom set a goal mid-2024: double engineering throughput in one year
- Primary metric: code changes per R&D person, despite acknowledged limitations (Goodhart's Law)
- Goal reached faster than one year, with a wild inflection point after consolidating on Claude Code in December 2024
- PR throughput from Claude Code is now in the 90%+ range
- Code review became the new bottleneck — 17.6% of PRs are now auto-approved by agents
- Defects are being closed faster than ever; some teams inspired to pursue "backlog zero"
- Stanford research group independently confirmed code quality has been increasing

### Organizational Change
- Updated job descriptions: if you're not adopting AI at Intercom, you are not meeting expectations — binary
- Staffed the 2x initiative full-time with a dedicated, growing team
- Constant executive messaging across every forum about the urgency of AI adoption
- Celebrated and rewarded AI adoption wins across Slack channels
- Ran hackathons and AI immersion days
- Recognized that AI adoption is unevenly distributed — created a maturity model for engineers

### Platform Consolidation
- Previously let engineers choose their own editors (Cursor, Augment, GitHub Copilot)
- Mid-2024: chose Claude Code as the unified platform
- Philosophy: "choosing one is important" — you don't get compounding benefits of a well-designed platform if spread across multiple tools
- Avoid "model anxiety" — analogous to being multi-cloud and missing compounding benefits
- Vision: Claude Code should act as a senior engineer on any technical task across Intercom
- Connected Claude Code to everything: production systems, internal tools, all workflows
- Onboarded Claude Code with all Intercom-specific knowledge: Rails conventions, architecture, React patterns, testing standards, security rules

### Skills Flywheel
- Encapsulated knowledge in engineering captures, skills, guidance, and hooks
- Focus on small, high-quality, durable, testable skills that do one job extremely well
- Used backtesting against historical work (code changes, incidents) to validate skill quality
- Continuous improvement: get skills to be self-updating and high quality
- Internal Claude Code plugins pushed to all laptops, bypassing update mechanisms
- Hundreds of contributors, tens of thousands of lines of code in Claude Code plugins
- Example: a flaky spec fixing skill built through feedback loops, not manual authoring — the agent wrote it through guided iteration
- All session transcripts pulled into S3 for data mining, reporting, and skill effectiveness analysis

### Principles for AI Adoption
- **All engineering is changing**: everything an engineer can do, the agent must be able to do
- **Give problems, not tasks**: describe the problem and let the agent figure out which skills to invoke
- **Technically conservative**: use single tools extremely well (same philosophy behind Ruby on Rails monolith)
- **Build durable components**: the tools change, but writing down how to do work at Intercom will always be valuable
- **Don't get stuck behind the curve**: use what others ship rather than building everything in-house
- **Job is moving up the stack**: analogous to the sysadmin-to-SRE transition when cloud arrived

### Automated Code Review
- 17.6% approval rate for automatic code review — not simple "Claude approve this"
- Used backtesting with human-labeled outputs to build confidence
- Shaped pull requests toward very safe and simple changes that should have always been auto-approved
- Worked with auditors to ensure SOC 2, ISO 27001, HIPAA compliance without humans in the loop
- Uses multimodal code reviews including Codex for code review — "multimodal code reviews are okay"
- Believes automated review is removing risk, not adding it, because humans aren't as good as well-defined agents

### Engineering AI Maturity Model
- Level 1: Use Claude Code for everything
- Level 2: Automate your work, then move it to a skill
- Level 3: Get really good at writing skills
- Level 4: Write and approve skills
- Level 5: Optimize the environment for agents (software architecture, documentation, ways of working)

### Intercom's AI Transformation
- 15-year-old Irish-American B2B SaaS company, ~1,400 people
- Pivoted to be an AI company "the weekend ChatGPT came out"
- Finn: AI agent for customer support with 8,000+ customers, revenue approaching $100M
- Launched Finn on the day GPT-4 came out — first product released on GPT-4
- Now serving 100% of Finn with Intercom's own model, outperforming frontier models
- ~2 million resolutions per week
- Used by Anthropic, Snowflake, Linear, Glean, LaunchDarkly for their customer support
- Claude Code is widely used across Intercom outside of software — gone "completely viral"

## Related
- [[BrianScanlan]] — speaker
- [[Intercom]] — company
- [[ClaudeCode]] — unified platform chosen
- [[Finn]] — Intercom's AI customer support agent
- [[Honeycomb]] — observability tool for skill invocation tracking
- [[DX]] — developer productivity measurement tool used
- [[Stanford]] — research partner studying code quality
- [[Ruby on Rails]] — Intercom's primary tech stack
- [[Doubling Engineering Throughput]] — the 2x concept
- [[Platform Consolidation for AI Coding]] — choosing one AI coding platform
- [[Automated Code Review and Approval]] — agent-driven PR approval
- [[Skills Flywheel]] — continuous improvement cycle for agent skills
- [[Model Anxiety]] — fear of missing out on different models
- [[Backtesting Agent Skills]] — validating skills against historical data
- [[Engineering AI Maturity Model]] — levels of AI adoption for engineers
- [[Agent-First Software Development]] — everything the agent must be able to do
- [[Agent Skills]] — Intercom's approach to durable skills
- [[DeveloperProductivityMeasurement]] — code changes per R&D person metric
- [[GoodhartsLaw]] — acknowledged limitation of the chosen metric
- [[AgentReviewerApprover]] — automated PR review and approval pattern
- [[GitHubCopilot]] — early tool adopted before consolidation
- [[Cursor]] — tool used before consolidation
- [[Augment Code]] — tool evaluated before consolidation
- [[Anthropic]] — Claude Code provider
- [[Codex]] — used for multimodal code review
- [[AmazonS3]] — session transcript storage
- [[ContinuousImprovement]] — underlying philosophy for skills flywheel
- [[ProgressiveDisclosure]] — used in skill organization
- [[SOC 2]] — compliance certification
- [[ISO 27001]] — compliance certification
- [[HIPAA]] — compliance certification
