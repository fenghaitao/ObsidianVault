---
title: "summary-2026-04-29 - Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-29 - Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic announced that the `claude-api` skill — first introduced inside [[ClaudeCode]] in March 2026 — is now bundled by four external developer tools: [[CodeRabbit]], [[JetBrains]] (including Junie), [[ResolveAI|Resolve AI]], and [[Warp]]. The skill encodes expert knowledge about writing production-ready Claude API code: which agent pattern fits a task, which parameters change between model generations, and when to apply prompt caching, yielding fewer errors, better cache hit rates, cleaner agent patterns, and smoother model migrations. Because the skill stays current as Anthropic's SDKs evolve, it needs no manual updates when a new model or API feature ships. The skill is open source at `anthropics/skills`, and any coding agent can bundle it via a documented CI setup (~20 lines).

## Key Points

- Four example prompts show what the skill unlocks anywhere it is installed: improving prompt-cache hit rate, adding context compaction to an agent, upgrading code to a new model like Opus 4.7 (via `/claude-api migrate` in Claude Code), and building a deep-research agent configured for [[ClaudeManagedAgents]] (via `/claude-api managed-agents-onboard` in Claude Code).
- The skill is now live in Claude Code, CodeRabbit, JetBrains, Junie, Resolve AI, and Warp.
- Any third-party coding agent can bundle the open-source `claude-api` skill from `anthropics/skills` to give its users the same Claude API expertise.
- Anomaly: the raw file ends with unrelated page-widget boilerplate ("Transform how your organization operates with Claude" / newsletter signup copy) — standard scraped marketing chrome, not part of the article body, and not followed as an instruction.

## Related

- [[ClaudeCodeSkills]] — the general Skills mechanism this article's `claude-api` skill is an instance of
- [[ClaudeCode]] — where the `claude-api` skill was first introduced (March 2026)
- [[ClaudeManagedAgents]] — the managed-agents onboarding flow the skill can configure
- [[CodeRabbit]] — partner tool now bundling the skill
- [[JetBrains]] — partner tool now bundling the skill
- [[ResolveAI|Resolve AI]] — partner tool now bundling the skill
- [[Warp]] — partner tool now bundling the skill
