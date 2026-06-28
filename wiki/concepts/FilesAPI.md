---
title: "FilesAPI"
type: concept
tags: [anthropic, api, files, storage, document-processing, agents]
sources: [raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md]
last_updated: 2026-06-28
---

# Files API

The Files API is an [[Anthropic]] API feature that simplifies document storage and access workflows by enabling developers to upload documents once and reference them repeatedly across conversations.

## Definition

The Files API provides a persistent document storage mechanism that allows developers to:
- Upload documents once to a managed storage layer
- Reference uploaded documents repeatedly across multiple API calls
- Eliminate the need to re-upload the same documents in each request
- Simplify multi-session document workflows

## Key Benefits

- **Storage Efficiency:** Upload documents once, reference many times
- **Simplified Workflows:** Eliminates repeated file uploads across conversations
- **Multi-Session Access:** Maintain document access across separate conversation threads
- **Cost Reduction:** Reduce token overhead by referencing stored documents
- **Integration:** Works seamlessly with code execution tool for direct file access

## Use Cases

- **Knowledge bases:** Store and access large document collections
- **Technical documentation:** Maintain persistent access to documentation across sessions
- **Dataset management:** Store datasets for repeated analysis by code execution tool
- **Multi-session analysis:** Reference same documents across multiple analysis workflows
- **Report generation:** Access stored documents and generate new reports

## Integration with Code Execution

The Files API integrates with the [[CodeExecutionTool|code execution tool]]:
- Claude can access uploaded files directly during code execution
- Produce output files (charts, graphs, reports) as part of response
- Developers upload dataset once, Claude analyzes across multiple sessions without re-uploading

## Availability

- [[Anthropic]] API (beta)
- Works with [[Claude4Opus]] and [[Claude4Sonnet]]

## Related

- [[Anthropic]] — API provider
- [[CodeExecutionTool]] — integrates with Files API for direct file access
- [[PromptCaching]] — complementary feature for efficient context management
- [[AIAgent]] — agents using Files API for document access
- [[Claude4Opus]] — model with Files API support
- [[Claude4Sonnet]] — model with Files API support
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement article
