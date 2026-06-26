---
title: "summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han"
type: source
tags: [source, transcript, fine-tuning, llama-3, gemma, phi-3, bugs, unsloth]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Core Summary

Daniel Han presents eight bugs discovered in Llama 3 (some unreleased at time of talk) that affect fine-tuning quality, along with prior bug fixes for Gemma and Phi-3. The talk covers common fine-tuning pitfalls: double BOS tokens, untrained special tokens causing NaN gradients, pad/EOS token conflicts leading to infinite generations, chat template mismatches between base and instruct models, and complications exporting to Ollama/GGUF. Han also introduces Unsloth, an open-source tool that automatically fixes these issues, and demonstrates their Colab notebooks for free fine-tuning with long-context support via gradient offloading.

## Key Points

- **Double BOS Tokens**: Adding a BOS token in the chat template when Hugging Face's `apply_chat_template` already adds one results in two BOS tokens during training but one during inference, degrading accuracy. Affects Llama 3, Mistral, and Gemma.
- **Untrained Special Tokens**: Llama 3 base model has reserved special tokens (0-250) with zero embeddings that cause NaN gradients during fine-tuning. The instruct model has these trained. Fix by setting them to the mean of trained tokens, excluding untrained tokens from the average. Using the instruct chat template on the base model will also break training.
- **Pad Token ≠ EOS Token**: If pad token and EOS token are the same, the model produces infinite generations because the EOS token gets masked out during cross-entropy loss calculation. Phi-3 has this issue by default. Fix by selecting an unreserved, untrained token as pad token, or adding a new one.
- **Ollama/GGUF Export**: Exporting fine-tuned models to Ollama requires exact chat template matching. Use CPU conversion (not GPU) when converting to llama.cpp/GGUF due to floating-point precision differences.
- **System Prompt Impact**: Adding a system prompt can sometimes significantly improve fine-tuning results — worth trying if missing.
- **LoRA Best Practices**: Target all linear layers (q, k, v, o, up, down, gate), set rank to powers of 2 (16-128), set alpha to 2× rank for better results.
- **Long Context via Gradient Offloading**: Unsloth achieves 4× longer context with only 1-2% slowdown by offloading gradients to system RAM using non-blocking calls (not disk, which is much slower).

## Related

- [[DanielHan]] — speaker, creator of Unsloth
- [[Unsloth]] — open-source fine-tuning tool with automatic bug fixes
- [[Llama3]] — Meta's language model with eight identified fine-tuning bugs
- [[Phi3]] — Microsoft model with sliding window and pad/EOS token issues
- [[Gemma]] — Google model with activation function and tokenization bugs
- [[LoRA]] — parameter-efficient fine-tuning method
- [[DoubleBOSTokens]] — fine-tuning bug concept
- [[UntrainedTokens]] — zero-embedding token issue
- [[PadTokenEOSTokenConflict]] — infinite generation bug
- [[ChatTemplateMismatch]] — base vs instruct template issue
- [[GradientOffloading]] — long-context training technique
- [[Ollama]] — local model runner
- [[GGUF]] — model format for llama.cpp
