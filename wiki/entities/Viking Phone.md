---
title: "Viking Phone"
type: entity
tags: [hardware, voip, legacy, reverse-engineering, phone]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Definition
The Viking Phone is a legacy VOIP hardware phone that uses Power over Ethernet (PoE) for connectivity and power. It has a proprietary, undocumented two-layer communication protocol with two-letter command codes and single-byte checksum encryption. It was reverse engineered by Boris Starkov using Claude Code to enable integration with Eleven Labs' conversational AI agent.

## Key Information
- Legacy VOIP hardware with only Windows XP-compatible configuration software
- Uses Power over Ethernet (PoE) for both connectivity and power
- Communicates via a proprietary text-based protocol on a network port
- Protocol uses two-letter command codes — 80 valid commands out of 676 possible combinations (brute-force discovered)
- Has both temporary and persistent memory — settings written via basic commands are lost on reboot
- Persistent memory requires a specific sequence of commands including a TS command with binary payload and checksum
- Single-byte checksum for protocol integrity (reverse engineered via man-in-the-middle analysis)
- Three senior engineers plus ChatGPT couldn't configure it a year before Claude Code succeeded
- Open-sourced as a Claude Code skill for anyone to use without a Windows machine

## Related
- [[Boris Starkov]] — reverse engineered the phone
- [[ClaudeCode]] — AI tool used for reverse engineering
- [[ElevenLabs]] — company that used it for a demo
- [[Twilio]] — SIP trunk provider connected to the phone
- [[AI-Assisted Hardware Reverse Engineering]] — methodology used
- [[Protocol Brute Forcing]] — technique for discovering valid commands
- [[Man-in-the-Middle Protocol Analysis]] — technique for discovering persistence commands
- [[Checksum Reverse Engineering]] — technique for cracking the protocol
- [[Power over Ethernet]] — connection method
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source
