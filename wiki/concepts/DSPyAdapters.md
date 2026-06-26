---
title: "DSPyAdapters"
type: concept
tags: [dspy, prompt-format, llm, adapter]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
DSPy Adapters are prompt formatters that sit between signatures and LLM calls, translating declarative intent into the specific message format sent to the model. They enable format experimentation without changing program logic.

## Key Information
- Adapters convert signatures, inputs, and other attributes into a message format (JSON, BAML, XML, etc.) that the LLM receives.
- The default adapter uses JSON schema formatting, but alternatives like BAML can improve performance by 5-10%.
- Different models may perform better with different formats; adapters allow mixing and matching at will.
- Changing an adapter does not require any changes to the rest of the DSPy program.
- The BAML adapter produces more human-readable and token-efficient prompts compared to JSON schema dumps.
- Adapters are what make DSPy's declarative approach work: developers express intent, adapters handle the prompt construction.

## Related
- [[DSPy]] — framework using adapters
- [[DSPySignatures]] — what adapters translate into prompts
- [[BAML]] — a specific adapter format
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
