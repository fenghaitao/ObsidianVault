---
title: "Data Flywheel"
type: concept
tags: [machine-learning, robotics, data]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260824 - Sergey Levine： Humanoid Robotics Results, Chinese Labs & Future Timelines.md"]
last_updated: 2026-09-23
---
## Definition
A data flywheel is a positive feedback loop in which deployed robots collect data that improves their models, which in turn enables more deployment.
## Key Information
- Sergey Levine: "the key" is an effective positive feedback loop in which more deployed robots translates to more model capability.
- The catch is scaling "the right thing": a welding robot that welds a million parts a month yields data that only makes it slightly better at welding — low marginal value.
- Data is "not quite as fungible" as electricity or oil; it has to be heterogeneous — "data is more like an education program for your robot than it is a fungible commodity."
- The timeline depends on how much structure you accept: unstructured home deployment has higher diversity but a higher safety bar; structured tasks start sooner with a smaller slope.
## Related
- [[Humanoid Robotics]] — where the flywheel will spin up
- [[Robot Foundation Models]] — the thing improved by the loop
- [[Reinforcement Learning]] — consumes autonomous experience
- [[Generalization]] — the capability the loop compounds
- [[Sergey Levine]] — articulates the concept
