---
title: "ClaudeCode"
type: entity
tags: [tool, coding-agent, anthropic]
sources: ["raw/01-articles/claude/2026-02-20 - Bringing automated preview, review, and merge to Claude Code on desktop.md", "raw/01-articles/claude/2026-02-23 - How AI helps break the cost barrier to COBOL modernization.md", "raw/01-articles/claude/2026-05-11 - Agent view in Claude Code.md", raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/02 - Installing Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md, raw/03-transcripts/Claude/Claude Code 101/04 - Your first Claude Code prompt.md, raw/03-transcripts/Claude/Claude Code 101/05 - The CLAUDE.md file.md, raw/03-transcripts/Claude/Claude Code 101/06 - The Explore → Plan → Code → Commit workflow in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/07 - Context Management in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/08 - MCP in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/09 - Hooks in Claude Code.md, raw/03-transcripts/Claude/Claude Code Skills/01 - What are skills.md, raw/03-transcripts/Claude/Claude Code subagents/03 - What are subagents.md, raw/01-articles/claude/2025-06-18 - Remote MCP support in Claude Code.md, raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md, raw/01-articles/claude/2025-07-24 - How Anthropic teams use Claude Code.md, raw/01-articles/claude/2025-08-20 - Claude Code and new admin controls for business plans.md, raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md, raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/13 - Running an AI-native engineering org.md, raw/01-articles/claude/2025-08-06 - Automate security reviews with Claude Code.md, raw/01-articles/claude/2025-10-06 - Optimize code performance quickly.md, raw/01-articles/claude/2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous.md, raw/01-articles/claude/2025-10-09 - Customize Claude Code with plugins.md, raw/01-articles/claude/2025-10-10 - Build responsive web layouts.md, raw/01-articles/claude/2025-10-15 - How to scale agentic coding across your engineering organization.md, "raw/01-articles/claude/2026-05-20 - Using Claude Code The unreasonable effectiveness of HTML.md", "raw/01-articles/claude/2026-05-26 - Code w Claude London 2026 Rethinking how we build.md", "raw/01-articles/claude/2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system.md", "raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md", "raw/01-articles/claude/2026-06-02 - A harness for every task dynamic workflows in Claude Code.md", "raw/01-articles/claude/2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code.md", "raw/01-articles/claude/2026-06-03 - How Anthropic enables self-service data analytics with Claude.md", "raw/01-articles/claude/2026-06-17 - Claude Design now stays on brand for daily work.md", "raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md", "raw/01-articles/claude/2026-06-18 - Claude Code now supports artifacts.md", "raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-07-07
---

## Definition

Claude Code is Anthropic's agentic coding tool that has direct access to a developer's files, terminal, and codebase. It can read code, edit files, run commands, and integrate with existing developer tools to accelerate software development.

Claude Code is led by [[BorisCherny]], Head of Claude Code at [[Anthropic]], who delivered the keynote at Code w/ Claude London 2026 framing the tool's philosophy around collapsing the distance between "I have an idea" and "it runs" — returning to the immediacy of programming before compilers, typecheckers, and build systems added layers of complexity.

## Key Information

- Available in the terminal, Visual Studio Code, JetBrains IDEs, the Claude desktop app, and the web (claude.ai/code).
- As of June 2026, Claude Code on desktop is available through [[ClaudeDesktop]] on AWS, Google Cloud, and Microsoft Foundry, with inference running in the customer's own cloud environment and per-surface policy keys for phased organizational rollout.
- Differs from Claude AI in that it has direct filesystem access rather than requiring copy-paste workflows.
- Operates as an AI agent: an LLM in a real-time loop with access to tools, external services, and other agents.
- By default asks for permission before running commands or modifying files.
- Can search the web for documentation and API references via [[WebSearch]], with access to current API documentation and technical articles.
- Not infallible: may misunderstand intent, introduce bugs, or over-engineer solutions.

### Installation

- **Terminal (macOS/Linux/WSL):** one-line curl command; Homebrew also available (no auto-update).
- **Windows:** PowerShell (Invoke-RestMethod), CMD (curl), or winget (no auto-update).
- **VS Code:** install the "Claude Code" extension by Anthropic (blue check verified) from the extensions panel.
- **JetBrains:** install the Claude Code plugin from the JetBrains Marketplace.
- **Claude Desktop:** toggle "Code" at the top after sign-in.
- **Web:** claude.ai/code, restricted to GitHub repositories only.
- First run: choose color theme, sign in (Pro/Max/Enterprise or API key), and set directory scope.
- The terminal receives features fastest; IDE integrations offer a more intertwined experience; desktop is good for background tasks; web supports remote GitHub work and parallel sessions.

### Business Plan Integration (August 2025)

Enterprise and Team plan customers can now access Claude Code via **premium seats** that bundle Claude and Claude Code under one subscription. Admins assign standard or premium seats per user; extra usage is available at standard API rates with per-user spend caps. Both plans include Claude Code usage analytics and self-serve seat management. See [[ClaudeEnterprise]] and [[ClaudeTeamPlan]] for plan details. Early adopters:

- **[[Behavox]]** (compliance/security): hundreds of developers onboarded; Claude Code became primary pair programmer.
- **[[Altana]]** (supply chain AI): 2–10x development velocity acceleration for AI/ML systems.

### Usage at Anthropic

Across [[Anthropic]], teams use [[ClaudeCode]] to:

- **Onboarding & Codebase Navigation** — Help new hires understand data pipelines and dependencies; serve as a "first stop" for identifying relevant files for bug fixes and features
- **Testing & Code Review** — Automate unit test generation and integrate with GitHub Actions for PR comments; enable test-driven development workflows
- **Production Debugging** — Diagnose incidents 3x faster by analyzing stack traces; gain confidence fixing bugs in unfamiliar codebases
- **Rapid Prototyping** — Build [[React]] applications with [[TypeScript]] for visualizing [[ReinforcementLearning]] models; develop features autonomously through iterative testing
- **Knowledge Consolidation** — Consolidate scattered technical documentation via [[MCP]] and CLAUDE.md files; create markdown runbooks and troubleshooting guides
- **Custom Automation** — Build tools without dedicated development resources; process data, generate variations, and create specialized workflows
- **Self-Service Data Analytics** — Power an [[AgenticAnalytics|agentic analytics]] stack handling 95% of business analytics queries with ~95% accuracy via [[ClaudeCodeSkills|skills]]; skills lift accuracy from 21% to 95%+ by encoding procedural knowledge for navigating data models, semantic layers, and validation workflows

See [[summary-2025-07-24 - How Anthropic teams use Claude Code]] for detailed case studies. See [[summary-2026-06-03 - How Anthropic enables self-service data analytics with Claude]] for the analytics case study.

### Scaling Adoption and Activity Metrics (October 2025)

Claude Code includes **Activity Metrics**, tracking lines of code accepted, suggestion acceptance rates, daily active users and sessions, organization-wide and per-user spend, and individual developer metrics — used as one of several success measures (alongside sprint throughput, task completion time, and developer satisfaction) when scaling [[AgenticCoding]] adoption across an engineering organization.

### Contribution Metrics (January 2026, public beta)

A GitHub-integrated dashboard (Claude GitHub App + Admin settings toggle) tracks PRs merged and lines of code committed with vs. without Claude Code assistance, plus per-user adoption data — calculated conservatively, counting only high-confidence Claude-assisted code by matching session activity against GitHub commits/PRs. Anthropic's internal engineering teams saw a 67% increase in PRs merged per engineer per day since adoption increased, with 70-90% of code across teams now written with Claude Code assistance. Designed to complement (not replace) DORA metrics and sprint velocity. Available in beta for Team and Enterprise customers.

### Responsive Web Layouts (October 2025)

For responsive-design issues spanning multiple stylesheets, Claude Code scans a project's CSS to find fixed-width styles and overflow-causing patterns (with line numbers), replaces them with responsive alternatives, adds breakpoint-specific media queries, tests at multiple viewport widths, and generates a Playwright test suite covering real device sizes to prevent regressions. See [[ResponsiveWebDesign]].

### Plugins (October 2025)

Claude Code plugins bundle any combination of slash commands, sub-agents, MCP servers, and hooks into a single installable package (`/plugin` command, public beta). Plugin marketplaces — a git/GitHub repo or URL with a `.claude-plugin/marketplace.json` file — let teams discover, curate, and distribute plugins organization-wide or to the community. See [[ClaudeCodePlugins]].

### Sandboxing and Claude Code on the Web (October 2025)

To reduce "approval fatigue" from constant permission prompts, Claude Code added a sandboxed bash tool (research preview, built on Linux bubblewrap / macOS Seatbelt) that enforces filesystem and network isolation so Claude can act freely within defined boundaries — enable via `claude --sandbox`. **Claude Code on the web** runs each session in an isolated cloud sandbox where sensitive credentials (git credentials, signing keys) never enter the sandbox; git operations are proxied through a scoped-credential service to [[GitHub]] instead. Both are framed as [[PromptInjection]] containment: even a successful injection can't exfiltrate data or reach unauthorized servers. See [[Sandboxing]].

Launched October 20, 2025 as a research preview: connect GitHub repositories from a browser, describe a task, and Claude Code runs it on Anthropic-managed cloud infrastructure — well suited to bug backlogs, routine fixes, and parallel development across repos, with automatic PR creation and change summaries. Custom network configuration lets teams choose which domains the sandbox can reach (e.g., allowing npm access to run tests). Also shipped to the [[ClaudeIOSApp]] as an early preview. Cloud sessions share rate limits with other Claude Code usage. Expanded November 12, 2025 to Team/Enterprise premium-seat users (on by default, admin-toggleable) in addition to Pro/Max.

### Code Performance Optimization (October 2025)

For performance issues spanning multiple files, Claude Code scans an entire codebase, correlates recent changes with performance degradation, and orchestrates targeted fixes (generating tests, validating improvements, preventing regressions) — e.g., detecting N+1 query problems and implementing eager loading, batch queries, composite indexes, or Redis caching. Best focused on performance-critical directories (`api/`, `core/`). [[Ramp]] uses Claude Code this way to accelerate delivery across hundreds of services. See [[CodePerformanceOptimization]].

### Customer Case Studies: Rakuten and Brex (October 2025)

[[Rakuten]]'s engineering team used Claude Code to autonomously implement a specific activation-vector extraction method in vLLM (12.5M lines, Python/C++/CUDA) in seven hours, reaching 99.9% numerical accuracy against the reference method. At [[Brex]], Claude Code drove a content designer's independent shipping of PRs and a company-wide content-guidelines rollout, a Product AI team's shift from "driver" to "reviewer" of code, and a Data & Analytics team's text-to-SQL tool ("Brex Explorer") and AI data-engineering agent — also serving as an informal "oracle" for navigating Brex's Kotlin/Bazel monorepo.

### Case Study: MacCoss Lab / Skyline (April 2026)

[[MacCossLab|MacCoss Lab]]'s Brendan MacLean applied the same incremental-onboarding methodology he'd used for 17 years to bring new human developers onto Skyline (700,000+ lines of C#) to onboarding Claude Code instead — a contained first project, explained context, then expanding scope, rather than starting each session from zero. He built context into a separate repository (`pwiz-ai`) rather than the codebase itself, so it survives across all branches and time points. Outcomes: a year-stalled feature finished in two weeks, a three-year-dormant module gaining new features in under a day, and custom MCP servers (written by Claude) automating screenshot-diff regression testing and a daily test/support summary email. See [[summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development]].

### Case Study: CLUE Cybersecurity Detection Platform (May 2026)

Anthropic's Detection Platform Engineering team (Technical Lead Jackie Bow) built **CLUE** ("Claude Looks Up Evidence") with Claude Code — a proof of concept in a day, full design docs and implementation within a week. CLUE Triage auto-dispositions every incoming security alert (false positive/true positive/malicious/expected) with a confidence score, dropping the false-positive rate from ~33% to 7%. CLUE Investigate answers natural-language questions over security-critical logs via an orchestrator dispatching sub-agents to run queries in parallel (see [[MultiAgentSystem]]), averaging 25 tool calls and ~11 queries per investigation, cutting hours-to-days manual investigations to 3-4 minutes. Over a 30-day window, CLUE automated ~12,000 queries and ~27,000 tool calls — an estimated 1,870 hours (234 person-days) of manual-equivalent work, 5-10x time savings. The team frames its roadmap as applying "the bitter lesson" to security operations: give Claude goals and tool access rather than rigid SOAR-style playbooks, move from reactive alert response to proactive threat-hunting, build organizational memory from stored investigation transcripts, and embrace non-deterministic parallel investigation strategies rather than treating variation as a bug. See [[summary-2026-05-12 - How Anthropic&#39;s cybersecurity team built a threat detection platform with Claude Code]] and the earlier, shorter [[summary-02 - How Anthropic uses Claude in Cybersecurity]].

### Code Review (March 2026)

**Code Review** (research preview, Team/Enterprise) dispatches a team of agents on every PR — finding bugs in parallel, verifying them to filter false positives, ranking by severity, and posting a single overview comment plus inline comments. Deeper and more expensive than the existing [[AutomatedSecurityReview|GitHub Action]] (which remains available). At Anthropic, substantive review comments rose from 16% to 54% of PRs; large PRs (1,000+ lines) get findings 84% of the time. Billed on token usage, averaging $15-25 per review. See [[CodeReview]].

### 1M Context General Availability (March 2026)

Claude Code sessions for Max, Team, and Enterprise users on [[Claude4.6Opus|Opus 4.6]] now default automatically to the full 1M-token [[ContextWindow|context window]] — previously an extra-usage feature — reducing compactions and keeping more of the conversation intact.

### Product Management Rhythm (March 2026)

Cat Wu, Head of Product for Claude Code, frames the team's PM approach around four shifts driven by exponential model improvement: **plan in short sprints** via self-directed "side quests" (short, off-roadmap experiments) rather than long-term roadmaps — Claude Code on Desktop, the AskUserQuestion tool, and todo lists all originated this way; **demos and evals over docs** — e.g. the [[ClaudeCodePlugins|plugins]] spec came back from Claude Code as a near-production prototype, and the **agent teams** feature (coordinating multiple Claude Code instances) was validated via hand-crafted evals rather than a written spec; **revisit features with new models** — Claude Code with Chrome emerged after the team noticed users manually copy-pasting between Claude Code and Claude in Chrome; and **do the simple thing that works** — e.g. a system-reminder hack that nudged the agent to update its own todo list was removed outright once a later model handled it natively, part of a pattern of cutting system-prompt/tool-description engineering with each model release (a 20% reduction for [[Claude4.6Opus|Opus 4.6]]). [[METR]] benchmarks cited to illustrate the pace: [[Claude3.5Sonnet|Sonnet 3.5 (new)]] handled ~21-minute tasks when Claude Code was first built; Opus 4.6 handles ~12-hour tasks half the time — a ~41x jump in 16 months. See [[summary-2026-03-19 - Product management on the AI exponential]].

### PM Workflow: Prototyping Against Your Own API (April 2026)

Jess Yan ([[ClaudeManagedAgents|Claude Managed Agents]] product manager) illustrates Cat Wu's "demos over docs" pattern with a concrete workflow split: she uses [[Claude.ai|Claude]] and [[ClaudeCowork|Claude Cowork]] for open-ended early-stage research and discovery, then switches to Claude Code plus Managed Agents once a job to be done is clear, to prototype and ship a custom agent. Prototyping directly against pre-production Managed Agents API specs in Claude Code — from "hello world" to a working agent within a single sitting — surfaced API-abstraction and Claude Console UX problems that a multi-week doc review would have missed and user feedback would have caught too late. To start, she loads the Managed Agents skill in Claude Code and sketches the job to be done; Claude builds the agent and explains its integration steps along the way. The same muscle that raises the ceiling on prototypes also lets her automate long-tail operational work (bespoke agents for one-off "jobs to be done") that previously couldn't scale due to per-launch quirks. See [[summary-2026-04-29 - Product development in the agentic era]].

### Computer Use and Dispatch (March 2026)

Claude Code gained the ability to use a developer's computer directly — pointing, clicking, and navigating open applications, the browser, and dev tools — when it lacks a specific tool/connector for the task (research preview, macOS and Windows, Claude Pro/Max). It prefers precise tools/connectors first, falls back to full screen control otherwise, and always requests permission before touching a new application. Safeguards include automatic in-model activation scanning to detect prompt-injection-style misuse, plus a user override to stop Claude at any time. Paired with [[Dispatch]] (extended from Claude Cowork), which lets a task be assigned from a phone and picked up later once the desktop app has completed work autonomously — e.g., making IDE changes, running tests, and opening a PR while the developer is away. See [[ComputerUse]].

### Auto Mode (March 2026)

**Auto mode** (research preview, Team plan; Enterprise/API rolling out shortly after) is a new permissions mode where Claude makes permission decisions on its own behalf: a classifier reviews each tool call before it runs, screening for potentially destructive actions (mass file deletion, sensitive data exfiltration, malicious code execution). Safe actions proceed automatically; blocked risky actions redirect Claude to a different approach; if Claude keeps hitting blocks on an action, it eventually triggers a human permission prompt. Positioned as a middle path safer than `--dangerously-skip-permissions` but riskier than the fully manual default. Works with both Claude Sonnet 4.6 and Opus 4.6, with a small expected impact on token consumption, cost, and latency. See [[PermissionModes]].

### Tool Design Philosophy: Seeing Like an Agent (April 2026)

Thariq Shihipar (Claude Code team) frames tool design as putting yourself in the model's shoes — tools should be shaped to an agent's actual abilities (paper vs. calculator vs. computer, depending on skill level), discovered by reading outputs and experimenting rather than assumed upfront. Claude Code currently ships ~20 tools total, with a deliberately high bar for adding new ones since each addition is one more option the model has to weigh. Case studies:

- **AskUserQuestion tool** (elicitation): three iterations before landing — (1) adding a questions array parameter to ExitPlanTool, dropped because it conflated "here's my plan" with "answer these questions" and left ambiguity about how to handle conflicting answers; (2) asking Claude to output a modified markdown bullet format for questions, dropped because Claude couldn't reliably hold the format (dropped options, extra sentences); (3) a dedicated tool invocable any time, prompted especially during plan mode, that pops a blocking modal — this worked because Claude reliably called it and it forces multiple-choice structure; also composable via the Agent SDK and Skills.
- **TodoWrite → Task tool** (staying on track vs. coordinating agents): TodoWrite (plus system reminders every 5 turns) kept early Claude Code models on track, but as models improved the reminders made Claude treat the list as fixed instead of revising it, and Opus 4.5's improved subagent use had no way to coordinate a shared todo list across subagents — replaced with the Task tool, which supports dependencies, cross-subagent updates, and model-driven edits/deletion. General lesson: tools that once helped a weaker model can constrain a stronger one — revisit assumptions as capability grows, which is also an argument for supporting a small, similarly-capable set of models at a time.
- **RAG → Grep tool → Agent Skills** (self-directed context gathering): Claude Code initially used RAG internally (pre-indexed vector DB feeding retrieved snippets to Claude) — powerful but fragile across environments, and it handed Claude context rather than letting it find its own. Replaced by a Grep tool so Claude could search the codebase itself, the same way it searches the web. [[ClaudeCodeSkills|Agent Skills]] formalized this into **progressive disclosure**: Claude reads a skill file, which can reference further files it reads recursively, enabling nested multi-layer search for exactly the context needed. See [[RetrievalAugmentedGeneration]].
- **Claude Code Guide subagent** (adding capability without adding a tool): Claude didn't know how to answer questions about Claude Code itself (e.g., how to add an MCP server, what a slash command does). Putting the answer in the system prompt was rejected as context rot for a rarely-needed capability; giving Claude a raw docs link via progressive disclosure worked but pulled oversized doc chunks into context for one-sentence answers. The fix: the **Claude Code Guide**, a dedicated subagent invoked whenever a user asks about Claude Code itself, which does the doc search in its own isolated context following detailed extraction instructions and returns only the answer — keeping the main agent's context clean. Not perfect (Claude can still get confused about its own setup), but it expanded Claude's action space without adding a new top-level tool.

See [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]].

### Prompt Caching Engineering Lessons (April 2026)

Thariq Shihipar detailed how Claude Code's harness is built entirely around [[PromptCaching|prompt caching]] — Anthropic alerts on cache hit rate and declares SEVs when it drops too low, since a high hit rate both cuts cost and enables more generous subscription rate limits. Key patterns: order static content before dynamic content in the prompt; push stale/time-sensitive updates into a `<system-reminder>` tag on the next turn rather than editing the system prompt (which breaks the cache); avoid mid-conversation model switches (caches are model-specific, so switching, e.g., from Opus to Haiku for an easy question can cost more than staying on Opus) in favor of a subagent "hand-off" message, as used by Claude Code's Haiku-based Explore agents; never change the tool set mid-conversation — the reason **Plan Mode** is implemented as `EnterPlanMode`/`ExitPlanMode` tools layered on top of a constant, unchanging tool set rather than a swapped-in read-only tool subset; and use the tool search tool's `defer_loading` stubs instead of removing MCP tools to keep large tool sets cache-stable. For [[ContextWindow|compaction]], Claude Code uses "cache-safe forking" — running the compaction call with the same system prompt, context, and tools as the parent conversation (appending only the compaction prompt as a final message) instead of a separate, differently-prefixed summarization call that would be entirely uncached — a pattern now built into the Claude API's native compaction feature. See [[summary-2026-04-30 - Lessons from building Claude Code Prompt caching is everything]].

### Agent View (May 2026)

**Agent view** (research preview) brings the desktop app's parallel-session orchestration to the terminal/CLI: a single list-style interface for managing many concurrent Claude Code sessions, replacing manual juggling of terminal tabs or a tmux grid. Opened via left-arrow from any session or `claude agents`, each row shows session status (needs input / working / done), the last response's content, and time since last interaction. Selecting a row lets a user "peek" at the last turn and reply inline, or press enter to attach to the full transcript. Any session can be sent to the background with `/bg`, or launched directly backgrounded with `claude --bg [task]`. Early-user patterns: scaling the number of concurrent sessions dispatched at once; managing long-running loops like PR babysitters and dashboard updaters (which show next-run time in the list, per [[ClaudeCodeRoutines]]); quickly branching to a related task and back; and scanning status indicators to see which sessions produced a PR. Available on Pro, Max, Team, Enterprise, and Claude API plans; opt in via `claude agents`. See [[summary-2026-05-11 - Agent view in Claude Code]].

### Rate Limit Increases (May 2026)

Announced at [[CodeWithClaude|Code w/ Claude SF 2026]], Anthropic doubled Claude Code rate limits and raised API limits for Claude Opus, aimed at letting developers, startups, and enterprises build more reliably at scale; both changes went live at announcement. The rate-limit change is linked from Anthropic's recap to a separate news post (URL slug references a SpaceX case study) not yet ingested into the wiki. See [[summary-2026-05-12 - Code w Claude SF 2026 recap Building on the AI exponential]].

### Desktop Redesign for Parallel Agents (April 2026)

Claude Code's desktop app was redesigned around orchestrating many concurrent sessions rather than one prompt at a time. A new **sidebar** lists every active and recent session, filterable by status/project/environment or grouped by project, and auto-archives sessions once their PR merges or closes. A **side chat** (⌘+; / Ctrl+;) lets a user branch off a question mid-task — it reads context from the main thread but doesn't write back to it, to avoid steering the main task off course. Every pane (terminal, preview, diff viewer, chat) is now drag-and-drop, extending the existing Preview/Review/Merge toolset into a rearrangeable workspace. The desktop app also gained **parity with CLI plugins** (org-managed or local), SSH support extended to Mac (alongside existing Linux support) for remote sessions, three view modes (Verbose/Normal/Summary), new keyboard shortcuts for session switching/spawning/navigation (⌘+/ or Ctrl+/), a usage button showing context-window and session usage, and an under-the-hood rebuild with streaming responses. Available for Pro, Max, Team, and Enterprise plans, and via the Claude API. See [[summary-2026-04-14 - Redesigning Claude Code on desktop for parallel agents]].

### Routines (April 2026)

Claude Code shipped **routines** in research preview: a configured-once automation (prompt, repo, connectors) that then runs repeatedly on a schedule, from an API call, or in response to a GitHub repository event, executing on Claude Code's web infrastructure independent of a local machine. Existing `/schedule` CLI tasks are now surfaced as scheduled routines. API-triggered routines get a dedicated endpoint and auth token (POST a message, receive a session URL); event-triggered routines subscribe to GitHub PR events and open one continuing session per matching PR. Available to Pro, Max, Team, and Enterprise users with Claude Code on the web enabled, with daily run caps (Pro 5/day, Max 15/day, Team/Enterprise 25/day) on top of standard subscription usage draw-down. See [[ClaudeCodeRoutines]] and [[summary-2026-04-14 - Introducing routines in Claude Code]].

### Session and Context Management Guidance, and /usage (April 2026)

Thariq Shihipar published practical guidance on managing sessions and context in Claude Code, prompted by the new **`/usage`** slash command (surfaces a user's Claude Code usage) and wide variance observed in how customers manage sessions under the newer 1M-token context window. Key recommendations: start a new session per new task, but stay in one session for closely related follow-on work (e.g. writing docs for a feature just implemented) to avoid Claude re-reading files it just touched; use **`/rewind`** (double-tap Esc) to jump back to a prior message and re-prompt with a correction, rather than layering "that didn't work, try X" onto a failed context — rewind can also produce a "summarize from here" handoff note to the next iteration; choose **`/compact`** (lossy self-summary, low effort, steerable with instructions like "focus on X, drop Y") vs. **`/clear`** (full manual reset, more effort, more precise) depending on how much prior context is still relevant; and proactively `/compact` with a stated direction rather than waiting for autocompact, since bad compacts happen when the model can't predict where work is headed next (e.g., a debugging-session summary drops an unrelated warning the user then asks about) and compaction itself happens when the model is at its least-intelligent, most context-rotted point. See [[summary-2026-04-15 - Using Claude Code session management and 1M context]].

### Opus 4.7 Best Practices (April 2026)

With the release of [[Claude4.7Opus|Opus 4.7]], Claude Code's default effort level became `xhigh` — a new level between `high` and `max` recommended for most agentic coding work. Anthropic advises treating Opus 4.7 more like a capable engineer being delegated to than a pair programmer guided line-by-line, and flags several default-behavior shifts from Opus 4.6 that can affect tuned prompts/harnesses: shorter, complexity-calibrated responses; fewer tool calls with more reasoning per call; and fewer subagents spawned by default (explicit prompting needed to encourage fan-out across files/independent items). See [[Claude4.7Opus]].

### Preview, Review, and Merge on Desktop (February 2026)

Claude Code on desktop can start dev servers and preview the running app in-app — viewing UI, reading console logs, and catching errors without switching to a browser; users can select visual elements in the preview and pass feedback directly to Claude. A "Review code" button has Claude examine local diffs and leave inline comments (bugs, suggestions, issues) before anything leaves the machine. For GitHub-hosted code, Claude Code monitors PR status via the GitHub CLI, with optional **auto-fix** (attempts CI failures automatically) and **auto-merge** (merges once checks pass) running in the background while the user moves to a new task. Sessions move across surfaces: `/desktop` brings a CLI session's context into the desktop app, and "Continue with Claude Code on the web" moves a desktop session to the cloud, pickable up from web or mobile.

### COBOL Modernization (February 2026)

Claude Code automates the exploration/discovery phase of migrating legacy COBOL systems — reading the full codebase to map entry points, execution paths, cross-module data flows, and implicit dependencies invisible to static analysis — compressing modernization timelines from years to quarters. See [[COBOLModernization]].

### Growth Marketing Case Study (January 2026)

Growth marketer Austin Lau (no prior coding experience) built a Figma plugin generating ad creative variants in one click and a Google Ads copy workflow (`/rsa` slash command) combining campaign data with Skills for brand tone/voice and RSA best practices, cutting ad creation from 30 minutes to 30 seconds. See [[Figma]] and [[Anthropic]].

### Respiro Case Study (May 2026)

Project manager Kostiantyn Vlasenko (no prior coding experience) built and shipped [[Respiro]], a real-time stress-detection iOS app, going from idea to App Store-ready in under six weeks after entering the Built With Opus 4.6 Claude Code Hackathon. He personally built and orchestrated a 15+ specialized-subagent architecture (TCA architect, Swift developer, Metal specialist, code reviewer, and more) running in parallel across modules, drawing an explicit analogy to managing a human team from his PM background. When an early React Native MVP proved untestable without an Android device, Claude Code rewrote the app in Swift from scratch in a few hours. Claude also guided him through unfamiliar developer consoles (Apple Developer Program, Meta API) via screenshot-based vision analysis, which Vlasenko considers Claude's most underrated feature. See [[MythicalGames]].

### GTM Sales Workflow Case Study: CLAFTS (June 2026)

Jared Sires, an Anthropic account executive with no prior coding experience, used Claude Code to build **CLAFTS** (Claude Drafts) — a ~4,300-line Gmail-integrated application using the [[ClaudeAPI|Claude API]] to draft customer email replies in his voice, saving 10–15 hours per week. Key elements of the build:

- **System prompt iteration**: Hundreds of iterations to match Jared's writing style, removing Claude's default hedging phrases and verbose tendencies.
- **CLAFTS Tones**: Pattern matching to mimic voice across different relationships (customers, peers, family), validated when Claude began refusing to generate increasingly angry test emails — confirming the tone-matching was working.
- **Documentation awareness**: Uses web search to pull current Anthropic product documentation on every draft, so responses reflect the latest shipped details rather than what Jared remembers.
- **Team scaling**: Shared in Slack, adopted by the sales org within 24 hours. Now packaged as a [[ClaudeCowork]] plugin with 20+ [[ClaudeCodeSkills|skills]] wired into Salesforce, Intercom, Gong, Google Calendar, Gmail, Google Drive, and BigQuery — adopted by ~80% of Anthropic's sales organization.
- **Role transformation**: Jared's success led to a shift from account executive to GTM product manager, focused on identifying sales-org problems and building Claude-powered solutions. He now sits in design conversations with product engineers, describing the shift as "the most empowering thing I've ever experienced."
- **Skills built**: `/customer-context` (360-degree account view in ~90 seconds), `/pipeline-management` (at-risk deals, forecasting guidance), daily brief (pre-call research from calendar + CRM), and daily recap (post-meeting follow-up drafts).
- **Next frontier**: Experimenting with the [[ClaudeAgentSDK|Agent SDK]] to chain workflows where one Claude run's output feeds the next.

See [[AIAcceleratedSalesWorkflows]] and [[summary-2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code]].

### Claude Code and Slack (December 2025)

Tagging @Claude on a bug report or feature request in [[Slack]] automatically spins up a [[ClaudeCode|Claude Code on the web]] session (beta, research preview) using surrounding channel/thread context, auto-selecting the authenticated repository to run against, posting status updates back to the thread, and linking to the full session with an option to open a PR — extending the existing Claude Slack app rather than adding a new surface.

### Y Combinator Startup Case Studies (November 2025)

Three [[YCombinator]] startups built substantially with Claude Code: [[HumanLayer]] pivoted around Claude Code and the [[ClaudeAgentSDK|Claude Agent SDK]]'s headless execution to build CodeLayer, running parallel Claude Code sessions via worktrees and remote cloud workers; [[Ambral]]'s sole engineer/CTO used a three-phase workflow (Opus for research/planning, Sonnet for implementation, discrete sessions per phase to avoid context contamination) and built the product itself on the Claude Agent SDK with per-data-type [[ClaudeCodeSubagents|subagents]]; [[Vulcan]]'s non-engineer founders won a Virginia state government contract for AI-powered regulatory analysis, reducing average home prices by $24,000 and prompting an executive order mandating agentic AI regulatory review statewide. Shared practice: use discrete prompts/sessions per phase and interrupt early on a wrong direction rather than letting a misguided approach run to completion.

### API Integration and Debugging Use Cases (October 2025)

Anthropic published paired use-case articles positioning [[Claude.ai]] for upfront planning and Claude Code for implementation:
- **[[APIIntegration]]**: Claude Code analyzes a codebase to generate typed API clients matching existing conventions, implements OAuth2/JWT/API-key-rotation auth flows via existing secret-management patterns, generates edge-case tests, then commits and opens a PR.
- **[[Debugging]]**: Claude Code independently explores a project, follows debugging trails across files, proposes fixes matching existing conventions, generates regression tests, then commits and opens a PR. [[Ramp]] is cited using Claude Code this way across hundreds of services.

### Automated Security Reviews (August 2025)

Claude Code added two ways to catch vulnerabilities before production, both built on a specialized security-focused prompt covering SQL injection, XSS, auth flaws, insecure data handling, and dependency vulnerabilities:

- **`/security-review` command**: ad-hoc, pre-commit vulnerability analysis from the terminal; Claude can also implement fixes.
- **GitHub Action**: automatically reviews every new pull request, filters false positives via customizable rules, and posts inline PR comments.

Anthropic uses both internally (including on Claude Code itself), catching a DNS-rebinding remote code execution vulnerability and an SSRF vulnerability in a credential-management proxy before they reached production. See [[AutomatedSecurityReview]] and [[VulnerabilityDetection]].

### Claude Agent SDK (September 2025)

The agent harness powering Claude Code was renamed from the **Claude Code SDK** to the **[[ClaudeAgentSDK]]** to reflect its broader applicability. Anthropic teams use Claude Code to power deep research, video creation, and note-taking in addition to coding — demonstrating that the same harness can drive general-purpose agent workflows. The SDK exposes the agent loop (gather context → take action → verify work) as primitives: agentic file-system navigation, custom tools, bash, code generation, MCP integrations, subagents, and the compact context feature.

### Large Codebases at Scale: Best Practices (May 2026)

The first article in Anthropic's "Claude Code at scale" series distills patterns from deployments across multi-million-line monorepos, decades-old legacy systems, and distributed multi-repository architectures — including languages teams don't always associate with AI coding tools (C, C++, C#, Java, PHP), where Claude Code performs better than expected, particularly with recent models.

- **Agentic search vs. RAG at scale**: Claude Code traverses the file system, greps, and follows references the way an engineer would, without a maintained codebase index. RAG-based competitors that embed the whole codebase can serve stale results at scale — a renamed function two weeks ago, or a module deleted last sprint, with no signal that either is out of date — because embedding pipelines can't keep pace with thousands of engineers committing continuously. Agentic search avoids this, but works best only when Claude has enough starting context to know where to look; a vague query across a billion-line codebase hits context-window limits before the work begins. See [[RetrievalAugmentedGeneration]].
- **The harness matters as much as the model**: capabilities are shaped by the ecosystem built around the model, not the model alone. The harness has five extension points — [[CLAUDE-md|CLAUDE.md]] files (every session), [[ClaudeCodeHooks|hooks]] (self-improving automation, not just guardrails), [[ClaudeCodeSkills|skills]] (on-demand, path-scopable expertise), [[ClaudeCodePlugins|plugins]] (distributing what works instead of leaving it tribal), and [[ModelContextProtocol|MCP servers]] (connecting internal tools/data) — plus two further capabilities, [[LanguageServerProtocol|LSP]] integrations (symbol-level navigation, accessed through the plugin layer) and [[ClaudeCodeSubagents|subagents]] (splitting exploration from editing — a read-only subagent maps a subsystem and writes findings to a file, then the main agent edits with the full picture).
- **Three configuration patterns from successful deployments**: (1) making the codebase navigable — lean/layered CLAUDE.md (root = pointers and gotchas only), initializing Claude Code in subdirectories rather than the repo root (it still walks up and loads every CLAUDE.md along the way), scoping test/lint commands per subdirectory, version-controlled `.ignore`/`permissions.deny` exclusions, lightweight root-level codebase maps where directory structure doesn't do the work, and LSP so Claude searches by symbol rather than string; (2) actively maintaining CLAUDE.md as model intelligence evolves, since instructions tuned for one model can constrain the next (e.g., forcing single-file refactors, or a hook enforcing `p4 edit` that became redundant once Claude Code added native Perforce support) — recommended review cadence every 3-6 months or whenever performance plateaus after a major model release; (3) assigning organizational ownership — a pre-rollout infrastructure investment, an emerging "agent manager" role (hybrid PM/engineer managing the ecosystem), or at minimum a DRI with authority over settings/permissions/plugin marketplace/CLAUDE.md conventions — since bottoms-up adoption without centralization leaves knowledge tribal. See [[AgenticCoding]] and [[ContextEngineering]].
- **Governance in regulated industries**: cross-functional working groups (engineering, infosec, governance) established early, starting with a defined set of approved skills/plugins, required code-review processes, and limited initial access, produced the smoothest deployments.
- Customer feedback for the article came from [[Zoox]] and members of Anthropic's Applied AI team.

See [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]].

### HTML as Output Format (May 2026)

[[ThariqShihipar]] advocates using HTML instead of Markdown as Claude Code's output format. HTML provides richer visualization (SVG diagrams, colors, diff annotations, tabs), better readability for long documents (100+ lines), easier browser-based sharing, and interactive capabilities (sliders, knobs, "copy as prompt" buttons). Key patterns:

- **Six use-case categories**: brainstorming/exploration (a web of HTML files for different planning stages), code review (rendered diffs with inline annotations and flowcharts), design prototyping (interactive HTML mockups with parameter-tuning controls), research/reports (synthesized multi-source explainers with SVG diagrams), purpose-built editors (throwaway single-file editors with export buttons), and interactive documents.
- **Token trade-off**: HTML uses more tokens than Markdown, but the 1M context window in Opus 4.7 makes overhead negligible, and the higher likelihood of the developer actually reading the output justifies the cost.
- **Workflow integration**: Prompting "make an HTML file" or "make an HTML artifact" is sufficient. HTML files from exploration phases are passed to implementation sessions and verification agents for broader context. Claude Code's filesystem, MCPs, browser, and git history provide far more context for building rich HTML artifacts than Claude.ai or [[ClaudeDesign]] alone.
- Shihipar has stopped using Markdown almost entirely, describing himself as "far on the HTML maximalist side."

See [[HTMLAsAgentOutputFormat]] and [[summary-2026-05-20 - Using Claude Code The unreasonable effectiveness of HTML]].

### Dynamic Workflows (May 2026)

**Dynamic workflows** let Claude tackle large-scale engineering tasks end-to-end by dynamically writing orchestration scripts that fan out work across tens to hundreds of parallel subagents, with independent verification and adversarial checking before results reach the user. Work that would normally be planned in quarters now finishes in days.

- **How it works**: Claude plans dynamically, breaks the task into subtasks, fans work across parallel subagents, verifies results, and iterates until answers converge — producing results a single pass cannot. Coordination happens outside the conversation, so the plan stays on track regardless of task size. Progress is saved as the run goes, so interrupted jobs resume where they left off.
- **Invocation**: Ask Claude to create a workflow directly, or enable `ultracode` (effort level xhigh) through the effort menu, which lets Claude decide automatically when to use workflows.
- **Availability**: GA in CLI, Desktop, and VS Code for Pro, Max, Team, and Enterprise plans; also on the Claude API, [[AmazonBedrock]], [[VertexAI]], and [[MicrosoftFoundry]]. On by default for Max, Team, and Enterprise; Pro plan users enable in `/config`. Admins can disable via managed settings.
- **Token consumption**: Substantially more than typical sessions; recommended to start on a scoped task to gauge usage. First workflow invocation shows what will run and asks for confirmation.
- **Use cases**: codebase-wide bug hunts, security audits, profiler-guided optimization, large migrations (framework swaps, API deprecations, language ports across thousands of files), and critical work requiring double-checking with adversarial verification.
- **Flagship example**: [[JarredSumner]] used dynamic workflows to port [[Bun]] from Zig to Rust — ~750,000 lines, 99.8% test pass rate, eleven days from first commit to merge, with hundreds of parallel agents and two reviewers per file.

See [[DynamicWorkflows]], [[Ultracode]], and [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]].

A follow-up article (June 2026) catalogs common workflow patterns (classifier routing, fan-out/synthesis, adversarial verification, tournaments, parallel competition, agentic loops, quarantine, model selection) and concrete use cases (debugging, research, triage, CLAUDE.md mining, evals, design exploration). See [[summary-2026-06-02 - A harness for every task dynamic workflows in Claude Code]].

### Claude Design Integration (June 2026)

Claude Code gained bidirectional integration with [[ClaudeDesign]]:

- **`/design-sync`**: Pull your design system into Claude Design, so everything built in Claude Design starts from existing components.
- **`/design`**: Create, edit, and sync design projects without leaving the terminal. Import a design into your codebase, turn code into a live prototype, or let Claude carry a project all the way through.
- When a design is ready to become software, hand it off to Claude Code, which continues from existing work instead of starting over from a screenshot.

See [[summary-2026-06-17 - Claude Design now stays on brand for daily work]].

### Artifacts (June 2026)

Claude Code now supports **artifacts**: live, interactive web pages built from a session's full context (codebase, connectors, conversation) that visualize work progress and auto-update as the session continues. Unlike [[ClaudeArtifacts|Claude.ai artifacts]] (user-described interactive apps), Claude Code artifacts translate agent sessions into collaborative views such as PR walkthroughs, system explainers, dashboards, incident timelines, and release checklists.

- **Session-context construction**: Artifacts are built from what already exists in the session -- codebase, connectors, and the conversation itself -- without requiring separate data-source wiring or infrastructure.
- **Auto-updating**: When Claude Code updates an artifact, the open page refreshes in place; teammates see updates immediately at the same URL. Every publish is a new version with full version history, and a gallery lets users browse all artifacts.
- **Incident investigation**: A flagship use case. An engineer kicks off an incident investigation before standup; Claude Code works through logs and publishes an artifact with a timeline, suspect commits, and an error-rate chart. By standup, Claude has republished updates incorporating the latest information, giving the team a shared view with the same context.
- **Privacy and access control**: Artifacts are private to the author by default. Sharing is restricted to authenticated org members (cannot be made public). Admins manage access via an org-level toggle, role-based scoping, retention policies, and the compliance API.
- **Availability**: Beta for Claude Team and Enterprise orgs, from the Claude Code CLI and desktop app; pages viewable in any browser.

See [[summary-2026-06-18 - Claude Code now supports artifacts]].

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-02 - Installing Claude Code]] — installation guide source
- [[summary-03 - How Claude Code Works]] — internals of the agentic loop
- [[summary-04 - Your first Claude Code prompt]] — prompting and plan mode
- [[summary-05 - The CLAUDE.md file]] — persistent project memory via CLAUDE.md
- [[summary-06 - The Explore → Plan → Code → Commit workflow in Claude Code]] — the recommended workflow
- [[summary-07 - Context Management in Claude Code]] — context management strategies
- [[summary-08 - MCP in Claude Code]] — MCP integration
- [[summary-09 - Hooks in Claude Code]] — deterministic lifecycle hooks
- [[summary-2025-06-18 - Remote MCP support in Claude Code]] — remote MCP servers announcement
- [[summary-2025-07-24 - How Anthropic teams use Claude Code]] — real-world usage patterns across Anthropic teams
- [[summary-2025-05-07 - Introducing web search on the Anthropic API]] — web search integration announcement
- [[summary-01 - What are skills]] — skills system introduction
- [[summary-03 - What are subagents]] — sub-agents introduction
- [[CLAUDE-md]] — the memory file concept
- [[ExplorePlanCodeCommit]] — the EPCC workflow
- [[ModelContextProtocol]] — the MCP standard
- [[ClaudeCodeHooks]] — the hooks system
- [[ClaudeCodeSkills]] — the skills system
- [[ClaudeCodeSubagents]] — the sub-agents system
- [[AIAgent]] — the agent paradigm Claude Code embodies
- [[AgenticCoding]] — development paradigm Claude Code exemplifies
- [[WebSearch]] — web search capability integrated into Claude Code
- [[AgenticLoop]] — the core operational pattern
- [[ContextWindow]] — the memory constraint Claude Code operates within
- [[analysis-claude-product-landscape]] — comparison with Managed Agents and Cowork
- [[analysis-claude-code-extension-mechanisms]] — when to use Skills, Sub-agents, Hooks, or CLAUDE.md
- [[ClaudeEnterprise]] — Enterprise plan offering Claude Code in premium seats
- [[ClaudeTeamPlan]] — Team plan offering Claude Code in premium seats
- [[Behavox]] — Customer using Claude Code as primary pair programmer
- [[Altana]] — Customer achieving 2–10x development velocity with Claude Code
- [[summary-2025-08-20 - Claude Code and new admin controls for business plans]] — Premium seats and business plan integration announcement
- [[summary-2025-09-29 - Building agents with the Claude Agent SDK]] — SDK rename announcement and agent-building best practices
- [[ClaudeAgentSDK]] — the renamed Claude Code SDK for general-purpose agent development
- [[ContextEngineering]] — file/folder structure as agent context design
- [[summary-13 - Running an AI-native engineering org]] — engineering-org lessons on how bottlenecks, planning, and code review changed inside the Claude Code team
- [[summary-17 - Preview your running app in Claude Code on desktop]] — product-launch teaser for live app preview in the desktop app
- [[summary-23 - Introducing Code Review]] — product-launch teaser introducing the Code Review capability
- [[summary-06 - Find and fix security vulnerabilities with Claude]] — product-launch teaser for vulnerability finding/fixing
- [[summary-25 - Find and fix security vulnerabilities with Claude]] — distinct product-launch teaser with the same title
- [[AutomatedSecurityReview]] — the `/security-review` command and GitHub Action
- [[VulnerabilityDetection]] — vulnerability classes detected by security review features
- [[CodeSecurity]] — broader security practices in Claude Code workflows
- [[GitHub]] — platform hosting the security-review GitHub Action integration
- [[summary-2025-08-06 - Automate security reviews with Claude Code]] — security review feature announcement
- [[CodePerformanceOptimization]] — project-wide performance optimization use case
- [[Ramp]] — customer using Claude Code for performance work across hundreds of services
- [[summary-2025-10-06 - Optimize code performance quickly]] — performance optimization use-case article
- [[Sandboxing]] — filesystem and network isolation underlying the sandboxed bash tool and Claude Code on the web
- [[PromptInjection]] — threat model sandboxing mitigates
- [[summary-2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous]] — sandboxing and Claude Code on the web announcement
- [[ClaudeCodePlugins]] — the plugin and marketplace system
- [[summary-2025-10-09 - Customize Claude Code with plugins]] — plugins announcement
- [[ResponsiveWebDesign]] — codebase-wide responsive-layout refactoring use case
- [[summary-2025-10-10 - Build responsive web layouts]] — responsive layout use-case article
- [[summary-2025-10-15 - How to scale agentic coding across your engineering organization]] — organizational rollout methodology and Activity Metrics
- [[summary-2026-01-29 - Understand Claude Code’s impact with contribution metrics]] — contribution metrics feature announcement
- [[GitHub]] — platform contribution metrics integrate with
- [[CodeReview]] — multi-agent PR review feature
- [[summary-2026-03-09 - Bringing Code Review to Claude Code]] — source article
- [[summary-2025-10-20 - Claude Code on the web]] — browser/cloud launch announcement with parallel tasks, PR creation, and iOS availability
- [[ClaudeIOSApp]] — mobile app now running Claude Code sessions
- [[APIIntegration]] — API-client and auth-flow implementation use case
- [[Debugging]] — autonomous multi-file debugging use case
- [[summary-2025-10-27 - How to integrate APIs seamlessly]] — API integration use-case article
- [[summary-2025-10-28 - Fix software bugs faster with Claude]] — debugging use-case article
- [[Rakuten]] — customer example, autonomous vLLM implementation
- [[Brex]] — customer example, three engineering-team case studies
- [[summary-2025-10-30 - Introduction to agentic coding]] — Rakuten case study and agentic-vs-autocomplete framing
- [[summary-2025-10-30 - How Brex improves code quality and productivity with Claude Code]] — Brex case study
- [[YCombinator]] — accelerator behind three profiled Claude Code startups
- [[HumanLayer]] — customer example, CodeLayer built on headless Claude Code sessions
- [[Ambral]] — customer example, product built on Claude Agent SDK with subagents
- [[Vulcan]] — customer example, non-engineer founders winning a government contract
- [[summary-2025-11-17 - How three YC startups built their companies with Claude Code]] — source article
- [[Slack]] — platform Claude Code sessions can now be delegated from
- [[summary-2025-12-08 - Claude Code and Slack]] — Claude Code and Slack integration announcement
- [[AugmentCode]] — customer example, development-speed case study
- [[Grafana]] — customer example, democratized-expertise case study
- [[summary-2025-12-01 - What are the key benefits of transitioning to agentic coding for software development]] — organizational-benefits article
- [[summary-2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code]] — Growth Marketing case study
- [[Respiro]] — customer example, non-technical PM's 15+ subagent stress-management app
- [[MythicalGames]] — Respiro creator's employer, now internally adopting Claude-based workflows
- [[summary-2026-05-01 - How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks]] — Respiro case study
- [[MultiAgentSystem]] — the orchestrator-subagent pattern Claude Code's own subagents exemplify
- [[summary-2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6]] — 1M context GA for Claude Code Max/Team/Enterprise users
- [[METR]] — benchmark org cited for Claude Code's capability-growth pace
- [[summary-2026-03-19 - Product management on the AI exponential]] — Claude Code's PM philosophy and rhythm
- [[ComputerUse]] — general computer-control capability added to Claude Code
- [[Dispatch]] — phone-based task assignment now available in Claude Code
- [[summary-2026-03-23 - Put Claude to work on your computer]] — computer use and Dispatch launch article
- [[PermissionModes]] — the permission-mode system, including the new auto mode
- [[summary-2026-03-24 - Auto mode for Claude Code]] — auto mode permissions feature announcement
- [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]] — tool-design philosophy and case studies (AskUserQuestion, Task tool, Claude Code Guide)
- [[RetrievalAugmentedGeneration]] — the RAG pipeline Claude Code replaced with self-directed search
- [[summary-2026-04-14 - Redesigning Claude Code on desktop for parallel agents]] — desktop app redesign for managing parallel agent sessions
- [[ClaudeCodeRoutines]] — scheduled/API/event-triggered automation feature
- [[summary-2026-04-14 - Introducing routines in Claude Code]] — routines research-preview announcement
- [[summary-2026-04-15 - Using Claude Code session management and 1M context]] — /rewind, compact-vs-clear decision framework, and bad-compact causes
- [[Claude4.7Opus]] — new default model behavior (xhigh effort, adaptive thinking) covered in the best-practices article
- [[summary-2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code]] — source article
- [[MacCossLab]] — customer example, 17-year legacy C# codebase onboarding methodology
- [[summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development]] — MacCoss Lab / Skyline case study
- [[summary-2026-05-12 - How Anthropic&#39;s cybersecurity team built a threat detection platform with Claude Code]] — CLUE cybersecurity detection-platform case study
- [[summary-2026-05-11 - Agent view in Claude Code]] — CLI agent view feature announcement
- [[PromptCaching]] — the caching mechanism Claude Code's harness is built around
- [[summary-2026-04-30 - Lessons from building Claude Code Prompt caching is everything]] — prompt-caching engineering lessons: static/dynamic ordering, model-switch cost, Plan Mode design, defer_loading, cache-safe compaction forking
- [[LanguageServerProtocol]] — symbol-level navigation capability for large, multi-language codebases
- [[AgenticCoding]] — organizational ownership models (DRI, agent manager role) for scaling adoption
- [[ContextEngineering]] — codebase-legibility patterns (layered CLAUDE.md, codebase maps) for large-scale navigation
- [[Zoox]] — customer providing feedback on the large-codebases best-practices article
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — large-codebase deployment patterns: agentic search vs. RAG at scale, the harness framework, and organizational ownership
- [[HTMLAsAgentOutputFormat]] — pattern of using HTML instead of Markdown for Claude Code outputs
- [[ClaudeDesign]] — Anthropic's HTML-based design prototyping tool
- [[ThariqShihipar]] — Claude Code team member, author of HTML effectiveness and tool-design articles
- [[summary-2026-05-20 - Using Claude Code The unreasonable effectiveness of HTML]] — source article on HTML as Claude Code output format
- [[BorisCherny]] — Head of Claude Code, London 2026 keynote speaker
- [[summary-2026-05-26 - Code w Claude London 2026 Rethinking how we build]] — London 2026 event recap
- [[CodeWithClaude]] — developer conference series featuring Claude Code
- [[DynamicWorkflows]] — large-scale parallel subagent orchestration feature
- [[Ultracode]] — effort setting enabling automatic workflow invocation
- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — dynamic workflows announcement
- [[summary-2026-06-02 - A harness for every task dynamic workflows in Claude Code]] — dynamic workflows patterns and use cases deep-dive
- [[JarredSumner]] — Bun creator, flagship dynamic workflows user
- [[MicrosoftFoundry]] — cloud platform supporting Claude Code dynamic workflows
- [[CodeRabbit]] — built an agent orchestration planning layer that sits above Claude Code
- [[AgentOrchestration]] — the orchestration pattern CodeRabbit implements, inserting structured planning before Claude Code execution
- [[summary-2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system]] — source article on CodeRabbit's planning layer
- [[AIAcceleratedSalesWorkflows]] — non-technical GTM staff building AI tools with Claude Code
- [[ClaudeCowork]] — platform through which sales tools are distributed as plugins
- [[summary-2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code]] — CLAFTS and sales-workflow case study
- [[ClaudeAPI]] — the API powering CLAFTS email drafts
- [[summary-2026-06-03 - How Anthropic enables self-service data analytics with Claude]] — internal data analytics case study
- [[AgenticAnalytics]] — the overarching paradigm of LLM-driven self-service business analytics
- [[summary-2026-06-17 - Claude Design now stays on brand for daily work]] — Claude Design integration (/design-sync, /design)
- [[summary-2026-06-18 - Claude Code now supports artifacts]] — artifacts support announcement
- [[WorkloadIdentityFederation]] — authentication mechanism replacing static API keys, supported in Claude Code
- [[DesignToCodeHandoff]] — the design-to-code workflow Claude Design and Claude Code participate in
- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — hackathon source summary
- [[Medkit]] — hackathon winner using Claude Code for medical training simulation
- [[WrenchBoard]] — hackathon winner using Claude Code for electronics repair diagnostics
- [[Maieutic]] — hackathon winner using Claude Code for CS education IDE
- [[VirtualPuppetTheater]] — hackathon winner using Claude Code for interactive puppet show
- [[MaestrIA]] — hackathon winner using Claude Code for home repair diagnostics
- [[ARIA]] — hackathon winner using Claude Code for industrial maintenance AI
- [[SpecFirstDevelopment]] — planning-first methodology used by multiple hackathon winners
- [[EvalDrivenDevelopment]] — eval-first methodology used by hackathon winners
- [[Superpowers]] — skills framework used alongside Claude Code in the hackathon
- [[ClaudeDesktop]] — the unified desktop app including Claude Code as a surface with cloud inference
- [[AWS]] — cloud platform for Claude Desktop inference
- [[CloudInference]] — the pattern of running AI inference within the customer's own cloud
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — cloud deployment announcement
- [[summary-19 - Build a proactive agent workflow with Claude Code]] — source summary
- [[summary-2026-02-20 - Bringing automated preview, review, and merge to Claude Code on desktop]] — source summary
