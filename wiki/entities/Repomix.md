---
title: "Repomix"
type: entity
tags: [product, tool, developer-tools]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-11
---

## Definition

Repomix (called "repo mix" in the transcript) is a tool that compresses an entire codebase into a single file, which [[Lazar]] uploads to [[Claude]] or [[ChatGPT]] as an external "consultant" when diagnosing a bug that other steps in his debugging framework haven't resolved.

## Key Information

- Used as the manual predecessor/alternative to connecting [[Codex]] directly to an exported GitHub repo: Lazar pastes the compressed codebase plus console logs and a problem description into Claude or ChatGPT and asks it to diagnose the issue — used purely for diagnosis, not for making code changes.
- Fits step three of Lazar's "[[4x4 Debugging Framework]]": bringing in an external tool as a fresh diagnostic facilitator once the AI coding tool itself and manual console-log debugging haven't fixed the problem.

## Related

- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — uses this tool
- [[4x4 Debugging Framework]] — debugging framework this tool supports
- [[Claude]] / [[ChatGPT]] — tools Repomix output is fed into
- [[Codex]] — alternative external diagnostic tool
