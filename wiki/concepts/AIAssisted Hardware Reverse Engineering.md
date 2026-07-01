---
title: "AI-Assisted Hardware Reverse Engineering"
type: concept
tags: [concept, reverse-engineering, hardware, ai-assisted, claude-code, protocol-analysis]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Definition
AI-Assisted Hardware Reverse Engineering is the practice of using AI coding tools (such as Claude Code) to discover, analyze, and exploit undocumented hardware protocols and interfaces without requiring a security engineering background. The AI autonomously performs network discovery, protocol brute forcing, traffic interception, and cryptographic analysis, while the human operator performs physical actions under AI direction.

## Key Information
- Demonstrated by Boris Starkov (Eleven Labs) using Claude Code to reverse engineer a Viking VOIP phone protocol
- Process: network discovery (nmap) → protocol interaction → command brute forcing → man-in-the-middle traffic analysis → checksum cracking
- The AI handles intellectual work (algorithm analysis, protocol discovery) while the human handles physical actions (rebooting, cable connections, VM interaction)
- Makes hardware reverse engineering accessible to "normal software engineers" who aren't security specialists
- Starkov: "without Claude Code it wouldn't be possible to do that demo. It's not just it made it 10 times faster, it just made it possible."
- Generalizable beyond Viking phones to any networked hardware device
- Enables bypassing proprietary software interfaces: "1 year ago you actually needed the proprietary software interface that the company that made the hardware provides. Now you don't need it."
- Token cost for the reverse engineering: $10-$100
- Outcome was open-sourced as a reusable Claude Code skill

## Related
- [[ClaudeCode]] — AI tool used
- [[Boris Starkov]] — engineer who demonstrated the approach
- [[Viking Phone]] — hardware reverse engineered
- [[Protocol Brute Forcing]] — sub-technique for command discovery
- [[ManInTheMiddle Protocol Analysis]] — sub-technique for traffic interception
- [[Checksum Reverse Engineering]] — sub-technique for cryptographic analysis
- [[AI as Orchestrator, Human as Hands]] — collaboration model
- [[Network Discovery with nmap]] — first step in the process
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source
