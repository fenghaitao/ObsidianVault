---
title: "CatastrophicForgetting"
type: concept
tags: [fine-tuning, training, llm, machine-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Catastrophic forgetting is the phenomenon where fine-tuning a model on new data causes it to lose previously learned knowledge. In the context of LLMs, full fine-tuning on domain-specific data can overwrite general capabilities, causing the model to become "obsessed" with the new data and unable to generalize.

## Key Information
- Classic ML problem: train a model on handwritten digits, then on house numbers, and it can no longer recognize handwritten digits
- In LLMs, full fine-tuning on a single document (e.g., 3M financial report) causes the model to only produce exact copy sentences from that document
- The model can perfectly memorize the new data (zero loss) but becomes useless for any task requiring generalization
- No one has fully solved catastrophic forgetting despite extensive theory and proposed approaches
- Parameter-efficient methods (LoRA, prefix tuning, memory layers) mitigate forgetting by updating only a tiny fraction of parameters
- Memory layers show the best results: they "basically don't forget at all" while learning close to as much as full fine-tuning
- LoRA "learns less and forgets less" compared to full fine-tuning — a deliberate trade-off

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[ParameterEfficientFineTuning]] — mitigation approach
- [[MemoryLayers]] — best-performing mitigation
- [[LoRA]] — popular mitigation
- [[SyntheticContinuedPreTraining]] — complementary technique
