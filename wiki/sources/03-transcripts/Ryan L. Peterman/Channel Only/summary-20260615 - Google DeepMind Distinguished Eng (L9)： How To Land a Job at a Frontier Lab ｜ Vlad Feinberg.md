---
title: "summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Core Summary
Vlad Feinberg, a Google DeepMind Distinguished Engineer (L9) and pre-training area lead, explains what it actually takes to land a job at a frontier lab: kernel and low-level engineering, programming-language abstractions, reinforcement learning, and the distributed-systems-meets-optimization overlap, all built on "mathematical maturity" and "research taste" for traversing the stochastic graph of research (Jacob Steinhardt's research-as-an-MDP framing). He walks through the research-vs-applied and software-vs-research spectra, scaling laws as the central pre-training question, and his team's three verticals — distillation, inference co-design, and quantization — before recounting the Flash 2.0 MoE war story and a Jeff Dean spot bonus for Bard. His practical advice: the strongest signal is tangible open-source work (vLLM, SGLang, TensorRT, NVIDIA Dynamo), and the best career strategy is to chase real problems people face and be the coworker others want to see succeed.
## Key Points
- Demand is "voracious" for kernel development and low-level engineering to accelerate LLM runtimes — efficient implementations, KV caching, and serving are classical back-end engineering applied at scale.
- Research vs applied is a spectrum, not a clean split: even making Gemini serve search results well requires hard research (grounded, citation-backed answers and assessing source quality).
- Software engineering vs AI research differ in the shape of the dependency DAG: software is deterministic and monotone, while research is stochastic and possibly a hidden MDP; navigating it is "research taste."
- A back-end engineer's first gap in research is the literature: building the skill to traverse citation trees, judge a paper's value before reading it fully, and absorb the prerequisites — "mathematical maturity."
- Scaling laws are the core pre-training question: predict the final test loss as you invest flops. The ImageNet problem becomes one-shot (practice on MNIST and CIFAR, then it must work on ImageNet the first time), grounded in the Kaplan paper, Chinchilla, GPT, and PaLM lines of work.
- Recommended domains beyond kernels: programming-language research (ThunderKittens, CuTe), reinforcement learning (RLHF and deep-RL methods like PPO), and the distributed-systems × optimization overlap for multi-GPU training (asynchrony, gradient staleness, pipelining).
- Vlad's pre-training team delivers the Flash and Flash-Lite models (AI Overviews, AI mode, ads, YouTube, and other 1P models), is the technical POC for the Google-Apple partnership, and runs three research verticals: distillation, inference co-design, and quantization.
- Quantization compresses FP32 weights toward 4-bit ints (and applies to activations); since ~99% of AI-hardware operating cost is power, lower-precision math directly cuts cost and latency.
- MFU (model FLOPS utilization) is not naively low: it divides useful flops by peak flops, and attention, activations, and HBM reads/writes mean you never hit 100% — inference co-design saturates every hardware unit jointly with quality.
- Flash 2.0 war story: moving to MoE hurt latency because sharding experts across chips forces per-layer token routing; pipeline prefill (a report's idea with Rahul Arya and Google's Israel team) moves layers instead of experts, breaking the HBM constraint and making MoE viable.
- The Flash 2.0 MoE bet was then validated through a ~40-day, five-person training rotation doing "SRE-style" work; the model landed atop the LMSYS Arena leaderboard just as DeepSeek V3 dominated a Wall Street Journal narrative.
- Signaling: contributions to vLLM or SGLang, or demos built on TensorRT or NVIDIA Dynamo, are "extremely positive" interview signals; so are the handwritten Scaling Book exercises plus a transformer-implementation video (invitation to interview, New York office).
- Internal transfer: Nate Lidzén moved from search to Vlad's team by becoming the person who effectively adopted and served LLMs inside his product area.
- Jeff Dean gave Vlad a spot bonus for a small SFT contribution to the first Bard launch; his manager Rohan Aneja pushed him to join instead of chasing NeurIPS/ICML/ICLR first-author papers.
- Career advice: chase problems people actually face (even the "menial" parts) and practice humility; and be the kind of coworker people want to see succeed — a lesson he credits to mentor Todd Lipkin.
## Related
- [[Vlad Feinberg]] — guest
- [[Google DeepMind]] — his employer
- [[Google Brain]] — his prior research org
- [[Gemini]] — the models his team works on
- [[Gemini Flash]] — his team's deliverable
- [[Bard]] — early project he contributed to
- [[Jeff Dean]] — gave him a spot bonus
- [[Distinguished Engineer]] — his L9 level
- [[Princeton University]] — where he lectured
- [[Ryan L. Peterman]] — host
- [[The Scaling Book]] — his hiring exercise
- [[Jacob Steinhardt]] — "research as an MDP" framing
- [[Sholto Douglas]] — early pipelining discussion
- [[Rahul Arya]] — pipeline prefill collaborator
- [[Nate Lidzén]] — internal-transfer example
- [[Rohan Aneja]] — his manager at Google Brain
- [[Todd Lipkin]] — his mentor
- [[Frontier Lab]] — the topic
- [[Research Taste]] — key differentiator
- [[Research as Markov Decision Process]] — research framing
- [[Mathematical Maturity]] — prerequisite skill
- [[Scaling Laws]] — core pre-training question
- [[Pre-training]] — his area
- [[Inference Co-Design]] — team vertical
- [[Model Quantization]] — team vertical
- [[Knowledge Distillation]] — team vertical
- [[Mixture of Experts]] — Flash 2.0 decision
- [[Pipeline Parallelism]] — Flash 2.0 innovation
- [[Model FLOPS Utilization]] — inference metric
- [[Reinforcement Learning from Human Feedback]] — recommended domain
- [[vLLM]] — open-source signal
- [[SGLang]] — open-source signal
- [[TensorRT]] — demo signal
- [[NVIDIA Dynamo]] — demo signal
- [[ThunderKittens]] — PL abstraction example
- [[CuTe]] — hardware DSL example
- [[XLA]] — compiler he "golfed"
- [[ImageNet]] — scaling-law analogy
- [[LMSYS Arena]] — leaderboard in the war story
- [[Transformer]] — the architecture
- [[OpenAI]] — peer frontier lab
- [[Anthropic]] — peer frontier lab
- [[DeepMind]] — lab merged into Google DeepMind
- [[Google]] — parent company
- [[Tensor Processing Unit (TPU)]] — serving hardware
- [[DeepSeek]] — rival on the leaderboard
