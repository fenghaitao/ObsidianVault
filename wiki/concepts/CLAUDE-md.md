---
title: "CLAUDE-md"
type: concept
tags: [claude-code, memory, configuration, markdown]
sources: [raw/03-transcripts/Claude/Claude Code 101/05 - The CLAUDE.md file.md, raw/01-articles/claude/2025-10-15 - How to scale agentic coding across your engineering organization.md, raw/01-articles/claude/2025-11-25 - Using CLAUDE.md files Customizing Claude Code for your codebase.md]
last_updated: 2026-07-04
---

## Definition

CLAUDE.md is a markdown configuration file that provides Claude Code with persistent project memory. Placed at the project root, its contents are automatically appended to every prompt, giving Claude ongoing context about the tech stack, conventions, commands, and preferences.

## Key Information

- Generated via the `/init` command, which analyzes the codebase and creates an initial version.
- Typical contents: tech stack, dev/build/test commands, code style (indentation, exports), architectural conventions (where routes go, preferred patterns).
- **Hierarchy:** project-level CLAUDE.md (root, shared via version control), user-level CLAUDE.md (personal config directory, applies across all projects), and session memory (saved on request when correcting Claude).
- **Best practice:** start without one, observe where Claude needs correction, then add only those items. Keep it compact.
- **Sharing:** project-level CLAUDE.md is intended for version control so the whole team benefits.
- References to project docs can be included using the `@` symbol with file paths.

## What to Include (November 2025 guidance)

- **Project summary and directory map**: a project description plus a simple directory tree gives Claude immediate orientation; document architectural patterns (domain-driven design, microservices, key frameworks) so Claude knows where to look and where to make changes.
- **Custom tools and MCP servers**: document team-specific scripts with usage examples, and note when a tool has a `--help` flag. For [[ModelContextProtocol|MCP]] servers, document scope/limits directly (e.g., "Slack MCP: posts to #dev-notifications only, rate limited to 10 messages/hour") so Claude doesn't misuse a connected tool.
- **Standard workflows**: define what Claude should do before making changes for different task types (e.g., explore-plan-code-commit for features, [[TestDrivenDevelopment|TDD]] for algorithmic work) — the goal is to make Claude think before acting rather than jumping straight to a solution that misses requirements.
- **Iterative growth**: use the `#` key during a session to add instructions you find yourself repeating; a CLAUDE.md that accumulates this way genuinely reflects team practice rather than a one-time speculative setup.
- **Security**: never include secrets, API keys, credentials, or vulnerability details — CLAUDE.md becomes part of the system prompt and should be treated as documentation that could be shared publicly.

## Complementary Context-Management Techniques (November 2025)

- **`/clear`**: resets the context window between distinct tasks while preserving CLAUDE.md — prevents accumulated irrelevant history (e.g., finished auth-debugging details) from degrading focus on new work.
- **Subagents for phase isolation**: instruct Claude to "use a sub-agent to perform a security review of that code" after implementation, so debugging context doesn't color a subsequent, differently-focused analysis. See [[ClaudeCodeSubagents]].
- **Custom slash commands**: markdown files in `.claude/commands/` (supporting `$ARGUMENTS`/`$1`/`$2` placeholders) turn a repeated prompt into a reusable `/command-name`; Claude can write these command files on request.
- **CLAUDE.md as subagent-trigger policy layer** (April 2026): distinct from custom subagent files (which define *who* the specialists are), CLAUDE.md can define *when* Claude must reach for them — e.g., "When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only)" — making the policy consistent across sessions and teammates without anyone needing to ask for it each time. See [[summary-2026-04-07 - How and when to use subagents in Claude Code]].

## Organizational Rollout Practice (October 2025)

When scaling [[AgenticCoding]] across an engineering organization, Anthropic recommends treating CLAUDE.md like living documentation:

- **Create project-level files** checked into the repository root so everyone inherits the same configuration automatically.
- **Update alongside architecture changes**: include CLAUDE.md updates in the same pull requests as the code changes that prompted them.
- **Include in onboarding**: make reviewing the project's CLAUDE.md part of new-hire onboarding.
- **Branch-specific variants**: for projects with significantly different patterns across branches, maintain branch-specific CLAUDE.md content.

## Maintaining CLAUDE.md as Model Intelligence Evolves (May 2026)

As models evolve, instructions written for the current model can work against a future one. A CLAUDE.md rule that helped an earlier model stay on track — e.g., "break every refactor into single-file changes" — may actively constrain a newer model that handles coordinated cross-file edits well. Skills and hooks built to compensate for specific model or tooling limitations become overhead once those limitations no longer exist (e.g., a hook that intercepted file writes to enforce `p4 edit` in a Perforce codebase became redundant once Claude Code added native Perforce mode). Recommended cadence: a meaningful configuration review every three to six months, and whenever performance feels like it's plateaued after a major model release. See [[ClaudeCodeHooks]] and [[AgenticCoding]].

## Context as a Separate Repository (April 2026)

Brendan MacLean ([[MacCossLab|MacCoss Lab]]/Skyline) keeps all AI context — including the root CLAUDE.md — in a dedicated repository (`pwiz-ai`) separate from the codebase, rather than inside it. Rationale: context grows and changes at a different pace than code, and a standalone repo applies uniformly across all branches and time points instead of being tied to one. He treats context as a versioned project artifact in its own right, not a one-time setup: "Understand that Claude can't learn without you recording 'context.' Don't expect magic... Invest in building and maintaining your context layer." Keeping context in the same repo as the code remains a valid alternative — what matters is that it is versioned, maintained, and available when needed, not which repository it lives in. For open-source projects with high contributor turnover, this maintained context layer belongs to the project rather than any one contributor and outlasts everyone who built it. See [[summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development]].

## Related

- [[summary-05 - The CLAUDE.md file]] — source summary
- [[ClaudeCode]] — the tool that consumes CLAUDE.md
- [[ContextWindow]] — the memory constraint CLAUDE.md helps manage
- [[AgenticCoding]] — organizational rollout methodology recommending CLAUDE.md as shared documentation
- [[summary-2025-10-15 - How to scale agentic coding across your engineering organization]] — CLAUDE.md-as-documentation guidance
- [[ClaudeCodeSubagents]] — used for context-isolated phase separation
- [[ModelContextProtocol]] — MCP server documentation pattern within CLAUDE.md
- [[summary-2025-11-25 - Using CLAUDE.md files Customizing Claude Code for your codebase]] — structuring guidance, `/init`, `/clear`, subagents, and custom slash commands
- [[summary-2026-04-07 - How and when to use subagents in Claude Code]] — CLAUDE.md as a subagent-trigger policy layer
- [[MacCossLab]] — customer example using a separate `pwiz-ai` context repository
- [[summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development]] — separate-repository context pattern case study
- [[ContextEngineering]] — layered CLAUDE.md hierarchy for large-codebase navigation
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — layering, subdirectory initialization, and model-evolution maintenance cadence
