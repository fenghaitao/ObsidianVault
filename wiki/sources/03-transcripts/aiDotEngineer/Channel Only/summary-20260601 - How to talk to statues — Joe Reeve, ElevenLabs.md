---
title: "How to talk to statues — Joe Reeve, ElevenLabs"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - How to talk to statues — Joe Reeve, ElevenLabs.md"
author: "Joe Reeve"
date: 2026-06-01
ingested: 2026-06-30
---

## Core Thesis

Vibe coding enables rapid prototyping of novel interaction patterns — like talking to statues — by stitching together existing APIs. The real value is in the glue and the story, not solving hard technical problems. Voice interfaces are evolving toward multimodal experiences where parallel input/output patterns (voice in, rich visual out) and better interruptibility will define the next generation of AI interactions. The cultural implications of giving voices to inanimate objects remain underexplored but are being taken seriously by museums and institutions.

## Key Points

- **The Statue App**: Joe Reeve built an app in 2 hours on a Sunday using Cursor that lets users take a picture of a statue, uses OpenAI deep research to identify it and generate historical context, uses ElevenLabs Voice Design API to create a matching voice, creates an ElevenLabs agent, and initiates a phone call — all within 30 seconds.
- **Viral impact**: Posted on Tuesday, got 50K impressions day 1, exploded to 1.5M impressions day 2. Museums (Science Museum, V&A, Sainsbury Centre) and businesses (Tripadvisor competitors, Bonhams, Christie's) reached out wanting the technology.
- **Vibe coding's power**: The app demonstrates that vibe coding is "so powerful" — stitching together existing APIs (OpenAI, ElevenLabs) tells a compelling story. The glue is the most important part, not solving hard technical problems.
- **Scaling the prototype**: The hard part is not user management or infrastructure (those are solved by APIs and tools like Supabase), but the content: working with curators to design authentic narratives for objects rather than relying on Google search results.
- **Voice Design for objects**: An academic process is underway (led by Jago at Sainsbury Centre) to determine what inanimate objects should sound like — considering material origins, carving locations, and exhibition history (e.g., Chinese mountain rock carved in Vietnam, displayed in Britain). This philosophical question extends to everyday objects like elevators.
- **Voice interaction problems**: Current voice agents have a binary on/off pattern. People are too polite to interrupt agents, but interrupting aggressively improves the experience. The "how to give people permission to interrupt" problem remains unsolved.
- **Multimodal conversations**: The future is voice + visual UI combined — speaking to a "product manager agent" that delegates to coding agents, with parallel interaction patterns where users voice input and receive rich visual output (diagrams, text, generated UI).
- **Information density asymmetry**: Users want voice input (high bandwidth out of their heads) but rich visual/text output back. Voice output alone has lower information density than reading.
- **Skim listening**: An open problem — what would "skim listening" look like? Ideas include speed dialing, forward/backward by concept (not sentence), and visual cues showing the agent wants to interrupt with a specific topic.
- **Consumer vibe coding**: Vibe coding hasn't gone consumer mainstream yet. Vibe coding events feel like "OG hackathons" — people who never thought about code as something humans make are building things. The "Instagram filters moment" or "TikTok moment" for vibe coding hasn't arrived yet.
- **Social vibe coding template**: Facebook Instant Games API (now deprecated) showed the pattern: social graph + simple primitives + easy creation = viral consumer apps. Something similar for vibe coding is likely the winning template.
- **Video creation tips**: Adding captions, having a hook in the first 6-12 seconds, and adding music (now easier with ElevenLabs music generation) make a massive difference for viral content. The statue video was edited in ~25 minutes on a phone using CapCut with a DJI lapel mic.
- **ElevenLabs platform**: Offers text-to-speech, transcription, music generation (first commercially legal AI music), sound effects, voice creation/editing, and a fully managed agents deployment platform. The Voice Design API (text description → generated voice) is underutilized.
- **Eleven Hacks**: The statue app's viral success led to the creation of "Eleven Hacks" — a program or initiative at ElevenLabs.

## Entities Mentioned

- [[Joe Reeve]] — Speaker, works in growth organization at ElevenLabs
- [[ElevenLabs]] — Audio AI foundation model company; Voice Design API, agents platform, music generation
- [[OpenAI]] — Deep research used for statue identification and historical context
- [[Cursor]] — AI coding tool used to build the statue app
- [[British Museum]] — Location where the statue app was demonstrated
- [[Science Museum (London)]] — Museum exploring interactive technology; co-CEO met with Joe Reeve
- [[V&A Museum]] — Victoria and Albert Museum; has a public API for collection data
- [[Sainsbury Centre]] — Museum/gallery run by Jago (former head of Americas at British Museum); location of Avengers HQ in films
- [[Spielwork]] — Mobile app for vibe coding games with TikTok-style swiping
- [[CapCut]] — Video editing app used to edit the viral statue video (on mobile, ~25 min)
- [[DJI]] — Maker of the Bluetooth lapel mic used for the video
- [[Bonhams]] — Auction house interested in talking-to-items technology
- [[Christie's]] — Auction house interested in talking-to-items technology
- [[Sir Michael Caine]] — Voice used for the red phone booth agent at the AIE event
- [[Supabase]] — Referenced for login/magic links in productionizing the app
- [[Tripadvisor]] — Competitors reached out wanting the statue technology
- [[OpenClaw]] — Referenced as a coding agent with ElevenLabs integration for phone call interactions
- [[Facebook Instant Games]] — Deprecated API that demonstrated the social + simple primitives = viral consumer apps template

## Concepts Introduced

- [[Voice Design]] — ElevenLabs API that generates a voice from a text description; underutilized but powerful
- [[Consumer Vibe Coding]] — Vibe coding going mainstream beyond developers; people who don't know apps are made by humans building things
- [[Agent Interruptibility]] — The challenge of making voice agents properly handle interruptions, including the politeness problem and signaling intent to interrupt
- [[Multimodal Conversations]] — Voice + visual UI combined; parallel input (voice) and output (rich visual) interaction patterns
- [[Social Vibe Coding]] — Vibe coding with social graph primitives enabling viral consumer experiences
- [[Skim Listening]] — The unsolved UX problem of skimming audio content by concept rather than sentence, analogous to skim reading
- [[Voice Interaction Patterns]] — Emerging design patterns for how users interact with voice agents, including push-to-talk and visual cues
- [[Information Density Asymmetry]] — The pattern where users prefer voice input (high bandwidth out) but rich visual output (high information density in)
- [[Viral Content Creation]] — Practical techniques for making AI demo videos go viral: captions, hooks in first 6-12 seconds, music

## Related

- [[summary-20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs]] — also from ElevenLabs (Voice Engine, voice agents)
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — also from ElevenLabs
- [[summary-20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry]] — vibe coding topic
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — vibe coding/engineering topic
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — new interaction patterns topic
