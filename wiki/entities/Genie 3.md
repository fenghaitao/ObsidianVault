---
title: "Genie 3"
type: entity
tags: [model, google, deepmind, world-model, game-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Genie 3 is Google DeepMind's world model for dynamically generating navigable 2D environments from text descriptions. Each frame is generated pixel by pixel with no physics engine, Unity, or Unreal Engine behind the scenes.

## Key Information
- World model for generating navigable 2D environments from text descriptions
- No physics engine, Unity, or Unreal Engine — each frame generated dynamically pixel by pixel
- Navigation via WASD keys for movement and arrow keys for perspective changes
- Composition of multiple models: Nano Banana, VEO, Gemini for prompting, plus distributed systems
- Environments respond to interactions (e.g., hitting lights triggers reactions as if a physics engine existed)
- Not currently available as an API; accessible via Ultra subscription in select countries
- Trusted tester program under active consideration
- Does NOT generate 3D game meshes or assets — outputs are 2D pixels only
- Demonstrated creating a Lego-brick Big Bend National Park with a pink ostrich character

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[Google DeepMind]] — creator
- [[World Model Building]] — concept
- [[Nano Banana 2]] — component model
- [[VEO 3.1 Light]] — component model
- [[World Labs]] — competitor with different approach
