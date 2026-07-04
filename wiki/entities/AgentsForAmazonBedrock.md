---
title: "Agents for Amazon Bedrock"
type: entity
tags: [aws, amazon-bedrock, agents, orchestration, aws-lambda]
sources: ["raw/01-articles/claude/2023-09-28 - Claude on Amazon Bedrock now available to every AWS customer.md"]
last_updated: 2026-07-04
---

## Definition

Agents for Amazon Bedrock is an AWS feature (announced in preview, September 2023) that lets foundation models like Claude orchestrate and perform API calls using AWS Lambda functions, expanding Claude's role from a conversational responder to a task-completing agent.

## Key Information

- Anthropic's team was instrumental in developing this feature alongside AWS.
- Enables Claude to: understand user requests, break down complex tasks into multiple steps, carry on conversations to collect additional details, look up information, and take actions to fulfill requests.
- Example use case: an e-commerce chat assistant built with Claude that goes beyond querying product inventory to actually updating orders, processing exchanges, and looking up user manuals.
- Announced as available in preview as of the September 2023 [[AmazonBedrock]] general-availability announcement.

## Related

- [[AmazonBedrock]] — the platform hosting this feature
- [[Claude2]] — model available on Bedrock at the time of this announcement
- [[Anthropic]] — co-developer of the feature
- [[AIAgent]] — the broader agent pattern this feature enables
- [[summary-2023-09-28 - Claude on Amazon Bedrock now available to every AWS customer]] — source article
