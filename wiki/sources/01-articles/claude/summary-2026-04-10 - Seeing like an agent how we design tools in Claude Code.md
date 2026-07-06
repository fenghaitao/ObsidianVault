---
title: "summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-10 - Seeing like an agent how we design tools in Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic's Thariq Shihipar (Claude Code team) explains the team's philosophy for designing agent tools: shape tools to the model's actual abilities rather than assumed ones, discovered by reading its outputs and experimenting — "learning to see like an agent." The article walks through four case studies from Claude Code's history: the three-iteration path to the AskUserQuestion tool (a parameter on ExitPlanTool, then a markdown output convention, then a dedicated blocking-modal tool); replacing TodoWrite with the Task tool as models got better at using subagents and started treating fixed todo lists as constraining; moving from an internal RAG pipeline to a self-directed Grep tool and eventually Agent Skills' progressive disclosure for context-gathering; and building the "Claude Code Guide" subagent so Claude could answer questions about itself without a new top-level tool or system-prompt bloat. The throughline: the bar for adding a new tool is high (Claude Code has ~20), because each tool is one more option the model must weigh, and yesterday's helpful tool can become tomorrow's constraint as model capability grows.

## Key Points

- **Design frame**: imagine solving a math problem — paper, calculator, or computer are all viable tools, but the right one depends on the solver's own skill level; agents are the same, so tool design must match the model's demonstrated abilities, learned by observing its outputs.
- **AskUserQuestion tool (elicitation)**: three attempts — (1) a questions array parameter on ExitPlanTool, dropped because it conflated presenting a plan with asking questions and left conflicts between plan and answers unresolved; (2) instructing Claude to emit a modified markdown question format for the harness to parse, dropped because Claude couldn't reliably hold the format (dropped options, extra text); (3) a dedicated tool Claude can call anytime (especially prompted during plan mode) that blocks the loop with a modal until answered — this stuck, and is composable via the Agent SDK and Skills.
- **TodoWrite → Task tool**: TodoWrite plus system reminders every 5 turns kept early models on track, but as models improved, the reminders made Claude treat the todo list as fixed rather than revisable, and better subagent usage (Opus 4.5) had no shared-list coordination mechanism — replaced by the Task tool, which supports dependencies, cross-subagent updates, and model-driven edit/delete. Lesson: tools that helped a weaker model can constrain a stronger one; revisit assumptions as capability grows, which also argues for supporting a small set of similarly-capable models.
- **RAG → Grep tool → Agent Skills**: Claude Code initially used an internally pre-indexed RAG pipeline to hand Claude retrieved snippets; it worked but required setup, was fragile across environments, and gave Claude context rather than letting it find its own. Replaced with a Grep tool for self-directed codebase search, later generalized by Agent Skills into **progressive disclosure** — recursive file-based context discovery.
- **Claude Code Guide subagent**: Claude couldn't answer questions about Claude Code itself (e.g., adding an MCP server). Putting docs in the system prompt was rejected as context rot for a rarely-needed capability; a raw progressive-disclosure doc link worked but pulled oversized chunks into context. Solution: a dedicated subagent that does the doc search in its own context per detailed extraction instructions and returns only the answer, keeping the main agent's context clean — not perfect, but expands Claude's action space without a new tool.
- **High bar for new tools**: Claude Code has ~20 tools; the team frequently revisits whether all are still needed, since each is one more option the model has to consider.
- Author: Thariq Shihipar, member of technical staff at Anthropic working on Claude Code.
- No prompt-injection-style anomalies were found in this raw file (clean article content throughout).

## Related

- [[ClaudeCode]] — the product whose tool-design history this article documents
- [[AIAgent]] — general agent-design framing ("see like an agent")
- [[ClaudeCodeSkills]] — progressive disclosure, the technique that generalized the Grep-tool insight
- [[ClaudeCodeSubagents]] — the Claude Code Guide subagent and the Task tool's subagent-coordination role
- [[RetrievalAugmentedGeneration]] — the RAG pipeline Claude Code replaced with self-directed search
