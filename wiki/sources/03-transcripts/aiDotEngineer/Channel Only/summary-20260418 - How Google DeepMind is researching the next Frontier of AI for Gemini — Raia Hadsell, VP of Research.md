---
title: "How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"
date: 2026-04-18
ingested: 2026-06-26
---

## Core Thesis
Raia Hadsell, VP of Research at Google DeepMind, presents three non-language-model research areas that are pushing the frontier of AI: omnimodal embedding models (Gemini Embeddings 2), AI-driven weather prediction (GraphCast, GenCast, FGN), and interactive world models (Genie 1/2/3), all unified by DeepMind's philosophy of finding and solving deep root-node problems rather than surface-level leaf-node optimizations.

## Key Points
- **Raia Hadsell background**: Philosophy of religion undergrad (1990s), CS PhD at NYU with Yann LeCun on convolutional networks for robots (2000s), joined DeepMind at ~30-40 people (2010s), now VP running ~1200 scientists/engineers across 10 labs
- **DeepMind philosophy**: Find root nodes (deepest unsolved problems) rather than wasting time on leaves; partner broadly; solve problems worth solving for the benefit of humanity
- **Gemini Embeddings 2**: Fully omnimodal embedding model derived from Gemini, supporting text (up to 8K tokens), 128 seconds of video, 80 seconds of audio, and full PDFs in a single unified vector. Uses Matryoshka Representation Learning (MRL) for dimension-scalable retrieval (start at 256 dims, expand for more expressiveness). Inspired by neuroscience "Jennifer Aniston cells" — neurons that encode specific concepts across all modalities
- **GraphCast**: Spherical graph neural network predicting 100 atmospheric variables autoregressively up to 15 days out, trained on 40 years of global weather data. Accurately predicted Hurricane Lee landfall 9 days out vs. 6 days for physics-based models
- **GenCast**: Probabilistic successor to GraphCast using a mesh-based approach. More accurate than gold-standard forecasts 97% of the time on 1,300 benchmarks. Produces 15-day forecast in 8 minutes on a single chip vs. hours on supercomputers
- **FGN (Functional Generative Network)**: Directly predicts cyclones (trajectory, wind speed, eye formation) within the network rather than post-processing. Already used by the US National Hurricane Center
- **Genie 1**: Early 2D platformer world model, ran for seconds, responded to left/right input with reasonable diversity
- **Genie 2**: Scaled to 3D games, interactive but not real-time, could not achieve real-world quality
- **Genie 3**: Real-time interactive 3D environments with high quality, body presence, memory (environments remember state when you return), and real-time prompting (change the world mid-experience). Demonstrated walking down a Kent lane, skiing, artist-created worlds brought to life, origami lizard world with perfect memory, and Camden Canal with real-time world switching

## Entities
- [[RaiaHadsell]] — VP of Research at Google DeepMind, presenter
- [[GoogleDeepMind]] — Google's AI research division
- [[GeminiEmbeddings2]] — Omnimodal embedding model derived from Gemini
- [[GraphCast]] — Spherical graph neural network for weather prediction
- [[GenCast]] — Probabilistic weather prediction model
- [[FGN]] — Functional Generative Network for cyclone prediction
- [[Genie 3]] — Interactive world model (Genie 3)
- [[Genie1]] — Early 2D platformer world model
- [[Genie2]] — Intermediate 3D world model
- [[Gemini]] — Google's frontier model family

## Concepts
- [[ContrastiveLoss]] — Loss function for embedding models, used in Siamese networks
- [[MatryoshkaRepresentationLearning]] — Dimension-scalable embedding representation (MRL)
- [[OmnimodalEmbeddings]] — Unified embeddings across text, video, audio, and PDF modalities
- [[GraphNeuralNetwork]] — Spherical graph neural network for atmospheric modeling
- [[ProbabilisticWeatherPrediction]] — Probabilistic approach to chaotic weather forecasting
- [[WorldModels]] — AI-generated interactive environments from text prompts
- [[RootNodeResearch]] — DeepMind's philosophy of solving deepest problems first
- [[JenniferAnistonCells]] — Neuroscience concept of modality-invariant concept encoding neurons
- [[MultimodalAI]] — AI systems handling multiple input modalities
- [[Multimodal Embeddings]] — Vector representations across modalities in unified space

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — also covers Genie 3 and DeepMind models
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — another DeepMind model presentation
- [[summary-20260105 - Welcome to AIE CODE - Jed Borovik, Google DeepMind]] — earlier DeepMind presentation
