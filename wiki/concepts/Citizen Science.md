---
title: "Citizen Science"
type: concept
tags: [ai, community, experimentation, research]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Citizen science in the AI context refers to the phenomenon of community members independently running experiments with local AI hardware and models, enabled by increasingly capable AI tools. While democratizing research, it also generates significant noise and potentially misleading results.

## Key Information
- Enabled by capable AI tools that let individuals quickly experiment and try things
- Primary information sources are Reddit and Twitter, where everyone reports different findings
- Problem: LLMs can tell experimenters "you've made a breakthrough" when the result is not actually meaningful
- Example of misleading results: heavily quantized models (1-bit) that appear to run large models on consumer hardware but are functionally useless
- Example: "I ran Kimmy on a MacBook" — but it's a 1-bit version with pruned experts, not practically usable
- EXO Labs aims to bring transparency by publishing rigorous, reproducible benchmarks across hardware, models, and configurations
- Alex Cheema argues citizen science needs the scientific method: well-reasoned hypotheses, controlled experiments, and iteration — not just throwing auto-research at problems

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[EXO Labs]] — aims to bring rigor to this space
- [[Quantization]] — frequently misused technique in citizen science
- [[Model Pruning]] — another technique subject to misleading claims
- [[Simon Woods]] — example of citizen science with auto-research
