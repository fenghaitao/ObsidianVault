---
title: "ClaudeOpus4.8"
type: entity
tags: [claude, model, anthropic]
sources: []
last_updated: 2026-07-07
---

## Definition

Claude Opus 4.8 is an Anthropic model and the successor to [[Claude4.7Opus|Opus 4.7]], featured in a dedicated Build Day hackathon (June 2026) and powering Claude Code's [[DynamicWorkflows|dynamic workflows]] feature.

## Key Information

- **Build Day hackathon (June 13, 2026)**: [[Anthropic]] held a 12-hour hackathon in San Francisco with 310 builders (selected from 1,500+ applicants), each given $500 in Claude Opus 4.8 credits. Three winning teams were profiled: [[Tekton]], [[SimFrancisco]], and [[CustomUniverse]].
- **Full-stack project building**: Opus 4.8 was used to build entire projects end-to-end, including both front and back ends. [[SimFrancisco]] had Opus 4.8 write the entire application; [[CustomUniverse]] had it build the project and operate a remote [[NVIDIAH100]] throughout the hackathon.
- **Dynamic workflows (June 2026)**: powers [[DynamicWorkflows|dynamic workflows]] in [[ClaudeCode]], where Claude writes and orchestrates its own multi-agent JavaScript harness on the fly for tasks like classifier routing, fan-out/synthesis, adversarial verification, and parallel competition.
- **Verifier and self-correction loops**: used to run independent verifier sub-agents in isolated context windows with self-correction loops. [[Tekton]] used this pattern to grade 3D reconstructions until all 20 tests passed.
- **Agentic patterns demonstrated**: sub-agent verification, adversarial testing, parallel workflows, evolutionary clustering (SimFrancisco batched 10,000 residents into ~300 personas, cutting inference cost 10-100x), and tool research/selection.
- **Predecessor**: succeeds [[Claude4.7Opus|Claude Opus 4.7]] (April 2026), which introduced the `xhigh` effort level and adaptive thinking.

## Related

- [[Claude4.7Opus]] — predecessor model
- [[Anthropic]] — creator
- [[Claude]] — model family
- [[DynamicWorkflows]] — Claude Code feature powered by this model
- [[ClaudeCode]] — product surface where dynamic workflows run
- [[Tekton]] — hackathon winning project using Opus 4.8 for 3D reconstruction and verification
- [[SimFrancisco]] — hackathon winning project where Opus 4.8 wrote the entire front and back end
- [[CustomUniverse]] — hackathon winning project where Opus 4.8 built the pipeline and operated a remote H100
- [[EvidenceChain]] — verification methodology demonstrated using Opus 4.8
- [[SyntheticData]] — use case demonstrated at the hackathon
- [[SyntheticPopulation]] — use case demonstrated at the hackathon
- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — hackathon source summary
- [[summary-2026-06-02 - A harness for every task dynamic workflows in Claude Code]] — dynamic workflows source summary
