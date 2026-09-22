---
title: "RISC vs CISC"
type: concept
tags: [computer-architecture, ISA, RISC, CISC]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---
## Definition
RISC (Reduced Instruction Set Computer) vs CISC (Complex Instruction Set Computer) was the 1980s debate over whether microprocessors should expose a few simple instructions or many sophisticated, high-level ones.
## Key Information
- Context: 1970s microprocessors were toys, and Intel/TI designers simply imitated the big companies (IBM mainframes, DEC minicomputers) that built ever more sophisticated instruction sets to "raise the level of abstraction" toward software.
- The analogy Patterson uses: CISC is a vocabulary full of "polysyllabic" words, RISC a vocabulary of "monosyllabic" words — the empirical question was the ratio of how many more instructions you need versus how much faster each runs.
- Outcome: RISC needs ~30-40% more instructions but executes them 4-5x faster, for a net ~3-4x speedup over CISC.
- Underlying mechanism: CISC carried a microcode interpreter; RISC skipped it by compiling directly into simpler instructions (see Microprogramming).
- The compiler was central: early compilers allocated registers so poorly that C added programmer register hints; as register allocation improved, RISC's many registers (32 vs CISC's 8-16) paid off, and compilers rarely used the sophisticated CISC instructions in the first place.
- Who won: Patterson calls the nostalgic verdict "CISC won" myopic — it holds only for the PC era, when binary software distribution locked in x86 (which survived by translating x86 to RISC micro-ops in hardware, worth the overhead for the software base). In the post-PC era RISC won decisively: ARM dominates mobile, Apple switched, and ARM is entering the cloud.
- Transcription note: the auto-transcript consistently writes "RISC" as "risk" and "CISC" as "CISK"; normalized throughout.
## Related
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[David Patterson]] — a principal in the debate
- [[Hennessy & Patterson]] — the RISC champions
- [[Arm]] — the commercial RISC winner
- [[Computer Architecture]] — the field
- [[Microprogramming]] — the CISC control overhead
