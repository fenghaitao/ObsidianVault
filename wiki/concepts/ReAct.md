---
title: "ReAct"
type: concept
tags: [agent, tool-calling, reasoning, dspy, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
ReAct (Reasoning + Acting) is a pattern for tool-calling agents that interleaves reasoning steps with tool invocations. In DSPy, `dspy.ReAct` is the built-in module that exposes Python functions as tools to the LLM.

## Key Information
- In DSPy, ReAct is the primary way to do tool calling: it wraps signatures and injects Python functions as available tools.
- The ReAct module handles the tool-calling loop under the hood, managing the back-and-forth between reasoning and action.
- DSPy's ReAct returns a trajectory object showing which tools were called, the arguments passed, and observations from each call.
- The trajectory is useful for debugging and understanding agent behavior.
- ReAct can be configured with a maximum number of rounds to prevent infinite loops.
- Tools in DSPy's ReAct context are simply Python functions decorated or passed to the module.

## Related
- [[DSPy]] — framework with built-in ReAct module
- [[DSPyModules]] — module system including ReAct
- [[ChainOfThought]] — related reasoning pattern
- [[ToolCalling]] — the broader concept
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
