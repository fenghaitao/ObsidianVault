---
title: "Client File Upload"
type: concept
tags: [api, gemini, file-upload, google, developer-experience]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29

---

## Definition
Client File Upload is a Gemini Developer API feature that simplifies file ingestion by handling upload, storage, and model access in a single call. It abstracts away the complexity of Vertex AI's bucket and ACL management, making files immediately accessible to the model.

## Key Information
- **Purpose**: Hide Vertex AI complexity (creating buckets, setting ACLs, managing permissions) from developers
- **Usage**: Upload a file (e.g., a full book from Project Gutenberg) and the model can immediately reference it in context
- **Contrast with Vertex AI**: Vertex AI requires explicit bucket creation, ACL configuration, and access management; Client File Upload handles all of this transparently
- **Limitation**: The file is re-sent with each chat turn when using chat mode, increasing latency and cost for large files
- **Interactions API improvement**: The newer Interactions API uses server-side state and automatic caching, eliminating the need to re-upload context on each turn
- **Use case in workshop**: Uploading entire books (The Wind in the Willows) to Gemini's large context window for character and scene prompt generation

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[Gemini]] — model using the feature
- [[GeminiInteractionsAPI]] — newer alternative
- [[VertexAI]] — enterprise platform with more complex file handling
- [[Project Gutenberg]] — source of uploaded books
