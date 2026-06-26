---
title: "FineTuning"
type: concept
tags: [technique, llm, training, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Fine-tuning is the process of further training a pre-trained LLM on domain-specific data to improve performance on particular tasks. In the 2024 AI Engineer Summit keynote, fine-tuning was critically discussed as a premature and costly optimization when pursued before having data-generating products, proper evals, and a clear understanding of value.

## Key Information
- Discussed in the operational section as a common but premature optimization
- Jason Lou's satire: "Find a machine learning engineer who can fine-tune as quickly as possible... hire someone for a quarter of a million dollars, give them 1% of their company to fight CUDA build errors"
- Fine-tuning is "much easier than figuring out how to build something worth charging for" — the sarcastic point being that companies chase fine-tuning to avoid the harder work of product development
- The recommended sequence: build application → capture data → then consider ML engineering and fine-tuning
- "Do not hire a machine learning engineer without having any data"
- The core critique: fine-tuning without data is putting the cart before the horse; first collect user interaction data through shipping, then determine if fine-tuning is warranted

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[JasonLou]] — critically discussed fine-tuning timing
- [[AIEngineer]] — the role that should precede ML engineering hires
- [[DataFlywheel]] — the data collection cycle that should precede fine-tuning
- [[ModelIsNotTheMoat]] — related strategic argument against over-investing in models
