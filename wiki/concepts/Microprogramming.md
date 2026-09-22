---
title: "Microprogramming"
type: concept
tags: [computer-architecture, control, ISA, microcode]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---
## Definition
Microprogramming (microcode) is a control technique in which a processor's control signals are stored in memory as "microinstructions" and stepped through, letting one simple interpreter execute a much more complex instruction set above it.
## Key Information
- Invented by computing pioneer Maurice Wilkes (transcribed "Maurice Welks"), who proposed listing all control signals as the output of a memory, with something tracking position to issue them.
- He called the control signals "microinstructions" and their programming "microprogramming"; IBM built such microprogrammed computers in the 1960s, treating control as essentially an interpreter.
- Classically, interpreting versus compiling costs about a factor of 5-10, but read-only memory and the memory latencies of the era made microcode reasonable up through the 1960s-70s.
- Around 1980 the question became whether to keep the microcode interpreter (CISC) or compile directly into those simpler instructions (close to the RISC idea).
- The microinstructions themselves were ~100 bits wide and complex; RISC shortened them into a more natural form to skip the interpretation step.
- Patterson's view: today no one would invent an instruction set sophisticated enough to require a microcoded interpreter — he doubts any ISA designed in the last 20 years needs one.
## Related
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[RISC vs CISC]] — the debate over this overhead
- [[Computer Architecture]] — the field (control was the hard part)
- [[David Patterson]] — who described its rise and fall
