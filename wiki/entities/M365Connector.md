---
title: "M365Connector"
type: entity
tags: [connector, microsoft, enterprise, data-access, m365]
sources: ["raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-07-07
---

## Definition

The M365 Connector is an enterprise integration for [[ClaudeDesktop]] that gives Claude access to an organization's Microsoft 365 mail and documents through their own Microsoft Entra application. It supports tenant allowlisting, GCC High/DoD endpoints (beta), and a local connector mode for the strictest data residency requirements.

## Key Information

- Operates through the organization's own Entra app, not through Anthropic's infrastructure.
- Supports **tenant allowlisting** to control which organizations can connect.
- **Beta support for GCC High and DoD endpoints**, enabling government and defense customers.
- **Local connector mode:** For the strictest residency requirements, the connection stays entirely between the device and Microsoft — data never passes through Anthropic infrastructure.
- Part of Claude Desktop's enterprise deployment controls, enabling Claude to work with files and communications already in Microsoft 365.

## Related

- [[ClaudeDesktop]] — the desktop application the M365 connector integrates with
- [[MicrosoftFoundry]] — Microsoft's cloud platform also supporting Claude Desktop
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — source article
