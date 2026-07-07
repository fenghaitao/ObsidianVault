---
title: "AppleRealityKit"
type: entity
tags: [apple, ar, 3d-scanning, framework, developer-tool]
sources: []
last_updated: 2026-07-07
---

## Definition

Apple RealityKit is Apple's framework for building augmented reality (AR) experiences, including 3D object capture and scene rendering. It enables developers to scan physical objects with a phone camera and bring them into digital environments as 3D assets.

## Key Information

- Used in the [[CustomUniverse]] pipeline to capture phone-scanned objects for 3D reconstruction during the [[ClaudeOpus4.8]] Build Day hackathon (June 2026).
- Phone-scanned objects captured with RealityKit are brought into a web app where [[ClaudeOpus4.8]] handles the 3D reconstruction and scene rendering pipeline.
- Part of Apple's AR development ecosystem, which also includes ARKit and the [[AppleFoundationModels|Foundation Models framework]].
- The [[CustomUniverse]] team used [[Claude]] to research and integrate RealityKit, which was an unfamiliar technology for them, demonstrating Claude's ability to help developers adopt new frameworks.
- Enables the phone-photo-to-3D-object pipeline that underpins [[SyntheticData|synthetic training data]] generation for robotics labs.

## Related

- [[CustomUniverse]] — hackathon project using RealityKit for phone-to-3D object capture
- [[SyntheticData]] — the broader use case enabled by RealityKit-based object capture
- [[AppleFoundationModels]] — another Apple framework that integrates with Claude
- [[ClaudeOpus4.8]] — the model that built the pipeline incorporating RealityKit
- [[NVIDIAH100]] — GPU hardware that processed RealityKit's captured output
- [[Anthropic]] — hosted the hackathon where RealityKit was used
