---
title: "ContextRot"
type: concept
tags: [concept, context-window, llm, attention, harness, problem]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20251218 - Are Agent Harnesses Bringing Back Vibe Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
last_updated: 2026-06-19
---

## Definition

Context rot is the degradation of LLM reasoning quality as more information accumulates in its context window. As the prompt grows past some threshold (highly model- and task-dependent), the LLM enters what [[ColeMedin]] calls **"the dumb zone"** — it gets overwhelmed, drops important details, makes mistakes it would have caught with less context. Context rot is the central problem [[AgentHarness]]es and [[ContextEngineering]] discipline are designed to solve.

## Key Information

### Symptoms

- The agent forgets earlier instructions when the conversation is long.
- The agent ignores tool descriptions when many tools are loaded.
- The agent invents details that contradict information actually in its context (because it stopped attending to that part).
- Quality degrades despite the model technically having the information available.

### Why it happens

Even with very large context windows (200K+ tokens for Claude, 1M+ for Gemini, etc.), attention is a finite resource. The model has to allocate "what to attend to" across the whole context. As context grows:
- Signal-to-noise drops (relevant info is diluted by irrelevant).
- Position effects matter — content in the middle of long contexts often gets less attention than content at the start or end.
- Reasoning capacity used by *parsing the context* is reasoning capacity not used for *the task*.

### Mitigation strategies

#### Within a single session ([[ContextEngineering]] level)

- **[[ContextReset]]** — clear context between distinct phases (e.g. between planning and execution).
- **[[ModularRulesArchitecture]]** — keep `CLAUDE.md` short; load reference docs only when relevant to the current task.
- **[[ProgressiveDisclosure]]** — [[ClaudeSkills]] only loads short descriptions upfront; full skill instructions load only when invoked.
- **Smart chunking in [[RetrievalAugmentedGeneration]]** — retrieve only the relevant chunks rather than dumping whole documents.

#### Across sessions ([[AgentHarness]] level)

- **Session boundaries** — fresh context window per session, with explicit handoff artifacts (progress files, codebase, git log).
- **Memory compaction** — summarize old sessions when handing off; lossy but bounded.
- **Sub-agents for isolation** — research/exploration in a sub-agent's own context window, only the result returns to the parent.
- **File system as memory** — write things you'll need later to disk rather than keeping them in context.

### The unsolvable part

Even perfect mitigation can't eliminate context rot — it can only push it further out. From `summary-agent-harnesses-and-vibe-coding`:

> "You can't predict which observation becomes critical 10 steps later." — Manus

True predictive context is essentially impossible. The handoff between sessions will *always* drop something that turns out to matter. The mitigation isn't elimination — it's making the loss tolerable.

### How [[ColeMedin]]'s techniques attack it

| Technique | How it fights context rot |
|---|---|
| [[ModularRulesArchitecture]] | Don't load every rule into every session |
| [[ContextReset]] | Discard accumulated planning context before execution |
| [[Commandification]] | Don't re-explain workflows; reuse compact command markdown |
| [[ClaudeSkills]] + [[ProgressiveDisclosure]] | Capabilities load on-demand, not upfront |
| [[ValidationGates]] | Catch context-rot-induced mistakes inside the session |
| [[HumanInTheLoop]] | Human catches what the rotted context missed |

### Connection to harness-era thinking

Context rot is *why* agent harnesses exist. If an LLM could just keep a 10M-token context window with no attention degradation, there'd be no need to chunk work into sessions. Until that's solved (if ever), harness architectures are how we get long-running agentic work to be reliable.

## Related

- [[AgentHarness]] — the architectural response
- [[ContextEngineering]] — discipline that minimizes context rot inside one session
- [[ContextReset]] — direct mitigation
- [[ClaudeSkills]], [[ProgressiveDisclosure]] — context-bloat-avoidance via lazy loading
- [[ModularRulesArchitecture]] — context-bloat avoidance via referencing
- [[ValidationGates]], [[HumanInTheLoop]] — catch rot-induced mistakes
- [[ColeMedin]] — articulator of the framing
- [[summary-agent-harnesses-and-vibe-coding]] — primary source where Cole defines the term
- [[fighting-context-rot]] — synthesis: every technique in the corpus that fights context rot, by layer
