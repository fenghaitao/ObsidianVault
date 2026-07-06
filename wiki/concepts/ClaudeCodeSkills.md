---
title: "ClaudeCodeSkills"
type: concept
tags: [claude-code, skills, automation, context, agent-skills, api]
sources: [raw/03-transcripts/Claude/Claude Code Skills/01 - What are skills.md, raw/03-transcripts/Claude/Claude Code Skills/02 - Troubleshooting skills.md, raw/03-transcripts/Claude/Claude Code Skills/03 - Sharing skills.md, raw/03-transcripts/Claude/Claude Code Skills/04 - How skills compare to other Claude Code features.md, raw/03-transcripts/Claude/Claude Code Skills/05 - Configuration and multi-file skills.md, raw/03-transcripts/Claude/Claude Code Skills/06 - Creating your first skill.md, raw/01-articles/claude/2025-10-16 - Introducing Agent Skills.md, raw/01-articles/claude/2025-11-12 - Improving frontend design through Skills.md, raw/01-articles/claude/2025-11-19 - How to create Skills Key steps, limitations, and examples.md, "raw/01-articles/claude/2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude.md", raw/01-articles/claude/2025-12-18 - Skills for organizations, partners, the ecosystem.md, raw/01-articles/claude/2025-12-19 - Extending Claude’s capabilities with skills and MCP servers.md, raw/01-articles/claude/2026-01-22 - Building agents with Skills Equipping agents for specialized work.md, "raw/01-articles/claude/2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code.md", raw/01-articles/claude/2026-01-29 - A complete guide to building skills for Claude.md, raw/01-articles/claude/2026-03-03 - Improving skill-creator Test, measure, and refine Agent Skills.md, raw/01-articles/claude/2026-03-05 - Skills explained How Skills compares to prompts, Projects, MCP, and subagents.md]
last_updated: 2026-07-04
---

## Definition

Claude Code skills are markdown-based instruction files that teach Claude specialized, task-specific knowledge once and have it applied automatically when relevant. They load on demand via description matching, keeping only a name and description in the context window until activated.

## Key Information

- **Automatic activation:** Claude matches user requests against available skill descriptions and activates matching ones without manual invocation.
- **Context efficiency:** only the skill name and description stay in context; full content loads on demand when activated.
- **Storage locations:** personal skills in `~/.claude/skills` (follow you across projects); project skills in `.claude/skills/` (shared via version control).
- **Comparison to other mechanisms:**
  - CLAUDE.md: loads into every conversation (persistent); skills load on demand (task-specific).
  - Slash commands: require manual typing; skills activate automatically.
  - MCP: tools load into context; skills only load name/description.
- **Use cases:** code review standards, commit message formats, brand guidelines, documentation formats, any repeated explanation to Claude.

### Sharing and Distribution

- **Project sharing:** commit to `.claude/skills` in repo; team gets them automatically on pull.
- **Plugin distribution:** create a `skills` directory in a plugin project; distribute via marketplace for community use.
- **Enterprise deployment:** admins deploy via managed settings; enterprise skills take highest priority and override all others with the same name.
- **Priority hierarchy:** enterprise > personal > project > plugins. Use descriptive names to avoid conflicts.

### Sub-agents and Skills

- Built-in agents (explorer, plan, verify) cannot access skills at all.
- Custom sub-agents only get skills explicitly listed in the `skills` field of their `agent.md` file.
- Skills load when the sub-agent starts, not on demand. Only list skills always relevant to the sub-agent's purpose.

### Advanced Configuration

- **`allowed-tools`:** restricts which tools Claude can use when the skill is active (e.g., read-only for security-sensitive workflows).
- **`model`:** specifies which Claude model to use for the skill.
- **Progressive disclosure:** keep `skill.md` under 500 lines; link to supporting files in `references/`, `scripts/`, `assets/` that load only when needed.
- **Scripts:** execute without loading contents into context; only output consumes tokens.
- **Description quality:** answer "what does this skill do" and "when should Claude use it"; add trigger phrases matching how users phrase requests.

## Agent Skills: The Platform-Wide Standard (October 2025)

Anthropic generalized this same skills mechanism into **Agent Skills**, usable consistently across Claude apps, Claude Code, and the Anthropic API — not just Claude Code:

