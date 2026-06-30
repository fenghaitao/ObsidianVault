---
title: "Vercel Sandbox"
type: entity
category: tool
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

# Vercel Sandbox

## Definition

Vercel Sandbox is a service by Vercel that provides isolated virtual machines for running agent-generated code. As of May 2026 (beta), it supports named persistent sandboxes — each sandbox has a unique name, can have multiple sessions (instances), and persists file system state across sessions via snapshots.

## Key Information

- **Creator**: Vercel
- **Type**: Cloud sandbox service
- **Key Operations**:
  - `sandbox.create` — Creates a new isolated VM
  - `sandbox.getURL` — Gets the URL for a running sandbox
  - `sandbox.runCommand` — Executes commands within the sandbox
- **Named Persistent Sandboxes (Beta, May 2026)**:
  - Each sandbox has a unique name (e.g., tied to user or session ID)
  - Each sandbox can have multiple sessions (instances)
  - Referencing by name either routes to an active session or spins up a new one with the latest file system snapshot
  - On inactivity timeout, the sandbox spins down but snapshots the file system
  - Subsequent requests spin up a new instance with the snapshot, making state persist
  - Eliminates manual lifecycle management (tarring file systems, storing in blob storage)
  - Installation: `pnpm add vercel-sandbox@beta`
  - Usage pattern: `createOrGetSandbox(name)` — returns existing or creates new
- **Usage**: Used in agent workshops to provide agents with persistent computers; used internally at Vercel for all agent deployments (GTM, data, customer support)
- **Alternative**: Can be replaced with local execution or other sandbox solutions

## Related

- [[Vercel]]
- [[WorkflowDevKit]]
- [[AISDK]]
- [[Persistent Sandboxes]] — the named sandbox pattern
- [[NicoAlbanese]] — demonstrated named sandboxes
- [[File System Memory]] — memory pattern enabled by persistent sandboxes
- [[BashTool]] — primary tool for sandbox interaction
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
