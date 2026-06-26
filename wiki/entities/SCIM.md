---
title: "SCIM"
type: entity
category: standard
---

# SCIM

## Definition

SCIM (System for Cross-domain Identity Management) is a standard protocol for automating user identity lifecycle management across applications. It enables IT teams to provision and deprovision user access, including revoking access tokens when employees leave.

## Key Information

- **Access Revocation**: SCIM allows full revocation of user access across applications, but many companies do not use it, leaving standing access tokens active for days, weeks, or months after an employee departs
- **MCP Gap**: MCP's OAuth model issues access tokens and refresh tokens independently of SCIM — even if SCIM is used, MCP server credentials may persist
- **XAA Improvement**: Cross-App Access with short-lived tokens (~5 minutes) reduces the dependency on SCIM for timely access revocation

## Related

- [[CrossAppAccess]]
- [[IDJAG]]
- [[Okta]]
- [[MCP]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
