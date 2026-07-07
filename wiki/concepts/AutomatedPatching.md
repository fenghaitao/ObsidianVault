---
title: "AutomatedPatching"
type: concept
tags: [security, patching, automated-remediation, llm-security, tdd]
sources: ["raw/01-articles/claude/2026-05-27 - Using LLMs to secure source code.md"]
last_updated: 2026-07-07
---

## Definition

Automated patching is the practice of using LLMs to generate, validate, and refine security patches for verified vulnerabilities — closing the loop from discovery to remediation with test-driven, adversarially-validated fixes.

## Key Information

- Patching is step 6 and the final step of Anthropic's six-step workflow for using LLMs to secure source code. It closes the loop and feeds learnings back into the threat model for the next scan cycle.
- **TDD-first approach**: before patching, write a new test that fails with the existing code. Then implement the fix and confirm the same test now passes without breaking anything else. Without a test, the fix can silently regress and it becomes hard to retroactively prove the bug was real.
- **PoC-based validation**: one pentester found that generated patches were inconsistent until the harness told the model to validate patches by re-running the proof of concept against the patched code. Giving the model feedback to iterate against improved patch quality significantly.
- **Root cause vs. symptom**: models may narrowly address findings at a specific call site instead of the root cause. Simply prompting the model to identify and fix the root cause can be effective. Then have the model look for variants at two levels: (1) same pattern — other call sites or copies of the same buggy code elsewhere, and (2) same class — a codebase with one SQL injection vulnerability tends to have more SQL injection vulnerabilities.
- **Adversarial pre-ship check**: before shipping the patch, have a new discovery agent probe the patch as an attacker to confirm it is comprehensive.
- **Patch minimality**: prompt for the smallest change that fixes the root cause — no refactoring, no drive-by cleanups, no reformatting. Minimal patches are easier to review and less likely to introduce new bugs.
- **Common failure mode**: patches tend to be as restrictive as possible, to the point of breaking connections with other services. One team reported this as their most common patch failure: the fix would address the issue but break the dependencies that allow the service to work.
- **Validation ladder**: validate each patch against a sequence of checks starting with the cheapest — re-running the PoC, running existing tests, checking for breaking changes to dependent services, and adversarial review.
- **Human ownership**: while the model can write the patch, a human still needs to own it. The goal is to validate each patch as much as possible so human review requires less effort — helping the dev team focus on nuances the model might be unaware of (e.g., incoming changes, code style).
- **Closing the loop**: update the threat model with validated findings and patches. Each cycle hardens the codebase and makes the next scan better informed.
- The `patch` skill in the [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) generates candidate diffs per finding with an independent reviewer agent checking each one.

## Related

- [[summary-2026-05-27 - Using LLMs to secure source code]] — source article describing the full six-step workflow
- [[VulnerabilityTriage]] — the triage phase whose ranked output feeds into patching
- [[VulnerabilityVerification]] — the verification phase that produces confirmed findings
- [[ThreatModeling]] — the threat model updated with validated findings to close the loop
- [[TestDrivenDevelopment]] — TDD applied to security patch generation
- [[Sandboxing]] — the sandbox where PoCs are re-run to validate patches
- [[Claude4.7Opus]] — the model used for patch generation
- [[ClaudeSecurity]] — the enterprise product that generates targeted, explained patches
- [[VulnerabilityDetection]] — discovery phase; findings from the n-th scan tend to have fewer but more complex vulnerabilities as simpler ones were patched in prior runs
