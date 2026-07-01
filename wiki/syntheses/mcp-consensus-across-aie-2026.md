---
title: "mcp-consensus-across-aie-2026"
type: synthesis
tags: [analysis, mcp, protocol, agents, connectivity, security, web]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260611 - The agent-ready web： Simplify user actions with WebMCP — Tara Agyemang, Google.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260615 - Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic.md"]
last_updated: 2026-07-01
---

# What Is the Consensus on MCP Across AI Engineer 2026 Talks?

## The Protocol Has Won

MCP has achieved escape velocity. [[DavidSoriaParra]] reported 110 million monthly downloads — growing faster than React at the same stage. It is used by OpenAI's Agent SDK, Google's ADK, LangChain, and thousands of frameworks as a dependency. The ecosystem has converged on one standard. [[IdoSalomon]] and [[Liad Yosef]] noted adoption by VS Code, Cursor, Copilot, GitHub, ChatGPT, Claude, Postman, Goose, and LibreChat.

But consensus on *how* to use MCP is still forming. Across 10+ talks at AI Engineer 2026, several tensions and emerging patterns stand out.

## Tension 1: Agent-First Design vs. REST API Wrappers

The strongest consensus: stop wrapping REST APIs one-to-one in MCP tools. [[JeremiahLowin]] framed this as "outcomes over operations" — compose multiple API calls into a single outcome-oriented tool rather than exposing every endpoint. His five best practices: outcomes over operations, flatten arguments (use primitives not nested dicts), instructions as context (docstrings and examples are the agent's interface), respect the token budget, and curate ruthlessly.

The counterexample: [[KellyKFL]] at Fiverr went from 188 tools to 5. [[JeremiahLowin]]'s 50-tool rule — performance degradation begins beyond ~50 tools per agent — is widely cited. With 800 tools and a 200K token window, each tool gets only ~250 tokens of description. The GitHub MCP server reportedly ships ~200K tokens on handshake alone.

[[DavidSoriaParra]] echoed: "design for how a human would interact — that's a good start for agents." [[TunShwe]] reinforced from the security angle: consolidate fine-grained operations into coarse outcome-oriented tools to shrink the attack surface. Good MCP design and good MCP security are the same discipline.

## Tension 2: Context Explosion vs. Progressive Discovery

[[MattCarey]] coined "MCP = Mega Context Problem": Cloudflare's OpenAPI spec is 2.3M tokens, ~1.1M tokens as tools — impossible to load all at once. Even splitting into 16 product-based MCP servers left gaps. Three solutions emerged:

1. **Tool Search** — keyword-based loading of relevant tools on demand. Used by Cloud Code. Works well but unused tools remain in context (~2,100 tokens loaded, only ~500 used). [[DavidSoriaParra]] demonstrated massive context reduction after implementing progressive discovery in Claude Code.
2. **Code Mode** — let the model write code against typed SDKs instead of sequential tool calls. [[MattCarey]] reduced the Cloudflare API surface (~2,600 endpoints) to two tool calls: search and execute, both accepting code strings — a 99.9% token reduction. A DDoS response that would take ~8 round trips with regular MCP is done in one shot.
3. **CLI-based interaction** — agents use shell access for `--help` and command parsing. Used by OpenClaw. Works well but requires shell access.

The emerging consensus: code mode + progressive discovery is the path forward for large API surfaces. [[DavidSoriaParra]] called progressive discovery "the number one thing we need to go and start building" on the client side.

## Tension 3: Security as Design, Not Afterthought

[[TunShwe]]'s five security principles map directly onto the design advice from [[JeremiahLowin]] and [[DavidSoriaParra]]: shrink attack surface, constrain inputs at schema level (use enums, reject free-form nested payloads), documentation as defense (clear descriptions crowd out poisoned neighboring servers), return only what the agent needs (strip PII, credentials), and minimize blast radius (scope permissions at tool/resource level).

The OWASP MCP Top 10 identifies tool poisoning (#3) and context injection (#10) as the primary attack vectors — both exploiting the fact that agents trust tool descriptions and returned data. [[NimrodHauser]] demonstrated bending a public MCP server without breaking it, showing that even well-intentioned servers can leak capabilities.

Each design dimension casts a security shadow: discovery (tool poisoning via descriptions), iteration (data leakage via retries), and context (context injection via oversharing). The implication: security cannot be bolted on after the server is built.

## Tension 4: Authentication — The Consent Screen Crisis

[[GarrettGalow]] identified a fundamental tension: MCP's OAuth model creates repeated consent screens that break the single sign-on model. IT teams have no visibility into which MCP servers developers connect to, and cannot revoke access when employees leave — access tokens and refresh tokens persist independently of SSO session revocation.

His Cross-App Access (XAA) solution, built on the ID JAG spec, lets identity providers like Okta act as trust brokers. The flow: user logs into IDP via SSO → client requests ID JAG token → exchanges it for short-lived access token (~5 minutes) → standard MCP communication. When SSO is revoked, no new tokens can be obtained. [[DavidSoriaParra]] listed cross-app access as a key roadmap item for Anthropic.

Current limitation: only Okta supports XAA (OIDC-based). Microsoft Entra does not yet support it. Authorization scoping (limiting what an agent can do within a service) is not part of the spec today.

## Tension 5: UI — MCP Apps and the "New Web"

[[IdoSalomon]] and [[Liad Yosef]] presented MCP Apps as the first official MCP extension, co-developed with Anthropic and OpenAI. The core thesis: text is a terrible interface for agent interactions. Companies should send their own branded, interactive UI chunks to chat hosts instead of walls of text.

MCP Apps supports three UI generation approaches: predefined UI (company-built black box), declarative UI (structured JSON, host renders components), and generative UI (model-generated). Claude's generative UI feature uses MCP Apps under the hood. Bidirectional message passing lets UI interactions send messages back to the host — notification, tool call, or prompt.

Early adopters like Shopify (millions of stores sending MCP UI chunks) and Hugging Face (all Spaces as MCP UI widgets) adopted even before standardization. Post-standardization: ChatGPT recommends MCP Apps as the way to build ChatGPT apps.

[[TaraAgyemang]] extended this to the browser with WebMCP — websites expose structured tools that agents call directly instead of parsing DOM, accessibility trees, and screenshots. [[RL Nabors]] explained the two flavors: declarative (HTML attributes on forms) and imperative (`navigator.modelContext.registerTools`). Not MCP-compliant — "WebMCP is to MCP as JavaScript is to Java."

[[FrédéricBarthelet]] explained the double-iframe architecture that makes this secure: outer iframe for origin isolation (Content Security Policy, no cookie/localStorage access), inner iframe for app content. Single srcdoc iframes fail because they share origin/CSP with the host.

The vision: a "new web" where personal assistants compose experiences from atomic UI chunks rather than users navigating monolithic websites. [[IdoSalomon]] framed it as 1 billion weekly ChatGPT users — 160x the iPhone user base when the App Store launched.

## The Connectivity Stack

[[DavidSoriaParra]] proposed the definitive framework: three tools for agent connectivity in 2026:

1. **Skills** — domain knowledge in simple files, reusable, continuously updateable, no plugin registries
2. **MCP** — rich semantics, UI, long-running tasks, resources, authorization, governance
3. **CLI/Computer Use** — great for local agents with sandboxes, pre-training familiarity (git, GitHub)

The best agents will use all three together. The right tool depends on the use case.

## Roadmap Convergence

Multiple speakers pointed to the same future:
- **Stateless transport** (Google/Anthropic) — for hyperscaler scaling, coming June 2026
- **Server discovery** via well-known URLs — crawlers auto-discover MCP servers
- **Skills over MCP** — ship domain knowledge with servers, continuously update without plugin registries
- **Async task primitive** — for agent-to-agent communication
- **MCP as middleware** — [[MattCarey]] predicted MCP becomes a flag in frameworks (`MCP=true`), natively in every TypeScript full-stack framework by end of year. "Express thousands of APIs from one Next.js app with `MCP=true`."
- **Cross-app access** — login once, use all MCP servers
- **Saved mini-scripts** — users save LLM-generated code for cron jobs and recurring tasks

## Remaining Debates

Not everything is settled:
- **Tool count**: 50 is the heuristic, but some argue for even fewer
- **Code mode vs. tool calling**: which paradigm dominates for which use cases
- **Generative UI vs. predefined UI**: Claude's generative UI uses MCP Apps under the hood, but the spectrum from predefined to fully generated is still being explored
- **A2UI vs. MCP Apps**: Google's generative UI protocol and MCP Apps are working toward interoperability, but convergence is not yet complete
- **Untrusted code execution**: code mode requires sandboxing — [[MattCarey]]'s WorkerD (V8 isolates with capability-based security), Deno, and Pydantic Monty are emerging primitives, but no standard has won yet
- **MCP client difficulty**: building MCP clients has been hard (stateful connections, resumability). Most clients are stripped-down, offloading to bare-bones SDKs. This will change as the SDK improves

## Related

- [[MCP]] — concept page
- [[MCPApplications]] — MCP Apps concept
- [[WebMCP]] — browser extension of MCP
- [[ProgressiveDiscovery]] — loading tools on demand
- [[CodeMode]] — programmatic tool calling
- [[MCPSecurity]] — security principles
- [[CrossAppAccess]] — enterprise SSO for MCP
