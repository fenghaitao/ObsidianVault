---
title: "summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Core Summary

Leslie Lamport, Turing Award winner, recounts the stories behind his foundational distributed-systems papers: the bakery algorithm, logical clocks and the "happens before" relation, the Byzantine generals problem, and Paxos. He argues that abstraction, state machines, and writing correct proofs — not raw "smartness" — are what actually made his contributions work, and reflects on working with Edsger Dijkstra and why people find Raft easier than Paxos.

## Key Points

- The bakery algorithm solved Dijkstra's mutual-exclusion/critical-section problem; inspired by a deli ticket system, it was the first first-come-first-served solution and worked even if a reader caught a value mid-write — surprising enough that colleague Anatol Holt refused to believe the proof.
- He started with a two-process solution that had a bug (caught by a CACM editor), which taught him concurrent programs are hard and "you needed a proof that they were correct."
- He spent a month in the Netherlands with Dijkstra (via colleague Carel Scholten); his simplification of Dijkstra's concurrent garbage-collection free-list earned him authorship, and Dijkstra later called his gift "a remarkable ability at abstraction."
- "Time, Clocks, and the Ordering of Events in a Distributed System" defined "happens before" by analogy to special relativity — an event precedes another if information could have traveled between them — and introduced the state-machine idea, which readers largely ignored.
- The Byzantine generals problem (named, with a catchier story, after the Chinese generals problem) showed that tolerating one arbitrary fault requires four processes without digital signatures, three with them; it mattered because computers were about to fly airplanes.
- Paxos grew from not believing DEC SRC's fault-tolerant storage system was possible: "that isn't a proof, it's an algorithm"; the algorithm preceded the "Part-Time Parliament" paper by eight years, and only Butler Lampson understood its importance.
- He distinguishes algorithms from programs: an algorithm is the abstract synchronization kernel you should design before writing code, and state machines are the right abstraction for concurrency.
- On Raft vs Paxos: he was sent the draft and asked for an algorithm/a proof; he sees Raft as Paxos with the two-phase structure told in the opposite, more comfortable order — but "a bug was discovered in Raft and fixed," and he suspects the "more understandable" version was the buggy one.
- Understanding, for him, means being able to write a proof; for most people it means "a warm fuzzy feeling" — hence the appeal of Raft and the fear mathematicians showed toward his hierarchical proof structure ("stupid people think they're smart because they're too stupid to realize they're not").
- He built LaTeX from TeX macros so he could write a book; the instruction-manual-before-code maxim forced him to change LaTeX where it was hard to explain.
- His maxim: "if you think you know something but don't write it down, you only think you know it."
- On his gift: not raw intelligence but abstraction, which he only recognized in his last decade; he never found the "Turing machine of concurrency," and now thinks state machines are effectively it — while rejecting language-centered approaches.
- Asked what advice he'd give his younger self, he declined: "I shouldn't waste time trying to answer questions that I don't have to answer."

## Related

- [[Leslie Lamport]] — guest
- [[Edsger Dijkstra]] — whose problem and EWDs shaped his early work
- [[Butler Lampson]] — the colleague who grasped Paxos's importance
- [[Whitfield Diffie]] — friend whose digital signatures seeded his toolkit
- [[Xerox PARC]] — where Lampson and Thacker built personal computing
- [[DEC Systems Research Center]] — where Paxos was developed
- [[SRI International]] — where the Byzantine generals work was done
- [[LaTeX]] — the typesetting system he created
- [[Turing Award]] — the prize for his contributions
- [[Paxos]] — his fault-tolerant consensus algorithm
- [[Raft]] — the competing, "more understandable" consensus algorithm
- [[Bakery Algorithm]] — his mutual-exclusion solution
- [[Byzantine Generals Problem]] — arbitrary-fault tolerance
- [[Logical Clocks]] — the happens-before/ordering contribution
- [[State Machine]] — the abstraction he champions
- [[Distributed Systems]] — the field his work founded
- [[Abstraction]] — his self-identified gift
- [[Writing as Communication]] — "thinking without writing"
