---
title: "Continuous Calibration Continuous Development (CCCD)"
type: concept
tags: [AI, framework, product-development, lifecycle, methodology]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Continuous Calibration Continuous Development (CCCD) is a framework for building AI products, created by Aishwaria Raanti and Kiti Bottom. It is a homage to CI/CD (Continuous Integration/Continuous Deployment) adapted for AI, where the "calibration" phase replaces the simple integration-and-deploy loops with ongoing behavior analysis, error pattern detection, and evaluation metric refinement.

## Key Information

- **Created by**: [[Aishwaria Raanti]] and [[Kiti Bottom]], based on their experience with 50+ AI product deployments
- **Two loops**:
  - **Continuous Development (right side)**: Scope capability → Curate data → Set up application → Design evaluation metrics → Deploy → Run evaluation metrics
  - **Continuous Calibration (left side)**: Analyze behavior → Spot error patterns → Apply fixes → Design new evaluation metrics for emerging patterns → Feed back into development
- **The calibration loop**: Catches behavior you hadn't expected in the beginning. Evaluation metrics only catch errors you already know about. Production monitoring catches emerging patterns.
- **Data curation is critical**: Before building, create a dataset of expected inputs and outputs. This exercise often reveals that team members are not aligned on how the product should behave.
- **Not all errors need new metrics**: Some errors are spot fixes (e.g., a tool calling error due to a poorly defined tool) — just fix and move on.
- **Lower agency iterations first**: While going through iterations, constrain the number of decisions AI systems can make and keep humans in the loop. Increase agency over time as you build a flywheel of behavior understanding.
- **Recalibration is ongoing**: Model deprecation (GPT-4o → GPT-5), changing user behavior, and new use cases can all require recalibration.
- The framework was born from a painful experience: building an end-to-end customer support agent that required so many hotfixes they had to shut it down.

## Related

- [[Agency-Control Trade-off]] — the progression embedded in CCCD
- [[Behavior Calibration]] — the core calibration activity
- [[AI Flywheel]] — the improvement mechanism CCCD builds
- [[Evals (Evaluation Metrics)]] — the evaluation metrics within CCCD
- [[Production Monitoring (AI)]] — the calibration data source
- [[Aishwaria Raanti]] — co-creator
- [[Kiti Bottom]] — co-creator
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
