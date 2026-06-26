---
title: "AgentReviewerApprover"
type: concept
tags: [ai, agents, quality-assurance, workflow, paperclip]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md"]
last_updated: 2026-06-26
---

## Definition
Agent reviewer/approver is a workflow pattern in Paperclip where tasks can require a QA reviewer agent to verify work and a manager approver to sign off before completion. This creates a quality gate between agent execution and task completion, addressing the common problem of agents skipping verification steps.

## Key Information
- Paperclip feature: tasks can be configured to require a reviewer and/or an approver
- **Reviewer (QA)**: An agent (often with the agent browser skill) that verifies the work — e.g., testing in a browser, checking outputs — and iterates with the coder until quality is sufficient
- **Approver (Manager)**: A higher-level agent (or human) that signs off that the combined work of coder and reviewer meets organizational standards and brand requirements
- Addresses a common agent failure mode: coding agents often skip testing/verification when asked to do it themselves
- Different from hooks in individual coding tools (Claude, Codex) which work differently in each tool — Paperclip provides a vendor-neutral harness
- Creates a higher degree of reliability that agents actually complete work as instructed
- Example: coder completes task → QA agent reviews with browser testing → iterations between coder and reviewer → manager approves final result

## Related
- [[Paperclip]] — the orchestrator implementing reviewer/approver gates
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source transcript
- [[AgentOrgChart]] — reviewer/approver roles fit within the org hierarchy
- [[HumanInTheLoopWorkflows]] — related human-in-the-loop pattern
- [[AgenticWorkflows]] — broader workflow automation context
- [[Skills]] — agent browser skill used by QA reviewers
