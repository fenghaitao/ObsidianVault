---
title: "Portal (Meta)"
type: entity
tags: [product, hardware, Meta, video-calling]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey.md"]
last_updated: 2026-07-21
---

## Definition

Portal was a standalone hardware video calling device developed by Meta (Facebook). It ran a forked version of Android with approximately 30 custom Android apps. Rahul Pandey worked on Portal as an Android engineer, and his work on Portal's infrastructure migration and debug tooling led to his IC6 promotion.

## Key Information

- Originally called Building 8 before being branded as Portal
- Ran a custom forked version of Android with ~30 custom Android apps
- The build system was very different from standard Android or even core Facebook Android — used Buck
- Engineers would flash the device with their own OS, then deploy only the specific app they were working on (building all 30 apps would take 3-4 hours)
- Rahul worked on the calling app specifically
- The Portal team grew from an experimental project to hundreds of engineers
- Rahul met his future co-founder Alex while working on Portal in 2017
- Rahul's IC6 promotion was partly driven by a Portal debug tool that saved hundreds of engineering hours every month
- The other major project was migrating Portal's video calling infrastructure back to the shared Messenger RTC infrastructure

## Related

- [[summary-20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey]] — source summary
- [[Meta]] — the company that built Portal
- [[Rahul]] — engineer who worked on Portal
- [[Building 8]] — the original name for the Portal division
- [[Alex]] — Rahul's co-founder, met on the Portal team
- [[Messenger]] — the infrastructure Portal migrated back to
- [[RTC]] — the video calling infrastructure team at Messenger
- [[Android]] — the operating system Portal ran on
- [[Buck]] — the build system used for Portal
