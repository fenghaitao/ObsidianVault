---
title: "Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver.md"
date: 2026-05-25
ingested: 2026-06-30
tags: [agent-design, bounded-autonomy, context-windows, llm-limitations, constraints, simplicity, representation, advertising]
---

## Core Thesis
Bounded autonomy is the productive middle ground between free will and determinism in agent design — neither fully autonomous nor fully scripted. Angus J. McLean draws on his experience as AI Director at Oliver (an AI-first advertising agency serving 200+ brands with 4,000 daily assets) to argue that constraints create creativity, context windows will never be enough, LLMs remain fundamentally closed boxes that don't understand data, and AI at its core is just translation between representations. His overarching advice: slow down, keep it simple, understand your model's limitations, and use multiple representation structures.

## Key Points

### Slow Down
- AI moves very fast with a "blink and you'll miss it" mentality, but if you did miss it, was it really that important? Probably not.
- The actual core of LLMs hasn't changed since at least the 1990s (Andris Drubel would argue even further back).
- LLMs do not actually understand the data they're presented with — they have clear, persistent limitations.

### LLM Limitations
- **Data efficiency**: Humans learn from very few examples; models need massive datasets for relatively simple conclusions.
- **No continuous learning**: Models don't continuously learn without forgetting in the way humans do — they're a closed box.
- **Recent gains come from brute force**: More from compute scaling than material breakthroughs.
- **Trend identification problem**: In advertising, if something is really new, the model won't recognize it.

### Band-Aid Fixes
- Most tools and techniques are band-aids around model constraints — temporary, superficial, masking symptoms rather than fixing problems.
- Even the way models are trained is a form of band-aid.
- How to spot band-aids: they're temporary quick fixes, not long-term solutions, often inadequate.

### LLMs as Closed Boxes
- LLMs are closed boxes with knowledge inside — best thought of as flexible databases capable of semantic math.
- No emergence or actual learning is expected from the model.
- Context windows act as soft constraints, as powerful as guardrails in shaping model behavior.
- Not giving the model internet access and instead providing high-quality documentation yields much better results.
- Models are very susceptible to SEO and bad at spotting promotional content.

### Context Windows Will Never Be Enough
- Most recent advances in agentic capabilities are largely due to increased context windows.
- Large context enables: history of actions, tool outputs, structured organization over time, goals and plans.
- Without large context, systems forget mid-task and can't handle long complex multi-step workflows.
- World knowledge doubles about every 12 hours — context windows, however large, will always be insufficient.
- The challenge has shifted from getting context in to keeping the noise out.

### Constraints Create Creativity
- Abundance stops you being scrappy. If progress stopped tomorrow, how would you make the most of what you have?
- Self-imposed constraints are valuable: how little of the context window can you use and still get the task done?
- Historical parallel: early computing constraints (4,000 words for Space War, Crash Bandicoot memory tricks on PS2) produced great innovations.
- Practical experiments: using older/smaller model versions, building your own harness/memory/compaction, preprocessing and archiving.
- This improves prompting ability, control, fundamentals, and understanding of your data.

### Keep It Simple
- Models are naturally verbose and tend towards complexity — they will suggest the most complicated solution.
- Personal example: a complex CV application was beaten 10-100x by just four letters: HTML.
- Just because you have the power of the gods doesn't mean you should use it.
- What matters most is building a simple version that works — shorten your feedback loop with reality.

### AI as Translation
- AI at its core is just translation — from the "Attention Is All You Need" paper (English to French) to text→images, images→audio, audio→video.
- Knowledge production itself is summarization — compacting experience into knowledge.
- Different data types can be converted into common internal representations and then transformed into something else.
- Structure is not an inherent property of the object but a property of the representation chosen by the observer.
- If you can manipulate something through a representation space, the structure of that data is not fixed.

### Multiple Representation Structures
- Markdown: for human-readable hierarchy and authoring.
- Graph relationships: for references and connections.
- Clustering: for large or unstructured bodies of text.
- Folders: for fast retrieval.
- Timelines: for chronological relevance.

### Have Fun and Experiment
- Much of what's learned comes through thoughtful play and experimentation, not just work.
- Hackathons provide space to experiment in ways day jobs don't allow.

### Agent Design in the Workplace
- Capitalism naturally breaks tasks down into small, easily repeatable chunks (Adam Smith's pin factory).
- Structured workflows are often far more effective than unstructured agent approaches.
- Don't automate a job unless you can do it yourself.
- Demonstrated an analytics cluster that processes 50,000 tweets, clusters them, and produces strategy insights for creative teams almost instantly.

## Entities
- [[Angus J. McLean]] — speaker, AI Director at Oliver
- [[Oliver]] — AI-first advertising startup, 3,000 staff across 46 countries, serves 200+ brands, generates 4,000 assets/day
- [[aiDotEngineer]] — conference where the talk was given

## Concepts
- [[Bounded Autonomy]] — the productive middle ground between free will and determinism in agent design
- [[BandAid Fixes]] — temporary, superficial fixes that mask symptoms of model constraints
- [[AI as Translation]] — framing AI's core capability as translation between representation spaces
- [[Representation Structures]] — using multiple data structures (markdown, graphs, clustering, folders, timelines) for different needs
- [[Constraints and Creativity]] — how constraints and limitations drive innovation in AI engineering
- [[Context Assembly]] — dynamic construction of context vs. static approaches like TF-IDF
- [[Context Management]] — the broader context management challenge
- [[SimpleDesignPhilosophy]] — keeping agent and system design simple
- [[ContextEngineering]] — deliberate curation of what goes into context
- [[Token Billionaire]] — referenced in the talk as an aspirational extreme

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — context as primary engineering concern
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — context window constraints and progressive discovery
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — simple design philosophy in agent architecture
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — agentic engineering and context
