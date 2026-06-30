---
title: "Generative UI"
type: concept
tags: [ui, agents, personalization, e-commerce, code-mode]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-26
---

## Definition
Generative UI is the concept of creating perfectly custom user interfaces for every individual user, generated on the fly by AI agents based on the user's specific context, needs, and state. It represents a departure from the traditional approach of building one-size-fits-all interfaces that must work for every user.

## Key Information
- Presented by Sunil Pai as a natural application of code mode and agent harnesses
- Traditional UI problem: the more popular an app gets, the more bland the UI becomes to serve everyone
- ML-based personalization (changing button colors) is shallow compared to generative UI
- Generative UI creates entirely different programs per user, backed by the same backend
- E-commerce example: one user needs to return shoes and find similar items under $100; another has a delayed order — different UIs generated for each
- The UI doesn't have to be a blank chat box (though "blank chat box e-commerce might be a lot of fun")
- UI programmers, due to their closeness to users, are positioned to do well in this paradigm
- Represents a rethinking of UI for the new age — "a part of the tech tree we have not really explored for 30 years because eval wasn't around"
- Now we have "safe eval" (sandboxed code execution) and models that generate code
- Pai used Opus to generate generative UI for his own slide about generative UI
- Claude's generative UI feature (released by Anthropic) uses MCP Apps under the hood — generative UI is streamed into an MCP App
- MCP Apps is agnostic to how UI is generated: supports predefined UI, declarative UI, and generative UI on a spectrum
- Generative UI represents the fully model-generated end of the spectrum, where the model creates UI "out of thin air"

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[CodeMode]] — paradigm enabling generative UI
- [[AgentHarness]] — infrastructure for running generated UI code
- [[SunilPai]] — speaker who presented the concept
- [[React]] — UI framework; React programmers positioned to excel here
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source (UI generated on the fly in End of Apps vision)
- [[End of Apps]] — Kitze's prediction that consumer apps disappear, replaced by generative UI
- [[Kitze]] — prediction that "the UI is going to pop on the fly"
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source (generative UI uses MCP Apps)
- [[MCP Apps]] — protocol that generative UI can be streamed into
- [[MCPApplications]] — concept page for MCP Applications
- [[Predefined UI]] — alternative UI approach (black box)
- [[Declarative UI]] — alternative UI approach (structured JSON)
