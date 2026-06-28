---
title: "Citations"
type: concept
tags: [citations, sources, verification, accountability]
sources: [raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md]
last_updated: 2026-06-28
---

# Citations

Source attribution mechanism that links AI-generated answers back to original materials, enabling verification and accountability.

## Overview

Citations are a core feature of [[WebSearch]] and other knowledge-retrieval capabilities in Claude. Every web-sourced response includes citations to the source materials, enabling users to verify information directly and establish the credibility of the answer.

## Purpose

- **Verification**: Users can check the original source to confirm the accuracy of the information provided
- **Accountability**: Citations establish a clear chain of evidence from the answer back to authoritative sources
- **Trust Building**: Particularly valuable for sensitive use cases that require accuracy and accountability
- **Transparency**: Users can see exactly where Claude sourced its information

## Implementation in Web Search

When [[WebSearch]] is enabled on the [[MessagesAPI]]:

1. Claude generates a search query and retrieves web results
2. Claude analyzes the results for key information
3. Claude provides an answer with direct citations to the source material
4. Users can follow the citations to the original sources for verification

## Use Cases

Citations are particularly important for:
- Legal and compliance-sensitive applications
- Financial analysis and recommendations
- Medical and health information
- Research and academic work
- News and current events analysis
- Any scenario requiring high accuracy and accountability

## Related

- [[WebSearch]] — Web search capability that provides cited results
- [[summary-2025-05-07 - Introducing web search on the Anthropic API]] — Source description
- [[ToolUse]] — Broader tool capability framework
- [[MessagesAPI]] — API providing citation-enabled responses
