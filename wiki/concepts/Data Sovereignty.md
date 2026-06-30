---
title: "Data Sovereignty"
type: concept
tags: [privacy, europe, regulation, google, cloud, data-governance, gdpr]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29

---

## Definition
Data Sovereignty refers to the requirement that data be stored and processed within a specific geographic region, particularly relevant in Europe where GDPR and similar regulations mandate EU-based data handling. For AI models, this creates availability gaps when models are only accessible via global (non-EU) endpoints.

## Key Information
- **European context**: EU regulations require data to be processed within EU data centers for many organizations
- **Google Cloud limitation**: Preview models are only available on global endpoints, not EU regional endpoints
- **Impact**: European companies cannot access the latest GenMedia models (Nano Banana 2, newer Gemini versions) while they remain in preview
- **Stuck on old models**: Some European companies are still on Nano Banana 1 because newer models haven't reached GA
- **Developer Advocate priority**: Guillaume Vernade identified this as his top advocacy priority ("P0 thing") within Google DeepMind
- **Root cause**: Google Cloud policy that preview models only run on global endpoints, combined with rapid release cycles that reset the preview-to-GA timeline

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[Model Preview vs GA]] — related lifecycle concept
- [[Guillaume Vernade]] — advocate
- [[GenMedia]] — affected product suite
- [[GoogleDeepMind]] — organization
