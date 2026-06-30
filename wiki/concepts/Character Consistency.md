---
title: "Character Consistency"
type: concept
tags: [image-generation, consistency, genmedia, prompt-engineering, reference-images, chat-mode]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
Character Consistency is a technique for maintaining coherent visual appearance of characters across multiple generated images. In the context of GenMedia, it involves using chat mode history or explicit reference images to ensure each subsequent generation depicts characters with the same visual traits.

## Key Information
- **Challenge**: When generating multiple images of the same character (e.g., for different chapters of a book), models tend to produce visually inconsistent depictions without explicit guidance
- **Strategy 1 — Chat mode history**: Using the chat API's conversation history so the model remembers previous images it generated; implicit consistency through context retention
- **Strategy 2 — Reference images**: Saving generated character images in an array, then passing them as explicit references in generate_content calls for each new scene; the model receives the specific character images relevant to the current chapter
- **Best practice for scale**: Generate multiple reference images per character (portrait, full body, side, back) and have Gemini determine which angles are needed for each scene
- **System instruction reinforcement**: Always describe character appearance in every prompt (clothing, colors, features) even when using reference images, as explicit text descriptions improve consistency
- **Trade-off**: Chat mode is simpler but re-sends entire context (including full book) on each call; reference image approach is more explicit and efficient but requires managing image arrays

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[GenMedia]] — product suite
- [[Nano Banana 2]] — image generation model
- [[Media Prompt Generation]] — related technique
