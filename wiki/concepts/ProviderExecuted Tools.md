---
title: "Provider-Executed Tools"
type: concept
tags: [ai-sdk, tools, llm, openai, anthropic, web-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
Provider-executed tools are one of three tool types in the AI SDK ecosystem. Unlike custom tools (developer provides everything) or provider-defined tools (developer provides execute function, provider provides schema), provider-executed tools are fully hosted on the LLM provider's infrastructure. The developer simply opts in, and if the agent decides to use the tool, the provider executes it on their servers and returns the result.

## Key Information
- **The Three Tool Types**:
  1. **Custom tools**: Developer defines description, input schema (Zod), and execute function. Gives the agent the ability to run arbitrary functions.
  2. **Provider-defined tools**: LLM providers post-train models to use these effectively (e.g., Anthropic's bash tool, computer use tool). Developer provides the execute function, but the provider crafted the description and input schema for optimal model performance.
  3. **Provider-executed tools**: Exist entirely in the LLM provider's infrastructure. Developer opts in; provider handles execution and returns results.
- **Classic Example**: Web search — both OpenAI and Anthropic offer web search as a provider-executed tool.
- **How It Works**: When importing the OpenAI provider and adding the web search tool, the SDK augments the request to OpenAI with an opt-in flag. The LLM decides whether to use it; if so, OpenAI executes the search on their servers, adds the result to the message state, and returns everything.
- **Advantages**: Zero additional code — the tool works out of the box. No API key management for search services. No execute function to write.
- **Disadvantages**: Tied to a single provider. Not portable across providers. Limited customization of the tool's behavior.
- **Configuration**: Some provider-executed tools accept configuration objects (e.g., web search can accept user location for localized results).
- **Rendering in UI**: Provider-executed tools appear as tool calls in the message parts, just like custom tools. They can be rendered in the UI with typed input/output via the AI SDK's end-to-end type system.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[AISDK]] — the framework
- [[Tool Loop Agent]] — the agent primitive using tools
- [[ToolCalling]] — general tool calling concept
- [[Tool Description]] — importance of descriptions for tool selection
- [[OpenAI]] — provider with web search tool
- [[Anthropic]] — provider with web search and other tools
- [[End-to-End Type Safety in Agents]] — type safety for tool parts in UI
