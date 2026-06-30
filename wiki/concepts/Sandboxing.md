---
title: "Sandboxing"
type: concept
tags: [security, agents, infrastructure, deployment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Sandboxing is the practice of running agents in isolated container environments with restricted network and file system access. It is the third and final layer of the Swiss cheese defense model for agent security, and a critical enabler for running untrusted agent-generated code.

## Key Information
- The Claude Agent SDK includes sandboxing capabilities: network requests can be restricted, file system operations outside the workspace can be blocked
- If an agent is compromised, sandboxing limits the blast radius — it prevents the lethal trifecta (execute code, change file system, exfiltrate data)
- Cloud sandbox providers (Cloudflare, Modal, DigitalOcean, AWS) add infrastructure-level security
- Cloudflare has an example integration with the Agent SDK using `sandbox.start`
- Agents should not run on personal computers or on machines with broad access to secrets
- Each agent typically runs in its own container with its own file system — a one-to-one architecture rather than traditional multi-tenant
- Sandboxing network access is particularly important for preventing data exfiltration
- **NeMo Claw**: Nvidia launched a security layer and sandbox plugin specifically for OpenClaw — Peter Steinberger tested it with Codex security and found 5 sandbox breakout methods in 30 minutes using Nvidia's internal model
- OpenClaw security recommendation: if you put the agent in a group chat, "turn on sandboxing because if anyone can talk to your agent, they can exfiltrate anything that the agent can do"
- Sandboxing is one of the key security recommendations for agent deployment alongside: don't put personal agent in group chat, personal agent should only be accessible by owner, team agent should only know what the team can know

### Sandbox Primitives for Untrusted Code (Matt Carey)
- **WorkerD** (Cloudflare): V8 isolates with programmable guardrails — toggle internet access on/off, restrict to specific domains. Runs at Cloudflare scale (billions of requests).
- **Deno**: JavaScript/TypeScript runtime with sandboxed `deno run` and permission flags
- **Pydantic Monty**: Python code interpreter for untrusted Python code
- Running untrusted code was historically considered a CVE-level vulnerability; now it's becoming a standard infrastructure primitive
- Matt Carey predicts many more sandbox primitives will emerge as models get smarter

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (NeMo Claw, OpenClaw sandboxing)
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (WorkerD, Deno, Pydantic Monty sandboxes)
- [[SwissCheeseDefense]] — the layered security model
- [[LethalTrifecta]] — what sandboxing defends against
- [[ClaudeAgentSDK]] — the framework with built-in sandboxing
- [[Cloudflare]] — sandbox provider
- [[WorkerD]] — Cloudflare's dynamic worker sandbox
- [[Deno]] — JavaScript/TypeScript sandbox
- [[Pydantic Monty]] — Python sandbox
- [[Modal]] — sandbox provider
- [[OpenClaw]] — project with sandboxing recommendations
- [[Nvidia]] — NeMo Claw sandbox for OpenClaw
- [[NeMo Claw]] — Nvidia's security sandbox for OpenClaw
- [[Untrusted Code Execution]] — the use case driving sandbox innovation
- [[CapabilityBasedSecurity]] — security model for sandboxes
