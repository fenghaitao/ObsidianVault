---
title: "OpenTelemetry"
type: concept
tags: [observability, telemetry, siem, enterprise, monitoring]
sources: [raw/01-articles/claude/2026-04-09 - Making Claude Cowork ready for enterprise.md]
last_updated: 2026-07-04
---

## Definition

OpenTelemetry (OTel) is an open observability standard that [[ClaudeCowork|Claude Cowork]] and other Claude products emit events through, allowing enterprises to pipe agent activity into standard monitoring and SIEM tooling.

## Key Information

- **April 2026 expansion (Cowork):** Cowork emits OTel events for tool and connector calls, files read or modified, skills used, and whether each AI-initiated action was approved manually or automatically.
- Compatible with standard SIEM pipelines such as Splunk and Cribl.
- A shared user account identifier lets organizations correlate OTel events with [[ComplianceAPI]] records for unified auditing.
- Available on Team and Enterprise plans.
- Earlier context: OpenTelemetry support for usage/cost/tool-activity tracking was already part of Cowork's admin controls as of February 2026 (see [[ClaudeCowork]]); this announcement expands the event coverage and adds SIEM/Compliance API correlation.

## Related

- [[ClaudeCowork]] — product emitting the expanded OTel events
- [[ClaudeEnterprise]] — plan where OTel-based observability supports governance
- [[ComplianceAPI]] — correlated via shared user identifier
- [[ClaudeForExcelPowerPoint]] — Excel/PowerPoint/Word/Outlook add-ins also expose an OTel collector for admins
- [[summary-2026-04-09 - Making Claude Cowork ready for enterprise]] — source announcement
- [[summary-2026-05-07 - Collaborate with Claude across Excel, PowerPoint, Word and Outlook]] — OTel collector config for the Office add-ins
