---
title: "Obsidian"
type: entity
tags: [tool, note-taking, knowledge-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com).md"]
last_updated: 2026-06-29
---

## Definition
Obsidian is a note-taking and knowledge management application based on local Markdown files. In Fulan's architecture, a separate Obsidian vault serves as the output destination for AI-generated reflections and insights, keeping analysis results separate from source data.

## Key Information
- Used as the output vault in Fulan's read-only AI architecture
- The separate Obsidian vault receives AI-generated markdown documents for human review
- The output could alternatively be Notion, text files, or any other system — Obsidian is one option
- The separation of output from source is a key architectural principle: the AI never writes back to source systems
- Radek Sienkiewicz uses a ~3,000-page Obsidian vault integrated with OpenClaw, containing work, personal, tasks, projects, research, articles, and an inbox of links
- The agent analyzes new links added to the inbox, adds tags and context, checks existing vault content on the topic, and creates connections — transforming unused bookmarks into an actively growing knowledge base
- The vault is indexed nightly (3-6 AM) along with QMD and memory indexes

## Related
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[summary-20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)]] — source (Radek's vault integration)
- [[Fulan]] — system that uses Obsidian as output
- [[ReadOnlyAI]] — design philosophy
- [[OpenClaw]] — agent framework integrated with Obsidian
- [[RadekSienkiewicz]] — user with 3,000-page vault
- [[AgentKnowledgeBase]] — concept of agent-integrated knowledge management
- [[AgentInboxProcessing]] — auto-tagging and contextualizing bookmarks
- [[AgentNightlyMaintenance]] — scheduled indexing routine
