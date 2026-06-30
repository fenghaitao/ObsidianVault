---
title: "Shallow Modules"
type: concept
tags: [software-design, architecture, anti-pattern, code-quality, ai-coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Shallow modules are a software design anti-pattern from John Ousterhout's "A Philosophy of Software Design." A shallow module has little functionality but exposes a complex interface — it creates overhead without providing meaningful abstraction.

## Key Information
- From John Ousterhout's "A Philosophy of Software Design"
- Shallow modules: not much functionality, complex interface — lots of surface area with little value
- In a codebase, shallow modules look like many tiny blobs that the AI has to walk through and navigate
- AI is really good at creating shallow module codebases — it tends to produce many small, poorly organized modules
- Shallow module codebases cause AI to fail at understanding code: it attempts to explore but can't reach the right module in time or understand all dependencies
- Contrast with deep modules: lots of functionality behind a simple interface
- Matt Pocock's "Improve Codebase Architecture" skill identifies and restructures shallow modules into deep modules
- Shallow modules make codebases hard to test because boundaries are unclear and interfaces are complex

## Related
- [[summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock]] — source transcript
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[JohnOusterhout]] — author of A Philosophy of Software Design
- [[Deep Modules]] — the contrasting concept
- [[Software Entropy]] — shallow modules are a symptom of entropy
- [[MattPocock]] — speaker who identified this as an AI-generated anti-pattern
