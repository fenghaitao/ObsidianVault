---
title: "Agency-Control Trade-off"
type: concept
tags: [AI, product-design, agent, autonomy, control]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

The agency-control trade-off is the principle that every time you give an AI system more autonomy (agency) to make decisions, you relinquish some amount of control over the outcome. AI systems must earn trust over time before being granted more autonomy. This is one of the two fundamental differences between AI and traditional software products.

## Key Information

- **Core trade-off**: More agency for the AI = less control for the human. You want to make sure the agent has earned trust before allowing it to make decisions.
- **Start with high control, low agency**: Don't start with fully autonomous agents on day one. Begin where there is minimal impact and more human control.
- **Progression model**: V1 = suggestions only (routing, drafting), V2 = co-pilot with human review, V3 = autonomous action. You don't "hike Half Dome on day one — you train in minor parts."
- **Examples of the progression**:
  - **Coding assistant**: V1 = inline completion suggestions, V2 = generate larger blocks for human review, V3 = apply changes and open PRs autonomously
  - **Marketing assistant**: V1 = draft emails/social copy, V2 = build multi-step campaigns, V3 = launch, AB test, and auto-optimize across channels
  - **Customer support**: V1 = route tickets to right department, V2 = provide draft suggestions for human agents, V3 = end-to-end resolution with refunds/feature requests
- **Ways to constrain autonomy**: (1) By number of actions the agent takes, (2) by topic/domain risk level, (3) by having pre-authorization layers (e.g., low-risk MRIs auto-approved, high-risk surgeries need human review)
- **When to move to the next stage**: When you're no longer seeing new data distribution patterns — when the amount of new information gained is very low. "It's all about minimizing surprise."
- **Recalibration triggers**: Model deprecation (e.g., GPT-4o → GPT-5), changing user behavior over time, new unexpected use cases.
- This trade-off is why "it's not about being the first company to have an agent — it's about having the right flywheels in place."
- The [[UC Berkeley]]/[[Data Bricks]] research paper found 74-75% of enterprises cite reliability as their biggest problem — explaining why most AI products today focus on productivity (low autonomy) vs end-to-end agents.

## Related

- [[Non-determinism in AI Products]] — the other fundamental difference
- [[AI Flywheel]] — logging human behavior to build trust
- [[Human-in-the-Loop]] — keeping humans in decision pathways
- [[Behavior Calibration]] — process of calibrating agency
- [[Continuous Calibration Continuous Development (CCCD)]] — framework embodying this trade-off
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
