---
title: "ComplianceAPI"
type: concept
tags: [compliance, governance, api, enterprise, audit]
sources: ["raw/01-articles/claude/2025-08-20 - Claude Code and new admin controls for business plans.md"]
last_updated: 2026-07-07
---

## Definition

The Compliance API is an [[Anthropic]] feature that provides programmatic, real-time access to Claude usage data — enabling organizations to build continuous monitoring, automated policy enforcement, and governance systems. It exposes two distinct data streams: an **Enterprise stream** (available since August 2025) that includes real-time access to customer conversation content, and a **Platform stream** (expanded March 2026) that provides activity and audit logs (login/logout, account settings, workspace/org config changes) and explicitly excludes inference activity — no user-model interaction content or model activity is logged.

## Key Information

- Introduced August 2025 for Enterprise plan customers.
- Replaces manual exports and periodic compliance reviews with always-on programmatic access.
- **Core capabilities:**
  - **Two data streams**: Enterprise stream provides real-time access to customer conversation content; Platform stream provides activity/audit logs (login/logout, account settings, workspace/org config changes) excluding inference activity
  - Integration with existing compliance dashboards
  - Automated flagging of potential policy issues
  - Selective data deletion for data retention management
- Enables organizations to build continuous monitoring and automated policy enforcement systems.
- Designed to help enterprises meet regulatory requirements at scale as AI adoption grows.
- Access requires contacting Anthropic sales.
- **March 2026**: Expanded from Claude Enterprise-only to the full Claude Platform — any Claude API organization can now use it, not just Enterprise. See [[summary-2026-03-30 - Audit Claude Platform activity with the Compliance API]].
- Activity feed is filterable by time range, specific users, or API keys.
- Logging begins only once the API is enabled for an org; historical activity from before enablement is not available.
- Organizations already using the Compliance API for Claude Enterprise can add their Claude API organization to the same parent organization to view combined activity in a single feed.
- Full documentation is published on the Anthropic Trust Center (trust.anthropic.com).
- **April 2026:** Claude Cowork's expanded OpenTelemetry events include a shared user account identifier, letting admins correlate OTel events (tool/connector calls, file activity, approval mode) with Compliance API records for unified auditing.

## Use Cases

- Building continuous monitoring pipelines over Claude usage
- Automating compliance policy enforcement
- Auditing AI-generated content for regulatory obligations
- Managing data retention through selective deletion

## Related

- [[ClaudeEnterprise]] — The plan this feature is available on
- [[Anthropic]] — Provider of the Compliance API
- [[Workspace]] — Related admin/management layer in Claude Enterprise
- [[summary-2025-08-20 - Claude Code and new admin controls for business plans]] — Source article announcing the Compliance API
- [[summary-2026-03-30 - Audit Claude Platform activity with the Compliance API]] — March 2026 update expanding availability to the full Claude Platform
- [[summary-2026-04-09 - Making Claude Cowork ready for enterprise]] — OTel/Compliance API correlation via Cowork
- [[summary-2026-05-07 - Collaborate with Claude across Excel, PowerPoint, Word and Outlook]] — Analytics API breakdown per user/app/day for Claude's Office add-ins
