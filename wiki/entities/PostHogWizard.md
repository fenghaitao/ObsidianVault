---
title: "PostHogWizard"
type: entity
tags: [product, autonomous-agents, code-generation, posthog, claude-agent-sdk]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md"]
last_updated: 2026-06-29
---

## Definition
The PostHog Wizard is an autonomous coding agent built by PostHog that automatically integrates PostHog analytics into users' projects. It processes 15,000 integrations per month, turning "2 hours of misery" into 8 minutes of working integration.

## Key Information
- Built by Danilo Campos at PostHog
- Processes 15,000 integrations per month
- Uses the Claude Agent SDK wrapped in a CLI
- PostHog covers inference costs via an LLM gateway — users get free inference by logging into PostHog
- Composition: 90% markdown files, 8% tools for delivering and processing markdown, 2% agent harness
- Uses skill files generated from a context service to drive agent behavior
- Loads fresh documentation from posthog.com as context to combat model rot
- Uses model airplanes (thin reference implementations) as patterns for consistent integrations
- Uses breadcrumbing (progressive task disclosure) to limit improvisation
- Performs inference-time interrogation at the stop hook to identify failures
- Uses fine-grained tool permissions to prevent reading sensitive files like .env
- Received unprompted positive social media posts from users

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[DaniloCampos]] — creator
- [[PostHog]] — company
- [[ClaudeAgentSDK]] — SDK used
- [[Model Rot]] — problem it solves
- [[Model Airplanes]] — technique it uses
- [[Breadcrumbing]] — technique it uses
- [[Inference-Time Interrogation]] — technique it uses
- [[Fine-Grained Tool Permissions]] — security approach
- [[Autonomous Coding Agents]] — broader category
