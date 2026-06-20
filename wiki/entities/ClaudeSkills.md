---
title: "ClaudeSkills"
type: entity
tags: [tool, anthropic, claude, capabilities, progressive-disclosure, agent-coding]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260101 - AI Exploded in 2025 - Here’s Everything That Happened.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260129 - Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260216 - How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260302 - Build BEAUTIFUL Diagrams with Claude Code (Full Workflow).md"
last_updated: 2026-06-20
---

## Definition

Claude Skills are [[Anthropic]]'s capability-packaging primitive for [[ClaudeCode]] (and other Claude-based agents). A skill is a folder with a `SKILL.md` describing one capability — and supporting files (Python scripts, reference markdown) — that loads via [[ProgressiveDisclosure]]: only the short description is always in context; full instructions and resources load on demand. By 2026 they're [[ColeMedin]]'s preferred way to give an agent many capabilities without paying upfront context cost for all of them.

## Key Information

### Timeline (2025 recap)

Skills were **released in October 2025** and gained major traction by **December 2025**, when Cole's year-in-review framed them as a defining 2026 paradigm — a more context-efficient alternative/complement to [[ModelContextProtocol]] thanks to [[ProgressiveDisclosure]], and "definitely not limited to the Claude ecosystem" (see `summary-ai-exploded-in-2025`).

### Anatomy of a skill

```
my-skill/
├── SKILL.md              # main instructions; loaded when skill is invoked
├── reference/
│   └── guide.md          # supplementary, loaded on-demand
└── cookbook/
    ├── create.py         # invoked when user wants to create
    └── edit.py           # invoked when user wants to edit
```

The `SKILL.md` starts with a short description (front-matter or first line) — that's the only thing that loads upfront. The rest waits until the agent decides this skill is relevant.

### How invocation works

The agent reads all skill descriptions at session start. When user input matches a skill's invocation criteria (described in the skill's metadata), the agent loads the full `SKILL.md` and proceeds to follow its instructions, optionally loading supplementary files as the workflow needs them.

No explicit `/use-skill <name>` command — the agent decides based on the description and request.

### Why Skills > MCP for this use case

[[ModelContextProtocol]] servers load *all* their tool descriptions at server-mount time. A 20-tool MCP costs ~3-5K tokens of always-loaded context per session. Build a [[SecondBrain]] with 50 capabilities via MCP and you've burned a hundred-thousand tokens before you've sent a prompt.

Skills are lazy by design. 50 skills cost ~50 short descriptions (~1500 tokens) upfront. The active skill's full content loads only when needed. This is the architectural primitive that makes [[SecondBrain]] systems scale.

### Skills Cole's [[SecondBrain]] template ships

| Skill | Origin | Purpose |
|---|---|---|
| **Skill creator** | Anthropic | Meta-skill that creates new skills |
| **Brand & voice generator** | Cole | One-time setup; produces the project's brand spec |
| **PowerPoint generator** | Cole | Python-script-based slide generation, on-brand |
| **Excalidraw diagram generator** | Cole | Diagrams || **Remotion video B-roll** | Cole | AI-generated video clips |
| **YouTube script generator** | Cole | Long-form scripts |
| **X / LinkedIn post generators** | Cole | Short-form ideation |
| **MCP-to-Skill** | Cole | Wraps an MCP server as a skill |

### MCP-to-Skill wrapper

A clever pattern from Cole: when you need an MCP server's capabilities (e.g. [[Zapier]] for Gmail/Calendar/Slack), don't connect it directly. Instead, wrap it in a skill. The skill's `SKILL.md` instructs the agent how to call a Python script that handles MCP. The MCP overhead lives behind progressive disclosure.

### Cross-agent portability — Skills are a universal pattern

Per `summary-build-skills-for-any-agent` (Jan 2026), the Skills *format* — folder + `SKILL.md` + [[ProgressiveDisclosure]] — works with **any** agent that can read markdown and follow filesystem-based capability descriptions. Anthropic popularized it, but it isn't Claude-specific. [[ColeMedin]] ships a [[PydanticAI]] template that reimplements it from scratch:

- **Layer 1 — dynamic system prompt**: at runtime, scan a `skills/` directory, extract each `skill.md`'s YAML front-matter **description + path**, and inject them alongside the static base prompt. (The base prompt must *explicitly teach the agent what skills are and how to invoke them* — LLMs don't innately know the pattern.)
- **Layer 2 — `load_skill` tool**: takes a skill name/path, returns the full `skill.md` contents (which then enter short-term memory).
- **Layer 3 — `read_reference` / `list_references` tools**: pull individual reference files or scripts on demand.

This is framework-agnostic (LangChain, CrewAI, no framework) and model-agnostic (OpenRouter, Ollama/local, OpenAI). Drop a new folder into `skills/` and the agent has the capability next run — exactly the [[ClaudeCode]] convention.

**Best-practice sizing** (Anthropic's guide): description **50–100 words** (~5% of the skill's context); `SKILL.md` typically **300–500 lines** (~30%); the rest in reference files. Simple skills may be a `SKILL.md` alone.

**Skill creator (meta-skill)**: Claude Desktop → Settings → Capabilities → Skills → example skills → toggle **skill creator** — a skill that builds skills, then hands you a `SKILL.md` (+ references) to drop into any agent's skills directory.

### SaaS platforms ship skills (avoiding training-cutoff hallucination)

Per `summary-agent-teams-live-build`, a growing pattern: SaaS/library vendors publish an official **integration skill** so a coding agent gets accurate, current SDK docs and builds correctly first-try — sidestepping the LLM's training-cutoff gap for newer platforms. Cole's example is a **ChargeBee** integration skill (tested with vs. without — "it makes a real difference"). His prediction: *"every single platform you integrate is going to have some skill."* This is the built-into-the-tools successor to what [[Archon]] originally did with RAG-over-documentation.

### Why `.claude/skills/` is the conventional location

Skills live in `.claude/skills/<skill-name>/` at the project root (or in user-global `~/.claude/skills/`). [[ClaudeCode]] reads this directory at session start and ingests every skill it finds. This is the same conventions pattern as `.claude/commands/` for [[Commandification]].

### Connection to the wiki this lives in

This vault uses Claude Skills extensively — see `.claude/skills/{ingest,query,lint}/` for the wiki-specific skills built for the [[KarpathyLLMWiki]] pattern.

## Related

- [[Anthropic]] — creator
- [[ClaudeCode]] — primary host
- [[ProgressiveDisclosure]] — loading strategy
- [[Excalidraw]] — Cole's Excalidraw diagram skill (visual self-validation example)
- [[PydanticAI]] — framework used to reimplement skills from scratch
- [[AgentEvaluation]] — verifying skills are invoked correctly
- [[AgentObservability]] — tracing skill usage in production
- [[SecondBrain]] — pattern that depends on Skills
- [[ModelContextProtocol]] — alternative-and-counterpoint capability surface
- [[Commandification]] — adjacent `.claude/` pattern
- [[ColeMedin]] — popularizer in this corpus
- [[summary-second-brain-with-claude-code-obsidian-skills]] — primary source
- [[summary-ai-exploded-in-2025]] — Oct 2025 release; the emerging 2026 paradigm
- [[summary-build-skills-for-any-agent]] — reimplementing skills in any framework
- [[summary-agent-teams-live-build]] — SaaS platforms shipping integration skills
- [[summary-beautiful-diagrams-claude-code]] — the Excalidraw diagram skill (visual self-validation)
