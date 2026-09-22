---
title: "Dennard Scaling"
type: concept
tags: [semiconductors, scaling, power, computer-architecture]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---
## Definition
Dennard scaling is Bob Dennard's observation that, as transistors shrink and are added, lowering the threshold voltage keeps power roughly constant — explaining why chips with more transistors didn't get hotter.
## Key Information
- Named for Bob Dennard (transcribed "Bob Dinard"), who observed that lowering the threshold voltage (the 0/1 distinction) has a ~squared effect, so doubling transistors while lowering voltage kept microprocessors at roughly 20-30 watts.
- Patterson and Hennessy's 1990 textbook didn't discuss power as an issue for its first three editions — a direct consequence of Dennard scaling still working.
- Around 2005 Dennard scaling stopped, which was "a shock"; Intel actually had a microprocessor generation fail because it couldn't get the power down and ran too hot.
- Its end forced the industry from "one very sophisticated processor" to multicore — two, then four, then eight simpler cores — and shifted the burden of Moore's-law improvements onto programmers parallelizing their code.
## Related
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[Moore's Law]] — the scaling law it complemented
- [[Computer Architecture]] — the field it shaped
- [[Domain-Specific Architecture]] — one consequence of its end
