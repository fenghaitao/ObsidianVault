---
title: "AWS"
type: entity
tags: [cloud-platform, infrastructure, amazon, aws]
sources: ["raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-07-07
---

## Definition

Amazon Web Services (AWS) is Amazon's cloud computing platform, providing infrastructure, platform, and software-as-a-service offerings for enterprises and developers. It serves as a cloud inference platform for [[ClaudeDesktop]], enabling organizations to run Claude's full desktop experience within their own AWS environment.

## Key Information

- AWS is one of three cloud platforms (alongside [[GoogleCloud]] and [[MicrosoftFoundry]]) where organizations can deploy the full Claude Desktop experience with inference running in their own cloud environment.
- Integrates with enterprise SSO via IAM Identity Center or Workforce Identity Federation for Claude Desktop sign-in.
- Organizations control the regions where inference runs and the aggregated telemetry Anthropic receives.
- Also hosts Claude models through [[AmazonBedrock]] for API access.

## Related

- [[ClaudeDesktop]] — the unified desktop application deployable on AWS
- [[AmazonBedrock]] — AWS managed service for Claude model API access
- [[GoogleCloud]] — alternative cloud platform for Claude Desktop
- [[MicrosoftFoundry]] — alternative cloud platform for Claude Desktop
- [[CloudInference]] — the pattern of running AI inference within the customer's own cloud
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — source article
- [[summary-22 - AI with Claude on AWS： From code to orchestration]] — source summary
