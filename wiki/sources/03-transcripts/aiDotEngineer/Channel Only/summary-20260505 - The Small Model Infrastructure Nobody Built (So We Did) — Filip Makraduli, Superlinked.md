---
title: "The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked.md"
date: 2026-05-05
tags: [small-models, inference, infrastructure, open-source, model-hot-swapping, gpu-utilization, vector-databases, ai-search, document-processing]
---

## Core Thesis

Small model inference for AI search and document processing requires a fundamentally different infrastructure approach than large model inference. Small models (embeddings, rerankers, NER) occupy only a few gigabytes of memory each, so provisioning a dedicated GPU per model wastes idle capacity. The solution combines two pillars — broad model support with architecture-aware forward pass re-implementation, and production-grade infrastructure with routing, auto-scaling, and hot-swapping — into an end-to-end open-source inference engine (Sie).

## Key Points

- **Why small model inference matters for agents**: Context rot degrades agent quality as context increases. Small models preprocess data (NER, embeddings, reranking) to manage context before it reaches the agent, and can also serve as tools for taxonomy classification and retrieval.
- **Community validation**: Andrej Karpathy builds knowledge graphs using NER models; Chroma ships its own preprocessing model; the community is building solutions to reduce token counts for agents.
- **What inference is NOT**: It's not just "add more GPUs." Small models waste GPU capacity if each gets its own GPU. It's also not just a server — production requires routing, auto-scaling, queuing, Prometheus metrics, and Grafana monitoring, which currently has no open-source end-to-end solution.
- **Model hot-swapping**: Sie enables multiple small models to share one GPU via hot-swapping with an LRU eviction policy, dramatically improving GPU utilization and lowering costs.
- **The Yin (model support)**: Supporting hundreds of models requires re-implementing the forward pass to handle architectural differences — LayerNorm variants (BERT vs Qwen), positional embeddings (absolute vs RoPE), QKV fusion (possible in some models, not in GQA models), and output types (vectors for embeddings, scores for rerankers, multiple vectors for ColBERT).
- **Variable-length flash attention**: Token-based batching with variable-length attention avoids wasting compute on padding tokens, a key differentiator for efficiency.
- **The Yang (infrastructure)**: Three API primitives (encode, score, extract) backed by a router, queuing mechanism, GPU pools with spot instances, and KEDA auto-scaling with Prometheus metrics. Models are config-driven with Terraform, Helm charts, and Docker images.
- **Production use case**: Taxonomy classification for an e-commerce store using small models as tool-calling components.
- **Background visual**: The slide background was a vector visualization of sinusoidal positional encodings used in transformer training.

## Entities

- [[FilipMakraduli]] — AI researcher/engineer at Superlinked, presenter
- [[Superlinked]] — company behind the Sie inference engine
- [[Sie]] — Superlinked Inference Engine, open-source small model inference platform
- [[Chroma]] — vector database partner that tested Sie
- [[Qdrant]] — vector database partner that tested Sie
- [[Weaviate]] — vector database partner that tested Sie
- [[LanceDB]] — vector database partner that tested Sie
- [[Stella]] — embedding model used as an example of small model
- [[Glyner]] — named entity recognition model used as an example
- [[ColBERT]] — late interaction model with multiple vector outputs
- [[BERT]] — model architecture with different LayerNorm and positional embeddings
- [[Qwen]] — model architecture with RoPE and GQA
- [[ModernBERT]] — advanced BERT variant with different architecture
- [[Gemma]] — Google's small model family with high ELO scores at low parameters
- [[AndrejKarpathy]] — referenced for building knowledge graphs with NER models
- [[HuggingFace]] — platform hosting millions of open-source models
- [[KEDA]] — Kubernetes Event-Driven Autoscaling used for auto-scaling
- [[Prometheus]] — metrics system used for auto-scaling triggers
- [[Grafana]] — monitoring dashboard
- [[Terraform]] — infrastructure-as-code for model configuration
- [[Helm]] — Kubernetes package manager for deployment
- [[Docker]] — containerization for model images

## Concepts

- [[Small Model Inference]] — inference optimized for models occupying only a few GB of memory
- [[Model Hot-Swapping]] — sharing one GPU across multiple small models with rapid switching
- [[GPU Utilization for Small Models]] — avoiding idle GPU capacity when models are small
- [[LRU Eviction Policy]] — least recently used policy for managing model cache on GPU
- [[Yin and Yang of Model Inference]] — combining model support (yin) with infrastructure (yang)
- [[Model Forward Pass Re-implementation]] — adapting attention, padding, and QKV fusion for diverse architectures
- [[Variable Length Flash Attention]] — flash attention that avoids padding waste in token-based batching
- [[Token-Based Batching]] — batching requests with variable token counts without padding to max
- [[Named Entity Recognition]] — using NER models to generate ontologies and knowledge graphs
- [[Knowledge Graphs]] — graph-based knowledge representation built from NER model outputs
- [[Cross Encoders]] — models that output scores rather than vectors
- [[Late Interaction Models]] — models like ColBERT that output multiple vectors
- [[KEDA Auto-Scaling]] — Kubernetes event-driven autoscaling for inference workloads
- [[AI Search and Document Processing]] — the primary use case for small model inference
- [[Encode Score Extract API]] — the three API primitives of Sie (encode vectors, score pairs, extract entities)
- [[Routing and Auto-Scaling for Inference]] — production infrastructure for model serving
- [[Embedding Models]] — models that produce vector representations of text
- [[Reranker Models]] — models that score relevance of document-query pairs
- [[Positional Encodings]] — sinusoidal encodings used in transformers, visualized in the talk background

## Related

- [[Context Rot]] — the problem small model preprocessing helps solve
- [[Context Management]] — managing context to combat context rot
- [[ToolCalling]] — using small models as tools in agentic workflows
- [[FlashAttention]] — optimized attention kernel that Sie re-implements for variable-length support
- [[GroupedQueryAttention]] — attention variant in Qwen that prevents QKV fusion
- [[VectorDatabases]] — partners testing Sie (Chroma, Qdrant, Weaviate, LanceDB)
- [[AgenticWorkflows]] — the downstream use case for small model preprocessing
- [[Taxonomy Classification]] — production use case for Sie tool calling
