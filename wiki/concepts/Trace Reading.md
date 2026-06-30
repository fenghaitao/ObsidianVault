---
title: "Trace Reading"
type: concept
tags: [ai, agents, debugging, harness, observability, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Trace Reading is the primary debugging methodology for agent harnesses: manually reading through agent transcripts line by line to understand where the agent's judgment diverged from human judgment, then tuning prompts accordingly. It requires developing empathy with the model — understanding why it made specific decisions given its limited perspective.

## Key Information
- **Primary Debugging Loop**: "The whole art to building this system and making it good was reading the traces." Not running more experiments — reading what the agent actually did
- **Process**: Read traces → find where agent's judgment diverged from human judgment → tune the prompt for that specific divergence → repeat
- **Same Muscle as Stack Traces**: Reading agent traces uses the same debugging skill as reading stack traces — pattern recognition, understanding causality, identifying root causes
- **Empathy Required**: Key skill is empathizing with the model — understanding its limited perspective. Analogy: navigating a web page with your eyes closed, opening them every 10 seconds to see a static snapshot, then closing them again. "Really putting yourself in the shoes of the model"
- **Tooling Tips**: Pipe agent transcripts into files, grep them with another agent, have another agent play through them and update prompts — closing the loop on harness building itself
- **Anthropic's Practice**: Anthropic in general "just like reading through traces by hand." Some automated first-pass analysis with Claude pointed at traces with custom prompts to identify where things veered off
- **Best Approach**: "By far and away the best approach is just reading the traces by hand. Only then do you truly get to relate to what the model is trying to actually do"
- **QA Agent Example**: Claude out-of-the-box is a bad QA agent — would find bugs and say "fix it later, might take 2 weeks." Only through trace reading could they identify and tune this behavior
- **Why It Matters for Harness Design**: Understanding model behavior through traces reveals which harness components are needed and which can be removed as models improve

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Agent Debuggability]] — broader concept of debugging agents
- [[Agent Observability]] — related infrastructure for understanding agent behavior
- [[Generator-Evaluator Pattern]] — harness pattern debugged via trace reading
- [[Harness Evolution]] — trace reading informs what to simplify
- [[Self-Evaluation Trap]] — behavior identified through trace reading
- [[Empathetic Debugging]] — the mindset required
