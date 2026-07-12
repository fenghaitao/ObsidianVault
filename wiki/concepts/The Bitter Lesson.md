---
title: "The Bitter Lesson"
type: concept
tags: [AI, machine-learning, research, philosophy]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-10
---

## Definition

"The Bitter Lesson" is an influential essay by AI researcher Richard Sutton arguing that general methods leveraging computation ultimately outperform approaches built on human knowledge. It was discussed in the context of whether LLMs will plateau and whether something new is needed to reach AGI.

## Key Information

- Richard Sutton discussed on a podcast (with Dwarkesh Patel) how LLMs may be approaching a plateau or dead end because of the way they learn
- Edwin Chen is "in the camp where I do believe that something new will be needed" to reach AGI, aligning with the spirit of the Bitter Lesson
- Edwin's biological perspective: "in the same way that there's a million different ways that humans learn, we need to build models that can mimic all those ways as well"
- The question is whether LLMs alone can learn in all the ways humans do, or if fundamentally different architectures are needed
- This connects to the evolution of post-training techniques — each new method (SFT, RLHF, RL environments) adds a different mode of learning

- Sherwin Wu applies the Bitter Lesson to building with AI: "we were trying to architect all this stuff around [the models] and turns out the models are just kind of eating it all away"
- OpenAI's API team has been "guilty" of taking left and right turns with scaffolding that models later obsoleted
- "The models still end up getting better and we're all learning the bitter lesson day in and day out"
- This is a version of the Bitter Lesson specific to the AI application layer: general methods (smarter models) outperform specialized human-built scaffolding
- Examples: agent frameworks, vector stores, skills files — all scaffolding that models may eventually "eat for breakfast"

## Related

- [[Richard Sutton]] — author of "The Bitter Lesson"
- [[Post-Training]] — the evolving suite of techniques for model learning
- [[Reinforcement Learning Environments]] — the latest new learning method
- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
