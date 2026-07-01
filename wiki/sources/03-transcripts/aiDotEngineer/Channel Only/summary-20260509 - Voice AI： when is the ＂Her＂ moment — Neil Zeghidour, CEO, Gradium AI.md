---
title: "summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI"
type: source
tags: [source, transcript, voice-ai, speech-to-speech, full-duplex, cascaded-systems, tts, on-device, tool-calling, latency, voice-cloning, paralinguistic-understanding, back-channeling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md"]
last_updated: 2026-06-29
---

## Core Summary
Neil Zeghidour, CEO of Gradium AI (a spin-off from Kyutai), delivers a pragmatic talk on the current state of voice AI and what it will take to reach the "Her moment" — truly natural, human-like voice interaction. He argues that while latency has improved, the real bottlenecks are now tool call unpredictability, the lack of full-duplex conversation handling, missing paralinguistic understanding, and prohibitive costs for consumer-scale voice applications. He positions Gradium's on-device TTS model (Gradium Phonon) as a path to cost-effective, private voice AI, while acknowledging that cascaded systems remain more practical and reliable than speech-to-speech models for production use.

## Key Points

### The "Her Moment" Hype vs Reality
- The "Her moment" is the most overused analogy in voice AI, but remains relevant because the 2013 movie still anticipates what natural AI voice interaction could look like
- Many demos on Twitter claim "Her moments" but are far from the real thing — still high latency, no simultaneous speaking, and mostly glorified text models with a voice wrapper
- Anything not in the text (paralinguistic cues, tone, emotion) is lost in cascaded systems

### Cascaded Systems Still Win on Practicality
- Cascaded architecture: Speech-to-Text → LLM → Text-to-Speech
- Gradium adds streaming STT, streaming TTS with voice cloning, and semantic VAD
- Neil admits he used to be "at war" against cascaded systems but now sees them as so practical and convenient that they're the default for production
- The main challenge is not the architecture but intelligence, reliability, and personalization

### Latency: The Real Bottleneck Is Now Tool Calling
- Gradium's TTS latency is ~200ms, but human conversation requires the entire stack (understand → produce → pronounce) to be ~200ms
- Tool call latency (via OpenRouter etc.) ranges from 500ms to 4 seconds — far more than TTS latency improvements of 10-20ms
- Fighting for TTS milliseconds feels irrelevant when tool calls are orders of magnitude slower

### Fillers as a Solution for Tool Call Latency
- LLM splits into two streams: sends a tool call AND keeps the conversation going naturally with fillers while waiting
- When the tool result returns, it's inserted back naturally into the conversation
- Live demo of a travel agent that fills with nice things about the destination while fetching results
- Makes latency feel more controlled and reliable despite tool call unpredictability

### Full Duplex vs Half Duplex
- Every speech-to-speech model except Moshi is half duplex — either listening or speaking, not both
- Half duplex cannot handle: overlap between speakers, coughing, back-channeling ("mhm", "uh huh")
- Full duplex = human conversation — up to 20% overlap in Japanese conversations due to back-channeling as politeness
- Demo shows how annoying half duplex is: model constantly interrupts, cannot handle back-channeling
- Moshi (2 years old) is still the only full duplex model — handles overlap robustly, model can start answering before user finishes, user can talk over model

### Paralinguistic Understanding
- The "Her" clip shows AI understanding the character is uncomfortable from tone alone
- This information exists in speech-to-speech models technically, but if models are trained on audio versions of instruct datasets (factual QA only), they never learn to exploit it
- Moshi had great conversational flow but was "very stupid" — no tool calling, no observability, no real paralinguistic understanding

### The Intelligence Gap
- Natural-sounding full-duplex models exist (Moshi) but lack: reliability, intelligence, personalization, tool calling, observability
- Until full-duplex models match cascaded systems on these dimensions, cascaded systems remain the path forward

### Voice AI Cost Problem
- Voice is very expensive — hyperscaler voice modes run at a loss as marketing
- Anyone building consumer voice apps finds: LLM cost is negligible, STT is cheap, diarization is affordable, but TTS consumes most of the budget
- People have burned their fundraising on TTS bills without getting user growth

### Privacy and On-Device Processing
- As AI voice assistants become always-on and deeply personal, privacy becomes critical
- Users fear database hacks exposing private voice data
- Gradium Phonon: on-device TTS running on smartphone CPU (not GPU), <100M parameters
- Better than all existing on-device models (including Kokoro which lacks voice cloning)
- Enables consumer voice apps at zero API cost

### The Path Forward
- Voice is not a commodity — the last mile is the most difficult to solve
- It will take science and engineering to reach the "Her" movie vision
- Gradium's approach: provide building blocks (models) for voice, not orchestration or vertical solutions

## Related
- [[Neil Zeghidour]] — speaker, CEO of Gradium AI
- [[Gradium AI]] — voice AI model provider
- [[Moshi]] — first full-duplex speech-to-speech model
- [[Kyutai]] — non-profit lab that created Moshi
- [[Gradium Phonon]] — on-device TTS model
- [[ElevenLabs]] — competitor mentioned as best voice AI company
- [[Sesame AI]] — competitor voice model
- [[OpenAI]] — advanced voice mode competitor
- [[Nvidia]] — published PersonalPlex based on Moshi
- [[Kokoro]] — on-device TTS competitor
- [[OpenRouter]] — tool call latency source
- [[Eric Schmidt]] — philanthropist who funded Kyutai
- [[Xavier Niel]] — philanthropist who funded Kyutai
- [[PersonalPlex]] — Nvidia model based on Moshi
- [[Voice AI]] — the overall domain
- [[Cascaded Systems (Voice)]] — STT → LLM → TTS architecture
- [[SpeechToSpeech Models]] — single-model alternative
- [[Full Duplex]] — true bidirectional voice conversation
- [[Half Duplex]] — either listening or speaking
- [[Back Channeling]] — conversational acknowledgments
- [[Paralinguistic Understanding]] — tone and emotion cues
- [[Fillers (Voice AI)]] — keeping conversation going during tool calls
- [[OnDevice TTS]] — local text-to-speech processing
- [[Voice Cloning]] — cloning from short audio samples
- [[Semantic VAD]] — voice activity detection
- [[Streaming TTS]] — low-latency text-to-speech
- [[Voice AI Cost]] — economics of voice AI
- [[Her Moment]] — the ideal of natural AI voice
- [[ToolCalling]] — LLM function calls
- [[Latency]] — response time in conversation
- [[aiDotEngineer]] — event host
