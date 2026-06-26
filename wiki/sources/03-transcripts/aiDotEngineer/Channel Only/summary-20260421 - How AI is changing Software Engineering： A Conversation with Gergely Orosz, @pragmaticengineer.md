---
title: "summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer"
type: source
tags: [source, transcript, ai, software-engineering, token-maxing, developer-productivity, big-tech, infra, career]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md"]
last_updated: 2026-06-26
---

## Core Summary
Gergely Orosz (The Pragmatic Engineer) joins swyx at AI Engineer for a wide-ranging conversation on how AI is reshaping software engineering. He shares insider stories about "token maxing" at Meta, Microsoft, and Salesforce — where engineers artificially inflate AI token usage to avoid appearing on the bottom of internal leaderboards. The discussion covers the changing role of software engineers (DevOps, testing, and product roles collapsing into engineering), why large companies are rebuilding their entire internal infra around AI, Shopify's strategy of trading churn for competitive advantage, and the growth of The Pragmatic Engineer newsletter.

## Key Points

### Token Maxing
- At Meta, Microsoft, and Salesforce, token output is measured — sometimes via leaderboards, sometimes via dollar spend tracking
- Meta had a leaderboard where people's token counts were visible; it was taken down after an article made them look bad, but token maxing continues
- Engineers game the system: asking agents to summarize docs instead of reading them, running autonomous agents to build junk just to increase token count
- At Salesforce, there's a minimum spend target per month (~$175), so people token max at the beginning of each month
- Token count is used as one data point in performance evaluations at Meta — can be "weaponized" (low performer + low tokens = "not even trying"; high performer + high tokens = "innovating")
- Gergely compares it to the old "lines of code" metric — equally stupid, but now happening at top-tier companies
- Coinbase CEO Brian Armstrong sent an email requiring all engineers to use AI tools, then fired an engineer a week later who didn't comply

### Why Leadership Pushes AI Adoption
- 6 months prior, CTOs were worried engineers were too skeptical of AI and not using it enough
- Experienced engineers found AI tools only "mildly useful" on existing codebases — not helping with refactoring or bug finding
- Leadership kept hearing Anthropic's stats about writing code with Claude, saw revenue going up, and concluded "we should be using it more"
- The push came from leadership wanting engineers to "use freaking AI" — they see it as "better than not using it"
- Big Tech selects for people willing to put up with BS (LeetCode interviews, token maxing) — the same personality type that grinds LeetCode for 2-3 months will also token max to keep the job

### Is AI Making Us More Productive?
- Individually yes, but as teams it's unclear — "we should be moving faster"
- The meter study (small sample, 30 people): participants felt 20% more productive but were actually 20% less productive on average — one outlier was genuinely more productive
- swyx's observation: enabling non-coding collaborators to code with agents is where the real productivity gain is — "serverless developers" who don't have to wait for engineers
- Simon Willison said after 2 years of using AI, he's still figuring out what works — there's no manual
- Understanding the theory (transformers, attention, etc.) does not make you better at using the tools — "absolute mind fuck"
- Teams getting the most value: low ego, open to learning, open to "leaving your priors behind"

### The Changing Role of Software Engineer
- DevOps collapsed into the engineer role in the mid-2010s (especially at VC-funded startups)
- Dedicated tester role has collapsed into engineering
- Product role is now starting to collapse — "product engineer" emerging
- Early career engineers are expected to do more senior-level work: planning, business understanding
- John Deere (200-year-old company): two-pizza teams are becoming one-pizza teams, partially due to AI tools

### Engineer as Manager of Agents?
- Gergely pushes back on the "everyone's an engineering manager now" framing
- Managing agents is more like a tech lead role — you orchestrate but don't deal with people problems, conflict, or personal issues
- DHH (creator of Ruby on Rails) calls it a "mech suit" — you can do seven things at once, faster, and you're in control
- Mitchell Hashimoto runs exactly two agents — "two is enough for me"
- The feedback loop with agents is much faster than managing people (where results take 6 months)

