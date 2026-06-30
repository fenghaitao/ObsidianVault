---
title: "summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful"
type: source
tags: [source, transcript, ai, vibe-engineering, effect, clone-the-repo, agents-md, back-pressure-loop, pattern-files, context-management, esLint-as-guardrail, ralph-loop, spec-driven-development, knowledge-cutoff, model-prompting-styles]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-29
---

## Core Summary
Michael Arnaldi, creator of the Effect TypeScript library, demonstrates "vibe engineering" — building a full-stack application with AI from scratch without prior preparation. Starting with an empty repository, he uses GPT 5.4 to scaffold a Bun + Vitest project, clone the Effect repository as a git subtree, generate best-practice pattern files by having the AI explore the Effect codebase, and then build a todo HTTP API with SQLite persistence, OpenAPI docs, and type-safe client. The core thesis: "just clone the [expletive] repo" — giving AI access to library source code is more effective than documentation, MCP servers, or skills for teaching models to use unfamiliar libraries.

## Key Points

### The Clone the Repo Pattern
- LLMs have a knowledge cutoff and cannot learn new information after training — they don't form long-term memory like humans
- Coding agents are trained to focus on your own code, not node_modules or gitignored directories
- The most effective way to teach an AI a library: clone the library repo into your project as a git subtree so the model treats it as your codebase
- This works across languages (TypeScript, Rust) and even for libraries with zero documentation
- Alternative approaches (MCP servers, skills, markdown docs) are less effective because models are primarily trained to consume and produce code, not read human documentation
- The effect.solutions website tried a CLI-based approach but eventually admitted "you should actually just clone the repository"

### Vibe Engineering Workflow
- Start completely from scratch with no preparation for authenticity
- Use GPT 5.4 (prefers lowercase prompts — GPT "gets scared" if you scream at it, unlike Claude which pays more attention to uppercase)
- Scaffold project: Bun runtime, Vitest for testing, TypeScript with strict diagnostics set to error
- Clone the Effect repo as a git subtree (squashed, no history) into a `repos/` folder
- Create `agents.md` with available commands and reference to the Effect repo
- For each feature: ask the model to explore the repo, generate pattern files (e.g., `patterns/http-api.md`, `patterns/sql.md`, `patterns/testing.md`), then implement following those patterns
- Use spec-driven development: discuss a plan with the model, persist it as a markdown file, then implement
- Use Ralph loops: a simple bash script that tells the model "pick up a small task, implement it, then exit" — run in a loop
- Restart sessions frequently to avoid context pollution (the "dumb zone" past ~50% context window fullness)

### Back Pressure Loop with ESLint
- ESLint is an essential piece of the feedback loop that keeps AI on track
- Write custom lint rules to prohibit AI shortcuts: ban `as X` type assertions, ban `any`, ban `unknown`, ban SQL type interfaces (force SQL schema usage)
- When the model finds workarounds (e.g., `as never as X`), add more rules
- Force branded types for identifiers instead of plain strings to prevent type confusion
- Force schema validation at the API edge instead of constructors inside handlers
- This is "babysitting a junior developer with a knife running through the kitchen"

### Live Demo: Building a Todo API
- Set up Bun + Vitest + TypeScript with all diagnostics as errors
- Cloned Effect repo as git subtree
- Created `agents.md` with commands and Effect repo reference
- Generated pattern files: `patterns/http-api.md` (shared HTTP API pattern, OpenAPI derivation), `patterns/sql.md` (Effect SQL + SQLite), `patterns/testing.md` (use `EffectTest`, `itLayer`, avoid custom wrappers)
- Built CRUD todo API with SQLite persistence, migrations, OpenAPI docs at `/docs`, type-safe client
- Tests use `itLayer` for providing layers; avoid `Layer.build` wrappers
- Model initially used unnecessary patterns (custom test wrappers, `Schema.Struct` instead of classes) — corrected via feedback

### Context Management Strategies
- Context window is limited; 1M token windows are not necessarily helpful — more information can confuse the model
- Restart sessions frequently to avoid context pollution
- Use Ralph loops: simple bash script that picks a small task, implements it, exits — run in a loop
- Less is more: reducing the number of tools the model has access to can improve results
- Experimenting with a coding agent that has a single `execute` tool (runs arbitrary TypeScript including bash via TypeScript) — model writes TypeScript transformers to modify code

### Model Selection and Prompting
- GPT models: use lowercase — they "get scared" and become passive/agreeable if you use uppercase
- Claude/Opus models: use uppercase — they pay more attention to capitalized instructions
- GPT 5.4 is more concise than Opus; Opus would write 200 lines of agents.md for the same task
- Opus tends to take shortcuts (e.g., `as any`); GPT takes longer but output is often better
- Open weights models lag frontier models by 3-6 months
- No single model is universally better — sometimes one one-shots a solution the other couldn't solve for half a day

### Workflows and Clustering (mentioned, not demoed)
- Effect has workflow/clustering capabilities (similar to Temporal) for durable execution
- Useful when two unrelated operations need to happen together (e.g., registration + email) — no database transaction spans them
- With AI integration, every process becomes longer-running (LLMs take minutes to answer), making durable execution more critical
- At scale, every edge case happens twice per day; with longer response times, even 10 users will hit failures

### Key Insights
- "Our job as programmers should be to set up repositories in ways that models can act good on it"
- Pattern files should be generated per-model because prompting styles differ (GPT vs Claude)
- Skills are useful for workflow automation but not for teaching models libraries — they pollute context
- Semantic code search helps models find existing implementations instead of reimplementing
- The model is good when it can operate at large scale using patterns — the zero-to-one problem is only a problem for the first 10 hours
- "Many times less is more" — the dumbest context management approach often works best

## Related
- [[Michael Arnaldi]] — speaker, creator of Effect
- [[Effect]] — TypeScript library for type-safe applications
- [[Effectful]] — Michael Arnaldi's company
- [[Clone the Repo Pattern]] — core technique demonstrated
- [[Vibe Engineering]] — the AI-assisted development approach
- [[Back Pressure Loop]] — ESLint-based AI guardrail pattern
- [[Pattern Files (AI)]] — AI-generated best practice references
- [[Model Prompting Styles]] — GPT vs Claude prompting differences
- [[AgentsDotMd]] — project configuration for AI agents
- [[Ralph Loop]] — iterative agent task loop
- [[SpecificationDrivenDevelopment]] — spec-driven approach used
- [[ContextEngineering]] — context management strategies
- [[KnowledgeCutoff]] — fundamental LLM limitation
- [[VibeCoding]] — related AI-assisted coding concept
- [[aiDotEngineer]] — event host
- [[Bun]] — JavaScript runtime used
- [[OpenAI]] — GPT 5.4 model used
- [[SQLite]] — database for persistence
- [[ESLint]] — linting tool used as AI guardrail
- [[Temporal]] — workflow solution mentioned for comparison
