---
title: "File System Memory"
type: concept
tags: [agents, memory, file-system, bash, sandbox, persistence]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
File System Memory is an approach to agent memory where the agent stores and retrieves information using the file system of its sandbox/computer, rather than relying on vector databases, external memory services, or in-context message history. The agent reads from and writes to files using bash commands, making memory deterministic and transparent.

## Key Information
- **Implementation**: A `memories.md` file stored in the agent's sandbox. The agent reads it on startup (via `prepareCall`), injects the contents into the system prompt with framing like "Here are your memories:", and writes new memories using bash commands.
- **Why File System**: Agents are very good at generating bash commands. They can use `find`, `ls`, `grep`, `glob`, and other Unix primitives to search and manage memory deterministically — no black-box vector similarity search.
- **Structure**: Nico suggests a structured approach:
  - `memories.md` — core facts injected into every turn (user name, preferences, important context)
  - `conversations.jsonl` — searchable conversation history for deeper lookups
  - Generated scripts (e.g., `weather.py`) — tools the agent built and stored for reuse
- **Self-Extending Pattern**: Agents can generate Python scripts for repeatable tasks, store them, and reuse them. The script descriptions are added to `memories.md` so the agent knows what tools it has built. Nico demonstrated this with a weather lookup script: first invocation generated it, second invocation reused it.
- **Behavioral Impact**: When agents have a file system scratchpad with a plan file, they follow through on tasks better. The plan file keeps the objective at the top, and instructions say "follow this plan file to a T, check things off as you go." This prevents early instructions from being lost in long context windows.
- **Vercel Internal Usage**: Every agent Vercel builds internally (GTM agent, data agent, customer support agent with 90% ticket deflection) uses this file-system-backed approach. Nico describes it as "emergent behavior" — agents paired with file systems stay on track and produce great artifacts showing exactly what work was done.
- **Pink Elephant Problem**: Nico demonstrated that telling the agent "don't record trivial interactions" can backfire — the agent may nuke all memories or record the wrong things. Good memory prompts focus on what TO record, not what NOT to record.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[Agent Memory]] — general concept of agent memory
- [[BashTool]] — the tool enabling file system interaction
- [[Persistent Sandboxes]] — infrastructure enabling persistent file systems
- [[VercelSandbox]] — the sandbox product
- [[Agent Sandbox]] — general sandbox concept
- [[Prepare Call]] — where memories are loaded
- [[FileSystemAsContextEngineering]] — related pattern for context
- [[CodeGenerationForNonCoding]] — agents generating and reusing scripts
