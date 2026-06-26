---
title: "SupplyChainAttack"
type: concept
tags: [security, open-source, dependency, attack-vector]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
last_updated: 2026-06-26
---

## Definition
A supply chain attack is a security exploit that targets a software project through its dependencies rather than its own code. Attackers compromise a package or library that the target project depends on, and the vulnerability propagates to all downstream consumers.

## Key Information
- OpenClaw was affected by an Axios vulnerability even though OpenClaw does not directly use Axios — Slack and MS Teams dependencies used Axios and didn't pin versions, so the vulnerability propagated through the dependency chain
- Ghost Claw was a nation-state supply chain attack (likely North Korea): attackers created a confusingly similar NPM package name, and users who downloaded from the wrong website got a rootkit
- This is "outside of our control" for project maintainers — "this happens for other people as well"
- Supply chain attacks are particularly dangerous in the open-source ecosystem because projects have deep dependency trees with transitive dependencies that are hard to audit
- Pinning dependency versions is a key mitigation, but not all downstream dependencies do it

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source
- [[OpenClaw]] — project affected by supply chain attacks
- [[Axios]] — library whose vulnerability propagated to OpenClaw
- [[Slack]] — dependency that used vulnerable Axios
- [[Microsoft]] — MS Teams dependency that used vulnerable Axios
