---
title: "Vercel Sandbox"
type: entity
category: tool
---

# Vercel Sandbox

## Definition

Vercel Sandbox is a service by Vercel that provides isolated virtual machines (similar to EC2 instances) for running agent-generated code. Each sandbox instantiation is a new VM that lasts for the duration of a session.

## Key Information

- **Creator**: Vercel
- **Type**: Cloud sandbox service
- **Key Operations**:
  - `sandbox.create` — Creates a new isolated VM
  - `sandbox.getURL` — Gets the URL for a running sandbox
  - `sandbox.runCommand` — Executes commands within the sandbox
- **Usage**: Used in the coding agent demo to run generated code in an isolated environment; the sandbox state is not managed by the workflow itself
- **Alternative**: Can be replaced with local execution or other sandbox solutions

## Related

- [[Vercel]]
- [[WorkflowDevKit]]
- [[AISDK]]
