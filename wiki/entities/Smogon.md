---
title: "Smogon"
type: entity
tags: [data-source, pokemon, competitive-gaming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
Smogon is an online competitive Pokémon community and data source that provides detailed information about Pokémon movesets, teammates, counters, and competitive viability. Used in the Claude Agent SDK workshop as an example of unstructured text data that an agent can analyze.

## Key Information
- Provides text-file data about Pokémon including their moves, which Pokémon they work well with, which counter them, and competitive rankings
- Used in the workshop demo where Claude Code analyzed Smogon data files to suggest a competitive team built around Venusaur
- The agent searched through text files, found Pokémon mentioning Venusaur, identified common teammates and counters, and generated analysis scripts
- Demonstrates how agents can work with unstructured domain-specific data without preprocessing

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[PokéAPI]] — complementary structured Pokémon data source
- [[AgenticSearchInterface]] — designing search for unstructured data
