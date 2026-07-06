---
title: "summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start"
type: source
tags: [source, original-material, claude-code, large-codebases, enterprise]
sources: ["raw/01-articles/claude/2026-05-14 - How Claude Code works in large codebases Best practices and where to start.md"]
last_updated: 2026-07-05
---

## Core Summary

The first article in Anthropic's "Claude Code at scale" series distills patterns from Claude Code deployments across multi-million-line monorepos, decades-old legacy systems, and distributed multi-repository architectures. Its central claim: Claude Code navigates large codebases agentically (traversing the file system, grepping, following references) rather than via a pre-built index, which avoids the staleness failures of RAG-style embedding pipelines at scale but means navigation quality is bounded by how well the codebase is set up for Claude to find things. Capability is determined as much by the surrounding "harness" -- CLAUDE.md files, hooks, skills, plugins, MCP servers, plus LSP integrations and subagents -- as by the underlying model. Three configuration patterns recur across successful deployments: making the codebase navigable (lean/layered CLAUDE.md, subdirectory initialization, per-directory test/lint scoping, .ignore-based exclusions, codebase maps, LSP-based symbol search), actively maintaining CLAUDE.md as models evolve (instructions that helped an older model can constrain a newer one), and assigning clear organizational ownership (a DRI or dedicated "agent manager" role, cross-functional governance groups) rather than letting adoption stay bottoms-up and tribal.

## Key Points

- Claude Code operates locally without a maintained codebase index; RAG-based competitors can serve stale results (renamed functions, deleted modules) because embedding pipelines lag active commit velocity -- agentic search avoids this but needs good starting context to know where to look.
- The harness has five extension points -- CLAUDE.md, hooks, skills, plugins, MCP servers -- plus two additional capabilities, LSP integrations and subagents; each has a distinct load timing (every session vs. on-demand vs. always-available vs. when-invoked) and a distinct common failure mode.
- Hooks' most valuable use is continuous self-improvement (a stop hook proposing CLAUDE.md updates; a start hook loading team-specific context), not just guardrails.
- LSP integration gives Claude symbol-level "go to definition"/"find references" precision instead of grep-based text pattern-matching, which is one of the highest-value investments for multi-language codebases.
- Subagents split exploration from editing: a read-only subagent maps a subsystem and writes findings to a file, then the main agent edits with the full picture.
- Recommended codebase-legibility patterns: lean/layered CLAUDE.md (root = pointers/gotchas only), initializing Claude Code in subdirectories (it still walks up and loads every CLAUDE.md along the path to root), scoping test/lint commands per subdirectory, version-controlled `.claude/settings.json` permissions.deny / .ignore exclusions, and lightweight root-level codebase-map markdown files where directory structure alone doesn't orient Claude.
- CLAUDE.md needs active maintenance as models evolve -- rules that compensated for an older model's weaknesses can constrain a newer, more capable one (e.g. forcing single-file refactors, or hooks compensating for missing native tool support like Perforce). Recommended cadence: a configuration review every 3-6 months, or whenever performance plateaus after a major model release.
- Organizational adoption needs a dedicated ownership layer beyond technical configuration: a pre-rollout infrastructure investment (a small team or one person wiring up tooling before broad access), an emerging "agent manager" role (hybrid PM/engineer managing the Claude Code ecosystem), or at minimum a DRI with authority over settings/permissions/plugin marketplace/CLAUDE.md conventions -- without this, bottoms-up adoption fragments and knowledge stays tribal.
- In regulated industries, cross-functional working groups (engineering, infosec, governance) established early, with an initial defined set of approved skills/plugins and required review processes, produced the smoothest rollouts.

## Related

- [[ClaudeCode]] -- the tool this article's best practices apply to
- [[CLAUDE-md]] -- layering, scoping, and maintenance guidance
- [[ClaudeCodeHooks]] -- self-improving hooks pattern
- [[ClaudeCodeSkills]] -- progressive disclosure and path-scoped skills
- [[ClaudeCodePlugins]] -- distribution mechanism for tribal knowledge
- [[ClaudeCodeSubagents]] -- exploration/editing split pattern
- [[ModelContextProtocol]] -- MCP servers as a harness extension point
- [[LanguageServerProtocol]] -- symbol-level navigation for large/multi-language codebases
- [[ContextEngineering]] -- codebase legibility and agentic search
- [[RetrievalAugmentedGeneration]] -- the staleness failure mode agentic search avoids
- [[AgenticCoding]] -- organizational ownership and adoption models
- [[Anthropic]] -- publisher, via its Applied AI team
- [[Zoox]] -- customer providing feedback on the article
