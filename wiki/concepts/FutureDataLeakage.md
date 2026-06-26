---
title: "FutureDataLeakage"
type: concept
tags: [research, methodology, training, data-quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Future data leakage is a pervasive research integrity problem where models are inadvertently or carelessly given access to future data during training, artificially inflating accuracy metrics to suspiciously high levels (98-100%) and invalidating research conclusions.

## Key Information
- **Detecting leakage**: Accuracy of 98% or 100% is a red flag — such near-perfect performance is highly suspicious and most often indicates future data contamination
- **Mechanism**: In transformer decoders that predict next tokens from previous tokens, including future tokens in the training context allows the model to "cheat" by seeing the answer
- **Primary responsibility**: Daniel Han argues the lead researcher is responsible for catching these issues — a 98% accuracy result should trigger immediate skepticism and investigation
- **Paper vs. code**: The leak can originate either in the research paper's methodology design or in the code implementation where the programmer misinterprets the methodology
- **Prevalence**: Described as a "very serious problem" that appears frequently across research papers in the field
- **Review importance**: Always check the methodology section of research papers for whether future data could have been included in training

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[LLMImplementationAnalysis]] — broader methodology for catching research issues