- **Properties**: composable (skills stack and Claude coordinates their use), portable (identical format across all three surfaces), efficient (loads only what's needed), and powerful (can include executable code for tasks better solved by traditional programming than token generation).
- **Claude apps**: available to Pro, Max, Team, and Enterprise users. Claude auto-invokes relevant skills (visible in its chain of thought). The "skill-creator" skill interactively builds new skills — asking about the workflow, generating folder structure, formatting `SKILL.md`, and bundling resources — with no manual file editing. Team/Enterprise admins must enable Skills org-wide first.
- **Claude Developer Platform (API)**: Skills can be added to Messages API requests; the `/v1/skills` endpoint gives programmatic control over custom skill versioning and management. Requires the **[[CodeExecutionTool|Code Execution Tool]]** beta for the secure environment Skills run in. Anthropic-created skills let Claude read/generate Excel, PowerPoint, Word, and fillable PDFs.
- **Claude Code**: skills install via plugins from the `anthropics/skills` marketplace, or manually to `~/.claude/skills`; the [[ClaudeAgentSDK]] provides the same Agent Skills support for custom-built agents.
- **Security note**: Skills grant Claude code-execution access — use only trusted sources.
- **December 18, 2025 update**: added organization-wide skill management (Team/Enterprise admins provision skills centrally, enabled by default org-wide while individuals can still opt out), a directory of partner-built skills (Notion, Canva, Figma, Atlassian, and others) at claude.com/connectors, easier authoring (describe-to-build, editing existing skills, full-content previews before enabling), and published Agent Skills as an open standard at agentskills.io for cross-platform portability, alongside [[ModelContextProtocol|MCP]]'s precedent.

## Why Skills Instead of Domain-Specific Agents (January 2026)

Anthropic initially expected agents for different domains (coding, research, finance, marketing) to need distinct tools and scaffolding, but converged on a different model: one general-purpose agent (Claude Code, using code as an interface for almost any digital work) equipped with Skills for domain expertise. The reasoning: general capability isn't the same as expertise — an agent without a Skill is like a math genius reasoning from first principles, versus a Skill-equipped agent that behaves like an experienced professional who's handled the task thousands of times.

- **Three-tier progressive disclosure with concrete token costs**: metadata (name/description from YAML frontmatter) stays visible at all times (~50 tokens); the full `SKILL.md` loads only once Claude judges it relevant (~500 tokens); a `references/` directory of supporting docs loads only on further demand (2,000+ tokens). This lets an agent carry hundreds of skills without context-window bloat.
- **Files as the universal primitive**: skills are plain files — versionable with Git, storable in Google Drive, shareable with a team — which is why skill authorship extends beyond engineers to product managers, analysts, and domain experts.
- **Code over traditional tool definitions**: traditional tools can have poorly-written instructions, can't be modified by the model, and bloat context; a real example — Claude kept rewriting the same script to apply Anthropic's brand styling to slides, so the script (`apply_template.py`) was saved once and referenced by the skill's documentation instead of being re-derived every time.
- **Three emerging skill types**: **foundational** (core capabilities like document/spreadsheet/presentation handling, in Anthropic's public skills repo), **partner-integration** (companies like K-Dense, Browserbase, and Notion building skills that make their own services agent-accessible), and **organizational/proprietary** (encoding a company's internal processes, compliance requirements, and institutional knowledge).
- **Emerging agent architecture**: the reasoning loop, the runtime that executes, [[ModelContextProtocol|MCP]] that connects, and skills that guide — four layers, each with a clear purpose that can evolve independently.
- Vertical expansion: skills enhanced Claude's financial-services and healthcare/life-sciences offerings shortly after the initial October 2025 launch.

## Testing, Benchmarking, and Description Tuning (March 2026)

Since most skill authors are subject-matter experts rather than engineers, skill-creator now brings software-testing rigor to skill authoring without requiring code:

- **Two skill categories, different testing needs**: **capability uplift** skills teach Claude something the base model can't reliably do alone (e.g., document-creation skills); **encoded preference** skills sequence steps Claude can already do individually according to a team's specific process (e.g., an NDA-review checklist).
- **Evals**: define test prompts (plus files) and describe what "good" looks like; skill-creator reports whether the skill holds up — isolating real failures precisely (e.g., a PDF skill's struggle with non-fillable forms was traced to missing coordinate anchoring, then fixed).
- **Two key eval uses**: catching quality regressions as models/infrastructure evolve, and detecting when a capability-uplift skill has become unnecessary because the base model now passes the evals without it loaded — a sign the skill's techniques were absorbed into default model behavior, not that the skill is broken.
- **Benchmark mode**: a standardized assessment run after model updates or skill iteration, tracking eval pass rate, elapsed time, and token usage; results can be stored locally, wired into a dashboard, or plugged into CI.
- **Multi-agent eval support**: runs evals in parallel via independent agents in clean contexts, avoiding cross-run bleed and slow sequential execution.
- **Comparator agents**: blind A/B judges comparing two skill versions (or skill vs. no skill) to confirm whether a change actually helped.
- **Description tuning**: analyzes a skill's current description against sample prompts and suggests edits reducing both false-positive and false-negative triggering — applied across Anthropic's document-creation skills, improving triggering on 5 of 6 public skills.
- Longer-term framing: today's SKILL.md is essentially an implementation plan (the "how"); as models improve, a natural-language description of the "what" (the evals themselves) may eventually be the skill.

## claude-api Skill Reaches Partner Tools (April 2026)

The `claude-api` skill — first introduced in [[ClaudeCode]] in March 2026 — encodes expertise for writing production-ready Claude API code: agent-pattern selection, cross-generation parameter differences, and prompt-caching rules. It stays current automatically as Anthropic's SDKs change. In April 2026 it moved beyond Claude Code into four external developer tools — [[CodeRabbit]], [[JetBrains]] (including Junie), [[ResolveAI|Resolve AI]], and [[Warp]] — via an open-source bundling guide (`anthropics/skills`, ~20 lines of CI), letting any coding agent give its users the same Claude API expertise. In Claude Code specifically, the skill exposes direct subcommands: `/claude-api migrate` (model-upgrade walkthrough) and `/claude-api managed-agents-onboard` (configuring [[ClaudeManagedAgents]]). See [[summary-2026-04-29 - Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp]].

## Case Study: MacCoss Lab / Skyline (April 2026)

Brendan MacLean's skill library for the 700,000-line Skyline C# codebase follows a **"reference do not embed"** principle: each skill points into a central documentation knowledgebase rather than duplicating its content, keeping skills lightweight and easy to maintain as the underlying docs change. His most-used skills: a `skyline-development` skill that orients Claude to the project and its documentation, a `version-control` skill encoding project-specific commit/PR conventions, and a `debugging` skill tuned with an explicit trigger condition — "ALWAYS load when investigating bugs, failures, or unexpected behavior" — designed to pull Claude out of "guess and test" mode and toward root-cause analysis before attempting a fix. See [[summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development]].

## Skills in the Full Agentic Stack (March 2026)

Anthropic clarified where Skills sit relative to the rest of Claude's agentic toolkit:

- **Skills vs. prompts**: prompts are ephemeral, conversational, natural-language instructions for one-off requests or refinement; if the same prompt keeps getting typed across conversations, that's the signal to capture it as a Skill instead.
- **Skills vs. [[Projects]]**: Projects provide persistent, static background knowledge for a specific initiative (200K context, auto-RAG beyond that); Skills provide dynamic, on-demand procedural expertise usable across any conversation or project. Key framing: Projects say "here's what you need to know," Skills say "here's how to do things." If the same instructions get copied across multiple Projects, extract them into a Skill instead.
- **Skills vs. [[ClaudeCodeSubagents|subagents]]**: subagents are complete, self-contained agents with their own context window and tool permissions handling a workflow independently; Skills are portable expertise any agent instance can load. Use them together — a subagent can apply a Skill for consistent domain standards (e.g., a code-review subagent using a language-specific best-practices Skill).
- **Skills vs. [[ModelContextProtocol|MCP]]**: MCP connects Claude to external data/tools; Skills teach Claude what to do with that access once connected. Use both together — MCP for connectivity, Skills for procedural knowledge.
- **Worked example**: a competitive-analysis research agent combining a Project (uploaded market research + standing instructions), MCP connections (Google Drive, GitHub), a competitive-analysis Skill (analytical framework), and parallel Claude Code subagents (market-researcher, technical-analyst) — refined turn-by-turn with conversational prompts.
- **Skills orchestrating parallel subagents** (April 2026): beyond a subagent *loading* a skill, a skill can itself define a workflow that launches multiple parallel subagents — e.g., a `/deep-review` skill running three parallel subagent reviews (security, performance, style) and synthesizing their findings into one prioritized summary. See [[summary-2026-04-07 - How and when to use subagents in Claude Code]].

## Skills vs. MCP: Connectivity vs. Expertise (December 2025)

- **MCP = connectivity, Skills = expertise**: MCP gives Claude secure, standardized access to external systems (GitHub, Salesforce, Notion, internal APIs); a Skill supplies the domain knowledge and workflow logic that turns that raw access into a reliable, team-specific outcome. Hardware-store analogy: MCP is having access to the aisles; a Skill is the employee's expertise on what to buy and how to use it.
- **Rule of thumb**: "If you're explaining *how* to do something, that's a skill. If you need Claude to *access* something, that's MCP." MCP-level instructions should stay generic (query syntax, API formats); skill-level instructions cover process-specific sequencing and output formatting — watch for the two contradicting each other (e.g., MCP says return JSON, skill says format as markdown tables).
- **Composability**: a single skill can orchestrate multiple MCP servers (e.g., a competitive-analysis skill coordinating web search, an internal database via MCP, Slack history, and Notion pages); a single MCP server can support many different skills. Adding a new MCP connection lets existing skills incorporate it automatically.
- **Worked examples**: a financial comparable-company-analysis skill paired with MCP connections to S&P Capital IQ, Daloopa, and Morningstar automates a valuation workflow that otherwise takes analysts hours of manual data-pulling and compliance formatting; Notion's "Meeting Intelligence" skill (which pages to search, how to structure output) paired with Notion's MCP server (search/read/create pages) automates meeting prep.

## Case Study: Legal Team Workflows (December 2025)

Anthropic's own legal team used Skills for two distinct purposes: **workflow consistency** (a marketing-review skill encoding the team's historical guidance so Claude flags publicity-rights, overstated-claims, and statistical-accuracy issues before formal submission) and **personal voice** (a skill built by having Claude analyze ten of a lawyer's own memos to learn his formatting and phrasing preferences, then apply them to new drafts). Different Skills served different legal specialties (employment, commercial, privacy, corporate), illustrating Skills as a way to encode and transfer institutional/individual expertise, not just task procedures.

## Case Study: Growth Marketing (January 2026)

A non-technical Anthropic growth marketer built Skills for brand tone/voice, product accuracy, and Google Ads RSA (responsive search ad) best practices, invoked via a custom `/rsa` slash command that cross-references campaign data and keywords against those Skills before producing upload-ready ad copy. The underlying copy/examples baked into the Skills were written in partnership with the product marketing and copywriting teams, so human judgment sits upstream of the Skill rather than being replaced by it. See [[summary-2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code]].

## Writing Effective Skills (November 2025)

- **Only name and description drive triggering** — Claude semantically matches a request against the description; instructions only come into play once a skill has already activated. A strong description states specific capabilities, clear triggers, relevant context, and explicit boundaries (what the skill is *not* for).
- **Build only for real, repeated tasks**: rule of thumb — done it 5+ times already, and expect 10+ more repetitions? That's a skill candidate. Don't write skills speculatively.
- **Menu-style progressive disclosure**: when a skill covers multiple distinct sub-workflows, SKILL.md describes what's available and references separate reference files by relative path (e.g., a docx skill routing to `docx-js.md` for creation vs. `ooxml.md` for editing); Claude reads only the file relevant to the current task.
- **Testing**: a test matrix of normal usage, edge cases, and out-of-scope requests, evaluating triggering and execution separately — triggering failures need broader descriptions, execution failures need more specific instructions.
- The **skill-creator** tool interactively builds skills via clarifying questions and formatting help, recommended for a team's first few skills.

## Case Study: Frontend Design Skill (November 2025)

Unguided, Claude's frontend output converges toward generic, "on-distribution" defaults (Inter fonts, purple gradients) because safe, universally inoffensive design choices dominate web training data — a phenomenon Anthropic's Applied AI team calls **distributional convergence**. Rather than adding frontend-design guidance to the system prompt (which would carry irrelevant context into every unrelated request), Anthropic packaged it as a ~400-token **frontend-aesthetics skill** covering typography, color/theme, motion, and backgrounds, loaded only when Claude is doing frontend work. The technique generalizes: any domain where Claude's default output is generic despite deeper latent capability is a candidate for a Skill — identify the convergent default, provide concrete alternatives, pitch guidance at the right altitude (between hardcoded hex codes and vague high-level assumptions), and package it as a reusable Skill. See [[Artifacts]] for the companion **web-artifacts-builder** skill, which removes a related architectural constraint on artifact complexity.

## Progressive Disclosure's Origin in Claude Code (April 2026)

Before Agent Skills existed, Claude Code's context-gathering evolved from an internally pre-indexed RAG pipeline (fragile across environments, and it handed Claude context rather than letting it search) to a self-directed Grep tool for codebase search. Agent Skills later formalized that same self-directed, recursive file-reading pattern into the named **progressive disclosure** technique. See [[RetrievalAugmentedGeneration]] and [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]].

## Related

- [[summary-01 - What are skills]] — source summary
- [[summary-02 - Troubleshooting skills]] — troubleshooting guide
- [[summary-03 - Sharing skills]] — sharing and distribution
- [[summary-04 - How skills compare to other Claude Code features]] — comparison with other mechanisms
- [[summary-05 - Configuration and multi-file skills]] — advanced configuration
- [[summary-06 - Creating your first skill]] — creation tutorial
- [[ClaudeCode]] — the tool skills extend
- [[CLAUDE-md]] — the persistent alternative
- [[ModelContextProtocol]] — similar tool integration mechanism
- [[analysis-claude-code-extension-mechanisms]] — decision guide for choosing among extension mechanisms
- [[CodeExecutionTool]] — required API beta for running Agent Skills
- [[ClaudeAgentSDK]] — provides the same Agent Skills support for custom agents
- [[ClaudeCodePlugins]] — plugins can bundle and distribute skills
- [[summary-2025-10-16 - Introducing Agent Skills]] — platform-wide Agent Skills announcement
- [[Artifacts]] — the web-artifacts-builder skill's target output format
- [[summary-2025-11-12 - Improving frontend design through Skills]] — frontend-aesthetics and web-artifacts-builder skill case study
- [[summary-2025-11-19 - How to create Skills Key steps, limitations, and examples]] — practical guide to writing SKILL.md files
- [[Anthropic]] — the company whose legal team is profiled as an internal Skills case study
- [[summary-2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude]] — legal-team Skills and MCP case study
- [[summary-2025-12-18 - Skills for organizations, partners, the ecosystem]] — org-wide management, partner directory, and open-standard announcement
- [[ModelContextProtocol]] — the connectivity layer Skills compose with
- [[ClaudeAgentSDK]] — the general-purpose agent runtime Skills equip with expertise
- [[Figma]] — plugin platform automated using a Skill for RSA/brand-voice ad copy
- [[summary-2025-12-19 - Extending Claude’s capabilities with skills and MCP servers]] — MCP-vs-Skills framing and worked examples
- [[summary-2026-01-22 - Building agents with Skills Equipping agents for specialized work]] — why Skills replaced domain-specific agents
- [[summary-2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code]] — Growth Marketing Skills case study
- [[summary-2026-01-29 - A complete guide to building skills for Claude]] — comprehensive downloadable guide to building, testing, and distributing Skills
- [[summary-2026-03-03 - Improving skill-creator Test, measure, and refine Agent Skills]] — evals, benchmark mode, and description-tuning tooling
- [[Projects]] — the persistent-context counterpart to Skills' on-demand expertise
- [[summary-2026-03-05 - Skills explained How Skills compares to prompts, Projects, MCP, and subagents]] — comparison across prompts, Projects, MCP, and subagents
- [[ClaudeForExcelPowerPoint]] — Office add-ins where Skills are now usable
- [[summary-2026-03-11 - Advancing Claude for Excel and PowerPoint]] — Skills support inside Excel/PowerPoint add-ins
- [[summary-2026-04-07 - How and when to use subagents in Claude Code]] — skills orchestrating parallel subagents
- [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]] — RAG-to-Grep-to-Skills progressive-disclosure origin story
- [[summary-2026-04-29 - Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp]] — claude-api skill's expansion into partner developer tools
- [[CodeRabbit]] — partner tool bundling the claude-api skill
- [[JetBrains]] — partner tool bundling the claude-api skill
- [[ResolveAI|Resolve AI]] — partner tool bundling the claude-api skill
- [[Warp]] — partner tool bundling the claude-api skill
- [[ClaudeManagedAgents]] — configurable via the claude-api skill's managed-agents-onboard subcommand
- [[MacCossLab]] — customer example, "reference do not embed" skill-library principle
- [[summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development]] — MacCoss Lab / Skyline skills case study
