---
title: "World Model Building"
type: concept
tags: [ai, world-model, game-generation, simulation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
World Model Building is the AI technique of dynamically generating navigable environments (2D or 3D) from text descriptions. Different approaches include Google DeepMind's Genie series (Genie 1: 2D platformers, Genie 2: 3D non-real-time, Genie 3: real-time 3D with memory and real-time prompting) and World Labs' approach (3D environment generation with game-engine-style assets).

## Key Information
- **Genie 1**: 2D platformer worlds, ran for seconds, responded to left/right input
- **Genie 2**: Scaled to 3D games, interactive but not real-time, limited quality
- **Genie 3**: Real-time 3D with body presence, environment memory (worlds remember state), and real-time prompting (change the world mid-experience)
- Genie 3 generates each frame dynamically pixel by pixel with no physics engine, Unity, or Unreal Engine
- Navigation via WASD keys for movement and arrow keys for perspective changes
- Environments respond to interactions based on training data patterns (e.g., hitting lights triggers reactions)
- Genie 3 is a composition of multiple models: Nano Banana, VEO, Gemini for prompting, plus distributed systems
- World Labs (Fei-Fei Li's company) takes a different approach focusing on 3D assets similar to Unity/Unreal Engine
- Genie 3 does NOT generate 3D game meshes — outputs are 2D pixels only
- Paige Bailey predicts future convergence of approaches toward multiple input/output modalities
- Genie 3 is not yet available as an API; accessible via Ultra subscription in select countries
- Applications: entertainment (adversarial prompting gaming), education (learning by exploring worlds)

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[Genie 3]] — Google DeepMind's implementation
- [[Genie1]] — first generation
- [[Genie2]] — second generation
- [[WorldModels]] — broader concept
- [[World Labs]] — alternative approach
- [[Fei-Fei Li]] — World Labs founder
- [[Nano Banana 2]] — component model in Genie 3 pipeline
