---
title: "summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs"
type: source
tags: [source, transcript, ai, llm, training, transformer, workshop, pytorch, tokenization, attention, inference]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Core Summary
Angelos Perivolaropoulos, who leads the speech-to-text team at ElevenLabs (creators of Scribe V2, the best transcription model on public benchmarks), delivers a hands-on workshop on training an LLM entirely from scratch using only PyTorch and basic libraries — no pre-trained weights, no HuggingFace Transformers. The workshop builds a ~1.8M parameter GPT-2-style decoder-only transformer on the Shakespeare dataset (~1M characters), covering all four building blocks: tokenizer, model architecture, training loop, and inference. The model can be trained locally on a laptop with 16GB RAM or on Google Colab's free T4 GPU, taking about 15 minutes to produce recognizable Shakespearean text.

## Key Points
- **Speaker Background**: Angelos Perivolaropoulos leads speech-to-text at ElevenLabs, a research engineer who trains new models and works on inference. His team built Scribe V2, currently the best transcription model on public benchmarks. He is currently working on real-time transcription models for agents.
- **Workshop Philosophy**: The workshop uses only torch and basic libraries (numpy, tqdm, tiktoken). This represents ~80% of what research engineers at big labs do — beyond this are optimizations, scaling, and use-case specialization. Inspired by Andrej Karpathy's nanoGPT project.
- **Four Building Blocks**: (1) Tokenizer — converts text to integers/embeddings; (2) Model Architecture — the transformer itself; (3) Training Loop — how the model learns; (4) Inference — generating text from the trained model.
- **Tokenizer — Character-Level**: Uses character-level tokenization with only 65 unique characters from the Shakespeare dataset. This means only 4,225 possible bigrams (65²), making training feasible with limited data. Trade-off: character-level doesn't scale well because models struggle to understand correlations between individual characters vs. whole words. For production models, Byte-Pair Encoding (BPE) is standard — it identifies common character patterns in training data and combines them into reusable tokens.
- **Tokenizer — BPE Explanation**: BPE tokenizers look at all training data (trillions of tokens), find common patterns, and create tokens from them. For code, keywords like "for" and "enumerate" become tokens. Uncommon variable names fall back to character-level or byte-level tokenization. A 50K vocab tokenizer would create a 19M parameter embedding table alone (50K × 384), more than 3× the entire model being built here.
- **Transformer Architecture — GPT-2 Based**: Uses a decoder-only causal model based on GPT-2 architecture. The fundamental building blocks haven't changed much: multi-head self-attention, MLP/feed-forward network, residual connections, and layer normalization. Newer models are more specialized for longer context and scaling, but the core architecture is the same.
- **Multi-Head Self-Attention**: The key differentiator of transformers — allows the model to attend to previous tokens and understand relationships between them. Different attention heads attend to different features (punctuation, grammar, etc.). Big labs like Gemini push to 1M context by finding ways to make the math work at scale.
- **MLP / Feed-Forward Network**: Takes the relationships between tokens from attention and combines them into a representation the model can use to generate logits (the distribution over next tokens).
- **Residual Connections**: Each layer adds to the previous input rather than replacing it entirely (X = X + attention_output). This prevents each layer from "reinventing" the activations and keeps training stable.
- **Layer Normalization**: Scales activations back to normal values so they don't explode across layers. Without it, a value multiplied by 2 through 32 layers becomes ~2^32, exceeding float32 range.
- **Model Configuration**: vocab_size=65, block_size=256 (context window), n_layer=6, n_head=6, n_embd=384. Total parameters: ~1.8M (token embeddings: 25K, positional embeddings: 98K, transformer blocks: ~1.2M per layer × 6 layers).
- **Model Code Structure**: GPT class as top-level module containing: token embeddings, positional embeddings, multiple transformer blocks (each with attention + MLP + layer norms), and an LM head that produces logits. The forward pass: token IDs → embeddings → add positional embeddings → pass through all blocks → layer norm → LM head → logits (and cross-entropy loss during training).
- **Transformer Block**: Each block contains: layer norm → attention → residual add → layer norm → MLP → residual add. This is the fundamental building block repeated n_layer times.
- **Training Data**: Shakespeare dataset (~1M characters), split into training and validation sets. Simple data loader: randomly samples 256-token sequences in batches of 64.
- **Device Support**: Works on Apple Silicon (MPS), CUDA, or CPU. Google Colab with T4 GPU is recommended for speed.
- **Learning Rate Schedule**: Warmup of 100 steps (starting very low to let optimizer stabilize), then cosine decay from peak down to near-zero over 5,000 total steps. Uses AdamW optimizer.
- **Training Loop**: For each step, take batch of 256 tokens × 64 sequences, run forward pass to get logits and loss, compute gradients via backward pass, optimizer step, adjust learning rate. Save checkpoint every 1,000 steps. Run inference on current checkpoint to observe progress.
- **Loss Progression**: Starts at ~4.17 (ln(65), completely random). At 3.3: model understands character frequencies (e.g., "th" appears). At 2.5: better bigram understanding, words like "in" appear. At 1.5-2.0: actual words form. At 1.0-1.2: decent Shakespearean text with recognizable names. Below 1.0: overfitting begins.
- **Validation Loss**: A held-out portion of data the model never sees during training. If train loss decreases but val loss increases, the model is overfitting. For this setup, optimal performance was at ~2,400 steps.
- **Overfitting**: The model memorizes training data rather than learning generalizable patterns. Val loss is a cheap proxy metric; serious LLM training uses benchmark evaluations running alongside training.
- **Inference — Greedy Decoding**: Always picks the highest-probability token. Works well for transcription (only one correct output) but makes LLMs boring and uncreative. Never use for generative LLMs.
- **Inference — Temperature**: Instead of always picking the top token, sometimes picks lower-probability tokens. Temperature ~0.7 is the best middle ground. This counterintuitively improves model performance by preventing repetitive loops. Risk: can randomly hit an end-of-text token, causing premature stopping.
- **Inference — Top-K Sampling**: Prevents the model from ever selecting very unlikely tokens (e.g., the 6th-most-likely token when only 5 are reasonable), even if temperature would randomly hit them. Combined with temperature for best results.
- **Inference Implementation**: Takes token IDs as input, passes through model, applies softmax with temperature to get probabilities, samples next token. Seeds can be used for reproducibility.
- **Final Code Structure**: Three files — model.py (architecture), train.py (data loading + training loop), generate.py (inference). Total: a few hundred lines of code. This same architecture with more data and compute is essentially what GPT-2 and GPT-3 were.
- **Historical Context**: When OpenAI was about to release GPT-2, they said it was "too dangerous for humanity." The code was essentially what's shown in this workshop — just a bigger model with more data. Now this seems funny, but it was a genuine concern at the time.
- **Competition / Challenge**: Participants train their own models and submit the best Shakespearean verse. Rules: must train the model yourself, use a seed with a specific prompt for reproducibility. Winner gets ElevenLabs swag.
- **Improvement Ideas**: Try different model sizes (0.5M to 85M parameters), train a custom BPE tokenizer, increase context length (512+), add dropout, tune learning rates, use better data.

