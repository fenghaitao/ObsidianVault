---
title: "On-Device Agent Skills"
type: concept
tags: [agents, on-device, edge, gemma, skills, privacy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
On-Device Agent Skills are user-created or community-shared agent capabilities that run entirely on local hardware using Gemma 4 Edge models, demonstrated through Google's gallery app. Skills include Wikipedia querying, mood journaling with trend analysis, photo-to-music generation, and animal sound generation — all executing locally without cloud API calls.

## Key Information
- Run entirely on-device using Gemma 4 Edge models (E2B, E4B) via Lite RT
- Demonstrated in Google's gallery app with sample code available for each skill
- Users can create custom skills directly within the gallery app without leaving it
- Community shares skills on GitHub; users can download and fork them
- Skills leverage new Gemma 4 capabilities: function calling, structured JSON output, chain-of-thought thinking
- Privacy-focused: all processing happens locally, no data leaves the device
- Gallery app is open source on GitHub; users can fork and modify it
- Examples: Wikipedia knowledge augmentation, sleep/mood journaling with trend analysis, photo-to-music pairing, animal sound generation from prompts
- Skills can manage complex multi-app workflows on-device
- QR code instructions available for building custom skills

## Related
- [[summary-20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind]] — source
- [[Gemma4]] — models powering the skills
- [[Lite RT]] — inference framework
- [[Google AI Edge]] — parent division
- [[OnDeviceAgentic]] — broader concept
- [[Agent Skills]] — general agent skills concept
- [[OnDeviceAI]] — broader concept
- [[Function Calling]] — capability used in skills
- [[Structured Outputs]] — capability used in skills
- [[ChainOfThought]] — thinking mode used in skills
