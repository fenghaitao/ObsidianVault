---
title: "AmazonS3"
type: entity
tags: [tool, aws, storage, cloud]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Amazon S3 (Simple Storage Service) is AWS's object storage service. In the Kiro demo, S3 was initially proposed as the persistence backend for agent conversation checkpointing before Agent Core's native memory feature was discovered as a more idiomatic alternative.

## Key Information
- Used in the Kiro demo as the initially proposed storage backend for persisting agent conversation state
- The demo illustrated how initial prompts can bias the agent toward familiar solutions (S3) when better alternatives exist (Agent Core native memory)
- Kiro generated CDK infrastructure code to create an S3 bucket with encryption for checkpoint storage
- Served as an example of how spec-driven development can help discover better alternatives by challenging initial assumptions

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[AWS]] — parent cloud platform
- [[AmazonDynamoDB]] — alternative AWS storage mentioned
- [[AgentCore]] — service whose native memory was the better alternative
