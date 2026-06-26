---
title: "DanielHan"
type: entity
tags: [person, ai, researcher, llm, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Daniel Han is an AI researcher and the creator of Unsloth, known for finding and fixing implementation bugs in open-source language models, including Gemma, Llama 3, Phi-3, Grok, and Nemotron. He teaches workshops on LLM internals and fine-tuning best practices.

## Key Information
- **Bug Hunting Methodology**: Opens three implementations side-by-side (DeepMind, HuggingFace, Keras) and compares them line-by-line to find discrepancies
- **Gemma Bugs**: Identified activation function issues (approximate vs. exact GELU), tokenization problems, and double BOS token issues
- **Llama 3 Bugs**: Discovered eight bugs including double BOS tokens, untrained special tokens causing NaN gradients, pad/EOS token conflicts, and chat template mismatches
- **Phi-3 Bugs**: Fixed sliding window off-by-one error (2048 not 2047), pad/EOS token conflict causing infinite generations, and QKV fusion issues for LoRA
- Developed Unsloth which automatically detects and fixes common fine-tuning bugs across model families
- Advocates that understanding low-level architectural details enables anyone to independently analyze new model releases
- Background in mathematics and computer science; strong advocate for learning Singular Value Decomposition (SVD)
- Argues that LLM implementation bug-finding cannot be fully automated because a human must judge which implementation is "correct"

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Unsloth]] — his open-source fine-tuning project
- [[Llama3]] — model with bugs identified
- [[Phi3]] — model with bugs identified
- [[Gemma]] — model with bugs identified
- [[LLMImplementationAnalysis]] — his core methodology
- [[DoubleBOSTokens]] — bug concept he publicized
- [[UntrainedTokens]] — bug concept he publicized
