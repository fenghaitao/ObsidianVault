---
title: "Three-Sum Problem"
type: concept
tags: [algorithms, complexity-theory, interview]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

The three-sum problem asks whether a list of n numbers contains three that sum to zero (or to a given target); it is a canonical fine-grained complexity problem and a popular coding-interview question.

## Key Information

- Brute force tries all triples in O(n³). The popular O(n²) algorithm sorts the numbers, then for each element A runs a two-pointer "finger search" over the remaining numbers.
- The finger search places a left finger on the minimum and a right finger on the maximum; if their sum with A is too large, move the right finger down; if too small, move the left finger up; if the fingers cross, there is no solution. Each search takes O(n), done once per A, for O(n²) overall.
- Surprisingly, three-sum can be solved faster than n²: break the sorted list into small groups (e.g., of size log n or √log n), preprocess a fast lookup structure for pairs of groups, and run finger searches at the group level.
- Known subquadratic bounds include n² / ((log n)(log log n))^(2/3). Williams notes such results build directly on the finger-search solution, often via the linear decision tree model.
- It is the opening question of the episode and described by the host as "the most popular LeetCode question."

## Related

- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[LeetCode]] — popular interview question
- [[Time Complexity]] — subquadratic bound
- [[Fine-Grained Complexity]] — field studying its optimal bound
