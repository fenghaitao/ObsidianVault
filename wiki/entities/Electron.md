---
title: "Electron"
type: entity
tags: [technology, framework, desktop-app, javascript, chromium, nodejs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Building your own software factory — Eric Zakariasson, Cursor.md"]
last_updated: 2026-06-29
---

## Definition
Electron is a framework for building cross-platform desktop applications using JavaScript, HTML, and CSS. It combines a Chromium rendering engine with a Node.js backend, split into a main process (system APIs) and a render process (front-end UI).

## Key Information
- **Architecture**: Main process handles system APIs; render process is the front-end (Chromium-based)
- **IPC (Inter-Process Communication)**: Communication layer between main and render processes
- **Single instance limitation**: Desktop apps built with Electron can only run one instance at a time, creating friction for parallel testing of multiple feature variants
- **Granola's web shell approach**: Abstracted IPC APIs to fall back to web standards when running in a web environment, making the render process agnostic of Electron so it can run as a standalone web app
- **Cursor's internal stack**: Uses Electron as part of its desktop application, with internal tools abstracting complex service startup (OrbStack, ClickHouse, Postgres, Redis, Electron, Glass)
- **Tauri comparison**: Granola evaluated Tauri as an alternative but didn't see massive performance gains, which is their primary concern; Electron's APIs continue to serve them well

## Related
- [[Granola]] — uses Electron for their meeting notes desktop app
- [[Web Shell Pattern]] — pattern for converting Electron apps to web-deployable front-ends
- [[Cursor]] — uses Electron for their desktop IDE
- [[summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola]] — source
- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — source
