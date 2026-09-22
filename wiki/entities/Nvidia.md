---
title: "Nvidia"
type: entity
tags: [company, GPUs, hardware, accelerators]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260302 - Distinguished Eng： Stack Ranking, Competing with Bezos, Regrets ｜ Bryan Cantrill.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---

## Definition

Nvidia is the proprietary GPU/accelerator company whose "own the whole stack" stance Bryan Cantrill cites to explain why Oxide stays focused on general-purpose CPU compute.

## Key Information

- Cantrill describes Nvidia as executing well but "a pretty proprietary company" that wants to own the whole stack.
- For Oxide's first-principles, hardware-software co-design approach — where you write the lowest layer of software — Nvidia's model is incompatible: the two doors were "compete with Nvidia" or "partner with Nvidia," and Oxide wanted neither.
- Oxide therefore focuses on general-purpose CPU, noting that even GPU-rich AI workloads have substantial attached CPU compute (e.g., the CPU "surfs the web" behind ChatGPT, not the GPU).
- David Patterson: GPUs emerged around 2000 as domain-specific architectures — no virtual memory, no compiler support, built only for graphics — using hardware multithreading and 16/32-bit floating point, which gave cheap, excellent single-precision performance per dollar.
- In 2006 Jensen Huang (transcribed "Jensen Wang") funded CUDA, a C-like proprietary language for the multithreaded GPU; the 2012 AlexNet win on a CUDA-trained GPU at the University of Toronto caused the ML field to switch to neural nets on GPUs.
- Nvidia's advantage is the "CUDA moat" — the language plus continually tailored libraries plus engineering headcount — which makes MLPerf less usable as a neutral benchmark and hard for startups (and Google) to match.

## Related

- [[summary-20260302 - Distinguished Eng： Stack Ranking, Competing with Bezos, Regrets ｜ Bryan Cantrill]] — source summary
- [[Oxide]] — the company that declines to compete or partner with Nvidia
- [[Bryan Cantrill]] — who frames the Nvidia decision
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[Tensor Processing Unit (TPU)]] — Google's rival accelerator
- [[Domain-Specific Architecture]] — the GPU's category
