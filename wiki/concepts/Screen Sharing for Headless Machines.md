---
title: "Screen Sharing for Headless Machines"
type: concept
tags: [AI, agent, OpenClaw, Mac, setup, tip]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

Screen sharing (and remote login) for headless Mac Minis is a setup technique that allows you to access your OpenClaw machine from your main laptop without a dedicated monitor, keyboard, or mouse. Once configured, the Mac Mini can run completely headless.

## Key Information

- **Screen sharing:** Go into Mac Mini settings and turn on screen sharing. Then on your main laptop (same Wi-Fi), open Screen Sharing and pull up the Mac Mini's screen.
- **Remote login (SSH):** Turn on remote login in settings. Get a one-line SSH command: `ssh username@ip-address`. As long as you're on the same Wi-Fi, you can terminal into the Mac Mini.
- Claire Vo: "This has been life-changing for me because I had Mac Minis and a monitor on my kitchen table for a really long time."
- Initial setup still requires a monitor, keyboard, and mouse — you need to turn on the settings somehow.
- After setup: no monitor, no keyboard, no mouse needed.
- Lenny Rachitsky: "You're going to save people so much money here."

## Why It Matters

- Removes the biggest practical barrier to running multiple Mac Minis: desk space, monitors, keyboards
- Makes it feasible to run 3+ Mac Minis for different agent teams
- Reduces cost and clutter

## Related

- [[OpenClaw]] — the platform
- [[Apple]] — Mac Mini hardware
- [[Clean Machine Principle for AI Agents]] — why separate machines
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
