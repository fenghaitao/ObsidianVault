---
title: "Voice Style Control"
type: concept
tags: [tts, voice, style, speech-synthesis, character-voice, google, deepmind]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29

---

## Definition
Voice Style Control is a technique for using a single TTS voice to simulate multiple distinct character voices by embedding style instructions (emotion, pacing, accent) in the transcript text. This creates the illusion of different speakers without requiring multiple voice models.

## Key Information
- **Core trick**: Write character dialogue with style annotations in parentheses (e.g., "breathless and unbolstered," "long poetic pauses," "whispering," "with a lot of emotion") that the TTS model interprets as performance direction
- **Single voice, multiple characters**: The same TTS voice can produce recognizably different "characters" when each character's lines are consistently annotated with distinct style instructions
- **Transcript format**: Write dialogue as a play script with narrator and character roles, each assigned a specific TTS voice preset (e.g., narrator = Sulafat, characters = Fenrir), with per-character style annotations
- **Accent capability**: The model can be directed to use specific accents (Irish, English, German, etc.) via text instructions, though this can be unreliable
- **Limitation**: Must always preface TTS input with "read this text" or similar — the model does not automatically know to read the provided text without an explicit instruction
- **Production approach**: For scale, maintain a full transcript with character names and a side mapping of per-character prompt templates, with per-line overrides for emotional variations
- **Inspiration**: Extends the NotebookLM two-voice podcast concept to arbitrarily many characters using a single voice

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[GenMedia]] — product suite
- [[NotebookLM]] — inspiration for multi-voice technique
- [[TTS]] — underlying model
