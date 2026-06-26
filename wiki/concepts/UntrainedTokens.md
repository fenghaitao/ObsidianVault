---
title: "UntrainedTokens"
type: concept
tags: [fine-tuning, llm, bug, embeddings, tokenization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition

Untrained tokens are special reserved tokens in a model's vocabulary whose embeddings have been intentionally set to zero (or near-zero) because they are not used in the base model's training. Using these tokens during fine-tuning causes NaN gradients and breaks training.

## Key Information

- Llama 3 base model has reserved special tokens (0-250) with zero embeddings, plus end-of-turn, start header, and end header tokens that are also untrained
- The instruct model has these tokens trained; the base model intentionally has them zeroed
- Using untrained tokens during fine-tuning causes NaN gradients, breaking the entire training run
- **Fix**: Set untrained token embeddings to the mean of the trained token embeddings — but the mean must exclude untrained tokens from the average, otherwise the result is biased toward zero
- **Alternative fix**: Train the LM head and embedding tokens, which will learn non-zero values for these tokens
- **Common mistake**: Using the Llama 3 instruct chat template (which references these tokens) on the base model — this will cause NaN gradients because the template invokes untrained tokens

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Llama3]] — model with this issue
- [[ChatTemplateMismatch]] — using instruct template on base model triggers this
- [[Unsloth]] — tool that auto-fixes this
