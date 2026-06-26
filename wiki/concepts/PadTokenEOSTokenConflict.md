---
title: "PadTokenEOSTokenConflict"
type: concept
tags: [fine-tuning, llm, bug, tokenization, generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition

The pad token / EOS token conflict occurs when a model's padding token and end-of-sequence (EOS) token share the same token ID. Because the pad token is masked during cross-entropy loss calculation, the EOS token also gets masked, causing the model to generate infinitely without knowing when to stop.

## Key Information

- During training, pad tokens are masked out of the loss calculation so they don't contribute to gradient updates
- If the EOS token has the same ID as the pad token, the model never learns to emit an EOS token
- Result: infinite generations during inference because the model doesn't know when to stop
- Phi-3 has this issue by default
- **Fix**: Select an unreserved, untrained token as the pad token, or add a completely new token with a unique hash to the vocabulary
- Unsloth automatically checks for this and fixes it by finding an unused token or adding a new one
- Fundamental rule: EOS token ID and pad token ID must always be different

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Phi3]] — model with this issue by default
- [[Unsloth]] — tool that auto-fixes this
- [[DoubleBOSTokens]] — another tokenization bug
