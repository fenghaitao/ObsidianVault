---
title: "PokéAPI"
type: entity
tags: [api, pokemon, rest, open-data]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
PokéAPI is a RESTful API providing comprehensive data about Pokémon games, including Pokémon species, moves, abilities, types, items, and more. Used by Thariq Shihipar as a prototyping example for building agents with the Claude Agent SDK.

## Key Information
- Provides structured data on thousands of Pokémon, each with numerous moves and attributes
- Used in the workshop to demonstrate code generation: Claude Code was prompted to generate a TypeScript SDK wrapping the API
- Chosen because it represents a complex, real-world API that the presenter hadn't worked with before, simulating real agent development
- The generated SDK included interfaces for Pokémon, moves, species, abilities, and methods like getByName, listPokémon, getAllPokémon

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[Smogon]] — competitive Pokémon data source also used in the demo
- [[CodeGenerationForNonCoding]] — technique demonstrated with this API
