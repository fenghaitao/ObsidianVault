---
title: "Reinforcement Learning"
type: concept
tags: [machine-learning, AI]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260824 - Sergey Levine： Humanoid Robotics Results, Chinese Labs & Future Timelines.md"]
last_updated: 2026-09-23
---
## Definition
Reinforcement learning (RL) is learning to act from trial-and-error experience and reward, using autonomous interaction rather than static demonstrations.
## Key Information
- Physical Intelligence's π* RL project (transcribed "PI star 6") late last year applied RL to longer-horizon tasks: assembling boxes at Dandelion Chocolate Factory over several days, and making espresso drinks for 13 hours.
- The espresso run relied on high-level prompting (commands roughly every 5 minutes); automating that high-level policy is ongoing work.
- Sergey Levine believes RL that "benefits from autonomous experience" can fine-tune the last few percentage points — going "from like 95 to actually 100%" reliability — the crucial unsolved step.
- RL is central to his proposed milestone: a robot that keeps improving from autonomously collected experience in a novel setting until it reaches practically relevant robustness.
## Related
- [[Physical Intelligence]] — the π* project
- [[Imitation Learning]] — the complementary static-data approach
- [[Data Flywheel]] — autonomous experience as fuel
- [[Generalization]] — what RL robustness buys
- [[Robot Foundation Models]] — the base model RL fine-tunes
