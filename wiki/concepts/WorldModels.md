---
title: "WorldModels"
type: concept
tags: [ai, world-model, simulation, game-generation, deepmind]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
World Models are AI systems that generate interactive, navigable environments from text descriptions, enabling users to explore and interact with dynamically created worlds. Google DeepMind's Genie series (1, 2, 3) demonstrates the progression from 2D platformers to real-time 3D environments with memory and real-time prompting.

## Key Information
- **Genie 1**: 2D platformer worlds, ran for seconds, responded to left/right input
- **Genie 2**: Scaled to 3D games, interactive but not real-time, limited quality
- **Genie 3**: Real-time 3D with body presence, environment memory, and real-time prompting (change the world mid-experience)
- **Memory**: Genie 3 environments remember state — run away and return, everything is exactly as it was
- **Real-time prompting**: Can change the world while in it by issuing new prompts
- **Applications**: Entertainment (new form of gaming with adversarial prompting), education (go into a world to learn about it)
- **No physics engine**: Frames generated pixel by pixel without Unity, Unreal, or physics engines
- **Built on**: DeepMind's long history of work on games and simulation (Atari, Go, StarCraft, MuJoCo)

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[Genie1]] — first generation
- [[Genie2]] — second generation
- [[Genie 3]] — third generation (current)
- [[World Model Building]] — related concept
- [[GoogleDeepMind]] — creator
- [[RaiaHadsell]] — research lead
