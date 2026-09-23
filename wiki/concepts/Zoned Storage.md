---
title: "Zoned Storage"
type: concept
tags: [storage, disks, hardware, interfaces]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-23
---

## Definition

Zoned storage is a disk interface model that exposes drives as sequential zones rather than random-addressable blocks — exemplified by ZBC (zone-based block control), the instruction set Dropbox used to directly address its shingled magnetic recording disks from Magic Pocket storage nodes.

## Key Information

- James Cowling glosses the instruction set as "ZBC, zone based block control, something like that" — an interface for accessing the new SMR disks.
- Dropbox operated off draft specifications of these disks and directly controlled them (removing the filesystem layer entirely) rather than waiting for general availability.
- Using zoned storage directly was part of the Discotech ("disk technology project") effort that shifted Magic Pocket's cost toward almost all disks.

## Related

- [[Shingled Magnetic Recording]] — the disk technology zoned interfaces target
- [[Discotech]] — the Dropbox disk project
- [[Magic Pocket]] — the storage system using it
- [[Dropbox]] — the company that adopted it at scale
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
