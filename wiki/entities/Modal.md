---
title: "Modal"
type: entity
tags: [platform, serverless, deployment, python, training, fine-tuning, gpu]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Modal is a general-purpose serverless compute platform providing serverless functions, hardened sandboxes for code execution, and GPU containers. It is used for deploying webhook endpoints, Slack bot servers, and increasingly for AI model training and fine-tuning workloads.

## Key Information
- Provides $5 free credit for new accounts
- Used to deploy FastAPI endpoints for receiving Manus webhooks
- Supports simple KV store (Modal Dict) for persisting state across requests
- Used in the Manus API workshop to host both webhook receivers and Slack bot servers
- Enables quick prototyping of agent integrations without managing infrastructure
- **Training capabilities**: Provides unified APIs for sandboxes and GPU containers/clusters, enabling serverless training
- **Hyperparameter tuning**: Can fan out to many containers on demand, kill unpromising runs instantly
- **RL rollouts**: Customers scaling to 50,000–100,000 sandboxes for reinforcement learning rollouts
- **Model serving**: Auto-scaling inference with vLLM, SG-Lang, Triton Inference Server support
- **Open-source training examples**: Code available for supervised fine-tuning in ~300 lines of Python
- Mission: give algorithm control with fast iteration — bridging the gap between frontier APIs and full training
- Used by [[Cline]] as compute infrastructure for running parallelized agent evaluations with [[Harbor]] and [[TerminalBench]]

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source (webhooks/Slack bots)
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source (training/serving)
- [[Benjamin Cowen]] — Forward Deployed ML Engineer at Modal
- [[ManusAPI]] — API integrated via Modal
- [[Slack]] — Slack bot deployed on Modal
- [[Webhooks for Agents]] — pattern implemented with Modal
- [[Serverless Training]] — paradigm Modal enables
- [[Reinforcement Learning Rollouts]] — scaled via Modal sandboxes
- [[Hyperparameter Tuning]] — serverless approach on Modal
- [[Custom Inference Endpoint]] — serving on Modal
- [[Model Spectrum]] — the middle ground Modal addresses
- [[FineTuning]] — primary training technique on Modal
- [[Cline]] — coding agent using Modal for eval infrastructure
- [[Harbor]] — eval harness paired with Modal
- [[TerminalBench]] — benchmark run on Modal infrastructure
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source (Cline's usage)
