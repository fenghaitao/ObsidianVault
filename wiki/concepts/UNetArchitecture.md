---
title: "UNetArchitecture"
type: concept
tags: [deep-learning, architecture, convolutional, diffusion, image-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
U-Net is a convolutional neural network architecture originally designed for image segmentation, later adopted as the initial architecture for diffusion model denoisers. It features an encoder-decoder structure with skip connections, making it well-suited for tasks where output dimensions match input dimensions.

## Key Information
- **Origin**: Originally designed for image segmentation tasks
- **Diffusion adoption**: Was the standard architecture for early diffusion models (including Stable Diffusion)
- **Structure**: Encoder-decoder with skip connections; output dimensions match input dimensions
- **Convolutional basis**: Uses convolutional layers with spatial inductive biases
- **Replaced by transformers**: Modern diffusion models have largely moved to transformer architectures
- **Why transformers won**: The LLM community's extensive knowledge about scaling transformers made them a practical choice for diffusion as well
- **Still relevant**: Represents an important phase in diffusion model evolution

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — primary application
- [[TransformerArchitecture]] — successor architecture
- [[Stable Diffusion]] — prominent U-Net based model
