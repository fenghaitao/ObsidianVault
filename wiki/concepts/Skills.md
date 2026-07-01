---
title: "Skills"
type: concept
tags: [coding-agents, prompt-engineering, system-prompt, extensibility]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Skills are an extendable system prompt mechanism in Claude Code that allows loading specialized instructions on demand. They function as optional context modules — the agent has a list of available skills with one-line descriptions and can invoke them when needed, loading additional context without permanently cluttering the main context window.

## Key Information
- Think of skills as extendable system prompts loaded on demand
- Designed to avoid cluttering the main context while providing deep specialized knowledge when needed
- Examples: docs updates (writing style and product knowledge), editing Microsoft Office files, design style guides, deep research
- Jared Zoneraich built his entire slide deck using skills: a slide-dev skill, a deep research skill, and a design skill
- Skills are not automatically invoked — users often need to manually call them
- The model should theoretically pick up skills automatically based on one-line descriptions, but this doesn't always work well yet
- Represents a new "first class paradigm" in agent design, similar to todo lists
- May require more post-training to get models to reliably invoke skills when appropriate
- Zoneraich built a deep research skill by feeding Claude Code an article on how deep research works and asking it to rebuild as a skill
- Brendan O'Leary describes skills as reusable playbooks for agents — on-demand workflows for repetitive tasks (motion graphics, daily/weekly/monthly changelog compilation). Skills are part of a three-bucket agent configuration system alongside modes (role-based behavior) and agents.md (always-on project rules).
- Paperclip has a built-in skills manager where agents can install skills from skills.sh. Paperclip-specific skills accumulate branding guides, preferences, and style over time as feedback is given to agents. Meta-agents like a "skill consultant" can diagnose whether other agents are using skills correctly.

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[ClaudeCode]] — the agent that implements skills
- [[Context Management]] — the problem skills help solve
- [[TodoListPattern]] — another prompt-based paradigm in Claude Code
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (skills as reusable playbooks)
- [[AgentModes]] — complementary mode-based configuration
- [[AgentsDotMd]] — complementary always-on configuration
- [[Paperclip]] — agent orchestrator with built-in skills manager
- [[AgentRoutines]] — Paperclip routines can incorporate skills
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (skills as part of connectivity stack, skills over MCP)
- [[ConnectivityStack]] — skills as one of three connectivity tools
- [[SkillsOverMCP]] — upcoming MCP extension for shipping skills with servers
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source (skills as a control mechanism: encode human judgment into work nodes with contingency handling)
- [[AgentHuman Collaboration]] — skills increase control by encoding human judgment that activates during work, unlike planning which requires upfront knowledge
- [[ProgressiveDiscovery]] — skills enable progressive discovery by handling contingencies encountered during execution
- [[JacobLauritzen]] — argued skills are superior to planning because they handle contingencies (e.g., a skill for reviewing termination clauses can encode special EU law)
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source (DeepMind's Darwinian skills governance)
- [[KP Sawhney]] — prefers skills over MCP; describes skills governance at Google scale
- [[Skills Governance]] — curating skills in large organizations to prevent sprawl
- [[SkillsOverMCP]] — the debate between skills and MCP as agent extensibility mechanisms
