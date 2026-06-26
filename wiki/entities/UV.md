---
title: "UV"
type: entity
tags: [tool, python, package-manager, dependency-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
UV is a Python package and project manager used for dependency management. In the workshop, it was used to manage dependencies for the deep research agent and writing workflow, and to run the FastMCP server as a subprocess via the command `uv run fastmcp run server.py`.

## Key Information
- Python package and project manager
- Used in the workshop for dependency management across the research and writing components
- Simplifies virtual environment creation and package installation
- Used to run the MCP server: `uv run fastmcp run <path-to-server-file>`
- Referenced in the mcp.json configuration for Claude Code integration

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[FastMCP]] — library run via UV
- [[MCP]] — protocol served via UV-managed FastMCP
- [[ClaudeCode]] — agent harness configured to use UV commands
