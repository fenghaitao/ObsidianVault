---
title: "summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md"]
last_updated: 2026-09-14
---

## Core Summary

Barbara Liskov recounts how the 1970s software crisis led her to invent data abstraction — the idea of a module with a hidden implementation exposed only through operations — codified in the CLU language and later formalized as the Liskov substitution principle. She then traces her distributed-systems work (Argus, Viewstamped Replication, Byzantine fault tolerance) and reflects on research direction, the cost of incremental work, and the gender barriers she faced in a hostile field.

## Key Points

- Rejected by Princeton's graduate program with a postcard reading "We do not admit women," she turned to Berkeley, then to a programming job that pulled her into computer science "by a happy accident."
- The software crisis: companies spent millions and man-years on big programs that had to be thrown away because no one knew how to build modular systems; procedures were the only modularity mechanism and didn't match real modules.
- Data abstraction: a module provides an interface of operations with a hidden implementation whose data is inaccessible from outside — the idea from her Mitre work, sketched with Steve Zilles and realized in CLU, later reaching industry via Ada and Java.
- Encapsulation is crucial to modularity: "your team is really only as strong as your weakest programmer," so the compiler should make bad behavior impossible — which Python, for instance, does not enforce.
- Entered distributed computing after reading Bob Kahn's paper; Argus was a CLU-influenced object-oriented language whose guardians communicated via remote procedure calls and whose computations ran as atomic transactions borrowed from databases.
- Viewstamped Replication (with Brian Oki) solved replicated-storage leader changeover and was, she says, the beginning of cloud storage; it independently matches Lamport's Paxos, which Google's File System actually used.
- The Liskov substitution principle came from her 1986 OOPSLA keynote: a subclass must behave like its superclass where the superclass is expected; formalized with Jeannette Wing as behavioral subtyping.
- On Dijkstra: "Go To Statement Considered Harmful" was a letter to CACM arguing reasoning about code correctness is hard; he was "not always as tactful as he might be," but won the argument.
- Research advice to students: don't do incremental work; find a good problem that is amenable to solution and matches your skill set, and recognize when a direction is bad. Tenure is judged by the research community.
- On the Turing Award backlash ("why did she get it?"), she reads it as a compliment: data abstraction and modularity became so foundational that people forgot there was a "before."

## Related

- [[Barbara Liskov]] — the guest
- [[Data Abstraction]] — her foundational idea
- [[Modularity]] — the problem she helped solve
- [[Liskov Substitution Principle]] — the principle named after her
- [[Viewstamped Replication]] — her consensus protocol
- [[Byzantine Fault Tolerance]] — the later protocol she co-developed
- [[Edsger Dijkstra]] — the correspondent she discusses
- [[Leslie Lamport]] — independently developed Paxos
- [[Alan Kay]] — parallel Smalltalk work on the West Coast
- [[Jeannette Wing]] — co-author on behavioral subtyping
- [[John Guttag]] — MIT colleague
- [[Steve Zilles]] — co-author on the data abstraction paper
- [[Brian Oki]] — Viewstamped Replication student
- [[Miguel Castro]] — Byzantine fault tolerance student
- [[Bob Kahn]] — whose paper inspired her distributed work
- [[Princeton University]] — rejected her as a woman
- [[MIT]] — where she spent her faculty career
- [[MITRE]] — where she invented her modularity notion
- [[Paxos]] — the equivalent of Viewstamped Replication
- [[Abstraction]] — the broader concept
- [[Distributed Systems]] — the field she advanced
