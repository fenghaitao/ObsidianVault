---
title: "CustomUniverse"
type: entity
tags: [project, hackathon, 3d-reconstruction, robotics, synthetic-data, claude-opus]
sources: ["raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Custom Universe is a winning project from [[Anthropic]]'s [[ClaudeOpus4.8]] Build Day hackathon (June 2026) that turns phone photos of objects into 3D models you can drop into a scene, restyle with text prompts, and move around while the rendered image updates in real time. It was built by [[JakeStevens]] and [[MauricioPereira]].

## Key Information

- **Target users**: robotics labs that need large volumes of synthetic data to train robots for specific tasks and settings. A lab can scan a machine from a factory floor, drop it into a scene, and generate data to fine-tune a robotics model for that exact environment.
- **Problem solved**: building synthetic training environments usually means hiring physicists and engineers to handle physics and collision geometry. Custom Universe lets users arrange scenes by dragging objects around instead, with plans to add precise placement (e.g., nudging an object 30 centimeters across a kitchen counter).
- **Technical architecture**: [[ClaudeOpus4.8]] built the project end-to-end and operated a remote [[NVIDIAH100]] that ran the model throughout the hackathon. The team used [[Claude]] to research which models produced the right output and to build the pipeline that brings phone-scanned objects, captured with [[AppleRealityKit|Apple's RealityKit]], into the web app.
- **Open source**: relies on open-source models and algorithms and is free to use; users can run it on their own GPUs.
- **Team**: [[JakeStevens]] (RIT computer-vision graduate, runs [[Luminal]]) and [[MauricioPereira]] (MIT robotics graduate, runs [[CoatRobotics]]). They met at the hackathon event. Jake had the scene builder as a side project; Mauricio brought the robotics training data problem he knew firsthand.
- **Builder advice**: use [[Claude]] to choose your tools, not just to write the code. The team used Claude for research on model selection and for integrating unfamiliar technologies like [[AppleRealityKit]].

## Related

- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — source summary
- [[ClaudeOpus4.8]] — the model used to build and operate Custom Universe
- [[SyntheticData]] — the concept underlying the project's use case
- [[JakeStevens]] — co-creator (Luminal founder)
- [[MauricioPereira]] — co-creator (Coat Robotics founder)
- [[Luminal]] — Jake Stevens's startup
- [[CoatRobotics]] — Mauricio Pereira's startup
- [[AppleRealityKit]] — Apple's 3D scanning framework used for object capture
- [[NVIDIAH100]] — GPU used to run the model during the hackathon
- [[Tekton]] — fellow winning hackathon project
- [[SimFrancisco]] — fellow winning hackathon project
