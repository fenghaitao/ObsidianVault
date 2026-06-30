---
title: "LLMTrainingFromScratch"
type: concept
tags: [llm, training, workshop, pytorch, transformer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Training an LLM from scratch means building and training a language model with no pre-trained weights — starting from random initialization — using only basic libraries like PyTorch. Angelos Perivolaropoulos's workshop demonstrated this with a ~1.8M parameter GPT-2-style transformer on the Shakespeare dataset, covering all four building blocks: tokenizer, model architecture, training loop, and inference.

## Key Information
- Uses no pre-trained weights, no HuggingFace Transformers library — only torch and basic libraries (numpy, tqdm, tiktoken)
- Represents ~80% of what research engineers at big labs do; beyond this are optimizations, scaling, and use-case specialization
- Four building blocks: (1) Tokenizer, (2) Model Architecture, (3) Training Loop, (4) Inference
- Workshop model: ~1.8M parameters, GPT-2 architecture, 6 layers, 6 attention heads, 384 embedding dim, 256 context window
- Trained on Shakespeare dataset (~1M characters) with character-level tokenization (65 tokens)
- Training takes ~15 minutes on Google Colab T4 GPU
- Loss progression: starts at ~4.17 (random), drops to 3.3 (character frequencies), 2.5 (bigrams), 1.5-2.0 (words), 1.0-1.2 (decent text), below 1.0 (overfitting)
- Uses AdamW optimizer with learning rate warmup (100 steps) and cosine decay (5,000 total steps)
- Validation loss used to detect overfitting; optimal performance at ~2,400 steps for this setup
- The same architecture with more data and compute powered GPT-2 and GPT-3
- Final code: three files (model.py, train.py, generate.py), a few hundred lines total

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[AngelosPerivolaropoulos]] — workshop presenter
- [[nanoGPT]] — inspiration project by Andrej Karpathy
- [[GPT-2]] — architecture basis
- [[TransformerArchitecture]] — underlying architecture
- [[CharacterLevelTokenization]] — tokenization approach used
- [[AdamW]] — optimizer used
- [[LearningRateScheduling]] — learning rate management
- [[CrossEntropyLoss]] — loss function
- [[Overfitting]] — training pitfall
