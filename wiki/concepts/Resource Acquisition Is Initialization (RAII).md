---
title: "Resource Acquisition Is Initialization (RAII)"
type: concept
tags: [concept, C++, resource-management, memory]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
RAII (Resource Acquisition Is Initialization) is the C++ idiom that ties acquisition of a resource (memory, locks, files) to an object's lifetime via constructors and destructors, so it is released automatically.

## Key Information
- Bjarne calls "RAII" (resource acquisition is initialization) "probably my worst naming ever."
- It generalizes memory management to all resources, not just garbage and not just memory.
- The technique existed from the start (C with Classes in 1979 already had constructors and destructors) but "people didn't get it" and it needed teaching.
- Its growing adoption over ~10 years caused usage of the C++ 11 garbage-collection interface to decline.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — the language featuring it
- [[Garbage Collection]] — the automatic alternative it partly displaced
- [[Memory Safety]] — the outcome RAII supports
