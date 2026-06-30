---
title: "Generator-Evaluator Pattern"
type: concept
tags: [ai, agents, harness, evaluation, adversarial, long-running-agents, anthropic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
The Generator-Evaluator Pattern is a harness architecture for long-running autonomous agents where the builder (generator) and QA critic (evaluator) run in separate context windows with adversarial pressure, inspired by Generative Adversarial Networks (GANs). The evaluator uses live browser testing (via Playwright) to grade output against a detailed rubric, then passes critique back to the generator for iterative improvement. The key insight: tuning a standalone critic to be harsh is tractable; tuning a builder to be self-critical is not.

## Key Information
- **GAN Inspiration**: Shamelessly stolen from GANs — generator builds, discriminator/evaluator grades, adversarial pressure between them drives quality improvement
- **Separate Context Windows**: Generator and evaluator get separate context windows, system prompts, and jobs — no shared thoughts or muddying between streams
- **Live Testing**: Evaluator doesn't just read diffs — it uses Playwright to open live pages, click around, try things out, then hands back critique
- **Why It Beats Self-Evaluation**: Tuning a standalone critic to be harsh is tractable; tuning a builder to be self-critical is not. Human analogy: it's easy to critique artwork or a meal, much harder to create it yourself
- **Course Correction**: When generator gets stuck on one criterion (e.g., low originality), the harness throws everything out and starts from scratch. Single-pass generation or RALPH loops keep patching the same broken thing
- **Pivoting Behavior**: The ability to throw away work and restart is unique to this pattern — something not seen in solo loops where the generator is "proud of its own work"
- **Contract Negotiation**: Before any code is written, generator and evaluator negotiate what "done" means via files on disk. Generator proposes features and tests; evaluator pushes back on scope, test strength, edge cases. Iterate until both agree. Evaluator grades against the contract, not the original spec
- **Three-Role Extension**: Full architecture adds a Planner (PM) that breaks one-line prompts into high-level sprints without over-specifying technical details. Mirrors PM/IC/QA org structure
- **QA Agent Tuning**: Claude out-of-the-box is a bad QA agent — sycophancy causes it to find bugs then say "fix it later." Requires extensive prompt tuning by reading traces and adjusting where agent judgment diverges from human judgment
- **Retro Forge Demo**: Same prompt, same model. Solo loop: play mode broken. Generator-evaluator (6h, ~$200): working game with physics, collision detection, AI-level assistant. 27 contract criteria between agents
- **Rubric-Based Evaluation**: Four criteria — design, originality, craft, functionality — weighted toward design and originality. Calibrated with few-shot examples to converge evaluator taste with human taste
- **Cost**: Currently very expensive (~$200 for 6 hours) and slow, but results are "startlingly different" from solo loops
- **Simplification Over Time**: As models improve, harness simplifies. Opus 4.5 needed evaluator at every sprint; Opus 4.6 runs evaluator only at end of generation

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Ash Prabaker]] — presenter
- [[Self-Evaluation Trap]] — the problem this pattern solves
- [[Contract Negotiation]] — key sub-mechanism
- [[Rubric-Based Evaluation]] — grading framework used by evaluator
- [[Adversarial Evaluation]] — related concept
- [[RALPH Loop]] — predecessor pattern compared against
- [[Harness Evolution]] — how the pattern simplifies as models improve
- [[Playwright]] — browser automation used for live testing
- [[Agent Harness]] — broader category
- [[File System as Shared State]] — inter-agent communication mechanism
- [[Sprint Decomposition]] — planner role's function
- [[GANs]] — inspiration source (Generative Adversarial Networks)
