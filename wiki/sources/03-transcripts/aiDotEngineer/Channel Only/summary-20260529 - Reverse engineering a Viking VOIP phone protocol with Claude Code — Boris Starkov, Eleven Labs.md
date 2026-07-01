---
title: "summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs"
type: source
tags: [source, transcript, reverse-engineering, hardware, claude-code, voip, protocol-analysis, ai-assisted-hacking, checksum, brute-force, man-in-the-middle]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Core Summary
Boris Starkov of Eleven Labs used Claude Code to reverse engineer the proprietary protocol of a legacy Viking VOIP phone, enabling it to connect to an Eleven Labs conversational AI agent via Twilio. The talk demonstrates how AI coding tools make hardware reverse engineering accessible to non-security engineers, and how the approach generalizes beyond Viking phones to any piece of networked hardware.

## Key Points

### The Problem
- Eleven Labs wanted to build a phone booth demo where visitors talk to an AI agent voiced as Michael Caine
- The Viking phone only had Windows XP-compatible configuration software
- Three senior software engineers plus ChatGPT (a year prior) could not make it work
- Nobody at Eleven Labs had a Windows laptop; virtual machine driver issues blocked the official software

### Reverse Engineering Process with Claude Code
- Connected laptop to phone via router using Power over Ethernet (PoE)
- Claude Code ran nmap to discover the phone on the network (found on port 1001, then the correct communication port)
- Sent random strings to the phone and observed error responses (ER prefix), confirming a text-based protocol
- Discovered the phone uses two-letter command codes by brute-forcing all 26x26 combinations
- 80 out of 676 combinations returned valid responses (non-error)
- Successfully programmed phone settings (credentials, SIP trunk info) but settings were lost on reboot — only written to temporary memory

### The Dead End and Breakthrough
- Claude Code tried all two-letter and three-letter commands, couldn't find the persistence mechanism
- Set up a Windows virtual machine with a TCP proxy (man-in-the-middle) to intercept traffic between the official software and the phone
- Captured a command (TS) with a binary payload including a checksum byte
- Reverse engineered the checksum algorithm (simple single-byte addition/subtraction) by observing known data and results
- Discovered the sequence of commands needed to save settings to persistent memory

### The Outcome
- Protocol fully cracked: two-layer structure with single-byte checksum encryption
- No longer needed the Windows virtual machine — can program the phone directly using the reverse-engineered protocol
- Open-sourced the reverse-engineered protocol as a Claude Code skill for reuse
- Demo worked: red phone booth on the third floor lets visitors talk to a Michael Caine-voiced AI agent about British AI history
- Total token cost: between $10 and $100

### Key Insight: Human as Hands for AI
- Starkov describes his role as "the agent for Claude" — Claude orchestrated the entire process
- He performed physical actions (rebooting phone, listening for beeps, controlling the VM) while Claude directed the intellectual work
- Claude was "smarter than me" — Starkov couldn't have intellectually unblocked it
- Without Claude Code, the demo "wouldn't be possible" — not just 10x faster, but fundamentally enabling

### Generalizability
- The approach applies to any networked hardware, not just Viking phones
- One year ago you needed proprietary software interfaces; now you can reverse engineer them with AI
- The skill is open-sourced so anyone with a Viking phone can use it without a Windows machine

## Related
- [[Boris Starkov]] — speaker, engineer at Eleven Labs
- [[ElevenLabs]] — company behind the demo
- [[ClaudeCode]] — AI tool used for reverse engineering
- [[Viking Phone]] — the legacy VOIP hardware
- [[Twilio]] — SIP trunk provider used as intermediary
- [[Sir Michael Caine]] — voice used for the AI agent
- [[UTM]] — virtual machine software on Mac
- [[AIAssisted Hardware Reverse Engineering]] — the core methodology
- [[Protocol Brute Forcing]] — iterating through all two-letter command combinations
- [[ManInTheMiddle Protocol Analysis]] — TCP proxy to intercept software-to-phone traffic
- [[Checksum Reverse Engineering]] — cracking the single-byte checksum
- [[AI as Orchestrator, Human as Hands]] — human performs physical actions while AI directs
- [[Power over Ethernet]] — physical connection method
- [[Network Discovery with nmap]] — finding the phone on the network
- [[aiDotEngineer]] — event host
