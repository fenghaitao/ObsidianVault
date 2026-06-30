---
title: "RAG"
type: concept
tags: [retrieval, llm, embeddings, vector-databases]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
RAG (Retrieval-Augmented Generation) is a technique where relevant documents are retrieved from a database (typically a vector database) and fed into an LLM's context window to answer queries. It is the dominant production approach for company-internal question answering but has fundamental limitations in reasoning across documents.

## Key Information
- Powered by vector databases storing embeddings of documents
- Extremely easy to use — as few as 5 lines of code to implement basic retrieval
- Fundamental limitations include: inability to capture latent relationships between documents, questions that require implied (not explicit) reasoning, and combinatorial relationships that exceed fixed-dimensional vector capacity
- Embedding inversion research shows vector databases provide no security benefit over plain text
- Standard embeddings are not adaptive — they represent one universal semantic space, causing related but distinct documents to cluster together
- Jack Morris argues RAG is "the file system of today" but will be superseded by weight-based approaches
- Agentic search (deep research) is a more powerful variant that makes multiple queries and reasons across results, but is expensive at inference time
- The trade-off: RAG is cheap but limited; better approaches cost more at either training time or inference time
- In the 2024 AI Engineer Summit keynote, RAG was referenced in Jason Lou's satirical advice: "If your RAG app doesn't work, try a vector database — a different vector database. If the methodology doesn't work, implement a new paper." The point was that tool-churning (trying new vector databases, embedding models, papers) is not a substitute for developing evaluation processes and expertise.
- Antje Barth identifies RAG as one of three main model customization techniques alongside prompt engineering and fine-tuning
- Amazon Bedrock integrates RAG workflows for model customization
- **Demand-Driven Context**: RAG is part of the industry's push strategy for providing institutional knowledge to agents. Raj notes that RAG can achieve 40% factual accuracy with documented knowledge bases, but this is insufficient because the underlying knowledge is a monolith (20% outdated, 20% unreliable, 10% duplicated, 40% tribal). The retrieval layer alone cannot fix knowledge quality.

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source (RAG as model customization technique)
- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source (evolution from fixed RAG to agentic RAG)
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[VectorDatabases]] — underlying technology
- [[EmbeddingInversion]] — security vulnerability
- [[ContextualEmbeddings]] — improvement on standard embeddings
- [[ContextBroad]] — limitation of context-based approaches
- [[NeuralFileSystem]] — proposed successor
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source (tool-churning critique)
- [[JasonLou]] — delivered the tool-churning critique
- [[Model Customization]] — broader category
- [[Prompt Engineering]] — alternative customization technique
- [[Fine-tuning]] — alternative customization technique
- [[Agentic RAG]] — the evolution replacing fixed pipelines with agent-controlled retrieval
- [[Demand-Driven Context]] — alternative pull-based approach
- [[Knowledge Base Monolith]] — the deeper problem RAG doesn't solve
