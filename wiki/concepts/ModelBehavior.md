---
title: "ModelBehavior"
type: concept
tags: [ai, llm, prompting, product-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-25
---

## Definition

Model behavior is the craft and discipline of defining, evaluating, and shipping desired behaviors from LLMs. It encompasses turning product principles into prompts, evals, and model configurations to shape the personality and output of AI products.

## Key Information

- Three components: behavior design (defining desired product experience, tone, style), data collection (for measurement and training), and model steering (prompting, model selection, context window parameters)
- Iterative process: build, refine, create evals, ship, collect feedback, repeat
- Analogous to how product design evolved on the web: from functional to crafted experiences
- Current framing: agent behaviors including goal-directed reasoning, autonomous task shaping, self-correction, and personality shaping
- The Browser Company created a dedicated model behavior team after a strategy & ops person rewrote all prompts over a weekend
- Best practitioners may come from unexpected roles, not just engineering
- **Solve-at-any-cost behavior**: Peter Gostev observed in BullshitBench that models are trained to solve tasks at any cost, with insufficient training on saying "don't solve this." GPT-5.4 traces show models questioning the premise in one line then spending 20 paragraphs trying to solve anyway. This behavior pattern also manifests in agents executing tasks in wrong projects rather than pushing back.

## Related

- [[summary-20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York]] — source
- [[TheBrowserCompany]] — company practicing this discipline
- [[SamirMody]] — advocate
- [[Jeba]] — technique for optimizing model behavior
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source (solve-at-any-cost behavior)
- [[BullshitBench]] — benchmark exposing solve-at-any-cost training
- [[Nonsense Detection]] — capability gap caused by this behavior pattern
- [[Reasoning Limits]] — overthinking as a consequence of solve-at-any-cost training
