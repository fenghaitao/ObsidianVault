---
title: "Do Not Disturb (Slack)"
type: concept
tags: [feature, product-design, rollout, slack]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/44 - Mental models for building products people love ft. Stewart Butterfield.md"]
last_updated: 2026-07-10
---

## Definition

Do Not Disturb is a Slack feature that allows users to mute notifications during specified hours. Its rollout was a carefully orchestrated example of balancing competing stakeholder needs through a multi-layered override system.

## Key Information

- **Challenge**: Slack had millions of users across tens of thousands of organizations, including ops alerts for on-call engineers. A blunt rollout could cause serious problems
- **Elaborate rollout system**:
  1. All Slack administrators were notified weeks in advance
  2. A default was set (e.g., 8:00 p.m. to 8:00 a.m. in local time zone)
  3. Administrators could override the default
  4. Individual end users could override the admin default
  5. If admins changed the default again, it would override end user preferences
  6. End users could override again
- **Purpose of the layered system**: not to create war, but to allow policy changes while preserving individual customization
- **Critical insight**: if the default wasn't set, most people wouldn't turn it on at all
- The investment in this careful rollout was justified because it was a critical feature that, if done poorly, would have caused widespread complaints and conflict

## Related

- [[summary-44 - Mental models for building products people love ft. Stewart Butterfield]] — source summary
- [[Slack]] — product
- [[Friction vs. Comprehension]] — related concept
