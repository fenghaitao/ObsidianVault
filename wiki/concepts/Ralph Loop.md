---
title: "Ralph Loop"
type: concept
tags: [ai, agents, workflow, implementation, automation, loop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-29
---

## Definition
The Ralph Loop (named after Ralph Wiggum from The Simpsons) is a simple iterative agent loop where an AI picks the next task, implements it, and repeats. The original concept from Jeffrey Hinton Lee (June 2025) was simply re-running the same prompt after the AI finishes — the AI would often review its own work and find things it missed. Matt Pocock structured it into a Kanban-based AFK workflow with TDD and feedback loops. Chris Parsons generalized it to "everything is a loop" — applying the pattern to coding, newsletters, email, calendar, project management, and even running a startup.

## Key Information

### Origin (Jeffrey Hinton Lee, June 2025)
- Named after Ralph Wiggum from The Simpsons — the character who tries the same thing over and over until it works
- Original idea: after AI finishes a task, give it the same prompt again. The AI often reviews its code and realizes it missed something
- This was important when AI coding tools frequently left work incomplete; modern models (GPT-5.1+, Claude Opus 4.6+) are much better at recognizing completion

### Matt Pocock's Structured Approach
- The prompt: local issue files are provided at context start, work on AFK issues only, pick the next task based on priority, implement with TDD, run feedback loops
- Task priority order: critical bug fixes → development infrastructure → trace bullets → polishing quick wins and refactors
- The simplest version is a bash script that cats all issue markdown files, grabs the last 5 commits, and runs Claude Code with permission mode accept-edits
- The AFK version runs in a Docker sandbox for safety
- Pocock recommends running the loop once first (human-in-the-loop version) to tune the prompt before running it repeatedly AFK
- The loop outputs a summary when each issue is complete, describing what was done
- Adds structure with the Kanban board and blocking relationships

### Chris Parsons' Generalized Approach
- Ralph loops applied to everything: coding, newsletters, email, calendar, content, client work
- Dumbest version: `while true; do claude "implement ticket 001"; done`
- Scaling approach: instead of pre-computing all dependencies (waterfall), just say "pick the next most important ticket" — AI figures out dependencies on the fly
- Claude Code's built-in `loop` command uses cron to schedule recurring tasks (sessions last ~3 days)
- Parsons' production Ralph loop skill includes: role definition, fresh context per run, ticket format, status values, Git state checking, recovery states for crashes, verification steps, parallel sub-agents
- Core rule: "Reversible Without Embarrassment" — agents can do reversible things autonomously, must prepare irreversible things for human review
- Runs multiple specialized loops: worker loop, morning loop, heartbeat loop, startup loop
- Key insight: parallelism isn't the bottleneck — human review speed is. Start with sequential loops before parallelizing

### Implementation Patterns
- **Same-session loop**: Claude Code `loop` command keeps context across iterations (convenient but context rot risk)
- **Fresh-context loop**: External while loop starts new session each time (forces information codification into repo)
- **Ticket formats**: Flat markdown files, Beads (Steve Yegge), Linear, Jira — anything the AI can access
- **Sandboxing**: Docker sandbox, separate VPS, fine-grained permissions, Lockbox (Parsons' tool)

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source transcript
- [[MattPocock]] — structured workflow creator
- [[ChrisParsons]] — generalized "everything is a loop" approach
- [[Michael Arnaldi]] — uses Ralph loops for Effect development
- [[JeffreyHintonLee]] — originator of the concept
- [[RalphWiggum]] — namesake
- [[AFK Tasks]] — what the loop processes (Pocock)
- [[Kanban Board for AI Tasks]] — the backlog (Pocock)
- [[Day Shift Night Shift]] — the workflow pattern (Pocock)
- [[Sandcastle]] — the parallelized version (Pocock)
- [[TDD with AI]] — the implementation methodology
- [[Everything is a Loop]] — Parsons' core thesis
- [[Loop Command]] — Claude Code built-in cron loop
- [[Worker Loop]] — Parsons' continuous project loop
- [[Morning Loop]] — Parsons' daily briefing loop
- [[Heartbeat Loop]] — Parsons' periodic check-in loop
- [[Startup Loop]] — Parsons' startup management loop
- [[Reversible Without Embarrassment]] — Parsons' agent autonomy rule
- [[Waterfall vs Loop]] — why loops beat pre-computed dependencies
- [[Theory of Constraints]] — why sequential often beats parallel
- [[Context Rot]] — trade-off in same-session loops
- [[Confirmation Bias in Agents]] — why sub-agent validation matters
- [[AgenticLoop]] — related technical concept
- [[MasterWhileLoop]] — related pattern
- [[Vibe Engineering]] — methodology that uses Ralph loops
- [[Beads]] — ticketing system for Ralph loops
- [[Agent Sandboxing]] — safety for autonomous loops
- [[Lethal Trifecta]] — security concern for autonomous agents
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source (Anthropic's perspective on Ralph loops vs generator-evaluator)
- [[Generator-Evaluator Pattern]] — more advanced adversarial pattern that evolved from Ralph loop limitations
- [[Self-Evaluation Trap]] — limitation of Ralph loops that generator-evaluator addresses
