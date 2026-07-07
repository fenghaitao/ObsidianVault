---
title: "AISecurityGovernance"
type: concept
tags: [security, governance, enterprise, compliance, AI]
sources: ["raw/01-articles/claude/2026-05-21 - Claude now works with more security and compliance tools.md"]
last_updated: 2026-07-07
---

## Definition

AI Security Governance is the practice of applying enterprise security, compliance, and data protection controls to AI tools and platforms, treating them as governed workplace applications alongside the rest of an organization's software stack.

## Key Information

- The core principle is that AI tools should not be exempt from existing organizational security policies — they should be governed through the same DLP, SIEM, SASE, eDiscovery, and identity management frameworks already in use.
- Programmatic APIs (such as the [[ClaudeComplianceApi|Claude Compliance API]]) are the key enabler, exposing conversation content and activity event data to external security platforms.
- The governance surface includes: conversation content monitoring, data loss prevention (DLP) for uploaded files and chat content, user activity auditing (logins, admin actions), configuration change tracking, and identity/access posture management.
- Categories of tools involved in AI security governance include: DLP, SIEM, SASE, data security platforms, identity security posture management, eDiscovery, AI security posture management (AI-SPM), and AI observability/telemetry infrastructure.
- Enterprise adoption of AI tools like [[ClaudeEnterprise|Claude Enterprise]] often depends on the availability of such governance integrations — security and compliance teams need visibility and control before approving organization-wide deployment.

## Related

- [[ClaudeComplianceApi]] — the API enabling AI security governance for Claude
- [[ClaudeEnterprise]] — the enterprise plan these governance controls primarily serve
- [[summary-2026-05-21 - Claude now works with more security and compliance tools]] — source announcement
- [[ClaudeSecurity]] — related enterprise security product
- [[summary-2026-03-30 - Audit Claude Platform activity with the Compliance API]] — earlier platform expansion of compliance capabilities
