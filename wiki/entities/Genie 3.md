---
title: "Genie 3"
type: entity
tags: [model, google, deepmind, world-model, game-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Genie 3 is Google DeepMind's world model for dynamically generating navigable interactive 3D environments from text descriptions, featuring real-time interaction, body presence, environment memory, and real-time prompting that allows changing the world mid-experience. Each frame is generated pixel by pixel with no physics engine, Unity, or Unreal Engine behind the scenes.

## Key Information
- World model for generating navigable interactive 3D environments from text descriptions
- **Real-time interaction**: Unlike Genie 2, operates in real-time with high quality
- **Body presence**: Users see their own body interacting with the world (e.g., walking, skiing)
- **Memory**: Environments remember state — run in one direction and return, everything is exactly as it was
- **Real-time prompting**: Can change the world while in it by issuing new prompts mid-experience
- No physics engine, Unity, or Unreal Engine — each frame generated dynamically pixel by pixel
- Navigation via WASD keys for movement and arrow keys for perspective changes
- Composition of multiple models: Nano Banana, VEO, Gemini for prompting, plus distributed systems
- Environments respond to interactions (e.g., hitting lights triggers reactions as if a physics engine existed)
- Not currently available as an API; accessible via Ultra subscription in select countries
- Trusted tester program under active consideration
- Does NOT generate 3D game meshes or assets — outputs are 2D pixels only
- Demonstrated: walking down a muddy Kent lane, skiing, artist-created worlds brought to life, origami lizard world with perfect memory, Camden Canal with real-time world switching

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[Google DeepMind]] — creator
- [[World Model Building]] — concept
- [[WorldModels]] — concept
- [[Genie1]] — predecessor (2D platformer)
- [[Genie2]] — predecessor (3D, not real-time)
- [[Nano Banana 2]] — component model
- [[VEO 3.1 Light]] — component model
- [[World Labs]] — competitor with different approach
- [[RaiaHadsell]] — research lead
