---
title: "Discotech"
type: entity
tags: [project, storage, disks, Dropbox, Rust]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Discotech ("disk technology project") was the Dropbox effort that removed the filesystem layer from storage nodes and directly addressed the disk heads using new shingled-magnetic-recording drives and the ZBC instruction set.
## Key Information
- Coincided with the rewrite of Magic Pocket's storage nodes from Go to Rust (both before those languages were generally available).
- Operated off draft specifications of new disks provided directly by the disk manufacturers.
- Aimed to control disks directly to maximize storage efficiency and reliability, contributing to the goal of making the cost pie chart almost entirely disks.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — the company it was built for
- [[Magic Pocket]] — the storage system it supported
- [[Rust]] — language used for the storage nodes
