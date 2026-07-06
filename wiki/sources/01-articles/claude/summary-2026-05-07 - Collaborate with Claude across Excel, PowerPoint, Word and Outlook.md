---
title: "summary-2026-05-07 - Collaborate with Claude across Excel, PowerPoint, Word and Outlook"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-05-07 - Collaborate with Claude across Excel, PowerPoint, Word and Outlook.md"]
last_updated: 2026-07-04
---

## Core Summary

On May 7, 2026, Anthropic announced that [[ClaudeForExcelPowerPoint|Claude for Excel, PowerPoint, and Word]] reached general availability, and that Claude for Outlook entered public beta for all paid plans. The headline capability is a single conversation that carries full context across all four Microsoft apps: a user can triage an email in Outlook, open its attachment in Word to draft a memo from a team template, build supporting analysis in Excel, and turn it into a PowerPoint deck — without re-explaining the task at each step. Claude works across files kept open side by side, so an assumption changed in Excel propagates automatically to a linked PowerPoint chart and a Word memo figure. Conversations persist per-file, so a sidebar session can be closed and resumed later (including via voice). Claude for Outlook specifically triages the inbox (sorting by needs-response / draftable / noise), drafts replies directly into Outlook's compose pane (recipients, subject, body pre-filled), and creates calendar invites that check attendee availability and open in Outlook's native event form — with the user reviewing and clicking send on every reply/invite before anything goes out. On the enterprise/admin side, Excel/PowerPoint/Word now ship under one Microsoft AppSource listing with a separate AppSource listing for Outlook (beta), both deployable from the Microsoft admin center; admins can wire up an [[OpenTelemetry]] collector to stream prompts, tool calls, and document references, and use the [[ComplianceAPI]] to break out activity per user/app/day. Organizations can use a Claude account directly or route traffic through an existing LLM gateway to Claude models on [[AmazonBedrock]], Google Cloud's Vertex AI, or Microsoft Foundry. Separately, Microsoft 365 Copilot customers can choose Claude models directly inside Excel and PowerPoint's Copilot agent mode.

## Key Points

- Claude for Excel, PowerPoint, and Word: general availability as of May 7, 2026.
- Claude for Outlook: public beta as of May 7, 2026, available on all paid plans.
- Single persistent conversation carries context across all four apps (Excel, PowerPoint, Word, Outlook) simultaneously, not just pairwise (prior Excel/PowerPoint cross-context was announced March 2026; this extends it to four apps).
- Cross-file live propagation: changing an assumption in Excel updates a linked PowerPoint chart and a Word memo number automatically, as long as the files are open side by side.
- Conversations persist per file — sidebar can be closed and reopened (next day) and resumed via keyboard or voice.
- Claude for Outlook features: inbox triage (sorts by needs-response / draftable / noise), drafts replies pre-filled with recipients/subject/body into Outlook's native compose pane, calendar invites that check attendee availability and open in Outlook's native event form.
- Human-in-the-loop guardrail: every reply and calendar invite requires user review; nothing sends automatically.
- Cross-app awareness example: opening an email attachment in Word or Excel, Claude already knows what the original sender asked for (context carried from Outlook).
- Admin/deployment: one Microsoft AppSource listing covers Excel + PowerPoint + Word; a separate AppSource listing adds Outlook (beta). Both deployable from the Microsoft admin center.
- Enterprise observability: admins can configure an [[OpenTelemetry]] collector to stream prompts, tool calls, and document references for security review; the [[ComplianceAPI]] (referred to here as "Analytics API") breaks out activity per user, per app, per day.
- Deployment flexibility: organizations can use a Claude account directly, or route through an existing LLM gateway to Claude models hosted on [[AmazonBedrock]], Google Cloud's Vertex AI, or Microsoft Foundry.
- Microsoft 365 Copilot customers can select Claude AI models directly within Excel and PowerPoint's agent mode (a separate integration path from the standalone Claude add-ins), per Microsoft support documentation linked in the article.
- Availability: all Mac and Windows users on paid Claude plans can access Claude for Microsoft 365; Claude for Outlook is in beta on all paid plans; admins deploy via Microsoft AppSource through the Microsoft admin center.
- Anomaly: the raw article text repeats the subheading "One conversation that carries context across all four apps" twice in immediate succession — appears to be a scraping/formatting artifact from the source page rather than injected instruction text. No prompt-injection-style content (e.g., embedded directives addressed to an AI reader) was found in this article.
- The article links to Microsoft support docs on choosing Claude models in Copilot's Excel and PowerPoint agent modes, and to Anthropic support docs on configuring an OpenTelemetry collector and on the Compliance/Analytics API reference guide.

## Related

- [[ClaudeForExcelPowerPoint]] — primary product page this article extends to GA plus Word and Outlook (beta)
- [[Microsoft365Copilot]] — separate integration path where Copilot customers pick Claude models in Excel/PowerPoint agent mode
- [[Microsoft]] — platform vendor (Excel, PowerPoint, Word, Outlook, AppSource, admin center)
- [[OpenTelemetry]] — enterprise observability mechanism referenced for these add-ins
- [[ComplianceAPI]] — per-user/per-app/per-day activity breakdown referenced as "Analytics API"
- [[AmazonBedrock]] — cloud hosting option for Claude models behind an LLM gateway
- [[VertexAI]] — Google Cloud's Vertex AI, cloud hosting option for Claude models behind an LLM gateway
- [[ClaudeEnterprise]] — plan tier relevant to admin controls described
