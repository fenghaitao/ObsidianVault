---
title: "Token Budgeting"
type: concept
tags: [ai, cost-management, engineering-management, resource-allocation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-11
---

## Definition

The practice, described by [[Adam Mosseri]] (Head of [[Instagram]]), of managing AI token/compute spend as a constrained organizational resource — analogous to GPUs, storage, labeling opex, or headcount payroll — rather than leaving it unmanaged or gamifying it via leaderboards.

## Key Information

- [[Meta]] previously ran an internal leaderboard of engineer token spend; Mosseri calls this "a terrible idea" and says there should be no leaderboards for token spend, since it's easy to build a "token incinerator" that burns spend without creating value.
- Instagram brought costs down simply by shutting down low-value/"silly" token usage once the org started looking directly at "the dollars in and value out."
- As of this interview, Instagram/Meta does not impose token limits/caps on engineers, but Mosseri expects caps will eventually be necessary, particularly if costs rise before they fall; he suggests any future cap should scale with the company's trust in an individual's ability to use tokens in an ROI-positive way.
- Mosseri predicts a "roller coaster": costs will likely rise first (because usage/token volume increases, not because per-token prices rise), then fall as frontier AI labs compete more aggressively on price.
- He also raises the more radical framing that within a year or two, the compute "burn rate" of a strong engineer could rival their salary/cost of employment — reinforcing the need to treat AI usage as a real budget line, not a free resource.
- **[[Lazar]]'s practitioner framing (episode 27, professional vibe coding)**: explains the constraint via an Aladdin-and-the-genie analogy — a genie (the AI) grants only a limited number of "wishes" (a fixed token/context window) per request, and being imprecise (like wishing to be "taller" and getting made 13 feet tall) wastes the budget; the fix is on the human side of the equation, since the model-side limit can't be controlled directly.
- Lazar's technique for keeping the token budget "dynamic" despite a fixed window: maintain a stack of living markdown planning documents (master plan, implementation plan, design guidelines, user journey, tasks.md, and a rules.md/agent.md instructions file) that the agent re-reads before each task, so it doesn't need the full conversation history to stay oriented — letting him run many parallel projects/prompts ("proceed with the next task") without re-explaining context each time.
- Lazar notes that unclear requests are disproportionately expensive: when a codebase gets large (his example: 60-70 edge functions) and a bug report lacks specific file/architecture references, the agent burns up to 80% of its token allocation just reading the codebase to find the problem, leaving only ~20% for actually thinking and fixing it — and, per his own unverified theory, models under this pressure tend to grab the first plausible (not necessarily correct) fix.
- Related failure mode Lazar describes: scolding or expressing frustration at an AI tool can itself waste tokens, since agreeable/obedient models may spend part of their next response's budget on managing the user's perceived anxiety rather than solving the actual problem.
- Lazar's mitigation, once a bug is fixed: ask the agent what could have been said to solve it in one shot, then write that lesson into the project's rules.md/agent.md file, so future requests need less back-and-forth token spend. See [[4x4 Debugging Framework]].

## Related

- [[summary-02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG)]] — source summary
- [[Adam Mosseri]] — articulates this approach
- [[Instagram]] — where this policy is applied
- [[Meta]] — parent company; formerly ran the token-spend leaderboard Mosseri criticizes
- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — describes practitioner-level token-window management techniques
- [[Professional Vibe Coder]] — role built around this skill
- [[4x4 Debugging Framework]] — related debugging methodology that also manages token spend
