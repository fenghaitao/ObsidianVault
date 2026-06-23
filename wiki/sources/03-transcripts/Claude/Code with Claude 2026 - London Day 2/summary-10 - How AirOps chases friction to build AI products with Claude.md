---
title: "How AirOps Chases Friction to Build AI Products with Claude"
type: source
tags: [aiops, content-marketing, agents, friction, sub-agents, tools]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/10 - How AirOps chases friction to build AI products with Claude.md]
last_updated: 2026-06-23

---

## Core Summary

Dylan from AirOps presents how their growth marketing platform evolved from a node-based workflow builder to an agent-based system using the Claude Agent SDK. The talk focuses on two key friction points: (1) fitting agents into content marketers' actual workflows through document-based playbooks with embedded human review gates, and (2) ensuring quality outputs through specialized tools and strategic sub-agent decomposition. Key results include enterprise customers going live in 1 week (vs. 1 month previously), 130% increase in citation rates, and 8% fewer tokens consumed through specialized tools.

## Key Points

- **Evolution path:** Node-based workflow builder (brittle, required technical expertise) → LLM-compiled workflows (too non-deterministic) → Traditional agent frameworks (code changes needed for orchestration changes) → Claude Agent SDK (markdown-based orchestration, skills for context).
- **Document-based playbooks:** Marketers are familiar with Google Docs; playbooks are natural-language skill-like documents with slash commands for tools, inputs, and outputs. Transparency about which tools are used at each step.
- **Human review gates:** Assign specific users to approve outputs at each section. Only the assigned user can unblock the agent. Review surfaces include an inbox and a grid view for content orchestration at scale.
- **Specialized tools over primitive loops:** Instead of agents making 20+ tool calls to analyze a page, create a single specialized tool that fetches everything needed in one call. This reduced token consumption by 8% and improved speed.
- **Sub-agent decomposition strategy:** Start with a single Claude harness, then add sub-agents as needed: compliance check (brand rules verification), dedicated writer (focused context window), brand kit fetcher (fetch all brand context upfront as artifact), and custom sub-agents per customer.
- **Context discipline:** Even with 1M token context windows, be cognizant of what the model attends to. Larger windows don't mean you should use all of them.
- **Next friction points:** Self-improvement and feedback loops (structuring trace summaries, forgetting as a feature), benchmarking content creation agents (taste is subjective, hard to create deterministic evals).
- **Results:** 10 enterprise customers publishing content in under 2 weeks during beta; 130% citation rate increase; 42% share of voice increase for Parallel case study.

## Related

- [[ClaudeCode]] — the agent SDK used for orchestration
- [[ClaudeManagedAgents]] — the managed agents API used
- [[ClaudeCodeSkills]] — playbooks as the skill equivalent for marketers
- [[AirOps]] — the company entity
- [[ClaudeCodeSubagents]] — sub-agent decomposition patterns
