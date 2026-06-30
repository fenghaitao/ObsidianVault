---
title: "summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal"
type: source
tags: [source, transcript, ai, fine-tuning, model-customization, serverless, training, frontier-api, modal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---

## Core Summary
Benjamin Cowen, a Forward Deployed ML Engineer at Modal, presents the case for fine-tuning as an emerging middle ground between frontier APIs and full model training. As AI products mature, companies are increasingly turning to fine-tuning for better performance, lower costs, and domain-specific optimization. Cowen argues that the modern tooling landscape — open-source libraries, serverless compute platforms — has made fine-tuning accessible in as few as 300 lines of Python, and that companies with mature data collection and eval systems should prepare for the transition now.

## Key Points

### The Model Spectrum
- **Frontier API**: Fast iteration, zero customization beyond prompt engineering, great for prototyping but doesn't scale economically
- **Fine-Tuning (Middle Ground)**: Algorithm-level control without managing clusters; retains fast iteration cycles of the frontier
- **Full Training**: Complete control but massive infrastructure responsibility; traditionally required dedicated clusters and infra engineers

### Signals It's Time to Fine-Tune
- API costs exceeding customer revenue (economics not scaling)
- Latency or throughput requirements not met by frontier APIs
- Eval scores plateauing despite prompt engineering efforts
- Enterprise contracts with strict SLAs that frontier APIs cannot meet

### Prerequisites for Fine-Tuning
- Mature data collection: if you have garbage data, it's garbage in, garbage out
- Developed evals: need to know what "better" means for your use case
- If you've built an agent harness and are evaluating your product, you likely already have everything needed to train

### Industry Results
- **Intercom** beating frontier API at 1/5 the cost
- **Pentress** seeing "orders of magnitude" improvement
- **Decagon**: frontier labs optimize for winning on everything; you should optimize for winning on your business logic

### Modern Training Tooling
- Supervised fine-tuning achievable in ~300 lines of Python
- Open-source RL libraries making reinforcement learning accessible
- Serverless platforms (like Modal) enabling hyperparameter tuning via fan-out to many containers
- Massive parallelism for RL rollouts: customers scaling to 50,000–100,000 sandboxes

### Model Serving After Training
- vLLM, SG-Lang, Triton Inference Server available as open-source serving solutions
- Serverless platforms can auto-scale inference to match incoming traffic
- Same infrastructure can handle both training and serving

### Key Takeaway
- Don't train your model today — but start preparing. Collect data, develop evals, and plan for when fine-tuning becomes the right move (6 months to 1 year out)
- If you have a differentiated product, it is inherently custom — stepping into domain-specific models is a matter of time

## Related
- [[Benjamin Cowen]] — speaker
- [[Modal]] — serverless compute platform
- [[Fine-tuning]] — core technique discussed
- [[Frontier API]] — starting point on the spectrum
- [[Model Spectrum]] — the continuum from API to custom training
- [[Serverless Training]] — emerging paradigm enabled by platforms like Modal
- [[Custom Inference Endpoint]] — serving fine-tuned models
- [[Reinforcement Learning Rollouts]] — massively parallel evaluation pattern
- [[Domain-Specific Models]] — the destination for maturing AI products
- [[Hyperparameter Tuning]] — use case for serverless training
- [[Supervised Fine-Tuning]] — accessible training technique
- [[Model Serving]] — what comes after training
- [[Model Customization]] — broader framework
- [[DataFlywheel]] — prerequisite data collection cycle
- [[Intercom]] — beating frontier API at 1/5 cost
- [[Decagon]] — customer perspective on business-specific optimization
- [[Pentress]] — orders of magnitude improvement
- [[vLLM]] — open-source model serving
- [[EvalEngineering]] — evaluation maturity prerequisite
