---
title: "Sandboxing"
type: concept
tags: [security, sandboxing, claude-code, filesystem-isolation, network-isolation, vulnerability-scanning]
sources: ["raw/01-articles/claude/2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous.md", "raw/01-articles/claude/2025-10-20 - Claude Code on the web.md", "raw/01-articles/claude/2026-05-27 - Using LLMs to secure source code.md", "raw/01-articles/claude/2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents.md"]
last_updated: 2026-07-07
---

## Definition

Sandboxing is a security approach that defines pre-set boundaries within which an AI agent can act freely, replacing per-action permission prompts with OS-level enforced limits on what the agent can touch — providing both more security and more autonomy than a manual-approval model.

## Key Information

- **Motivation**: [[ClaudeCode]]'s default permission-based model (ask before every modification or command) causes "approval fatigue," where constant clicking leads users to stop scrutinizing what they approve.
- **Two required components** — both are necessary, neither is sufficient alone:
  - **Filesystem isolation**: restricts an agent to specific directories, preventing a prompt-injected agent from modifying sensitive system files or escaping the sandbox.
  - **Network isolation**: restricts connections to approved servers/domains, preventing a prompt-injected agent from exfiltrating data (e.g., SSH keys) or downloading malware.
- **Sandboxed bash tool** (research preview): open-source runtime letting developers define exactly which directories and network hosts a process, agent, or MCP server can access, without managing containers. Built on OS-level primitives — Linux bubblewrap and macOS Seatbelt — covering not just direct commands but any spawned subprocesses. Network access is only permitted through a unix domain socket to a proxy server that enforces domain rules and handles user confirmation for new domains (further customizable for arbitrary traffic rules). Enabled via `claude --sandbox`.
- **Claude Code on the web**: runs each session in an isolated cloud sandbox; sensitive credentials (git credentials, signing keys) never enter the sandbox. Git operations are proxied through a service that authenticates a scoped credential, verifies the interaction (e.g., only pushing to the configured branch), then attaches the real token before forwarding to [[GitHub]]. Launched October 20, 2025 as a research preview supporting parallel tasks across repos, automatic PR creation, and custom network configuration to allow specific domains (e.g., npm) from within the sandbox.
- Anthropic open-sourced the sandboxing runtime to encourage other AI companies/agent builders to adopt the same approach.
- Directly framed as a [[PromptInjection]] mitigation: even a successful prompt injection is fully isolated and cannot affect overall user security.
- **Self-hosted sandboxes for Claude Managed Agents (May 19, 2026, public beta)**: extends the sandboxing pattern to [[ClaudeManagedAgents]] at the infrastructure level — the agent loop (orchestration, context management, error recovery) stays on Anthropic's infrastructure, but the sandbox where tools actually execute moves to infrastructure the customer controls: their own servers, or a managed sandbox provider ([[Cloudflare]], [[Daytona]], [[Modal]], [[Vercel]]). Because execution happens inside the customer's perimeter, existing network policies, audit logging, and security tooling apply automatically, and files/repositories never leave it; the customer also controls compute sizing and runtime image, so compute-heavy tasks (long builds, image generation) get the capacity they need. Paired in the same announcement with [[ModelContextProtocol|MCP]] tunnels, which apply the same "keep it inside the perimeter" principle to reaching private MCP servers rather than to tool execution. See [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]].
- **Decoupled architecture in Managed Agents (June 2026)**: [[ClaudeManagedAgents]] fundamentally separates the brain (harness/orchestration calling Claude) from the hands (sandbox where code executes), connected by an append-only session event log. This architecture means Claude can begin reasoning before any container exists, the sandbox stays far from credentials (which live in a separate vault with envelope encryption), and a whole run can be reconstructed from its session at any point. This contrasts with the common pattern where agent harnesses run inside the same container as the filesystem — exposing credentials to generated code and losing the run when the container dies. See [[summary-2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents]].
- **Security-scanning sandboxes (May 2026)**: Anthropic's vulnerability-scanning workflow uses sandboxes for two distinct purposes:
  - **System protection**: to enable models to run safely and autonomously, a strong isolation layer is needed. Match isolation to the threat model: containers are fine for the discovery agent reading code, but run the target and its PoCs in a microVM (like Firecracker) or a full VM with egress locked down so nothing can reach production systems. Never have credentials (`~/.aws`, `~/.ssh`, `.env`) available to the agent.
  - **Setup workflow**: give the sandbox network access only during setup — pull dependencies, build, install tools, deploy the target, run existing tests to confirm everything works. Then snapshot the environment and remove network access. During scanning, allow traffic only to the model API, routed through a local proxy. Load the snapshot at the start of each run so every scan begins from the same clean slate.
  - **Exploitability proof**: during static scanning, the model reads code and hypothesizes what might break but cannot test reachability or compensating controls. When teams built a sandbox where the agent could compile code, run tests, and detonate a PoC, non-exploitable findings dropped significantly. One offensive-security team's assessment: "the biggest efficacy lever has been giving the model test beds, live systems, and running the PoCs."
  - **Pinned reproducibility**: pin everything (image tags, commit SHAs, dependencies, build commands) so every run uses the same code in the same environment. Cache a local copy so the build requires no network. One team's scan flagged a vulnerability from an older library version the agent downloaded by mistake — they now build containers with dependencies pinned to match production.
  - **Faithfulness to production**: excluding dependencies (like a queue or datastore) can lead to under-reporting bugs. Ignoring production defenses (like a WAF or auth gateway) leads to reporting unexploitable findings. Strike a balance. If building a representative sandbox is impractical, start with static discovery and invest in the sandbox later once the volume of findings justifies it.

## Related

- [[ClaudeCode]] — the tool implementing sandboxing via the sandboxed bash tool and Claude Code on the web
- [[PromptInjection]] — the threat model sandboxing mitigates
- [[CodeSecurity]] — broader security practices this complements
- [[GitHub]] — target of the scoped git-credential proxy in Claude Code on the web
- [[summary-2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous]] — source article
- [[summary-2025-10-20 - Claude Code on the web]] — cloud sandbox launch announcement
- [[ClaudeManagedAgents]] — product now offering self-hosted sandboxes
- [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]] — self-hosted sandboxes launch article
- [[Cloudflare]] — self-hosted sandbox provider
- [[Daytona]] — self-hosted sandbox provider
- [[Modal]] — self-hosted sandbox provider
- [[Vercel]] — self-hosted sandbox provider
- [[summary-2026-05-27 - Using LLMs to secure source code]] — security-scanning sandbox design guidance
- [[ThreatModeling]] — the threat model that determines sandbox isolation requirements
- [[VulnerabilityVerification]] — the verification phase that uses the sandbox to build and run PoCs
- [[Claude4.7Opus]] — the model used in the security-scanning sandbox workflow
- [[summary-2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents]] — decoupled brain/hands architecture in Managed Agents
- [[ContextAnxiety]] — model behavior motivating harness evolution alongside sandbox design
