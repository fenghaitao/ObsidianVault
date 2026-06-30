---
title: "Persistent Sandboxes"
type: concept
tags: [sandbox, vercel, agents, infrastructure, file-system, state]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
Persistent sandboxes (also called named sandboxes) are sandbox instances identified by a unique name that persist their file system state across sessions via snapshots. When referenced by name, the platform either routes to an active session or spins up a new instance with the latest file system snapshot, creating the illusion of a single persistent machine.

## Key Information
- **Introduced by**: Vercel Sandbox (beta, as of May 2026)
- **Architecture**: Each sandbox has a name (e.g., tied to a user or session). Each sandbox can have sessions (instances). Under the hood, Vercel either routes to an active instance or creates a new one with the snapshot state.
- **Lifecycle**: Sandboxes spin down after an inactivity timeout. On spin-down, the file system is snapshotted. On next request, a new instance spins up with the snapshot, making state persist across sessions.
- **Usage Pattern**: `createOrGetSandbox(name)` — checks if a sandbox with the given name exists, returns it if so, creates it otherwise.
- **Eliminates Lifecycle Management**: Previously, developers had to manually manage sandbox state — tarring file systems after each request, storing in blob storage, spinning up new instances. Named sandboxes abstract this away.
- **Installation**: `pnpm add vercel-sandbox@beta`
- **Importance for Agents**: Enables agents to build persistent workspaces — file system memory, generated scripts, project files — that survive across chat sessions and agent invocations. This is what Nico calls "giving your agent a computer."
- **Application Binding**: In production, sandbox names are tied to user IDs or session IDs, giving each user/session their own persistent sandbox.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[VercelSandbox]] — the Vercel product
- [[Vercel]] — creator
- [[Agent Sandbox]] — general concept of sandboxed agent execution
- [[Agent Sandboxing]] — isolation practice
- [[File System Memory]] — memory pattern enabled by persistent sandboxes
- [[BashTool]] — primary tool for interacting with sandbox file systems
- [[Cloud-Based Agent Sandboxes]] — broader category
