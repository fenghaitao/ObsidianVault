---
title: "Magic Link Authentication"
type: concept
tags: [authentication, ux, mobile, slack]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/44 - Mental models for building products people love ft. Stewart Butterfield.md"]
last_updated: 2026-07-10
---

## Definition

Magic link authentication is a passwordless login method where users enter their email address and receive a link that automatically authenticates them. Slack was one of the first companies to scale this approach for mobile apps.

## Key Information

- **Origin**: someone on the Slack team (possibly Andrew or Ben Brown) proposed: "Why ask for email and password if email ownership was what allowed account creation? Why not just send them a link?"
- **Problem it solved**: typing passwords on phones with good password hygiene (capital H, lowercase q, 6, correct, period) is a terrible experience
- **Implementation**: user enters email address, receives a link, link automatically opens the app and authenticates
- Butterfield had seen the idea in a blog post before, but Slack was the first to really scale it and make it a standard
- This was an example of Slack investing in craft and reducing friction in the right places (authentication, where user intent is high)

## Related

- [[summary-44 - Mental models for building products people love ft. Stewart Butterfield]] — source summary
- [[Slack]] — early adopter
- [[Friction vs. Comprehension]] — related concept
