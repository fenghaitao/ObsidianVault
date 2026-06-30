---
title: "UTM"
type: entity
tags: [tool, virtualization, macos, windows]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs.md"]
last_updated: 2026-06-30
---

## Definition
UTM is a virtualization tool for macOS that allows running virtual machines including Windows. Boris Starkov used it during the Viking phone reverse engineering to run the Windows XP-compatible configuration software, enabling the man-in-the-middle protocol analysis.

## Key Information
- macOS virtualization software used to run a Windows virtual machine
- Limitation: cannot bridge Wi-Fi to macOS, so the Windows VM has no direct internet connection
- Workaround: Claude Code set up a TCP proxy on the Mac to relay traffic between the VM and the phone
- Used to run the Viking phone's proprietary Windows XP configuration software for protocol analysis
- Once the protocol was reverse engineered, the VM was no longer needed — the phone could be programmed directly

## Related
- [[Viking Phone]] — hardware configured via UTM
- [[Man-in-the-Middle Protocol Analysis]] — technique enabled by UTM
- [[Boris Starkov]] — used UTM during reverse engineering
- [[ClaudeCode]] — set up the TCP proxy workaround
- [[summary-20260529 - Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs]] — source
