---
title: "summary-20260403 - Niamh Gavin AI Research Fails - Anecdotes from the Frontline - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, research, failures, debugging]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260403 - Niamh Gavin AI Research Fails - Anecdotes from the Frontline - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Niamh Gavin shares humorous but instructive AI research failure anecdotes: an agent naming containers "MS-13" (an international criminal organization) triggering a security escalation; a training run that consumed all compute debating the Immaculate Conception vs. biology textbooks; and classic computer vision failures (Chihuahua vs. blueberry muffin). Argues that modern debugging tools (Logfire, structured traces) make failures far easier to diagnose than in the pre-LLM era.

## Key Points

- Container naming incident: agent followed naming convention "MS" + number, but "MS-13" matched a sanctioned organization, triggering P0 security escalation
- Training run incident: model discovered contradiction between the Bible (Immaculate Conception) and biology textbooks (asexual reproduction impossible in humans), consumed massive compute in internal debate
- Classic CV failures: single-pixel adversarial attacks could turn turtles into rifles; Chihuahuas vs. muffins indistinguishable to models
- Modern debugging advantage: LLM actions are codified in English with chain-of-thought, making failures traceable vs. opaque vector math
- Agent-to-agent communication can bypass human language entirely for efficiency (speech-to-speech without text intermediate)

## Related

- [[Logfire]] — observability tool praised for debugging
- [[AgentEvaluation]] — the practice of measuring and debugging agent behavior
- [[AISafety]] — security implications of agent actions
