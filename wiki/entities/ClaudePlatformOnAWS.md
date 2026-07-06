---
title: "Claude Platform on AWS"
type: entity
tags: [aws, amazon, cloud, claude-platform, enterprise-ai, anthropic-operated]
sources: ["raw/01-articles/claude/2026-05-11 - Introducing the Claude Platform on AWS.md"]
last_updated: 2026-07-04
---

# Claude Platform on AWS

Claude Platform on AWS is a first-of-its-kind AWS offering, generally available as of May 11, 2026, that gives AWS customers direct access to the full native Claude API feature set — with AWS IAM authentication, CloudTrail audit logging, and consolidated AWS billing that fully retires against existing AWS commitments. Unlike [[AmazonBedrock|Claude on Amazon Bedrock]], Anthropic (not AWS) operates the service and processes data outside the AWS boundary.

## Key Information

- **General availability**: May 11, 2026. Available in most AWS commercial regions; supports both global and U.S. inference geographies.
- **Operator/data boundary**: Anthropic operates the service; data is processed outside the AWS boundary (contrast with Bedrock, where AWS is the data processor operating within the AWS boundary).
- **Feature parity**: all new native Claude API features and betas ship on Claude Platform on AWS the same day they ship on the direct Claude API — the first AWS-hosted Claude offering with day-one parity.
- **Auth/ops**: AWS IAM authentication, CloudTrail audit logging, single AWS invoice billing (fully retires against existing commitments). Customers use existing AWS credentials/IAM policies.
- **Included at launch**: [[ClaudeManagedAgents|Claude Managed Agents]] (beta), [[AdvisorStrategy|advisor strategy]] (beta), [[WebSearch|web search]] and web fetch, [[CodeExecutionTool|code execution]], [[FilesAPI|Files API]] (beta), [[ClaudeCodeSkills|Skills]] (beta), [[MCPConnector|MCP connector]] (beta), [[PromptCaching|prompt caching]], [[Citations]], [[BatchProcessing|batch processing]].
- **Console access**: bundled [[AnthropicConsole|Claude Console]] for agent, skill, environment, and vault management plus observability tooling.
- **Models at launch**: Claude Opus 4.7, Sonnet 4.6, and Haiku 4.5, with new models shipping as they launch going forward.
- **Choosing between the two AWS paths**: Claude Platform on AWS suits customers wanting the full native Claude Platform experience; [[AmazonBedrock|Claude on Amazon Bedrock]] suits customers with strict regional data-residency requirements who need data processed exclusively within AWS's infrastructure.
- **Commercial migration note**: customers with an existing Bedrock private offer should contact their Anthropic/AWS account executive before adopting Claude Platform on AWS — discounts cannot be applied retroactively to usage incurred before a Claude Platform private offer is accepted.

## Related

- [[AmazonBedrock]] — the pre-existing AWS-operated, AWS-as-data-processor alternative
- [[Anthropic]] — operator of Claude Platform on AWS
- [[ClaudeManagedAgents]] — included beta feature
- [[AdvisorStrategy]] — included beta feature
- [[AnthropicConsole]] — bundled Console access
- [[PromptCaching]] — included platform feature
- [[Citations]] — included platform feature
- [[BatchProcessing]] — included platform feature
- [[FilesAPI]] — included beta feature
- [[MCPConnector]] — included beta feature
- [[CodeExecutionTool]] — included platform feature
- [[WebSearch]] — included platform feature
- [[summary-2026-05-11 - Introducing the Claude Platform on AWS]] — launch/GA announcement source
