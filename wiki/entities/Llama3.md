---
title: "Llama3"
type: entity
tags: [model, meta, llm, open-source, fine-tuning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-26
---

## Definition

Llama 3 is Meta's language model that had eight identified fine-tuning bugs (some unreleased at the time of the talk). The instruct and base versions have critical differences in token training that affect fine-tuning workflows.

## Key Information

- **Eight Known Bugs**: Including double BOS tokens, untrained special tokens, pad/EOS token conflicts, chat template mismatches, and GGUF conversion issues
- **Instruct vs Base**: The instruct model has trained special tokens (reserved tokens 0-250, end-of-turn, start/end header) while the base model has these set to zero embeddings — using the instruct chat template on the base model causes NaN gradients
- **Double BOS Risk**: The `apply_chat_template` function already adds a BOS token; adding another manually creates training/inference mismatch
- **Community Fix**: Llama.cpp now warns about double BOS tokens thanks to community contributions
- **System Prompt**: Adding a system prompt can improve fine-tuning results; many users omit it accidentally
- **GGUF Conversion**: Must use CPU conversion (not GPU) when converting to GGUF/llama.cpp format due to floating-point precision differences

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Meta]] — company behind Llama 3
- [[DoubleBOSTokens]] — fine-tuning bug
- [[UntrainedTokens]] — zero-embedding token issue
- [[ChatTemplateMismatch]] — base vs instruct template issue
- [[Unsloth]] — tool that automatically fixes Llama 3 bugs
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source (used as baseline architecture for long-context training research)
- [[Long Context Training]] — domain using Llama 3B architecture as baseline
