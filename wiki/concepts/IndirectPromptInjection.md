---
title: "IndirectPromptInjection"
type: concept
tags: [security, llm, vulnerability, ai-safety, injection]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

Indirect prompt injection is an attack vector where malicious instructions are placed in external content (web pages, emails, URLs, databases) rather than being directly provided by the user. The instructions lie in wait for an LLM to fetch and process them, exploiting the lack of native separation between trusted system instructions and untrusted external data.

## Key Information

- Attackers place malicious instructions in publicly accessible content: HTML, URLs, emails, or any system the LLM interacts with
- Proof-of-concept: Researchers edited a Wikipedia page about Albert Einstein to include a prompt instructing the LLM to search for a code that linked to an attacker's website containing malware
- Real-world case (March 2026): Websites embedding prompts specifically crafted to manipulate AI advertising review systems into approving non-compliant content — the first documented case of AI-based decision-making being overruled by the data it evaluates
- Root cause: LLMs have no native mechanism to distinguish between trusted developer instructions and untrusted external data
- This attack vector is particularly dangerous in agentic systems that autonomously browse the web and interact with external content

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[PromptInjection]] — related direct injection attack vector
- [[Guardrails]] — defensive mechanism against this attack
- [[AgenticAttackVector]] — related attack class in agentic systems
