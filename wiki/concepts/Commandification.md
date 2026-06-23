---
title: "Commandification"
type: concept
tags: [concept, agentic-engineering, slash-commands, workflow, claude-code, technique]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering).md"
last_updated: 2026-06-20
---

## Definition

Commandification is [[ColeMedin]]'s practice of packaging any prompt or workflow he's used more than twice into a reusable slash command — a markdown file in `.claude/commands/` that can be invoked as `/<name>` in [[ClaudeCode]] (or pasted as a prompt in any other [[AICodingAssistant]]).

## Key Information

### The rule

> *"Anytime you send in a prompt to your coding agent more than twice, that should scream to you that it's an opportunity to turn it into a command or a reusable workflow."* — Cole Medin

Two reasons:
1. Saves keystrokes immediately.
2. Standardizes the process so it doesn't drift across sessions or team members.

### Anatomy of a command

A slash command is a markdown file in `.claude/commands/<name>.md`. Cole's typical structure:

```markdown
# /<name>

## Goal
[one-line statement of what this command does]

## Process
1. Step one
2. Step two — possibly with conditional branches
3. Step three

## Constraints
- [explicit don'ts]
- [explicit dos]

## Output format
[what the command should produce — file path, structure, sections]
```

The agent reads this file as the prompt when the command is invoked. The argument (anything after `/<name> `) replaces an `$ARGUMENTS` placeholder in the markdown.

### Examples Cole ships in his habit-tracker repo

| Command | Purpose |
|---|---|
| `/prime` | Load codebase + PRD into context at session start |
| `/create-prd` | Generate the project's north-star PRD ([[PRDFirstDevelopment]]) |
| `/plan-feature` | Run a planning conversation, output structured-plan markdown |
| `/execute-plan <path>` | Build the feature with clean context ([[ContextReset]]) |
| `/git-commit` | Standardized commit message format |
| `/code-review` | Run a structured review pass |
| `/system-evolve` | After feature, reflect on bugs and update rules ([[SystemEvolution]]) |

### Cross-IDE portability

Slash commands are **markdown files**. Three ways to use them:

1. **In [[ClaudeCode]]**: native `/<name>` invocation.
2. **In other AI IDEs** ([[Cursor]], [[Windsurf]], Kiro, Roo Code): paste the file's contents into the prompt and tell the agent to use it.
3. **Shared across team / projects**: commit the `.claude/commands/` folder, every contributor inherits the workflow.

### Why this works

- **Compounding leverage**: a command written once gets used hundreds of times.
- **Self-documenting workflow**: the command markdown *is* the documentation of how Cole uses the agent.
- **Handoff artifact**: a teammate can read your `.claude/commands/` and immediately understand your process.
- **Subject to [[SystemEvolution]]**: commands improve as the project matures.

### Connection to [[PRPFramework]]

PRP framework's `/generate-prp` and `/execute-prp` are commands. The framework is itself a commandification of context-engineering workflows.

### Commands vs skills (Claude Code merged them)

Per `summary-complete-agentic-coding-workflow`, Claude Code recently **merged commands with skills**, but Cole keeps a useful conceptual distinction:
- **Commands** = things *you* invoke explicitly (e.g. `/commit`, `/create-prd`) — a chosen point in a workflow.
- **Skills** = context the *agent* decides to load when it recognizes it needs to do something ([[ClaudeSkills]] / [[ProgressiveDisclosure]]).

Same underlying mechanism (markdown the agent reads); the difference is who triggers it.

### When to skip commandification

Don't commandify ad-hoc one-shot prompts or anything where the command would be longer than just typing the prompt. The "more than twice" rule is the trigger; one-shots stay as prompts.

## Related

- [[AgenticEngineering]] — technique 3 of 5
- [[ContextEngineering]] — broader discipline
- [[ClaudeCode]] — primary surface
- [[PRPFramework]] — the canonical commandified workflow
- [[PRDFirstDevelopment]], [[ModularRulesArchitecture]], [[ContextReset]], [[SystemEvolution]] — companion techniques
- [[ColeMedin]] — author
- [[summary-20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now]] — primary source
- [[summary-20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)]] — commands-vs-skills distinction; command suite in practice
