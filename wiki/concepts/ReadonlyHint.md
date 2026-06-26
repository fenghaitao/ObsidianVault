---
title: "Readonly Hint"
type: concept
tags: [mcp, annotations, permissions, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
The Readonly Hint is an MCP spec annotation that marks a tool as read-only, allowing clients to handle permissions differently and avoid unnecessary confirmation prompts for non-destructive operations.

## Key Information
- Part of the MCP spec's annotations system, a restricted subset of annotations on various components
- Motivation: help clients with permission setting
- Clients like ChatGPT will ask for extra permission if a tool does NOT have this annotation set, because it presumes the tool can have side effects
- In "YOLO mode" or with disabled permissions, this annotation is irrelevant
- Block's playbook recommends using this annotation
- Not yet widely adopted, though ChatGPT's developer mode uses it
- Represents one form of design where the client can choose to provide a better experience based on server annotations

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[MCP]] — protocol that defines this annotation
- [[AgenticProductDesign]] — design philosophy this supports
