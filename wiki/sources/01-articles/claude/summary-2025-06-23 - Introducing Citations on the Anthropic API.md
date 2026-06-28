---
title: "Introducing Citations on the Anthropic API"
type: source
tags: [API, citations, source-tracking, hallucination-reduction]
sources: [raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md]
last_updated: 2026-06-28
---

# Introducing Citations on the Anthropic API

## Summary

[[Anthropic]] launches Citations, a new API feature that enables [[Claude]] to provide detailed references to exact passages and sentences it uses to generate responses. This feature addresses a critical need for verifiable, trustworthy AI outputs by grounding answers in source documents.

## Key Features

- **Automatic Citation Generation**: Claude automatically cites claims in its output that are inferred from provided source documents
- **Document Support**: Processes PDF documents and plain text files by chunking them into sentences
- **Flexible Integration**: Seamlessly integrates with the Messages API without requiring file storage
- **Superior Performance**: Internal evaluations show 15% recall accuracy improvement over custom implementations
- **Token-Efficient Pricing**: Uses standard token-based pricing; users don't pay for output tokens that return quoted text

## Availability

- Generally available on the Anthropic API and Google Cloud's [[VertexAI]]
- Available on [[AmazonBedrock]] as of June 30, 2025
- Supported on [[Claude3.5Sonnet]] and [[Claude3.5Haiku]]

## Use Cases

Citations enables AI solutions with enhanced accountability for:
- Legal document analysis
- Financial research
- Knowledge synthesis
- Professional advisory services

## Real-World Applications

### Thomson Reuters - CoCounsel
[[ThomsonReuters]] uses Citations in CoCounsel to help legal and tax professionals. The feature minimizes hallucination risk and strengthens trust in AI-generated content for practicing attorneys.

### Endex - Financial Research
Endex uses Citations in their Autonomous Agent for financial firms, reducing source hallucinations and formatting issues from 10% to 0%, with a 20% increase in references per response.

## Technical Approach

The Citations feature operates by:
1. Processing user-provided source documents through chunking into sentences
2. Passing chunked sentences and context to the model with the user's query
3. Claude analyzing the query and generating responses with precise citations
4. Optional: Users can provide their own chunks for source documents

## Related

[[Anthropic]] — The company behind Claude and the Citations API feature
[[Claude]] — The language model powering the Citations feature
[[Claude3.5Sonnet]] — Model with Citations support
[[Claude3.5Haiku]] — Model with Citations support
[[RetrievalAugmentedGeneration]] — Related concept of grounding responses in external sources
[[AmazonBedrock]] — Platform offering Citations feature
[[VertexAI]] — Google Cloud platform offering Citations feature
[[ThomsonReuters]] — Enterprise customer using Citations
