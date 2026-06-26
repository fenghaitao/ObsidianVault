---
title: "AWS"
type: entity
tags: [company, cloud, sandbox, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md"]
last_updated: 2026-06-26
---

## Definition
Amazon Web Services (AWS) is a cloud infrastructure provider. Mentioned in the Claude Agent SDK workshop as one of the sandbox providers suitable for hosting agent environments in production.

## Key Information
- Provides sandboxed container environments suitable for hosting agents built with the Claude Agent SDK
- Part of the layered security approach for agent deployment
- **Kiro context**: AWS is the parent organization of Amazon Kiro. Kiro is "brought to you by AWS" but not deeply integrated with the rest of the AWS ecosystem. AWS services used in Kiro demos include Agent Core (agent deployment), S3 (storage), DynamoDB (database), and CDK (infrastructure-as-code). The Kiro CLI includes a `use AWS` tool wrapping the AWS SDK. AWS provides an MCP documentation server that Kiro can use for research.

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[Sandboxing]] — the security approach
- [[Modal]] — another sandbox provider
- [[Cloudflare]] — another sandbox provider
- [[DigitalOcean]] — another sandbox provider
- [[AmazonKiro]] — agentic IDE built on AWS
- [[AgentCore]] — AWS agent deployment service
- [[AmazonS3]] — AWS storage service
- [[AmazonDynamoDB]] — AWS database service
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source (Amazon Q Developer, Amazon Bedrock, Converse API)
- [[Amazon Q Developer]] — AI-powered software development assistant
- [[Amazon Titan]] — AWS's own foundation model family
