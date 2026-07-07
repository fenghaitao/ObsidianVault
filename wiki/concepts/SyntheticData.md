---
title: "SyntheticData"
type: concept
tags: [synthetic-data, robotics, training-data, simulation, 3d-reconstruction]
sources: ["raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Synthetic data is artificially generated data that mimics real-world data distributions, used to train machine learning models when real data is scarce, expensive, or difficult to collect. In the context of the [[ClaudeOpus4.8]] Build Day hackathon, it was the primary use case for [[CustomUniverse]], which generates synthetic training data for robotics models.

## Key Information

- **Robotics application**: robotics labs need large volumes of synthetic data to train robots for specific tasks and settings. [[CustomUniverse]] lets a lab scan a machine from a factory floor, drop it into a scene, and generate data to fine-tune a robotics model for that exact environment.
- **Barrier reduction**: building synthetic training environments traditionally requires hiring physicists and engineers to handle physics and collision geometry. [[CustomUniverse]] replaces this with drag-and-drop scene arrangement, with plans for precise placement (e.g., nudging an object 30 centimeters across a kitchen counter).
- **Pipeline**: phone-scanned objects captured with [[AppleRealityKit|Apple's RealityKit]] are brought into a web app where [[ClaudeOpus4.8]] handles the 3D reconstruction and scene rendering pipeline. The system operates on a remote [[NVIDIAH100]].
- **Open-source approach**: [[CustomUniverse]] relies on open-source models and algorithms, is free to use, and users can run it on their own GPUs — lowering the barrier for robotics labs that lack specialized simulation engineers.

## Related

- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — source article
- [[CustomUniverse]] — the hackathon project demonstrating synthetic data generation for robotics
- [[ClaudeOpus4.8]] — the model used to build the pipeline
- [[SyntheticPopulation]] — a related concept using synthetic data for population simulation
- [[AppleRealityKit]] — Apple's 3D scanning framework used in the pipeline
- [[NVIDIAH100]] — GPU hardware used for model inference
