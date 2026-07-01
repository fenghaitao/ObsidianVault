---
title: "Protocol Brute Forcing"
type: concept
tags: [concept, reverse-engineering, protocol-analysis, brute-force, command-discovery]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Definition
Protocol Brute Forcing is a reverse engineering technique that systematically iterates through all possible command combinations in a protocol's command space to discover valid commands. When a protocol uses short command codes (e.g., two-letter commands), the entire search space can be exhaustively tested by sending each combination and observing whether the response is an error or a valid result.

## Key Information
- Used by Claude Code to reverse engineer the Viking phone protocol, which used two-letter command codes
- Search space: 26 × 26 = 676 possible two-letter combinations
- Result: 80 valid commands discovered, most returned error codes
- Some commands made semantic sense (e.g., "SA" for status) while others were opaque
- Claude Code wrote a program to automate the brute forcing by sending each combination and recording results
- After two-letter brute force failed to find persistence commands, also attempted three-letter commands and "reasonable words" — no additional valid commands found
- The technique works when the protocol has a small, enumerable command space and provides distinguishable error vs. success responses
- Contrast with the man-in-the-middle approach, which was needed for discovering commands with binary payloads (like the TS persistence command)

## Related
- [[AIAssisted Hardware Reverse Engineering]] — broader methodology
- [[ManInTheMiddle Protocol Analysis]] — complementary technique for hidden commands
- [[Checksum Reverse Engineering]] — next step after discovering commands
- [[Viking Phone]] — hardware whose protocol was brute-forced
- [[ClaudeCode]] — AI tool that automated the brute force
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source
