---
title: "File Upload for Agents"
type: concept
tags: [agents, context, api, files]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
File upload for agents is a mechanism for providing documents, images, and data files as context to AI agent tasks, enabling the agent to process, analyze, and act on user-provided content.

## Key Information
- Manus supports three methods: direct file upload (via PUT request), URL attachments (publicly accessible files), and base64-encoded images
- Uploaded files are automatically deleted after 48 hours for privacy; users can also delete them manually at any time
- Supports PDFs, images, JSON, and multimodal content out of the box
- File upload returns a file ID used to attach the file to a task
- URL attachments work automatically — the agent detects file type (e.g., recognizing a PDF despite a .json extension)
- Base64-encoded images enable visual tasks like bug investigation from screenshots
- Files are stored in a database and served via signed URLs
- Particularly useful for sensitive files that should not persist indefinitely

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAPI]] — API providing file upload
- [[Agent Sandbox]] — environment where files are processed
- [[Structured Outputs]] — output format for file analysis results
