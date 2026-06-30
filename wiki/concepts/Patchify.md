---
title: "Patchify"
type: concept
tags: [computer-vision, transformer, preprocessing, vit, image-processing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
Patchify is the preprocessing step that converts an image into a sequence of tokens for Vision Transformers by splitting the image into fixed-size patches (originally 16×16 pixels), which are then linearly projected into embedding vectors with learned positional encodings.

## Key Information
- The core operation that adapts transformers (designed for 1D token sequences) to 2D images
- Original ViT used 16×16 patches, creating (n/16)² patches for an n×n image
- ConvNeXt used a finer 4×4 patchify for more detailed initial processing
- Added learned positional encodings tell the transformer where each patch is in the image
- Creates O(n⁴) compute scaling: (n/16)² patches → (n/16)⁴ attention operations
- The patch structure is what enables MAE pretraining: random patches can be dropped and the model learns to reconstruct them
- MAE's patch dropout is why MAE is ViT-specific — you can't "drop a patch" in a CNN where convolution processes the whole image uniformly

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[ViT (Vision Transformer)]] — architecture using patchify
- [[MAE (Masked Autoencoder)]] — pretraining that depends on patch structure
- [[Convolutional Neural Networks]] — alternative that processes images holistically
- [[Inductive Bias]] — positional encodings are the only spatial information injected
