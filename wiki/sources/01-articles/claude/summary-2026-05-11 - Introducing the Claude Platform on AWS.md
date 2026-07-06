---
title: "summary-2026-05-11 - Introducing the Claude Platform on AWS"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-05-11 - Introducing the Claude Platform on AWS.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic announces general availability of the Claude Platform on AWS, a new first-of-its-kind offering that gives AWS customers direct access to the full native Claude API feature set — with AWS IAM authentication, CloudTrail audit logging, and consolidated AWS billing that fully retires against existing commitments — while Anthropic (not AWS) operates the service and processes data outside the AWS boundary. This is explicitly distinguished from [[AmazonBedrock|Claude on Amazon Bedrock]], which remains available and keeps AWS as the data processor operating within the AWS boundary for customers with strict data-residency requirements. New features and betas ship to Claude Platform on AWS the same day they ship on the native Claude API, closing the historical feature-parity gap that Bedrock has had with the direct API.

## Key Points

- **General availability**: Claude Platform on AWS is generally available as of May 11, 2026, available in most AWS commercial regions, supporting both global and U.S. inference geographies.
- **Two distinct AWS paths for Claude**, differentiated by operator and data boundary:
  - **Claude Platform on AWS**: Anthropic operates the service; data processed outside the AWS boundary; full native Claude API feature parity from day one (new features/betas ship same-day as the direct API).
  - **Claude on Amazon Bedrock**: AWS operates as data processor within the AWS boundary; better fit for strict regional data-residency requirements.
- **Authentication/ops model**: AWS IAM for authentication, CloudTrail for audit logging, single AWS invoice for billing that fully retires against existing AWS commitments; customers keep using existing AWS credentials/IAM policies.
- **Feature set included at launch**: Claude Managed Agents (beta), advisor strategy (beta), web search and web fetch, code execution, Files API (beta), Skills (beta), MCP connector (beta), prompt caching, Citations, batch processing.
- **Console access included**: customers get the Claude Console, covering agent/skill/environment/vault management and observability tooling.
- **Models available at launch**: Claude Opus 4.7, Sonnet 4.6, and Haiku 4.5, with new models shipping on Claude Platform on AWS as they launch going forward.
- **Migration/commercial note**: customers with an existing Bedrock private offer are told to contact their Anthropic or AWS account executive before adopting Claude Platform on AWS, since discounts cannot be applied retroactively to usage incurred before a Claude Platform private offer is accepted.
- **Getting started**: available via a dedicated AWS marketplace page (aws.amazon.com/claude-platform) and Anthropic's platform docs.
- **Anomaly**: no prompt-injection-style embedded instructions were found in the source article; the trailing "Get the developer newsletter" line is standard blog-footer boilerplate, not a genuine anomaly worth flagging further.

## Related

- [[AmazonBedrock]] — the pre-existing AWS-operated Claude access path this new offering is explicitly contrasted with
- [[ClaudeManagedAgents]] — included beta feature, deployable at scale via this platform
- [[AdvisorStrategy]] — included beta feature (advisor strategy)
- [[AnthropicConsole]] — Console access bundled with Claude Platform on AWS
- [[PromptCaching]] — included platform feature
- [[Citations]] — included platform feature
- [[BatchProcessing]] — included platform feature
- [[FilesAPI]] — included beta feature
- [[MCPConnector]] — included beta feature
- [[CodeExecutionTool]] — included platform feature
- [[WebSearch]] — included platform feature
- [[Anthropic]] — service operator for this offering
