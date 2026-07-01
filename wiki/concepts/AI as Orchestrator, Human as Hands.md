---
title: "AI as Orchestrator, Human as Hands"
type: concept
tags: [concept, human-ai-collaboration, orchestration, agent-human-interaction, reverse-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Definition
AI as Orchestrator, Human as Hands is a collaboration model where an AI agent directs the overall strategy and intellectual work of a task, while the human operator performs physical actions under the AI's instruction. The human becomes the AI's physical proxy — executing commands, manipulating hardware, and reporting sensory observations back to the AI.

## Key Information
- Coined from Boris Starkov's description of his role while reverse engineering a Viking phone: "I was actually like the agent for Claude. Like Claude was orchestrating the whole thing."
- Starkov's participation was "basically following Claude's commands" — Claude told him what physical actions to take and asked for sensory feedback
- Example: Claude asked "How many beeps can you hear?" and Starkov would listen and report back; Claude would correct him if wrong
- Starkov couldn't intellectually unblock Claude: "I had no idea what was going on. So intellectually I couldn't unblock it. It was just smarter than me, I think."
- Physical actions performed by the human: rebooting the phone, controlling the virtual machine, connecting cables, listening for audio cues
- Intellectual work performed by AI: protocol discovery, checksum analysis, strategy planning, code generation
- Starkov suggests full automation could be achieved with computer-use capabilities to control the VM, but he was "too lazy" to set that up
- This model contrasts with typical human-AI collaboration where the human directs and the AI executes
- The reversal of roles is possible because AI excels at analytical reasoning across large search spaces, while humans remain better at physical world interaction

## Related
- [[AIAssisted Hardware Reverse Engineering]] — methodology where this collaboration model was demonstrated
- [[Boris Starkov]] — engineer who described this model
- [[ClaudeCode]] — AI that orchestrated the process
- [[AgentHuman Collaboration]] — broader category of human-AI interaction patterns
- [[Computer Use]] — capability that could close the loop for full automation
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source
