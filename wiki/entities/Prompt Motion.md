---
title: "Prompt Motion"
type: entity
tags: [application, video-generation, cloudflare, containers, sandboxing, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Definition
Prompt Motion (promptmotion.app) is a video generation application built by Harshil Agrawal on Cloudflare's developer platform. Users describe motion graphics in natural language, and the AI writes motion code with dependencies, spins up a dev server, and provides a live preview URL. It uses container-based sandboxing for full isolation between users.

## Key Information
- Built by Harshil Agrawal, Senior Developer Advocate at Cloudflare
- Live production application at promptmotion.app
- User workflow: type a description (e.g., "Animate this logo") → AI evaluates request → writes code → starts dev server → shows live preview
- Requires container-based sandboxing because it needs: git clone, npm install, dev server, exposed port — all impossible with isolates
- Architecture: main worker → Sandbox SDK → Durable Object (stateful coordinator) → Container VM (real Linux with bash, Node.js, git, npm)
- Each user gets their own container with completely separate file system
- Demonstrates the container approach to sandboxing: full Linux environment for building and deploying applications

## Related
- [[summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare]] — source
- [[Harshil Agrawal]] — creator
- [[Cloudflare]] — hosting platform
- [[ContainerBased Sandboxing]] — the sandboxing approach used
- [[Sandboxing]] — broader security concept
- [[CloudflareWorkers]] — platform component
