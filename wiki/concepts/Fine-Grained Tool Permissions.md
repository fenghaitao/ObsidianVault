---
title: "Fine-Grained Tool Permissions"
type: concept
tags: [security, agents, tool-calling, sandboxing, privacy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
Fine-grained tool permissions is a security practice for autonomous coding agents where tool access is locked down to only the specific operations needed, rather than granting broad file system access. This prevents agents from accidentally reading sensitive data (like .env files) and sending it to cloud logs.

## Key Information
- Articulated by Danilo Campos (PostHog) based on a security incident with the PostHog Wizard
- Early versions of the Wizard would read entire .env files (necessary for writes), but this sent secrets to cloud logs — "obviously bad news"
- Solution: lock down what the agent is allowed to do around sensitive files
- Built a dedicated tool with exactly two capabilities for .env files:
  1. Check the presence of a key ("Does this key exist?")
  2. Write a new value to a key
- No .env contents ever go up for inference — the agent never reads the full file
- Broader principle: "When you're designing these things, you have fine-grained control over tool usage. You can decide: these tools are okay, these kinds of reads are okay, these kinds of reads are not okay."
- Running an agent on someone else's machine demands huge trust; security shenanigans must be proactively addressed
- Even if the agent solves the promised problem, doing it in a way that exposes secrets "makes you look like an [untrustworthy actor]"
- **n8n Field-Level Permissions**: In n8n, every tool node exposes individual fields to the AI agent. The agent can only set fields you explicitly configure — unlike platforms where the AI gets full API access. You can mix "From AI" values with hardcoded static text and references to other fields. This is described as a "double-edged sword": it provides security but requires configuring every field individually
- **n8n Tool Description Control**: Field-level descriptions can be added to guide the AI on specific parameters (e.g., "summary" in Google Calendar is actually the event title). The auto-generated key can be renamed (e.g., from "summary" to "title") to improve AI comprehension

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[DaniloCampos]] — articulated the concept
- [[PostHogWizard]] — product that implements this
- [[SandboxingAndPermissions]] — related security practice
- [[Sandboxing]] — broader category
- [[CapabilityBasedSecurity]] — related security model
- [[Agent as Octopus]] — complementary design philosophy (constrain security, not problem-solving)
- [[Autonomous Coding Agents]] — broader category where this applies
- [[n8n]] — platform with field-level tool permission control
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[ToolCalling]] — underlying mechanism for tool-based permissions
- [[HumanInTheLoopWorkflows]] — complementary pattern for destructive action control
