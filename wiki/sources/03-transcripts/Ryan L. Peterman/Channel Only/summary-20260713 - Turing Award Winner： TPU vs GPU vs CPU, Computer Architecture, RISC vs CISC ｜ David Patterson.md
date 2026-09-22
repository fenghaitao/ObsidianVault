---
title: "summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---
## Core Summary
David Patterson, Turing Award-winning computer architect, retells the RISC vs CISC debate and argues that RISC decisively won in the post-PC era — ARM now dominates mobile (350 billion chips shipped), Apple switched from x86, and ARM is entering the cloud while the x86 market shrinks. He explains the deeper mechanism (Maurice Wilkes' microprogramming versus compiling directly into simple instructions) and the role of improving compilers and plentiful registers. With Dennard scaling ending around 2005 and Moore's law slowing in the 2010s, general-purpose CPUs stagnated, so the industry turned to domain-specific architectures: Nvidia repurposed GPUs for machine learning via CUDA, and Google's TPU (debuted 2016) was the watershed that showed dedicated ML hardware could beat CPUs and GPUs. He closes with career and life lessons — family first, happiness over wealth, courage, optimism, and finishing.
## Key Points
- RISC vs CISC history: 1970s microprocessors were toys; Intel and TI designers imitated IBM mainframes and DEC minicomputers, which piled on increasingly sophisticated (complex) instruction sets to "raise the level of abstraction."
- The debate was partly philosophical because it couldn't be settled quantitatively — like "how many angels on the head of a pin" — until measurements showed RISC needs ~30-40% more instructions but runs them 4-5x faster (a net ~3-4x speedup).
- Mechanism: the hard part was control; Maurice Wilkes invented microprogramming (control signals stored as "microinstructions"), which CISC used as an interpreter — RISC skipped the interpretation and compiled directly, and no one has designed an ISA needing a microcoded interpreter in the last 20 years.
- Compilers' role: early compilers allocated registers poorly (so C let programmers give register hints), but the algorithms improved; CISC chips had 8-16 registers, RISC put in 32, and compilers rarely used the sophisticated CISC instructions anyway.
- Verdict: "CISC won" is myopic — true only for the PC era when binary software distribution locked in x86; x86 survived by translating to RISC micro-ops in hardware. Post-PC, RISC won: ARM (Acorn's RISC Machine, adopted by Apple/Nokia) dominates mobile, ~99% of processors are RISC, Apple switched, and Amazon/Microsoft/Google build ARM for the cloud.
- Dennard scaling (why chips didn't heat up as transistor counts doubled): lowering threshold voltage has a ~squared effect, keeping CPUs at ~20-30W; its end ~2005 forced multicore (2→4→8 simpler cores) instead of one faster core.
- Moore's law slowed in the 2010s; ~2015 architects turned to domain-specific architectures — a CPU must run everything, but a specialized chip (GPU, TPU) shuffles resources to do one narrow class of programs far more efficiently.
- GPUs (~2000) were the first domain-specific architectures: no virtual memory, no compiler support, graphics only, highly multithreaded with 16/32-bit float — cheap with excellent floating-point performance per dollar; Jensen Huang (transcribed "Jensen Wang") funded CUDA in 2006 to make them programmable.
- AlexNet (2012): a CUDA-trained neural network at the University of Toronto "crushed" the image-recognition competition, and within a few years everyone switched to neural nets running on GPUs.
- TPU design: Google started from a clean slate (no graphics) — a giant matrix-multiply unit at the heart, no hardware cache (software schedules memory because ML knows its access pattern), and bfloat16 (Brain Float 16), the first float format with a larger exponent than fraction, prioritizing range over precision.
- TPU impact: ~30x better than a contemporary GPU and ~80x better than a CPU at inference; the 2016 debut was the watershed that made the whole industry design ML-specific hardware (Intel bought companies, Nvidia adapted, hyperscalers built their own).
- Continued gains: no single simplifying guideline now — advanced packaging (chiplets, two full-reticle dies), keeping transistors close, narrower floats (8-bit, 4-bit), and bigger matrix-multiply units; Google's training-TPU block diagram has stayed essentially constant for a decade.
- Benchmarks and moat: MLPerf (SPEC-inspired) is used less because Nvidia runs it best; Nvidia's "CUDA moat" is the language plus continually tailored libraries plus engineering headcount — hard for startups (and Google) to match.
- Career/life advice: "How to have a bad career" (teach via negation); family first ("no one on their deathbed wishes they'd spent more time in the office"); choose happiness over wealth; finish things ("it's not how many things you start, it's how many you finish"); courage ("fortune favors the bold"); optimism (the going-steady story, married 59 years); the "nine magic words" — "I was wrong. You were right. I love you."; his one regret is not noticing harassment of young women at SIGARCH conferences when he chaired one.
- Transcription notes: the auto-transcript renders "RISC" as "risk", "CISC" as "CISK", "Moore's law" as "Morris law", "Dennard scaling" as "dinard scaling", "Jensen Huang" as "Jensen Wang", and "Maurice Wilkes" as "Maurice Welks"; these are normalized throughout the wiki pages.
## Related
- [[David Patterson]] — guest
- [[Hennessy & Patterson]] — the collaboration and textbook
- [[Arm]] — RISC's dominance in mobile and cloud
- [[Turing Award]] — the award he won
- [[Tensor Processing Unit (TPU)]] — Google's ML accelerator
- [[Google]] — where the TPU was built
- [[Nvidia]] — the GPU/CUDA context
- [[UC Berkeley]] — Patterson's university
- [[Computer Architecture]] — his field
- [[RISC vs CISC]] — the historic debate
- [[Moore's Law]] — its end drives specialization
- [[Dennard Scaling]] — why power stayed flat
- [[Domain-Specific Architecture]] — the post-Moore direction
- [[Microprogramming]] — the control technique at stake
- [[How to Have a Bad Career]] — his career advice
