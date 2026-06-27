---
title: "Audit Claude Platform activity with the Compliance API"
type: article
source: https://claude.com/blog/claude-platform-compliance-api
description: "The Compliance API gives admins programmatic access to audit logs across their Claude Platform organization."
author: "Anthropic"
published: 2026-03-30
last_modified: 2026-06-21
---

# Audit Claude Platform activity with the Compliance API

The Compliance API gives admins programmatic access to audit logs across their Claude Platform organization.

The Compliance API gives admins programmatic access to audit logs across their Claude Platform organization.

The Compliance API is now available on the Claude Platform, giving admins programmatic access to audit logs across their organization. Security and compliance teams can track user activity, monitor configuration changes, and integrate Claude usage data into their existing compliance infrastructure.

Organizations in regulated industries—like financial services, healthcare, legal—need detailed records of who accessed what, when, and what changed. Without programmatic access to this data, compliance teams need to rely on manual exports and periodic reviews, which don't scale.

The Compliance API provides an activity feed that logs security-relevant events across your organization. Admins can fetch activity logs filtered by time range, specific users, or API keys.

The API currently tracks two categories of activity:

Together, these cover user login and logout events, account setting updates, workspace changes, and other organizational audit events. The API does not log inference activities, such as user interactions with the model or model activities.

Contact your account team to enable the Compliance API for your organization. Once enabled, create an admin API key and use it to query the activity feed endpoint. Note that logging begins once the API is enabled—historical activities prior to that point aren't available.

Organizations that already use the Compliance API for Claude Enterprise can add their Claude API organization to the same parent organization and filter activity across both from a single feed.

Read the documentation on the[ Anthropic Trust Center](https://trust.anthropic.com/resources?s=tob70gqyan60x3dwb7nkap&name=anthropic-compliance-api) to learn more.

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.
