---
title: "summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind"
type: source
tags: [source, transcript, deepmind, agents, scale, antigravity, quota, skills, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Core Summary

KP Sawhney (software engineer, DeepMind AI platform team) and Ian Ballantyne (developer relations engineer, Google DeepMind) discuss how DeepMind builds and scales agentic software. Ballantyne demos Antigravity, a VS Code-style IDE with a built-in agent manager that runs multiple agents with planning, DOM inspection, browser control, and human-in-the-loop editing. Sawhney describes the challenges of running agents at Google scale: token-hungry agents require quota management, mixing cheaper models (Gemma 4) with advanced models for specific components, evaluating complex agentic workflows using mock TPUs to save compute, curating a library of skills that can sprawl out of control in large organizations, and building custom observability tooling including a trajectory store for diagnosing agent failures. Both emphasize a future of seamless model tiering, agent-to-agent collaboration through shared workspaces, and humans acting as supervisors on a digital assembly line.

## Key Points

- **Antigravity demo**: VS Code-style IDE with agent manager that spawns multiple agents, includes planning system, DOM inspection, browser control, human-in-the-loop editing, and task completion reports. Agents rewrite code from scratch based on specs.
- **Agent scaling challenges**: Token-hungry agents consume enormous compute; quota management is brute-force but necessary. Google has SRE teams monitoring usage spikes 24/7 who reach out when jobs need to stop.
- **Model tiering strategy**: Mix cheaper models like Gemma 4 (effectively free from a quota perspective using local GPUs/TPUs) with more advanced models for specific agentic system components. Future vision: seamless fallback when quota is exhausted without interrupting workflows.
- **Skills governance at scale**: DeepMind builds a library of skills contributed by domain experts, but in an organization as large as Google, skills can "sprawl out of control." Focus on improving skills and ensuring only the best survive — described as "almost Darwinian."
- **Skills vs MCP**: Sawhney prefers skills over MCP, calling MCP "a bit of a flash in the pan." Likes MCP for auth but finds skills + CLI interactions work better for speeding up development. Both will continue to be supported.
- **Evaluation challenges**: Complex agentic workflows are hard to evaluate. Using mock TPUs to test harnesses without consuming real TPU hours. Hardest part is creating new datasets; onus falls on skill authors to design testing. Agents are being experimented with to design evaluations themselves.
- **Custom observability**: Built a custom web app for agent observability with hierarchical drill-down to raw predict requests. Also built an agent trajectory store for coding agents to diagnose exactly when looping started or when the model went off the rails.
- **Deep Research re-architecture**: Exploring re-architecting the deep research agent to use the Antigravity harness, making each element a collaborator in a shared workspace (like how humans research) rather than passing huge blobs of context through the system. Could enable infographics and additional support artifacts.
- **Agent-to-agent communication**: Current Antigravity agents work on different tracks but aren't obviously coordinating. Future vision: efficient agent-to-agent communication with humans as supervisors on a "digital assembly line."
- **Code review automation**: Google has language-specific auto-review models fine-tuned on style guides and good code examples. Product teams create custom SRIs and prompts. Sawhney recently received an agent-generated PR comment without triggering it manually.
- **Pricing implications**: Subscription models don't work well for token-hungry agentic systems (referencing Anthropic blocking OpenClaw). Active exploration of how to price agentic workloads.

## Related

- [[KP Sawhney]] — presenter, software engineer at DeepMind
- [[Ian Ballantyne]] — presenter, developer relations engineer at DeepMind
- [[GoogleDeepMind]] — company
- [[Antigravity]] — agentic IDE and platform
- [[Agent Quota Management]] — scaling concept
- [[Model Tiering]] — seamless model fallback concept
- [[Agent Trajectory Store]] — observability concept
- [[Skills]] — domain expertise mechanism
- [[Agent Skills]] — skill libraries at scale
- [[Skills Governance]] — curating skills in large orgs
- [[AgenticEvaluations]] — evaluating complex agent workflows
- [[Deep Research Agent]] — being re-architected with harness
- [[AgentToAgentCommunication]] — future collaboration vision
- [[Agentic Code Review]] — automated PR review agents
- [[Tokenomics]] — pricing challenges for agentic systems
- [[AgentObservability]] — custom tracing and debugging
- [[Gemma4]] — cheaper model for agent components
- [[Computer Use]] — browser control capability
- [[AgentHarness]] — platform for running agents
