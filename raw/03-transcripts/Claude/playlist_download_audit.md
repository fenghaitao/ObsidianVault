# @claude Playlist Download Audit

**Channel:** https://www.youtube.com/@claude/playlists
**Date:** 2026-06-23
**Tooling:** `download_playlists_public.py` (android_vr) + `download_playlists_auth.py` (web client + cookies)

## Summary

| Metric | Count |
|---|---|
| Total videos across 12 playlists | 129 |
| Transcripts on disk | 85 |
| Missing | 44 |
| — No captions on YouTube yet | 40 |
| — Removed by uploader | 3 |
| — Private (no access grant) | 1 |
| Recoverable via auth path but not yet fetched | **0** |

**Key conclusion:** the on-disk set is complete relative to what YouTube exposes. Switching missing videos from `_public.py` to `_auth.py` recovers nothing — every gap is genuinely uncaptioned, removed, or private. The android_vr under-reporting case (SF #04) was already backfilled via the web client.

## Per-playlist coverage

| Playlist | On disk / Total | Missing |
|---|---|---|
| Code with Claude 2026 - Japan | 2 / 2 | 0 |
| The Problem Solvers | 6 / 6 | 0 |
| Code with Claude 2026 - London Day 2 | 8 / 15 | 7 |
| Code with Claude 2026 - London | 12 / 24 | 12 |
| How Anthropic uses Claude Cowork | 3 / 3 | 0 |
| Code with Claude 2026 - San Francisco | 9 / 19 | 10 |
| How teams use Claude | 7 / 7 | 0 |
| Claude Code 101 | 9 / 9 | 0 |
| Claude Code subagents | 4 / 4 | 0 |
| Claude Code Skills | 6 / 6 | 0 |
| Product Launches | 14 / 28 | 14 |
| How Anthropic uses Claude | 5 / 6 | 1 |

## Missing video classification

Status legend: `NO-CAPTIONS` = no English caption track exists on YouTube (auto or manual), verified under both android_vr and web clients; `REMOVED` = video taken down by uploader; `PRIVATE` = video private, authenticated account not on allow-list.

### Code with Claude 2026 - London Day 2

| Idx | Video ID | Title | Status |
|---|---|---|---|
| 08 | tUoO4ucrNc0 | Fighting financial crime with Claude Cowork | NO-CAPTIONS |
| 09 | T8N0MED3IJo | Where code meets court: AI at the legal-technical frontier | NO-CAPTIONS |
| 11 | A3rmSUp6Dxg | How Metaview built self-improving prompts for application review | NO-CAPTIONS |
| 12 | uGroRwlC9y4 | Teaching agents to learn from your team | NO-CAPTIONS |
| 13 | K4-flzsPraE | Building the best agentic analytics harness: Powered by Claude, built with Claude Code | NO-CAPTIONS |
| 14 | iLtmWCjuGIQ | (title unavailable) | REMOVED |
| 15 | RQcrm2CK-iQ | (title unavailable) | REMOVED |

### Code with Claude 2026 - London

| Idx | Video ID | Title | Status |
|---|---|---|---|
| 02 | tuY2ChJIx48 | Beyond the basics with Claude Code | NO-CAPTIONS |
| 04 | QIriO1-vHYw | Getting more out of the Claude Platform | NO-CAPTIONS |
| 06 | DNRddIEoH3c | The capability curve | NO-CAPTIONS |
| 07 | Uvl-tRga98g | Designing with Claude: From prompt to production | NO-CAPTIONS |
| 08 | l8fxVYIP4HQ | Building with Claude on Google Cloud | NO-CAPTIONS |
| 12 | nho1YAEPuwA | What legal agents inherit from coding agents: Lessons from Legora | NO-CAPTIONS |
| 16 | mhW-XXnDFSU | How Lovable vibecodes production software at scale | NO-CAPTIONS |
| 17 | XFaeIbL-lvE | Building AI-native at enterprise scale: monday.com, Doctolib, and Delivery Hero | NO-CAPTIONS |
| 18 | VueeyKcquoA | From one person to 80: Scaling a hypergrowth engineering org with Claude Code | NO-CAPTIONS |
| 21 | zFslvuvYifQ | Coding is no longer the constraint: Scaling devex to teams and agents at Spotify | NO-CAPTIONS |
| 23 | wI0ptqCSL0I | Stop babysitting your agents | NO-CAPTIONS |
| 24 | sRvUXLquiRg | What's new in Claude Code | NO-CAPTIONS |

### Code with Claude 2026 - San Francisco

| Idx | Video ID | Title | Status |
|---|---|---|---|
| 01 | GMIWm5y90xA | Code with Claude 2026: Opening Keynote | NO-CAPTIONS |
| 02 | 7xco5Qd2Oo8 | A conversation with Dario Amodei & Daniela Amodei | NO-CAPTIONS |
| 03 | IMZa42k6L6M | What's new in Claude Code | NO-CAPTIONS |
| 05 | y5TmF_6o6xk | Caching, harnesses, and advisors: Building on Claude at GitHub scale | NO-CAPTIONS |
| 06 | E9gaQHrw_rg | How to get to production faster with Claude Managed Agents | NO-CAPTIONS |
| 07 | OFDm3T7pVlc | Building AI-native: Inside the stacks powering Cognition, Gamma, and Harvey | NO-CAPTIONS |
| 08 | 7oO37GRhwGk | Getting more out of the Claude Platform | NO-CAPTIONS |
| 09 | EdmuYPBt_EM | How Datadog built a universal machine tool for Claude Code | NO-CAPTIONS |
| 10 | tP4MGcJ80Y0 | The capability curve | NO-CAPTIONS |
| 11 | bJKdXhnw7NU | Architecting for model step-changes: A fireside with Vercel's Guillermo Rauch | NO-CAPTIONS |

### Product Launches

| Idx | Video ID | Title | Status |
|---|---|---|---|
| 01 | m7TJqx8CYG8 | Artifacts in Claude Code: share your work as it happens | NO-CAPTIONS |
| 03 | 7-1tNo8HAwk | New agents for legal professionals \| Claude Cowork | NO-CAPTIONS |
| 04 | -INveHwbRz4 | Introducing agent view in Claude Code | NO-CAPTIONS |
| 07 | Gen8rG40ntA | Claude now connects to Autodesk Fusion | NO-CAPTIONS |
| 08 | LZMWsZbZU5w | Claude now connects to Blender | NO-CAPTIONS |
| 09 | U9jGOz_Lcbo | All your everyday apps, in one conversation | NO-CAPTIONS |
| 10 | rWaQSQEm_aY | The new Claude Code desktop app, redesigned for parallel agents | NO-CAPTIONS |
| 15 | NAwvkrxompk | Your apps come alive on Claude mobile | NO-CAPTIONS |
| 16 | NAauIR6JFps | Put Claude to work on your computer, from anywhere | NO-CAPTIONS |
| 21 | cIctgHKEeMA | One conversation across Claude for Excel and PowerPoint | NO-CAPTIONS |
| 22 | OKC1qUJA4Fc | One conversation across Claude for Excel and PowerPoint | NO-CAPTIONS |
| 24 | v5IOHK5xFlc | Cowork and Plugins: Helping enterprises move faster | NO-CAPTIONS |
| 26 | orTd3grSYsQ | Claude for everyday work | NO-CAPTIONS |
| 27 | 1z3nazC3LK0 | (title unavailable) | REMOVED |

### How Anthropic uses Claude

| Idx | Video ID | Title | Status |
|---|---|---|---|
| 06 | UE4C06a7QqY | (title unavailable) | PRIVATE |

## Backfill note

The 40 `NO-CAPTIONS` videos are recent uploads YouTube has not auto-captioned yet; they become downloadable once captions are generated. Re-run the auth script periodically — it re-scans each playlist (`skip_if_done=False`) and skips VTTs already on disk:

```
python3 download_playlists_auth.py "Claude" www.youtube.com_cookies.txt
```

`REMOVED` and `PRIVATE` videos will not become available through these tools.
