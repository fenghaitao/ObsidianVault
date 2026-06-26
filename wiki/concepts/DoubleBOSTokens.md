---
title: "DoubleBOSTokens"
type: concept
tags: [fine-tuning, llm, bug, tokenization, chat-template]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition

Double BOS tokens is a common fine-tuning bug where two beginning-of-sequence (BOS) tokens are added to the training data (one from the chat template and one from `apply_chat_template`), but only one is present during inference, causing a training/inference mismatch that degrades model accuracy.

## Key Information

- Hugging Face's `apply_chat_template` automatically adds a BOS token if the chat template specifies one
- If users manually add a BOS token in their chat template on top of this, training sees two BOS tokens while inference sees one
- Affects multiple models: Llama 3, Mistral, and Gemma
- Unsloth automatically detects and removes the extra BOS token
- Llama.cpp now emits a warning when double BOS tokens are detected (community contribution)
- Simple check: if `apply_chat_template` is used, do not manually add a BOS token to the chat template

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Unsloth]] — tool that auto-fixes this bug
- [[Llama3]] — affected model
- [[ChatTemplateMismatch]] — related template issue
