---
title: "MonitoredVsUnmonitoredCapabilities"
type: concept
tags: [ai-safety, capabilities, monitoring, evaluation, time-horizon]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md"]
last_updated: 2026-06-26
---

## Definition
Monitored vs. Unmonitored Capabilities is the distinction between what AI can accomplish under close safety monitoring (by other AIs or humans reviewing transcripts) versus without monitoring. Safety controls may reduce effective time horizon by 1-2 orders of magnitude.

## Key Information
- Proposed by Joel Becker as a way to extend the useful range of time horizon measurements
- If AI can do 40-hour tasks without monitoring but only 2-hour tasks while being watched closely, safety monitoring effectively buys "a load more doublings" before dangerous capabilities emerge
- Monitoring could involve other AI models reviewing transcripts of AI work for suspicious activity, with escalation to humans
- This approach acknowledges that fooling monitors may not be impossible but would be challenging
- Becker expects monitoring to reduce effective time horizon by "maybe an order of magnitude or two"
- There is tension: publishing this insight might encourage labs to focus less on safety or argue against safety because it "impacts capability"
- Some model shops likely already evaluate capability with and without safety controls due to internal debates between researchers and safety teams

## Related
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[TimeHorizon]] — the metric this concept extends
- [[CapabilityExtrapolation]] — broader framework this fits into
- [[JoelBecker]] — proposed this concept
- [[METR]] — organization exploring this approach
