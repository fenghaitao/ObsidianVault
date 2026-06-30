---
title: "Voice Design"
type: concept
tags: [voice, audio, text-to-speech, elevenlabs, api]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - How to talk to statues — Joe Reeve, ElevenLabs.md"]
last_updated: 2026-06-30
---

## Definition
Voice Design is the ElevenLabs API that generates a synthetic voice from a text description of the desired voice characteristics. It is described as "really underutilized" but was central to the viral statue app, where it created voices matching the historical identity of photographed statues.

## Key Information
- Part of ElevenLabs' voice creation and editing capabilities
- Takes a text description of a voice and generates a matching synthetic voice
- Used in the statue app: after OpenAI deep research identifies a statue and generates historical context, Voice Design creates a voice matching what the statue "would have sounded like if alive"
- Described by Joe Reeve as "really underutilized" — people don't use ElevenLabs enough for voice creation/editing
- Part of a pipeline: photo → OpenAI deep research → Voice Design API → ElevenLabs agent → phone call
- The academic/philosophical question of voice design for inanimate objects is being studied by Jago at the Sainsbury Centre: what should a statue sound like based on material origins, carving location, and exhibition history?
- Extends beyond statues to everyday objects like elevators — what should a lift sound like?
- Represents a new design discipline: crafting voices for objects and agents based on context and identity rather than just technical quality

## Related
- [[summary-20260601 - How to talk to statues — Joe Reeve, ElevenLabs]] — source
- [[ElevenLabs]] — company providing the Voice Design API
- [[Joe Reeve]] — used Voice Design in the statue app
- [[Sainsbury Centre]] — Jago's academic research on voice design for objects
- [[Voice Agents]] — the broader category Voice Design enables
- [[VoiceEngine]] — related ElevenLabs product for wrapping chat agents with voice
