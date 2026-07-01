---
title: "Agents on the Canvas in tldraw — Steve Ruiz, tldraw"
type: source-summary
source: raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md
author: Steve Ruiz
company: tldraw
date: 2026-05-01
---

# Agents on the Canvas in tldraw — Steve Ruiz, tldraw

## Core Thesis

AI agents work best as visible collaborators on a shared canvas rather than hidden in a sidebar. By bringing agents onto the canvas with spatial presence, visual state, and awareness of each other's actions, tldraw transforms AI from a keyboard-stealing tool into a collaborative partner. The progression from Make Real (2023) to Fairies (2025) to desktop app script injection demonstrates an expanding frontier of agent capability, where local-first, file-based apps become the ideal platform for maximizing AI agency while containing risk.

## Key Points

1. **tldraw Overview**: tldraw is an online whiteboard, a London-based startup, and an SDK used by Replit (agent canvas), Luma AI, and Stitches (annotate mode). The canvas is built with React components, making it hackable and extensible.

2. **Make Real (2023)**: One of the first AI projects to "break containment" — users drew UI mockups on a canvas, sent them to a vision model, and got back working HTML prototypes. This predated Lovable and the term "vibe coding." Users could annotate on top of outputs to iterate: "make this green," "use these colors."

3. **AI as Canvas Collaborator**: The next evolution had AI producing structured outputs (shapes, circles, diagrams) rather than images. The model could draw cats, complete diagrams, finish slides, and correctly interpret visual context (a cat blowing out a candle) without explicit instruction about what a candle is.

4. **Vision Model Training Conflicts**: Vision models have less training data than text models, and that data contains conflicts that don't exist in text. Examples: the Y-axis goes up on Cartesian graphs but down on the web (top-left origin); "left" can mean stage left, viewer left, or object left. Prompt engineering around these conflicts was extremely challenging.

5. **Agentic Loop on Canvas**: The butterfly lifecycle demo put AI into an agentic loop — produce output, review it, iterate until done — with sub-features like rejection, thinking visualization, and progress tracking. This followed the conventions of coding agents at the time.

6. **Fairies: Multi-Agent Canvas**: Fairies (fairies.tldraw.com) places multiple agents directly on the canvas as animated sprites. Each agent has visible state (thinking, acting), spatial position relative to other agents, and awareness of what other agents are doing. They can work independently on different parts of the canvas or be grouped together.

7. **Leader-Follower Orchestration**: When multiple fairies are selected together, one is elected leader. The leader scouts the canvas, creates a to-do list, delegates tasks to followers, observes their work, judges completion, and verifies correctness. This was built in late 2024, concurrent with the broader industry figuring out agent orchestration.

8. **Shared State and Collision Avoidance**: Key orchestration challenges included giving agents shared state, managing the fact that agents are "essentially blind while they're working," and preventing overlapping work.

9. **Desktop App and Script Injection**: To give agents more canvas access, tldraw built an Electron desktop app wrapper that exposes an HTTP endpoint. Anything POSTed to the endpoint is executed as JavaScript — a "terrible idea" for a web app but acceptable for an offline, file-based desktop app where the worst case is the user hurting themselves.

10. **AI's Willingness to Script Inject**: The AI has "no qualms" about script injection, happily modifying minified code bundles (e.g., removing podcasts from Spotify's desktop app). It documents itself with "this is how you should do this" patterns and seems to "love" getting its claws into websites.

11. **Local-First Philosophy Validated by AI**: The local-first, file-over-app philosophy — previously idealistic — becomes practical with AI agents. If you want to maximize agency and accept the risk, you hand the user a local file-based app and say "good luck." This is the only way to give agents full access.

12. **Sharp Tools**: The desktop app approach uses "sharp tools" — powerful but dangerous. Like Claude Code's approach, the philosophy is "have fun, you know?"

## Entities

- [[Steve Ruiz]] — founder of tldraw, presenter
- [[TLDraw]] — online whiteboard, startup, and SDK; hackable React-based canvas
- [[Make Real]] — 2023 project: draw UI → AI generates working prototype
- [[Fairies]] — multi-agent canvas project at fairies.tldraw.com
- [[Replit]] — uses tldraw SDK for agent canvas
- [[Luma AI]] — uses tldraw canvas
- [[Stitches]] — uses tldraw canvas in annotate mode
- [[Lovelace]] — design app using tldraw
- [[Magic Path]] — design app using tldraw
- [[ClaudeCode]] — referenced as "sharp tools" philosophy analog
- [[Spotify]] — example of AI script injection target

## Concepts

- [[Agents on Canvas]] — agents as visible spatial collaborators rather than sidebar tools
- [[LeaderFollower Agent Pattern]] — one agent elected leader, scouts, delegates, judges
- [[Canvas as Agent Workspace]] — spatial canvas as shared state for multi-agent work
- [[FileOverApp]] — local-first philosophy validated by AI agent use cases
- [[Script Injection by AI]] — AI's willingness to modify running application code
- [[Vision Model Training Conflicts]] — Y-axis, left/right ambiguity in vision training data
- [[Make Real Pattern]] — draw → AI generates working prototype (precursor to vibe coding)
- [[AgenticLoop]] — produce → review → iterate loop used for canvas generation
- [[Agent Orchestration]] — leader-follower delegation and shared state management
- [[AgentVisualization]] — visible agent state, thinking, and action on canvas
- [[AgentHuman Collaboration]] — AI as collaborator on shared canvas vs. keyboard-stealing tool
- [[Structured Outputs]] — using structured data (shapes, circles) instead of image generation
- [[Sandboxing]] — desktop app as sandbox boundary for risky agent actions
- [[Computer Use]] — desktop app automation via HTTP endpoint and script execution
- [[AgenticProductDesign]] — canvas as agent-optimized interface vs. sidebar chat

## Related

- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — tldraw used in Kenton's state machine demo
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — agents need more than chat interface
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — multi-agent orchestration
