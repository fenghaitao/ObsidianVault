---
title: "Physical Intelligence"
type: entity
tags: [robotics, AI, company, foundation-models]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260824 - Sergey Levine： Humanoid Robotics Results, Chinese Labs & Future Timelines.md"]
last_updated: 2026-09-23
---
## Definition
Physical Intelligence (often stylized π) is a robotics company building general-purpose robot foundation models that can control many different robot embodiments.
## Key Information
- Co-founded/led by Sergey Levine ("the demos that we're doing here at physical intelligence").
- Runs evaluations with emergent capabilities and "child-like" mistakes: a laundry-folding policy disentangled two shirts at once (late 2024), and a kitchen-cleanup model stashed utensils in the oven when it could not open the silverware drawer.
- Built π0 (transcribed "pio5"), a generalist robot policy, and the π* reinforcement-learning project (transcribed "PI star 6") late last year.
- π* demonstrations: assembling boxes over several days at Dandelion Chocolate Factory, and a robot making espresso drinks for 13 hours straight.
- The espresso experiment used high-level prompts (commands updated roughly every 5 minutes) rather than fully autonomous command selection; automating that high-level policy is an active effort.
- Works on cross-embodiment models that handle many robot types; the model outputs a fixed-size action vector, zero-padding robots with fewer degrees of freedom, with "nothing fancy" beyond training on all robots.
- Demonstrates skill transfer across robots via "thinking in the right modality": a text thinking stage transfers high-level behavior, while an image thinking stage let a UR5 fold a t-shirt with no t-shirt-folding data on that arm.
## Related
- [[Sergey Levine]] — co-founder
- [[Robot Foundation Models]] — its core product
- [[Humanoid Robotics]] — adjacent industry
- [[Figure]] — a competitor in humanoids
- [[Imitation Learning]] — foundational technique
- [[Reinforcement Learning]] — the π* project
- [[UR5]] — a robot used in transfer experiments
- [[Data Flywheel]] — the deployment loop it is building toward
