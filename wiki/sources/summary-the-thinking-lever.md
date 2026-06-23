---
title: "The Thinking Lever"
type: source
tags: [test-time-compute, thinking, reasoning, effort, adaptive-thinking]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/15 - The thinking lever.md]
last_updated: 2026-06-23
---

## Core Summary

Alexander Briken from Anthropic's applied AI research team explains how Claude leverages test-time compute (inference-time tokens) to improve problem-solving through three capabilities: thinking (internal reasoning scratchpad), tool calling (interfacing with external systems), and text output. The talk introduces adaptive thinking, an evolution beyond interleaved thinking where Claude freely chooses when to think, call tools, or output text in any order, without being forced to think at predetermined points. Practical guidance is provided on effort levels (low through max) and when to use larger vs. smaller models.

## Key Points

- **Test-time compute scaling:** Claude's performance increases as it spends more tokens thinking, similar to how larger models perform better with more training compute. The max effort score matches the largest model score on the same benchmark.
- **Three capabilities:** Thinking (scratchpad reasoning), tool calling (interfacing with outside world), and text (output to user). These can now be interleaved freely.
- **Adaptive thinking:** Claude chooses when to think, call tools, or output text in any order. It can skip thinking entirely for simple questions (like "what is 10+10"). This is Pareto efficient relative to interleaved thinking.
- **Thinking toggle is a poor proxy:** Turning off extended thinking removes a core capability rather than expressing desired effort. Better to let Claude always have access to thinking and control effort through the effort dial.
- **Effort levels:** Low (latency-sensitive, classification/summarization), Medium, High (good balance for intelligent tasks), Extra High (default for Claude Code and claude.ai), Max (hardest tasks, diminishing returns).
- **Model size vs. effort:** For tasks requiring any intelligence, use a larger model even at low effort rather than a small model at high effort. Small models suit low-intelligence use cases.
- **Claude Plays Pokémon insight:** At low effort, Claude found creative shortcuts (using repels, escape ropes, running from battles) rather than brute-forcing through the game.
- **Future vision:** Users set budget constraints (time or cost) and Claude autonomously allocates compute across tasks.

## Related

- [[ClaudeFable5]] — the model generation enabling these capabilities
- [[ClaudeCode]] — defaults to extra high effort
- [[AdaptiveThinking]] — the concept of models choosing when to reason
- [[ContextWindow]] — related constraint on model reasoning
