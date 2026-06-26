---
title: "Unsloth"
type: entity
tags: [project, open-source, llm, tool]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Unsloth is Daniel Han's open-source fine-tuning tool that automatically detects and fixes common bugs in popular language models (Llama 3, Gemma, Phi-3, Mistral, and more). It provides free Colab notebooks, supports 4-bit QLoRA training, long-context training via gradient offloading, and automated Ollama/GGUF export.

## Key Information
- **Automatic Bug Fixes**: Detects and fixes double BOS tokens, untrained special tokens, pad/EOS conflicts, and chat template mismatches
- **4-bit Training**: Supports QLoRA-style 4-bit training to reduce GPU memory usage
- **Long Context**: Achieves 4× longer context with only 1-2% slowdown via non-blocking gradient offloading to system RAM
- **Model Support**: Works with any Hugging Face model name (Llama, Mistral, Gemma, Phi-3, and more)
- **LoRA Best Practices**: Recommends targeting all linear layers (q, k, v, o, up, down, gate), using powers of 2 for rank, and alpha = 2× rank
- **Ollama Export**: Automatically generates correct Ollama model files with matching chat templates; supports multi-GGUF export
- **Community**: Active Discord channel, blog posts documenting all bug fixes, and free Colab notebooks for getting started
- Founded by Daniel Han and his brother
- Collaborates with Google DeepMind on Gemma 4 support, ensuring community tools work with new models at launch

## Related
- [[DanielHan]] — founder
- [[Gemma4]] — supported model family
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[summary-20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind]] — source
- [[LoRA]] — fine-tuning method used
- [[Ollama]] — export target
- [[GGUF]] — model format for export
- [[Llama3]] — supported model
- [[Gemma]] — supported model
- [[Phi3]] — supported model
- [[GradientOffloading]] — long-context training technique
- [[DoubleBOSTokens]] — bug auto-fixed
- [[UntrainedTokens]] — bug auto-fixed
- [[PadTokenEOSTokenConflict]] — bug auto-fixed
- [[LLMImplementationAnalysis]] — core methodology
