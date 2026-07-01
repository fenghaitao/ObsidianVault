---
title: "Guardrails"
type: concept
tags: [safety, production, monitoring, llm, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---
## Definition
Guardrails are automated checks deployed in production to catch and prevent defects in LLM outputs. They function as table-stakes quality controls covering toxicity, personally identifiable information (PII), copyright, expected language, and hallucinations, and are essential because the cost to catch and fix defects is orders of magnitude larger than the cost to produce them.

## Key Information
- Presented in the tactical section of the 2024 AI Engineer Summit keynote by Eugene Yan
- Invokes Brandolini's Law: the energy needed to catch and fix defects is an order of magnitude larger than the energy needed to produce them
- Table-stakes guardrails: toxicity detection, PII detection, copyright violation detection, expected language enforcement
- Hallucination guardrails: check whether generated output contains information not present in the source document (entailment vs. contradiction)
- Reference-free evals can be repurposed as guardrails — if you build a hallucination eval that checks entailment against source documents, it can guard all new outputs
- Context matters: even basic checks like expected language can fail in surprising ways (e.g., ads posted in non-English languages on English-language websites)
- Guardrails run either asynchronously or in the critical path, and need ongoing maintenance to stay aligned with evolving quality definitions

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[EugeneYan]] — presented guardrails in the keynote
- [[BrandoliniLaw]] — the asymmetry principle that motivates guardrails
- [[ReferenceFreeEvals]] — technique that can double as guardrails
- [[LLMAsJudge]] — can serve as a guardrail mechanism
- [[EvalEngineering]] — broader practice guardrails are part of

- **Encoder-based guardrails**: Fine-tuned ModernBERT can classify prompts as safe/unsafe in 35ms at ~85% accuracy, providing a low-latency, self-hosted alternative to LLM-as-judge
- **Defense-in-depth**: Multiple safety checkpoints should be placed throughout the LLM application pipeline — user inputs, model responses, RAG context, MCP calls, and agentic plans
- **Implementation options**: Rule filtering, canary tokens, encoder discriminators, constrained decoding, and LLM-as-judge (in order of increasing latency)
- **Agent scope limitation**: Guardrails can increase trust in agents by limiting what they can do — restricting file access, directory reads, and website searches. Claude Code's trust spectrum ranges from asking permission for every action (low trust) to YOLO mode (high trust).
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source (guardrails as a trust-increasing strategy)
- [[AgentHuman Collaboration]] — guardrails increase trust by limiting agent scope
- [[VerifiersRule]] — guardrails help bring tasks down the verifiability spectrum