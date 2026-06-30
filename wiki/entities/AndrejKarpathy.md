---
title: "AndrejKarpathy"
type: entity
tags: [person, ai, researcher, openai, tesla]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Andrej Karpathy is a prominent AI researcher (formerly OpenAI, Tesla) who coined the terms "Software 2.0" and "system prompt learning." He has publicly discussed paradigms around iterating on system prompts using English feedback.

## Key Information
- Coined "Software 2.0," a paradigm where software is built by specifying objectives and verification criteria rather than writing explicit code. This concept underpins specification-driven development and AI coding agents.
- Coined the term "system prompt learning" to describe the practice of iteratively improving system prompts based on English-language feedback.
- Compared the process to the movie Memento, where the protagonist writes down what he learns and uses those notes to guide future actions — analogous to an agent learning from past mistakes recorded in its system prompt.
- His viral tweet on system prompt learning helped popularize the concept and frame it as a distinct paradigm from reinforcement learning.
- Characterized embeddings as "the file system of LLMs" in his OS-for-LLMs diagram, a framing that Jack Morris argues will be superseded by weight-based knowledge storage.
- Demonstrated synthetic continued pre-training by generating diverse training examples to teach a small LLM about himself, showing that novel behaviors can be taught through synthetic data generation and fine-tuning.
- Coined "context engineering," describing it as "a delicate art and science of filling the context window with just what needs to happen for the agent to have the right context for the right iteration for the next step." This concept is central to the agentic engineering paradigm.

- Quoted in the closing of the 2024 AI Engineer Summit keynote: "There's a large class of problems that are really easy to imagine and build demos for, but it's extremely hard to build real products out of." This frame was used to illustrate the gap between LLM demos and production systems, with the example of neural-network-driven cars taking from 1988 to the 2020s to reach production.
- Runs OpenClaw to control his house — swyx mentioned during the Peter Steinberger AMA that Karpathy is one of the prominent users running OpenClaw for home automation
- Posted a viral tweet about LLM knowledge bases that Radek Sienkiewicz cited — Radek realized his OpenClaw + Obsidian setup matched Karpathy's description, which made him recognize how sophisticated his own setup had become

## Related
- [[Software2.0]] — the paradigm he coined
- [[PromptLearning]] — the concept he named and popularized
- [[summary-20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI]] — source (Software 2.0)
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source (prompt learning)
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source (synthetic pre-training, embeddings as file system)
- [[summary-20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)]] — source (viral knowledge base tweet)
- [[SyntheticContinuedPreTraining]] — technique he demonstrated
- [[NeuralFileSystem]] — concept contrasting his embeddings-as-file-system framing
- [[ContextEngineering]] — concept he coined
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (context engineering)
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source (demo-to-production quote)
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (runs OpenClaw for home automation)
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source (LLMs as wiki article)
- [[OpenClaw]] — project he uses for home automation
- [[Waymo]] — example used alongside his quote
- [[AgentKnowledgeBase]] — concept related to his viral tweet
- [[nanoGPT]] — his educational GPT implementation that inspired the LLM training workshop
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source (nanoGPT as workshop inspiration)
- [[Zettelkasten]] — related knowledge management approach
- [[Mem Palace]] — alternative knowledge management approach
