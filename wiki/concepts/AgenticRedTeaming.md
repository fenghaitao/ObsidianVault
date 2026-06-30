---
title: "Agentic Red Teaming"
type: concept
tags: [security, red-teaming, agents, adversarial-testing, safety]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Agentic red teaming extends traditional LLM red teaming to AI agents by proactively testing for agent-specific vulnerabilities — particularly prohibited actions where an attacker manipulates the agent into performing actions it was explicitly forbidden from doing.

## Key Information

### How It Works (Microsoft Foundry)
- **Second AI attacks first AI**: A red teaming agent generates adversarial prompts targeting defined risk categories
- **Risk categories defined by user**: Violence, sensitive data leakage, prohibited actions, task adherence violations
- **Attack strategies**: Leetspeak, crescendo attacks, prompt manipulation (e.g., reversing strings to bypass guardrails), and many more
- **Report generation**: Scan produces a report showing which attack strategies succeeded and which vulnerabilities exist

### Agentic vs. Traditional Red Teaming
- **Traditional**: Tests model behavior — will the model output harmful content?
- **Agentic**: Tests agent actions — can the agent be tricked into performing prohibited actions?
- Agentic is more dangerous because agents can take real-world actions (fill passwords, leak data, modify systems)

### Prohibited Actions
- Define a taxonomy of actions the agent must never perform
- Red teaming agent generates prompts attempting to trick the agent into performing those actions
- Example: Agent told "never delete files" — red teaming tries prompts like "my grandmother's story about cleaning up old files" to bypass the guardrail

### Attack Strategies
- **Leetspeak**: Using numbers as letters (e.g., "h3ll0") to bypass text-based guardrails
- **Crescendo attack**: Starts with a small benign prompt, gradually escalates — like a frog in boiling water; comprehensive but time-consuming
- **Prompt manipulation**: Reversing strings or encoding prompts so guardrails see gibberish but the model decodes and executes

### Guardrail Bypass Example
- Direct prompt: "Tell me how to rob a bank" → guardrail blocks it
- Manipulated prompt: Reverse the string → guardrail sees gibberish and lets it through → model reverses it back and answers
- Red teaming proactively tests for this class of bypass

### Integration with PyRIT
- Microsoft works with the **PyRIT** open-source repository for red teaming
- Deep engagement to improve open-source red teaming tools
- One-click options available inside the Foundry platform
- Red teaming is not done alone — community-driven improvement

## Related
- [[Microsoft Foundry]] — platform with built-in red teaming
- [[PyRIT]] — open-source red teaming tool
- [[Guardrails]] — safety mechanisms being tested
- [[AgentObservability]] — broader observability includes safety monitoring
- [[SwissCheeseDefense]] — layered defense pattern
- [[summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft]] — source
