---
title: "Behavior Calibration"
type: concept
tags: [AI, product-design, agent, reliability]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Behavior calibration is the ongoing process of understanding and refining how an AI system behaves in production. It is the core activity of the Continuous Calibration loop in the CCCD framework — analyzing unexpected behavior, spotting error patterns, applying fixes, and designing new evaluation metrics for emerging patterns.

## Key Information

- **Core idea**: "With AI systems, it's all about behavior calibration. It's incredibly impossible to predict up front how your system behaves."
- **The goal**: Minimize surprise — don't ruin customer experience or erode trust while calibrating.
- **How it works**: Deploy with high human control, log what humans do (creating free error analysis), and use that data to improve the system.
- **Calibration frequency**: Calibrate every 1-2 days. When you stop seeing new data distribution patterns and users are consistent, you're ready to increase agency (move to the next stage).
- **Recalibration triggers**: Model deprecation (e.g., GPT-4o → GPT-5), users evolving their behavior (trying the system on new tasks), and new data distributions.
- **Example**: An underwriting AI system was calibrated and working well for 3 months, then users started asking "for a case like this, what did previous underwriters do?" — a natural extension that required significant recalibration because the system now needed to understand what "like this" means (income range? geo? etc.).
- **The Air Canada lesson**: Without proper behavior calibration, an AI agent hallucinated a refund policy and the company was legally forced to honor it.

## Related

- [[Continuous Calibration Continuous Development (CCCD)]] — the framework this is part of
- [[Agency-Control Trade-off]] — how you constrain autonomy during calibration
- [[AI Flywheel]] — the improvement mechanism built through calibration
- [[Evals (Evaluation Metrics)]] — catch known errors; calibration catches unknowns
- [[Production Monitoring (AI)]] — provides the signals for calibration
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
