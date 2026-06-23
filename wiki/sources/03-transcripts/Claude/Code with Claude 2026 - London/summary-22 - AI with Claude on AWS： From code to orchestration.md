---
title: "AI with Claude on AWS: From Code to Orchestration"
type: source
tags: [aws, bedrock, cloud, deployment, enterprise, workshop]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/22 - AI with Claude on AWS： From code to orchestration.md]
last_updated: 2026-06-23
---

## Core Summary

Antonio Rodriguez from AWS presents the Anthropic-AWS partnership and demonstrates three ways to use Claude on AWS: through Amazon Bedrock (direct model access with enterprise security), Claude Platform on AWS (full feature parity with consolidated billing), and Claude Desktop connected to Bedrock. The session includes a hands-on workshop covering Claude Code setup on AWS, MCP integration with Playwright, Git workflows, sub-agents, plugins, custom skills, and hooks. Key themes are data sovereignty, enterprise compliance, and the "better together" story of combining Anthropic's frontier models with AWS infrastructure.

## Key Points

- **Three ways to use Claude on AWS:** (1) Amazon Bedrock direct API access, (2) Claude Platform on AWS (gateway with full feature parity), (3) Claude Desktop connected to Bedrock via CodeWhisperer 3P.
- **Project Rainier:** One of the largest AI compute infrastructures, built on AWS for training and hosting Claude models using custom Trainium chips (3rd generation).
- **Amazon Bedrock features:** Model evaluation, prompt optimization, fine-tuning (only provider allowing Haiku fine-tuning), model distillation, knowledge bases for RAG, guardrails (content filters, PII masking), automated reasoning checks.
- **Bedrock Agent Core:** Infrastructure for hosting agents built with any open framework (LangChain, CrewAI, Claude Agent SDK), fully compatible.
- **Security and compliance:** Zero operator access (no Amazon or Anthropic employee can access instances), private link for fully private communication, FedRAMP/HIPAA compliance, built-in auth (SSO, OAuth, IAM roles).
- **Workshop modules:** Basic (Claude Code setup, Scaled Draw), Intermediate (Playwright MCP, Git workflows), Advanced (sub-agents, plugins, custom skills, hooks), Production (team standards, dashboards, cost control, ROI measurement).
- **Enterprise controls:** Consolidated billing, CloudWatch/CloudTrail observability, guaranteed SLAs, region selection for GDPR compliance.

## Related

- [[ClaudeCode]] — the tool deployed on AWS in this workshop
- [[Anthropic]] — the model provider in the AWS partnership
- [[AmazonBedrock]] — the AWS service for foundation models
- [[ModelContextProtocol]] — MCP integration demonstrated in the workshop
- [[ClaudeCodeSkills]] — custom skills covered in advanced workshop modules