## Related
- [[AngelosPerivolaropoulos]] — speaker, ElevenLabs
- [[ElevenLabs]] — his employer
- [[ScribeV2]] — transcription model his team built
- [[aiDotEngineer]] — conference
- [[AndrejKarpathy]] — nanoGPT inspiration
- [[nanoGPT]] — Karpathy's project that inspired the workshop
- [[PyTorch]] — framework used
- [[GPT-2]] — architecture basis
- [[GPT-3]] — referenced as using same fundamental code
- [[GoogleColab]] — recommended training platform
- [[AdamW]] — optimizer used
- [[TransformerArchitecture]] — core architecture
- [[Tokenization]] — general concept
- [[CharacterLevelTokenization]] — tokenization approach used
- [[BytePairEncoding]] — production tokenization alternative
- [[SelfAttentionMechanism]] — attention mechanism
- [[MultiHeadAttention]] — multiple attention heads
- [[CausalSelfAttention]] — decoder-only attention
- [[ResidualConnections]] — stability mechanism
- [[LayerNorm]] — normalization technique
- [[EmbeddingLayer]] — token-to-vector conversion
- [[PositionalEmbeddings]] — position encoding
- [[NextTokenPrediction]] — training objective
- [[CrossEntropyLoss]] — loss function
- [[LearningRateScheduling]] — learning rate management
- [[LearningRateWarmup]] — warmup phase
- [[CosineDecay]] — decay schedule
- [[WeightDecay]] — regularization
- [[Overfitting]] — training pitfall
- [[ValidationLoss]] — overfitting detection
- [[GreedyDecoding]] — inference method
- [[TemperatureInAI]] — inference parameter
- [[TopKSampling]] — inference method
- [[LLMTrainingFromScratch]] — overarching concept
- [[SoftmaxNumericalStability]] — related to inference