### Large Tech Rebuilding Internal AI Infra
- Uber, Airbnb, Intercom, Meta, Microsoft, and mid-size companies are all building custom AI infra
- Examples: custom background coding agents integrated into monorepos, MCP gateways integrated with service discovery, retooled on-call tooling, AI-categorized code review systems
- Three reasons: (1) low-risk way to get hands-on with AI, (2) custom solutions work better for massive codebases that don't fit in context windows, (3) anything with "AI" in it gets funded — "agent experience" gets headcount, "developer platform" doesn't
- Gergely predicts: by next year, every large company will have built the same things

### Shopify's AI Strategy: Churn as Investment
- Shopify was the first company to get GitHub Copilot access in 2021 — a full year before public release
- Farhan Thawar (head of engineering) pinged Thomas Dohmke (GitHub CEO) directly: "We would like to roll out to all of Shopify, and in return, we will give you feedback for 3,000 people"
- Shopify gives unlimited AI tool budget and spends significant time ironing out bugs
- Strategy: trade off churn and expense to be 6 months ahead of competition
- Farhan: "It would look silly if I said you cannot have these tools — how would I hire the best?"
- Innovation + recruitment advantage makes the churn worth it

### The Pragmatic Engineer Newsletter
- Started during COVID after Uber layoffs — Gergely's team was hit, morale was low
- First article was about Uber's platform/product split — never written about publicly before
- Felt product-market fit immediately: 100 paid subscribers ($100/year) before publishing anything; 1,000 in 6 weeks (matching his old Uber base salary)
- Strategy: said no to all interviews, collaborations, podcasts for 2 years — just focused on writing
- Number one paid technology newsletter for 3 years; now SemiAnalysis has overtaken
- Started a podcast 1.5 years ago; grew the team with researchers

## Related
- [[GergelyOrosz]] — speaker, author of The Pragmatic Engineer
- [[PragmaticEngineer]] — the newsletter
- [[swyx]] — host, founder of AI Engineer
- [[TokenMaxing]] — key concept discussed
- [[GoodhartsLaw]] — "whatever gets measured gets abused"
- [[MechSuit]] — DHH's metaphor for AI-augmented development
- [[OnePizzaTeam]] — teams shrinking with AI
- [[ProductEngineer]] — emerging role
- [[InternalAIPlatform]] — companies building custom AI infra
- [[ChurnAsInvestment]] — Shopify's strategy
- [[DeveloperProductivityMeasurement]] — token counts, leaderboards
- [[LeavingPriorsBehind]] — mindset for AI adoption
- [[Meta]] — token maxing, leaderboard
- [[Microsoft]] — token maxing, leaderboard
- [[Salesforce]] — minimum AI spend targets
- [[Coinbase]] — Brian Armstrong firing engineer over AI usage
- [[Shopify]] — early Copilot access, churn as investment
- [[Uber]] — internal platform, layoffs, spinouts
- [[Anthropic]] — Claude Code, code generation stats
- [[GitHubCopilot]] — Shopify early access story
- [[ThomasDohmke]] — gave Shopify early Copilot access
- [[FarhanThawar]] — Shopify head of engineering
- [[BrianArmstrong]] — Coinbase CEO, fired engineer over AI
- [[DHH]] — mech suit metaphor
- [[MitchellHashimoto]] — runs two agents
- [[SimonWillison]] — 2 years still figuring out AI
- [[JohnDeere]] — two-pizza to one-pizza teams
- [[Block]] — layoffs mentioned
- [[Airbnb]] — building internal AI infra
- [[Intercom]] — building internal AI infra
- [[Temporal]] — Uber spinout
- [[Chronosphere]] — Uber spinout
- [[SemiAnalysis]] — overtook Pragmatic Engineer as #1 tech newsletter
- [[MikaelParyk]] — Shopify CTO, swyx's next podcast guest
- [[MCPGateway]] — companies building their own
- [[AgentOrchestration]] — mech suit vs management
- [[AIasJuniorDeveloper]] — core mental model
- [[AgenticEngineering]] — working with AI paradigm
