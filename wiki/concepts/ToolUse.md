---
title: "Tool Use"
type: concept
tags: [ai, claude, tools, api, function-calling, agentic]
sources: [raw/01-articles/claude/2024-05-30 - Claude can now use tools.md]
last_updated: 2026-06-28
---

# Tool Use

Tool use is the capability for an LLM to interact with external tools and APIs to perform tasks, manipulate data, and deliver more accurate responses. It enables Claude to act agentively within defined workflows by selecting and executing appropriate tools based on the user's natural language request.

## Definition

Tool use allows Claude to:
- Receive a set of tool definitions from the developer
- Understand user requests in natural language
- Select the appropriate tool(s) to fulfill the task
- Execute the corresponding action
- Return results for further reasoning or presentation

## Key Characteristics

- **Developer-controlled**: Developers define the toolset available to Claude
- **Natural language interface**: Users specify requests naturally; Claude determines which tools to use
- **Agentic behavior**: Enables dynamic responses based on task requirements
- **Multi-step workflows**: Tools can be chained for complex operations
- **General availability**: Became GA across Claude 3 family on May 30, 2024

## Availability

As of May 2024, tool use is available across:
- [[Anthropic]] Messages API
- [[AmazonBedrock]] (AWS)
- Google Cloud's Vertex AI

Supported across the entire [[Claude3]] model family ([[Claude3Opus]], [[Claude3Haiku]], and other variants).

## Limitations

- No support for parallel tool calls (as of May 2024)

## Enterprise Applications

Tool use has enabled organizations to build:
- **AI tutoring systems** ([[StudyFetch]])
- **Browser automation platforms** ([[Intuned]])
- **Financial and legal AI assistants** ([[Hebbia]])

## Contrast with Related Concepts

- **Function calling**: Earlier LLM capability; tool use is the evolved Claude implementation
- **Agent reasoning**: Tool use is one capability within agentic systems (see [[AIAgent]])
- **API integration**: Tool use abstracts API complexity by letting Claude handle tool selection

## Related

- [[Claude3]] — model family with full tool use support
- [[Claude3Opus]] — flagship model with enhanced reasoning for tool selection
- [[Claude3Haiku]] — efficient model widely used for tool-based applications
- [[Anthropic]] — creator of Claude's tool use capability
- [[AIAgent]] — broader agentic framework incorporating tool use
- [[StudyFetch]] — education platform leveraging tool use
- [[Intuned]] — browser automation using tool use
- [[Hebbia]] — financial/legal services platform using tool use
- [[summary-2024-05-30 - Claude can now use tools]] — GA announcement and use case studies
