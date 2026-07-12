---
title: "AI Agent Training"
type: concept
tags: [AI, agents, training, go-to-market, deployment]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/35 - We replaced our sales team with 20 AI agents—here's what happened next ｜ Jason Lemkin (SaaStr).md"]
last_updated: 2026-07-10
---

## Definition

AI Agent Training is the process of preparing an AI sales agent for production use through three phases: ingestion (uploading company data, content, and best sales scripts), training (answering the agent's questions and iterating on its outputs), and QA/testing (daily review and correction of mistakes). It takes approximately 30 days of daily iteration to get an agent to "pretty good."

## Key Information

- Three phases: (1) Ingestion — upload website URLs, wiki, training docs, prospectus, CRM data; (2) Training — answer questions the agent generates, iterate on responses; (3) QA — daily review of outputs, correcting mistakes and hallucinations
- The process is not technically hard — "it's the same B2B stuff we've been doing for over a decade" — it's just sequenced differently
- Ingestion means uploading and processing data (RAG, vectoring), but the user doesn't need to understand the technical details
- Training is simply "answering questions and getting better and better"
- The critical mistake of 2024: vendors claimed agents would work "out of the box" with no training needed — this was false
- Daily commitment: in the early days, Jason Lemkin spent an hour each morning reviewing Deli's outputs and fixing mistakes
- Timeline: if you spend 1-2 hours daily correcting mistakes for 30 days, the agent will be "pretty good" by day 30
- The "prompt" (a string of text describing what you want) is the output of training — once you have a good prompt, you can port it to other platforms
- SaaStr trained 3 agents, then took the best prompt and gave it to Agentforce — it was "pretty good" in one day
- Anyone in B2B or SaaS can do this — "it is not that different than other things we've done"
- Doing it yourself is critical: "if you're waiting for people on your team to do it, if you're waiting for an agency to do it, I think you're going to be out of a job"

## Related

- [[summary-35 - We replaced our sales team with 20 AI agents—here's what happened next ｜ Jason Lemkin (SaaStr)]] — source summary
- [[AI Sales Agents]] — the agents being trained
- [[Forward Deployed Engineer]] — helps with training
- [[Agent Orchestration]] — what happens after training
