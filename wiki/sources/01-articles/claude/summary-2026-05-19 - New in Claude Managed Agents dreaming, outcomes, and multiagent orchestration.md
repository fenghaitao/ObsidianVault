---
title: "summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration"
type: source
tags: [source, original-material, managed-agents, dreaming, outcomes, multi-agent]
sources: ["raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration.md"]
last_updated: 2026-07-05
---

## Core Summary

Anthropic launches dreaming in [[ClaudeManagedAgents]] as a research preview: a scheduled process that reviews past agent sessions and memory stores, extracts patterns (recurring mistakes, converged-on workflows, team-wide preferences), and curates memory so agents self-improve between sessions, either automatically or with human review before changes land. Alongside dreaming, Anthropic moves outcomes (rubric-based grading with a separate, independent grader), multiagent orchestration (a lead agent decomposing work across specialist subagents on a shared filesystem), and webhooks (completion notifications) to general availability for developers building on Managed Agents. Together these updates aim to let agents handle more complex tasks with less human steering. The article closes with four customer examples, [[Harvey]], [[Netflix]], [[Spiral]] (by [[Every]]), and [[Wisedocs]], showing dreaming, outcomes, and multiagent orchestration in production.

## Key Points

- Dreaming (research preview): reviews sessions plus memory stores, extracts cross-agent patterns, restructures memory to stay high-signal; developer controls how much autonomy dreaming has (auto-update memory vs. review-before-land). Complements real-time [[AgenticMemory|memory]]: memory captures learning during work, dreaming refines it between sessions, especially valuable for long-running work and multiagent orchestration.
- Outcomes: developer writes a rubric describing success; a separate grader evaluates output against it in its own context window (not influenced by the agent's own reasoning), pinpoints what's wrong, and the agent retries. Useful for exhaustive-coverage tasks and subjective quality (brand voice, visual guidelines). Internal testing: up to 10 points task-success improvement over a standard prompting loop (largest gains on hardest problems); +8.4% on docx generation, +10.1% on pptx generation. Outcomes can now be paired with a webhook that fires on completion.
- Multiagent orchestration: a lead agent breaks work into pieces and delegates to specialists, each with its own model/prompt/tools, working in parallel on a shared filesystem. Events are persistent, so the lead agent can check back in with subagents mid-workflow, and every step is traceable in the [[AnthropicConsole|Claude Console]] (which agent did what, in what order, why).
- Status change: outcomes, multiagent orchestration, and memory move from research preview to public beta; dreaming enters as a research preview (request access required).
- Customer evidence: [[Harvey]], dreaming lets agents remember filetype workarounds and tool-specific patterns between sessions on long-form legal drafting; completion rates rose about 6x. [[Netflix]], a platform-team analysis agent uses multiagent orchestration to process build logs from hundreds of sources in parallel and surface only recurring, actionable patterns. [[Spiral]] (by [[Every]]), a Haiku-led, Opus-subagent writing product uses multiagent orchestration (parallel draft generation) plus outcomes (rubric graded against editorial principles and user voice pulled from memory) to gate what gets returned to users. [[Wisedocs]], a document quality-check agent grades each review against internal guidelines using outcomes; reviews reportedly run 50% faster.

## Related

- [[ClaudeManagedAgents]] - the platform these features ship on
- [[AgenticMemory]] - the memory system dreaming extends
- [[MultiAgentSystem]] - the coordination pattern productized as multiagent orchestration
- [[Harvey]] - dreaming customer example
- [[Netflix]] - multiagent orchestration customer example
- [[Spiral]] - outcomes and multiagent orchestration customer example
- [[Wisedocs]] - outcomes customer example
- [[Every]] - company behind Spiral
- [[AnthropicConsole]] - where multiagent orchestration traces are surfaced
