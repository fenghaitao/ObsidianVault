---
title: "Container-based Sandboxing"
type: concept
tags: [security, sandboxing, containers, ai-code, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Definition
Container-based Sandboxing is an approach to isolating AI-generated code using full Linux containers with real file systems, real processes, and real networking. It is the appropriate choice when the code needs to install packages, run build steps, start servers, or perform any operation requiring a full operating system environment.

## Key Information
- Provides a full Linux environment: bash, Node.js, git, npm, and whatever tools are configured
- Supports: git clone, npm install, build steps, dev servers, exposed ports, long-running processes
- Each user gets their own container with completely separate file system — files from one user's container literally do not exist in another's
- Architecture pattern (Cloudflare): main worker → Sandbox SDK → Durable Object (stateful coordinator) → Container VM
- Startup time: seconds (vs. milliseconds for isolates)
- More expensive than isolates — allocating real CPU and memory per sandbox
- More complex architecture with moving parts: SDK, durable object, container orchestration, networking layer
- Use when the code needs: file system access, process spawning, package installation, or running servers
- Decision tree: need file system, processes, or package installs? → Containers. Otherwise → Isolates
- Critical patterns: one user one sandbox (never share), proxy secrets through worker (never pass API keys as env vars), clean up with try/finally, set maximum lifetimes
- Cloudflare containers have a default timeout of 10 minutes
- Complementary to isolates — use isolates for fast iteration (the "brain") and containers for building real things (the "workbench")

## Related
- [[summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare]] — source
- [[Sandboxing]] — broader security concept
- [[Isolate-based Sandboxing]] — the complementary approach
- [[Agent Sandboxing]] — agent-specific sandboxing
- [[CapabilityBasedSecurity]] — underlying security model
- [[Proxy Pattern (Secrets)]] — key pattern for secrets management
- [[Prompt Motion]] — example application using container sandboxing
- [[Cloudflare]] — platform providing container sandboxing
- [[CloudflareWorkers]] — platform component
