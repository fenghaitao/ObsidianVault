---
title: "MultimodalAI"
type: concept
tags: [llm, multimodal, images, audio, dspy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Multimodal AI refers to LLM applications that work with multiple input modalities (images, audio, text, PDFs) simultaneously. DSPy supports multimodality by default, allowing images and other media to be passed as signature inputs.

## Key Information
- DSPy supports multiple modalities (images, audio, etc.) natively as part of its signature system.
- The "attachments" library simplifies working with different file types, converting them into formats easily consumed by LLMs.
- Multimodal DSPy signatures can take images as input fields and produce structured text outputs.
- Example use cases include: analyzing street sign images to determine parking rules, extracting data from SEC Form 4 PDFs, and classifying document types from page images.
- Different models may be better at different modalities (e.g., Gemini for image recognition), and DSPy's model mixing allows routing multimodal tasks to the best model.

## Key Information (Gemma 4)
- Gemma 4 models are natively multimodal from the start, supporting vision, text, and audio inputs
- 31B and 26B use a 550M parameter vision encoder; E2B and E4B use a compact 150M parameter encoder
- Vision processing: images split into 16x16 pixel patches, then 3x3 grids of patches become single embeddings
- Variable aspect ratios and variable resolutions give developers control over image processing quality vs. token budget
- E2B and E4B add audio input via a 305M parameter conformer with mel spectrogram tokenizer for speech recognition and translation
- Five soft token budgets available across all models for flexible image processing

## Key Information (Gemini 3.1)
- Gemini models are multimodal for both inputs and outputs, unlike most competitors which only handle text/code outputs
- Input modalities: video, images, audio, text, code
- Output modalities: text, code, audio, images
- Flexible input formats: PDFs with embedded images, various video and audio types
- Google DeepMind's embeddings model supports video, images, audio, text, and code in the same embedding space
- Gemini Live supports real-time screen sharing, video feeds, and audio conversations

## Key Information (Gemini Embeddings 2)
- Fully omnimodal embedding model: single vector for text (up to 8K tokens), 128 seconds of video, 80 seconds of audio, full PDFs
- Uses Matryoshka Representation Learning for dimension-scalable retrieval
- Inspired by neuroscience "Jennifer Aniston cells" — modality-invariant concept encoding
- Trained with contrastive losses for robust cross-modal retrieval and comparison

## Related
- [[DSPy]] — framework with multimodal support
- [[Gemma4]] — natively multimodal model family
- [[VariableAspectRatios]] — Gemma 4 vision feature
- [[VariableResolution]] — Gemma 4 vision feature
- [[Conformer]] — audio encoder architecture
- [[AudioTokenizer]] — audio preprocessing pipeline
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[Gemini 3.1 Pro]] — multimodal model
- [[Multimodal Embeddings]] — related concept
- [[GeminiEmbeddings2]] — omnimodal embedding model
- [[OmnimodalEmbeddings]] — stricter form of multimodal embeddings
- [[JenniferAnistonCells]] — neuroscience inspiration
