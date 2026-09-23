---
title: "Imitation Learning"
type: concept
tags: [machine-learning, robotics]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260824 - Sergey Levine： Humanoid Robotics Results, Chinese Labs & Future Timelines.md"]
last_updated: 2026-09-23
---
## Definition
Imitation learning is the technique of learning a behavior policy from demonstrations rather than from a reward signal.
## Key Information
- The seminal ACT (Action Chunking with Transformers) / ALOHA paper, led by Tony Zhao with Sergey Levine as co-author, showed that cheap teleoperated demonstration collection plus a straightforward transformer could learn surprisingly dexterous tasks.
- Hardware: bimanual ~$7,000 hobbyist arms (Trossen Robotics, transcribed "Trusson Robotics") in a leader-follower teleop setup.
- Representative tasks included replacing batteries in a remote control and putting a shoe on a mannequin foot for an assistive use case.
- The paper's influence came from calibration ("the details matter, but the details don't have to be complicated"), not from a new mathematical idea.
- Zhao open-sourced the ACT code, which became the common starting kit ("starter kit") for robotic learning.
## Related
- [[Tony Zhao]] — lead author
- [[Trossen Robotics]] — the arms
- [[Sergey Levine]] — co-author and advocate
- [[Robot Foundation Models]] — the scaled descendant
- [[Reinforcement Learning]] — the complementary autonomous-experience approach
