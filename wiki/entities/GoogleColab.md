---
title: "GoogleColab"
type: entity
tags: [tool, cloud, gpu, machine-learning, python, jupyter]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Google Colab is a free cloud-based Jupyter notebook environment that provides free GPU access (T4), making it suitable for training small machine learning models. Angelos Perivolaropoulos recommended it as an alternative to local training for his LLM workshop, as it provides faster training than most laptops.

## Key Information
- Provides free T4 GPU access for training small models
- Recommended by Angelos Perivolaropoulos for his LLM training workshop as an alternative to local laptop training
- Training the workshop's ~1.8M parameter model took about 15 minutes on Google Colab with T4 GPU
- Users must change runtime type to T4 GPU for accelerated training
- Can install dependencies via pip (torch, numpy, tqdm, tiktoken)
- Supports CUDA, which is automatically detected by the workshop training code
- Faster than CPU-only training and competitive with Apple Silicon (MPS)

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[LLMTrainingFromScratch]] — workshop context
- [[PyTorch]] — framework used
