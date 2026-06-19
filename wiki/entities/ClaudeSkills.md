---
title: "ClaudeSkills"
type: entity
tags: [tool, anthropic, claude, capabilities, progressive-disclosure, agent-coding]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
last_updated: 2026-06-19
---

## Definition

Claude Skills are [[Anthropic]]'s capability-packaging primitive for [[ClaudeCode]] (and other Claude-based agents). A skill is a folder with a `SKILL.md` describing one capability — and supporting files (Python scripts, reference markdown) — that loads via [[ProgressiveDisclosure]]: only the short description is always in context; full instructions and resources load on demand. By 2026 they're [[ColeMedin]]'s preferred way to give an agent many capabilities without paying upfront context cost for all of them.

## Key Information

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
| **Excalidraw diagram generator** | Cole | Diagrams |
| **Remotion video B-roll** | Cole | AI-generated video clips |
| **YouTube script generator** | Cole | Long-form scripts |
| **X / LinkedIn post generators** | Cole | Short-form ideation |
| **MCP-to-Skill** | Cole | Wraps an MCP server as a skill |

### MCP-to-Skill wrapper

A clever pattern from Cole: when you need an MCP server's capabilities (e.g. [[Zapier]] for Gmail/Calendar/Slack), don't connect it directly. Instead, wrap it in a skill. The skill's `SKILL.md` instructs the agent how to call a Python script that handles MCP. The MCP overhead lives behind progressive disclosure.

### Cross-agent portability

Per a January 2026 video (`Claude Skills Aren't Just for Claude — How to Build Them for ANY Agent`, planned for Tier-3 ingest in a future batch): the Skills *format* — folder + `SKILL.md` + progressive disclosure — works with any agent that can read markdown and follow filesystem-based capability descriptions. So Skills aren't strictly Claude-specific; the framework Anthropic shipped is just the most polished implementation.

### Why `.claude/skills/` is the conventional location

Skills live in `.claude/skills/<skill-name>/` at the project root (or in user-global `~/.claude/skills/`). [[ClaudeCode]] reads this directory at session start and ingests every skill it finds. This is the same conventions pattern as `.claude/commands/` for [[Commandification]].

### Connection to the wiki this lives in

This vault uses Claude Skills extensively — see `.claude/skills/{ingest,query,lint}/` for the wiki-specific skills built for the [[KarpathyLLMWiki]] pattern.

## Related

- [[Anthropic]] — creator
- [[ClaudeCode]] — primary host
- [[ProgressiveDisclosure]] — loading strategy
- [[SecondBrain]] — pattern that depends on Skills
- [[ModelContextProtocol]] — alternative-and-counterpoint capability surface
- [[Commandification]] — adjacent `.claude/` pattern
- [[ColeMedin]] — popularizer in this corpus
- [[summary-second-brain-with-claude-code-obsidian-skills]] — primary source
