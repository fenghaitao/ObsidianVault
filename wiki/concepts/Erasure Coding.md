---
title: "Erasure Coding"
type: concept
tags: [storage, durability, encoding, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Erasure coding is a technique for storing data as encoded fragments spread across locations, so the original can be reconstructed from a subset of fragments — the mechanism behind Dropbox's ~24-nines durability.
## Key Information
- Combines several blocks via an encoding scheme and spreads them across racks, rows (different power feeds), drive generations, and manufacturers to avoid correlated failures.
- Dropbox developed a custom encoding matrix called a Vandermonde matrix, plugging in variables like disk cost and network bandwidth cost (re-replication cost) to pick the optimal scheme.
- Example: reconstruct a file by reading any 6 of 9 fragments — ask all 9 and return as soon as the first 6 arrive, which is actually faster than non-replicated reads.
- Can scale to e.g. ~27 fragments, stored efficiently (not 27x data), plus a local low-latency copy near the user's home region.
- Trade-off embedded in the scheme: store more copies, or store fewer and re-replicate fast when a disk fails (which costs network bandwidth).
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — the company that uses it
- [[Magic Pocket]] — the storage system
- [[Multi-Homing]] — the complementary replication strategy
