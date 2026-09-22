---
title: "Moore's Law"
type: concept
tags: [semiconductors, scaling, computer-architecture, transistors]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---
## Definition
Moore's Law is Gordon Moore's observation — originally yearly, later amended to every two years — that the number of transistors on a chip doubles, which guided semiconductor manufacturing and CPU performance for about 50 years.
## Key Information
- Patterson traces the whole microprocessor story through Moore's law: early believers expected the microprocessor to eventually be "a serious computer" as transistors doubled.
- The law worked as an industry-wide guideline: manufacturers asked "how are we going to build the equipment" to deliver the doubling, coordinating the entire semiconductor business.
- Patterson says it has ended — transistors no longer double, and "if people assume [leaving Moore's law] means technology is not improving, that's not the same thing."
- Improvement is now non-uniform: logic gates still improve, static RAM (SRAM) "hardly improves at all," and DRAM density used to quadruple every ~3 years but now takes ~10 years.
- Advanced packaging (chiplets, or two full-reticle dies per package) still adds transistors to a package, which some — Patterson references Jim Keller's "Moore's law isn't dead" — cite as continuation, but Patterson says "just look at the data" doesn't back that up; he notes an emotional/identity dimension for manufacturers who "make Moore's law" their career.
- Its slowdown, after Dennard scaling already ended ~2005, is what pushed architects to domain-specific architectures around 2015.
## Related
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[Dennard Scaling]] — its power companion
- [[Computer Architecture]] — the field it guided
- [[Domain-Specific Architecture]] — the response to its end
