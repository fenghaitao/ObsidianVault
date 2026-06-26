---
title: "Multi-Persona Problem"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

The Multi-Persona Problem describes the challenge that building and evaluating AI agents is not something engineers do in isolation — it requires collaboration across engineers (product, AI, systems), subject matter experts (SMEs) with domain knowledge, and non-technical stakeholders. Eval platforms must serve all these personas effectively.

## Key Information

- **Personas involved**:
  - **Engineers**: Product engineers, AI engineers, systems engineers — build and run the agent
  - **SMEs**: Domain experts who understand what correct behavior looks like
  - **Non-technical stakeholders**: Product managers, business users who need to evaluate agent quality
- **Challenge**: Non-technical users won't engage with spreadsheets; they need approachable UIs
- **Value of inclusion**: SMEs and non-technical users add unique domain expertise and proximity to users
- **Platform requirement**: Must support both SDK-driven experiences (for engineers) and UI-driven experiences (for non-technical users)
- **Evals as a team sport**: The best eval outcomes come from bringing diverse perspectives into the evaluation process

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[EvalPlatforms]] — the platform context
- [[PlaygroundFeature]] — UI capability for non-technical users
- [[EvalMaturityStages]] — progression toward multi-persona support
- [[AgentQualityPlatform]] — platform category addressing this problem
