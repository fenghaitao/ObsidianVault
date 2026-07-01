---
title: "Quadratic Attention"
type: concept
tags: [attention, transformers, complexity, scaling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Quadratic attention refers to the O(n²) computational and memory complexity of standard transformer self-attention, where every token in a sequence must compute pairwise interactions with every other token. This is one of the two fundamental bottlenecks in long-context training.

## Key Information
- **Complexity**: For a sequence of length n, the attention matrix (QK^T) has dimensions n × n, requiring O(n²) memory and computation
- **Impact at scale**: For a 3 million token sequence, a naive allocation would create a tensor with 3 million × 3 million entries, which is prohibitively large
- **Relationship to memory**: The query, key, and value (QKV) matrices create pairwise interactions that dominate memory usage in long-context scenarios
- **Mitigations**: [[Context Parallelism]], [[FlashAttention]] (processes attention in blocks to avoid materializing the full matrix), and [[Untitled Ulysses]] all address this bottleneck
- **Second bottleneck**: Even with quadratic attention addressed, linear memory growth from activations still poses a challenge requiring techniques like [[Activation Checkpointing]] and [[Activation Offloading]]

## Related
- [[Context Parallelism]] — technique to distribute attention computation
- [[FlashAttention]] — optimized kernel that avoids materializing the full attention matrix
- [[Long Context Training]] — application domain where quadratic attention is the primary bottleneck
- [[Untitled Ulysses]] — advanced context parallelism technique
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
