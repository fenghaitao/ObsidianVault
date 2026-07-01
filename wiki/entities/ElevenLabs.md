---
title: "ElevenLabs"
type: entity
tags: [tool, text-to-speech, audio, ai-pricing, speech-to-text, transcription, voice-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Mastering AI Pricing — Mayank Pant, Stripe.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - How to talk to statues — Joe Reeve, ElevenLabs.md"]
last_updated: 2026-06-30
---

## Definition
ElevenLabs is a text-to-speech and speech-to-text provider that builds on Stripe with hybrid pricing, using tiered plans (good, better, best, enterprise) with credit-based abstraction. Their speech-to-text team, led by Angelos Perivolaropoulos, built Scribe V2 — currently the best transcription model on public benchmarks. In 2026, they launched Voice Engine, a first-class primitive for wrapping existing chat agents with voice capabilities. Joe Reeve in their growth organization built the viral "statue app" using their Voice Design API, demonstrating how ElevenLabs APIs enable rapid prototyping of novel voice interaction patterns.

## Key Information
- Builds on Stripe with hybrid pricing model
- Uses tiered plans (good, better, best, enterprise) with credits abstracting feature costs
- Features move between plans under the hood while customer-facing plans remain stable
- Used in a French learning app demo built entirely with Manus
- Integrated alongside structured output language models and Whisper transcription
- Chosen because the developer had extra credits available
- Demonstrates Manus's ability to integrate arbitrary third-party services
- Speech-to-text team led by Angelos Perivolaropoulos built Scribe V2, the best transcription model on public benchmarks
- Currently working on real-time transcription models for agents
- Launched Voice Engine, a wrapper SDK for adding voice to existing chat agents without rebuilding
- Voice Engine combines Scribe (speech-to-text), V3 (text-to-speech), and emotion-context-aware turn taking
- Powers voice agents for customers like Revolut's customer support
- Provides both a full conversational agent platform and Voice Engine as a wrapper for existing agents
- Head of Growth: Luke Harries
- Neil Zeghidour (Gradium AI CEO) called ElevenLabs "the best voice AI company in the world" and used their demo as a reference point for the current state of voice AI
- Demo showed a government AI helper — still had high latency, no simultaneous speaking handling, and was a "glorified text model with a voice around it"
- RL Nabors suggested using 11 Labs for higher-quality agent TTS over the browser's built-in Web Speech API, which she described as "sounding terrible"
- Joe Reeve in growth org built the viral statue app using Voice Design API + OpenAI deep research + agents platform, going from 50K to 1.5M impressions in 2 days
- The Voice Design API (text description → generated voice) is described as "really underutilized" but was central to the statue app
- The agents platform supports knowledge files and MCP calling for agent capabilities
- "Eleven Hacks" program was created following the statue app's viral success
- Museums (Science Museum, V&A, British Museum, Sainsbury Centre) and auction houses (Bonhams, Christie's) expressed interest in using ElevenLabs for conversational object experiences
- Commissioning a physical statue with embedded ElevenLabs technology (speaker, microphone, phone) for direct interaction without screens
- Built a red K6 phone booth experience with an agent voiced as Sir Michael Caine
- Boris Starkov used Claude Code to reverse engineer a Viking VOIP phone protocol for the K6 phone booth demo, connecting the legacy hardware to Eleven Labs' conversational AI agent via Twilio
- The phone booth demo was presented at an AI engineering summit — visitors talk to a Michael Caine-voiced AI agent about British AI history

## Related
- [[summary-20260501 - Mastering AI Pricing — Mayank Pant, Stripe]] — source (pricing model)
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source (speech-to-text, Scribe V2)
- [[summary-20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs]] — source (Voice Engine)
- [[AngelosPerivolaropoulos]] — leads speech-to-text team
- [[LukeHarries]] — Head of Growth, presented Voice Engine
- [[ScribeV2]] — transcription model built by their team
- [[VoiceEngine]] — wrapper product for adding voice to chat agents
- [[Revolut]] — customer using ElevenLabs for customer support
- [[Hybrid Pricing]] — pricing model used
- [[CreditBased Pricing]] — abstraction technique used
- [[Stripe]] — billing platform
- [[ManusAI]] — platform used to build the integration
- [[Agent Sandbox]] — enables installing arbitrary packages
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source (industry reference)
- [[summary-20260601 - How to talk to statues — Joe Reeve, ElevenLabs]] — source (statue app, Voice Design API)
- [[Gradium AI]] — competitor referenced them
- [[Neil Zeghidour]] — called them best voice AI company
- [[Joe Reeve]] — growth org, built the viral statue app
- [[Voice Design]] — underutilized API for generating voices from text descriptions
- [[British Museum]] — location of statue app demo
- [[Science Museum (London)]] — museum interested in the technology
- [[V&A Museum]] — museum with public API for collection data
- [[Sainsbury Centre]] — museum exploring voice design philosophy for objects
- [[Bonhams]] — auction house interested in talking-to-items
- [[Christie's]] — auction house interested in talking-to-items
- [[Sir Michael Caine]] — voice used in the phone booth agent experience
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source (Viking phone reverse engineering)
- [[Boris Starkov]] — engineer who reverse engineered the Viking phone
- [[Viking Phone]] — legacy VOIP hardware used in the phone booth demo
- [[Twilio]] — SIP trunk provider used in the phone booth demo
- [[ClaudeCode]] — AI tool used for the reverse engineering
