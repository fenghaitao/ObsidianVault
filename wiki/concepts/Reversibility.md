---
type: concept
tags: [agents, design-pattern, UX, safety]
---

# Reversibility

## Definition

Reversibility is a design pattern for AI agents where users can reverse or undo the actions the agent has taken. By providing undo capabilities at multiple levels of granularity, the cost of mistakes is bounded, making the ROI calculation easier and encouraging users to take bolder risks with higher-value tasks.

## Key Information

- **Origin:** Identified by [[MarduSwanepoel]] ([[FlinnAI]]) in his aiDotEngineer talk "What the Best Agents Share" (2026-05-26).
- **Exemplars:**
  - **[[Cursor]]:** Offers reversibility at multiple granularities:
    - **Line-level:** Accept or reject individual changes.
    - **File-level:** Accept or reject all changes in a file.
    - **Conversation-state rollback:** Jump back to a specific point in the conversation, undoing all subsequent changes.
    - **Parallel outputs:** Run the same input through different models, accepting only the best result.
  - **[[Harvey]]:** Integrates with native Microsoft Word change tracking, allowing users to review and accept/reject changes as a reviewer or editor would.
- **Benefits:**
  - **Bounded mistake cost:** Knowing the worst-case outcome makes the ROI calculation easier.
  - **Bolder users:** Users are more prone to taking risks and tackling higher-value tasks.
  - **Experimentation:** Safe to try things out, knowing you can always undo.

## Related

- [[MarduSwanepoel]] — Speaker who identified this pattern.
- [[Cursor]] — Exemplar agent with multi-granularity reversibility.
- [[Harvey]] — Exemplar agent with native Word change tracking integration.
- [[FocusModes]] — Companion pattern: constraining action space per mode.
- [[TransparentExecution]] — Companion pattern: making agent actions visible.
- [[AgentPersonalization]] — Companion pattern: encoding user principles.
