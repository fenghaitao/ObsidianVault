---
title: "PromptLearning"
type: concept
tags: [prompt-engineering, eval, coding-agents, iteration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Prompt learning (also called system prompt learning) is a paradigm for improving LLM agent performance by iteratively refining system prompts based on English-language feedback from evaluation, rather than using scalar rewards or fine-tuning.

## Key Information
- Coined by Andrej Karpathy, who compared it to the movie Memento: the agent "writes down" what it learns from mistakes and uses those notes in future interactions.
- The process: agent performs a task → evaluation generates English feedback explaining failures → a meta prompt synthesizes improved system prompt rules → agent re-runs with updated rules.
- Contrasted with reinforcement learning (RL): RL uses scalar rewards (e.g., 70% score) requiring the model to blindly infer what to improve; prompt learning provides explicit English explanations of what went wrong.
- Key advantages over RL: more sample-efficient, less data-hungry, no data science team required, and well-suited for teams building agents since LLMs are already highly capable.
- In experiments on SWE-bench with 150 examples, prompt learning improved Claude Code by 5% and Cline by 15% with no model fine-tuning.
- The quality of eval prompts (eval engineering) is the critical differentiator — better explanations lead to better system prompt improvements.
- Prompt learning outperformed DSPy's GEA optimizer in benchmarks, achieving better results in fewer optimization loops.
- The approach reframes overfitting as building expertise: agents should specialize to their domain, similar to how engineers develop domain knowledge.
- Requires co-evolving optimization loops: one for agent prompts and one for eval prompts, since the agent loop only works as well as the eval signal.

## Related
- [[AndrejKarpathy]] — coined the term "system prompt learning"
- [[LLM-as-Judge]] — the evaluation method that generates English feedback
- [[MetaPrompt]] — the prompt that synthesizes improved system prompt rules
- [[EvalEngineering]] — the practice of crafting high-quality eval prompts
- [[DSPy]] — framework with a similar prompt optimization approach (GEA/Jeepa)
- [[CoEvolvingLoops]] — parallel optimization loops for agent and eval prompts
- [[OverfittingAsExpertise]] — reframing of overfitting in prompt learning
- [[RuleBasedPrompting]] — the output of prompt learning
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
