---
title: "Twilio"
type: entity
tags: [company, voip, sip, communication, api]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Definition
Twilio is a cloud communications platform providing SIP trunking and telephony APIs. In the Eleven Labs phone booth demo, Twilio served as the intermediary between the Viking VOIP phone and the Eleven Labs conversational AI agent, handling SIP domain complexity.

## Key Information
- Organizer of the summit where the talk was presented
- Provided SIP trunk services to bridge the Viking phone to Eleven Labs' AI agent
- Handles SIP domain complexity so the phone only needs to make a standard phone call
- Architecture: Viking Phone → Twilio → Eleven Labs
- Enables legacy hardware to connect to modern AI voice services without direct protocol integration

## Related
- [[Viking Phone]] — hardware connected through Twilio
- [[ElevenLabs]] — AI agent connected through Twilio
- [[Boris Starkov]] — set up the integration
- [[SIP Trunking]] — the protocol service Twilio provides
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source
