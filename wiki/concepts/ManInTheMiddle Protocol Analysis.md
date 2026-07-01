---
title: "Man-in-the-Middle Protocol Analysis"
type: concept
tags: [concept, reverse-engineering, protocol-analysis, man-in-the-middle, tcp-proxy, traffic-interception]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Definition
Man-in-the-Middle Protocol Analysis is a reverse engineering technique where a proxy is placed between the official configuration software and the target hardware to intercept, log, and analyze their communication. This reveals protocol details (commands, payloads, checksums) that cannot be discovered through brute-force interaction alone.

## Key Information
- Used when brute forcing fails to discover certain protocol features (e.g., persistence commands with binary payloads)
- Implementation in the Viking phone case: Claude Code set up a TCP proxy on macOS that relayed traffic between a Windows VM (running the official software) and the Viking phone while logging all communication
- The Windows VM couldn't bridge Wi-Fi to macOS, so the proxy also served as a connectivity workaround
- Revealed the "TS" command with a binary payload that included a checksum byte — a command not discoverable through text-based brute forcing
- The logged data enabled reverse engineering of both the command format and the checksum algorithm
- Once the protocol was fully understood, the proxy and VM were no longer needed — the phone could be programmed directly
- This technique is generalizable: any time official software exists but the protocol is undocumented, a proxy can bridge the knowledge gap

## Related
- [[AIAssisted Hardware Reverse Engineering]] — broader methodology
- [[Protocol Brute Forcing]] — complementary technique used first
- [[Checksum Reverse Engineering]] — analysis enabled by captured traffic
- [[Viking Phone]] — hardware analyzed via this technique
- [[UTM]] — virtualization tool used to run the Windows VM
- [[ClaudeCode]] — AI tool that set up the TCP proxy
- [[TCP Proxy]] — the specific network tool used
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source
