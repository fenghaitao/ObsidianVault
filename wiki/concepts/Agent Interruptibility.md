---
title: "Agent Interruptibility"
type: concept
tags: [voice, agents, ux, turn-taking, multimodal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - How to talk to statues — Joe Reeve, ElevenLabs.md"]
last_updated: 2026-06-30
---

## Definition
Agent Interruptibility is the challenge of designing voice agent interactions where users can naturally interrupt, provide back-channel feedback ("yeah," "uh-huh"), and navigate agent responses without the social friction of feeling rude or the technical limitation of binary on/off voice interaction.

## Key Information
- Current voice agents have a binary pattern: you're either interacting with voice or interacting another way — no smooth blending
- People are "too polite" to interrupt voice agents, which degrades the experience; aggressive interruption actually improves it
- The problem: "how to give people permission to interrupt" remains unsolved
- Back-channeling (saying "yeah, yeah" while listening) doesn't work with current agents — they can't distinguish between active listening cues and actual interruptions
- In human conversation, speakers can sense when someone is about to interrupt and adjust pace; agents lack this capability
- Users don't know how long an agent response will be (10 seconds vs. a minute) — they want a preview of response length
- When users interrupt and say "go to the next one," the agent treats it as a new prompt rather than skipping ahead in the current response
- The transcript of a conversation could be analyzed asynchronously to detect when the agent should have something to add
- A proposed improvement: show visual cues (like a circle appearing) indicating "the agent wants to ask you a question" rather than interrupting
- Another proposal: signal the topic the agent wants to discuss, adding more context than human conversation provides
- Voice agents could use timestamps to edit the transcript at the point of interruption, forgetting any text generated after that point
- Push-to-talk (hold to talk, release to finish) is a workaround that augments pure audio with a manual cue
- The Claude app shows higher-level sections during voice interactions that users can tap on — a step toward multimodal interruptibility

## Related
- [[summary-20260601 - How to talk to statues — Joe Reeve, ElevenLabs]] — source
- [[Voice Agents]] — the broader category
- [[Multimodal Conversations]] — the voice + visual approach that could solve interruptibility
- [[Turn Taking]] — related capability for natural conversation flow
- [[Voice Interaction Patterns]] — the design patterns emerging around voice UX
- [[Skim Listening]] — the related problem of navigating audio content non-linearly
- [[Half Duplex]] — the current technical limitation
- [[Full Duplex]] — the ideal state for natural interruption
