---
title: "Agent Sandbox"
type: concept
tags: [agents, infrastructure, execution, docker, vercel, persistence]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
An agent sandbox is an isolated execution environment provided per agent session, enabling the agent to install arbitrary packages, run code, set up services, and build full applications without affecting other sessions. Modern sandboxes like Vercel's named persistent sandboxes persist file system state across sessions via snapshots, giving agents a persistent "computer" to work with.

## Key Information
- **Manus Sandboxes**: Every Manus chat ships with its own sandbox, providing a full Docker image. Supports installing any pip package, Redis (via BMQ), and other services. Enables webhook support (e.g., Stripe) because the sandbox is a full application. Allows running multiple Selenium instances in parallel.
- **Vercel Named Persistent Sandboxes (Beta, May 2026)**: Each sandbox has a unique name tied to a user or session. Sandboxes have sessions (instances) that can be spun up/down. On inactivity timeout, the file system is snapshotted. Subsequent requests spin up a new instance with the snapshot, making state persist across sessions. This eliminates complex lifecycle management (tarring file systems, storing in blob storage).
- **Usage Pattern**: `createOrGetSandbox(name)` checks if sandbox exists, returns it if so, creates it otherwise. Sandbox is passed to the agent as a call option and injected into runtime context for tool access.
- **Vercel Internal Usage**: All Vercel internal agents (GTM, data, customer support with 90% ticket deflection) use file-system-backed sandbox agents. Nico describes this as "emergent behavior" — agents paired with file systems stay on track, follow plans, and produce artifacts showing exactly what work was done.
- **Future plans (Manus)**: Autoscaling and warm deployments
- Differentiates from platforms that only provide front-end capabilities
- The sandbox is what enables general AI agents to do things verticalized products cannot

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source (Vercel sandboxes)
- [[ManusAI]] — platform providing sandboxes
- [[VercelSandbox]] — Vercel's sandbox product
- [[Persistent Sandboxes]] — the named sandbox pattern
- [[General AI Agent]] — philosophy enabled by sandboxes
- [[Computer Use]] — related sandboxed browser approach
- [[Browser Use]] — related browser automation approach
- [[File System Memory]] — memory pattern enabled by persistent sandboxes
- [[BashTool]] — primary tool for sandbox interaction
- [[NicoAlbanese]] — demonstrated Vercel sandbox workshop
