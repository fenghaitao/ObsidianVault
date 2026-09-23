---
title: "Sim-to-Real Transfer"
type: concept
tags: [machine-learning, robotics, simulation]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260824 - Sergey Levine： Humanoid Robotics Results, Chinese Labs & Future Timelines.md"]
last_updated: 2026-09-23
---
## Definition
Sim-to-real transfer is learning in simulation and transferring behavior to real robots; more broadly, it is the question of which data sources (simulation, video, teleoperation, real interaction) a robot model should train on.
## Key Information
- Sergey Levine's stance is "a little bit upside down" from the instinct to imitate LLM pre-training: he argues a model grounded in lots of real embodied data absorbs other sources better.
- Analogy: a flight simulator makes sense to a person because they already have world knowledge; simulations help the model only once it can ground them.
- Evidence (with a colleague transcribed "Saraj" and Simar from Georgia Tech): a robot-data model's representations of human vs. robot experience are fully separated with little robot data, but with lots of robot data they group by task, not embodiment — "minimal sensitivity to embodiment" even though the base model never saw human data.
- The takeaway: put robot experience first, then layer on simulation and video, not the reverse.
## Related
- [[Robot Foundation Models]] — uses the grounding insight
- [[Embodied AI]] — physical grounding
- [[Imitation Learning]] — a key real-data source
- [[Data Flywheel]] — autonomous experience collection
- [[Sergey Levine]] — the argument's source
