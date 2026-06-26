---
title: "Pydantic"
type: entity
tags: [tool, python, library, structured-outputs, data-validation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Pydantic is a Python library for data validation and settings management using type annotations. In the context of the workshop, it was used to define structured output objects for the evaluator-optimizer pattern, where the reviewer outputs a list of Pydantic objects with profile, location, and comment attributes for each review finding.

## Key Information
- Python library for data validation via type annotations
- Used in the writing workflow's evaluator-optimizer pattern for structured reviewer feedback
- Pydantic objects have a field description property that serves as prompt engineering — explaining to the LLM what each attribute should contain
- The review model uses attributes: profile (which profile was violated), location (where in the post), and comment (what the issue is)
- Structured outputs via Pydantic were found to be more performant than free-form LLM responses for reviewer feedback
- Enables the editor to understand exactly what was violated and where, enabling precise fixes

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[Structured Outputs]] — concept enabled by Pydantic
- [[Evaluator-Optimizer Pattern]] — pattern using Pydantic for reviewer output
- [[Paul Iusztin]] — presenter who used Pydantic in the workflow
