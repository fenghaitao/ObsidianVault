---
title: "OpenKnowledgeFormat"
type: entity
tags: [standard, google, knowledge-base, karpathy-llm-wiki, mcp]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE.md"
last_updated: 2026-07-06
---

## Definition

The Open Knowledge Format (OKF) is a standard released by [[Google]] for building and sharing personal/team knowledge bases, built on top of [[AndrejKarpathy]]'s [[KarpathyLLMWiki]] pattern. It standardizes how knowledge-base documents are organized (nested indexes, "bundles") and which YAML metadata fields exist (`type` required; `tags`, `related`, etc. optional), so that a knowledge base built by one person's agent can be read and navigated by anyone else's agent.

## Key Information

- **Origin**: published as a `spec.md` file, in the same spirit as Karpathy's original gist — copy the spec into a coding agent and it can build (or refactor) a knowledge base to the standard, including using sub-agents to refactor large existing wikis section by section.
- **Two things it standardizes**: (1) organization — nested indexes (a top-level index pointing at section indexes pointing at documents) and "bundles" (packaged, shareable sets of related documents); (2) metadata — `type` is the only required frontmatter field; everything else is optional but recommended.
- **Analogy** (per [[ColeMedin]]): "what [[ModelContextProtocol|MCP]] did for agent-to-tool communication, OKF is doing for agent-to-knowledge-base communication."
- **Bundles as a distribution mechanism**: Cole publishes an example OKF bundle of his own best AI-coding videos plus extracted concept pages on GitHub; anyone can hand the spec + bundle link to their coding agent and immediately query the content without re-ingesting source transcripts.
- **Critique Cole partly agrees with**: OKF is "minimally opinionated" — it doesn't add much beyond Karpathy's original pattern. He frames that thinness as the point: a low-friction standard that's easy to interoperate on beats a heavyweight one, even if OKF itself isn't the final standard the industry converges on.

## Related

- [[KarpathyLLMWiki]] — the pattern OKF formalizes into a shareable standard
- [[ModelContextProtocol]] — the analogous standard for tool use
- [[SecondBrain]] — personal-knowledge-base use case OKF targets
- [[Google]] — publisher
- [[AndrejKarpathy]] — original pattern author
- [[ColeMedin]] — analyst; publishes an example OKF bundle
- [[summary-20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE]] — primary source
