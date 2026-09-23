---
title: "Robot Foundation Models"
type: concept
tags: [robotics, AI, foundation-models]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260824 - Sergey Levine： Humanoid Robotics Results, Chinese Labs & Future Timelines.md"]
last_updated: 2026-09-23
---
## Definition
Robot foundation models are generalist learned models trained on broad robot data across many tasks and embodiments, analogous to language foundation models.
## Key Information
- Sergey Levine's core claim: it is better to train a more general model on data from a breadth of problems than a narrow specialist, even for a specialized application (the machine-translation analogy — build a language model, not a translation system).
- The "foundation model ethos" is deeply uncomfortable in robotics because it contradicts the instinct to build traditional vertically integrated systems.
- Scaling insight: machine learning works at scale, but only if you "scale the right thing"; the LSTM-to-transformer shift shows the winning technology is the one that scales, and robotics is still figuring out its scalable levers ("puzzle pieces").
- Cross-embodiment: the model can output a fixed-size action vector and zero-pad robots with fewer degrees of freedom; deployment usually still needs some data from the target robot, but skills transfer so you need less.
- Cross-robot transfer can be enabled by "thinking in the right modality": text for high-level semantic structure, images for low-level spatial milestones (the UR5 t-shirt-folding example).
- Grounding lesson: start with real robot data; internally, human and robot features group by task rather than embodiment as robot data grows (t-SNE embedding, transcribed "TC embedding"), so the model absorbs human video better afterward.
## Related
- [[Embodied AI]] — the field
- [[Physical Intelligence]] — builds them
- [[Generalization]] — the goal
- [[Data Flywheel]] — how they improve in deployment
- [[Imitation Learning]] — an input technique
- [[Scaling Laws]] — the LLM-era lesson
