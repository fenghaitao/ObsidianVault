---
title: "Software Entropy"
type: concept
tags: [software-design, software-engineering, code-quality, ai-coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md"]
last_updated: 2026-06-26
---

## Definition
Software entropy is the tendency of software systems to degrade over time as changes are made. From The Pragmatic Programmer, it describes how each change made without considering the overall design of the system causes the codebase to get progressively worse, trending toward disorder and collapse.

## Key Information
- From The Pragmatic Programmer by Andrew Hunt and David Thomas
- Describes how most software systems behave: every change made without design consideration degrades the codebase
- Matt Pocock observed this directly when using specs-to-code: running the AI "compiler" repeatedly produced progressively worse code
- Each iteration of specs-to-code made the code worse because each change was made in isolation without considering overall system design
- The antidote is investing in system design every day (Kent Beck's principle)
- AI accelerates entropy because it can produce changes faster than humans can review design implications
- Good codebases resist entropy because they are structured to accommodate change without degradation

## Related
- [[summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock]] — source transcript
- [[SpecsToCode]] — the approach that demonstrates entropy
- [[Deep Modules]] — architectural pattern that resists entropy
- [[AgentEntropy]] — related concept in agent systems
- [[CodeSlop]] — the result of unchecked entropy
- [[Design the Interface, Delegate the Implementation]] — strategy to manage entropy
