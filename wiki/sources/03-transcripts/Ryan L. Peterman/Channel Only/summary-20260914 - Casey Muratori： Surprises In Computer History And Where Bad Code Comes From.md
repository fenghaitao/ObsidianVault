---
title: "summary-20260914 - Casey Muratori： Surprises In Computer History And Where Bad Code Comes From"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260914 - Casey Muratori： Surprises In Computer History And Where Bad Code Comes From.md"]
last_updated: 2026-09-23
---

## Core Summary

Casey Muratori traces the origin and later distortion of Donald Knuth's "premature optimization is the root of all evil," arguing the phrase was a context-specific nudge aimed at a 1970s culture obsessed with assembly micro-optimization, not a license to ignore performance. From that history, and from Ivan Sutherland's Sketchpad (which he argues already contained an entity-component-system architecture the OOP world failed to adopt, the "35-year mistake"), he generalizes that bad code comes from not engaging with the actual problem. His larger messages: performance is a trade-off you should be aware of rather than defer, Conway's law is the closest thing software has to an unbreakable law, bottom-up programming beats upfront design, and unexamined AI "vibe coding" risk making already-mediocre software worse.

## Key Points

- "Premature optimization is the root of all evil" came into print around 1974 in Knuth's "Structured Programming with go to Statements," where two threads converged: the late-60s/early-70s software crisis and the newly available execution profiler.
- The phrase stuck because people keep repeating and reinterpreting it; today it is often (mis)read as "don't think about performance until the end," which Casey argues inverts Knuth's meaning of "only optimize what you've measured as mattering."
- Dijkstra's "Go To Statement Considered Harmful" began as "A Case Against the Go-To Statement" from a conference conversation with Brian Randell; editor Niklaus Wirth retitled it clickbait-style and ran it as a letter to the editor to skip refereeing, drawing angry letters.
- Casey's dumpster diving surfaced a 1960s Tony Hoare note he abandoned after Peter Naur dismissed multipass compilers as "easy" — something Casey reads as essentially static single assignment form, possibly ~15-20 years early.
- Sketchpad already solved the cross-cutting "edit one property across many objects" problem in the early 1960s; the OOP era instead took away inheritance hierarchies (via Alan Kay's reading), which Casey calls "the big oops."
- Clean Code / Refactoring-style guidance (tiny functions, dynamic dispatch, "code shouldn't know its types") prevents compilers from inlining, unrolling, and vectorizing — performance trade-offs the books should discuss rather than dismiss as "usually okay."
- Bad code comes from upfront design that never engages the real problem; Casey advocates bottom-up programming where abstractions are extracted from working code rather than imposed from the top.
- Conway's law — products mirror the communication topology that built them — is the one software "law" Casey would bet on, and it extends to AI agents, not just humans.
- NASA's "no recursion" rule is sane for safety-critical code: recursion hides stack-depth bounds, whereas a loop plus explicit stack and a state machine is fully predictable.
- On vibe coding / AI: quality will only get worse if the adoption curve outruns AI capability; the sane approach is to measure the tool and integrate it when it is a net positive.

## Related

- [[Casey Muratori]] — guest
- [[Ryan L. Peterman]] — host
- [[Donald Knuth]] — credited origin of "premature optimization"
- [[Premature Optimization]] — the phrase and its drift
- [[Software Crisis]] — first historical thread
- [[Structured Programming]] — Knuth's proposed response to the crisis
- [[Execution Profiling]] — second historical thread
- [[Edsger Dijkstra]] — structured programming and the "considered harmful" letter
- [[Go To Statement Considered Harmful]] — the retitled letter
- [[Niklaus Wirth]] — retitled the letter and created Pascal
- [[Tony Hoare]] — the note that anticipated SSA
- [[Peter Naur]] — the "multipass compilers are easy" dismissal
- [[Static Single Assignment Form]] — what Hoare nearly described
- [[Sketchpad]] — the 1960s program with ECS-like architecture
- [[Ivan Sutherland]] — Sketchpad's creator
- [[Entity Component System]] — the architecture Sketchpad already implied
- [[Object-Oriented Programming]] — the domain-model hierarchy critique
- [[Clean Code]] — the book he critiques
- [[Refactoring]] — another book that defers performance
- [[Conway's Law]] — the "only unbreakable law"
- [[Melvin Conway]] — author of the law
- [[Bottom-Up Programming]] — his antidote to upfront design
- [[Vibe Coding]] — the AI-quality concern
- [[Rad Game Tools]] — his character animation system
- [[Jonathan Blow]] — The Witness
- [[NASA]] — the no-recursion rule
