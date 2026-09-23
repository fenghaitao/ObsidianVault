---
title: "AI and Software Engineering"
type: concept
tags: [AI, career, engineering, future-of-work]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250501 - Industry Secrets We Wish We Knew Before Graduating (Staff Engs Talk at UCLA).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250711 - Meta Senior Staff Eng (IC7)： Zuck Stories, Rapid Career Growth, Code Machine Archetype.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260511 - Harvard Professor： CS50, What Matters More Than Programming Now, Lecturing Well ｜ David J Malan.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md",
  "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260909 - Creator of TypeScript & C#： AI Software Engineering Predictions ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Definition

AI and Software Engineering examines the relationship between artificial intelligence tools and the software engineering profession, particularly the question of whether AI will replace or augment entry-level engineers.

## Key Information

- In the short term (5-10 years), AI is not expected to completely replace entry-level software engineers — there are still things LLMs have difficulty doing
- AI is seen as a tool that empowers engineers, similar to other non-AI tools that generate code without scaring anyone
- Ricky's perspective: there will always be people who need to "tell the AI what to do" and verify the output is correct — even if future entry-level engineers code less, they'll still be figuring out how to direct the AI
- Someone still needs to build the AI itself
- The advice to students: don't change your major from CS because you're worried about AI eliminating jobs — at least not for people already in college
- For current college students, AI is "just a little bit further" along the spectrum of tools that assist engineers, not a fundamental replacement

### Michael Novati's LLM Perspective
- His current workflow mostly uses AI to generate code he already knows how to write, and he reports ~5x more code than six months prior
- His prediction: AI tools first make experienced engineers with strong taste far more productive, while juniors struggle harder to build up that experience
- Beyond augmentation, if AI writes and maintains its own code, it may not look like human-readable code at all — just API contracts meeting specifications
- He argues we should make the AI world "the best it can be" rather than resist the shift

### Boris Cherny and Claude Code
- Claude Code was built on "don't build for the model of today, build for the model 6 months from now" — it went from writing ~10% of Boris's code to writing 80–90% of Claude Code itself once the models matured, lifting Anthropic's productivity per engineer ~70% despite tripling headcount ([[summary-20251215 - Boris Cherny (Creator of Claude Code) On What Grew His Career And Building at Anthropic]])

### Marc Brooker's Perspective

- Software has been supply-constrained and the changing economics of AI will produce more software — bigger, better, more personal. Careers will span a craft/hobby tier, a shrinking "old way" (analog-electronics analogy), and the mainstream (agentic/AI/specification-driven development).
- Juniors should learn to find problems that matter and understand customers/business early; the most technical, deeply expert folks also become more valuable as boilerplate shrinks.
- Seniors must get hands-on and use the new tools, or their opinions "tend to be essentially fiction"; people using agentic-powered practices have grounded views, while non-hands-on people have a poor mental model.

### David J. Malan's Perspective
- CS50 is "not about Scratch and C and Python and JavaScript... but how to solve problems"; those languages are implementation details.
- AI is "pretty darn good already at generating code" and will absorb the un-fun parts (boilerplate, unit tests); the fun part — designing the system, UX, database design — is what he doesn't want the computer to take.
- Reassurance to anxious students: "the world is only getting more technological," and CS enrollments have ebbed and flowed before (the dot-com bust).
- Humans should stay in charge for now: Claude returned a ~90%-correct solution and he had to correct a hallucinated API detail; hallucination will decrease, but oversight is still needed.

### Charlie Marsh's Perspective
- The cost of putting up a plausible PR has fallen to zero while the cost to review it remains constant, creating poor open-source dynamics and a review bottleneck.
- His team now reviews his agent-generated PRs closely ("you're not writing it anymore; it's the agent"); he self-reviews each line in the GitHub UI.
- Strong software engineers are more valuable than ever because they use agents more effectively; he remains concerned about the "garbage" he'd ship without significant engineering experience.
- It's a hard time to be an early-career engineer — he's unsure what the learning loop looks like when you're mostly instructing models.

### Anders Hejlsberg's Perspective
- AI is "at heart a big stochastic machine that has memorized the entire internet" — it can't write the TypeScript compiler because it has seen nothing like it in its training set, and it is not deterministic.
- AI favors incumbent languages: trained on the world's code, it is best at JavaScript/TypeScript/Python — the adoption "knee" in TypeScript coincides with AI, and incumbents get stronger.
- "Don't hand AI the keys": if you can't understand the code you still carry responsibility (when the app misbehaves, the user sues you, not the AI).
- On "AI will write 90% of code" / "no IDE needed within a year": people overreach to 100% — "there still has to be someone understanding what's going on" and connecting the work to the business problem.
- If AI replaces junior engineers, "where are the seniors going to come from?" The craft shifts from typing code to reviewing agents' work — more reviewing, less typing.
- Practical tip: ask AI to write a program that computes the answer (a spreadsheet, a translation tool) rather than the answer itself, since nondeterminism breaks trust.
- On the "90%" claim: it depends what you count — AI already writes 100% of some no-code apps, and exploding output volume makes the prediction self-fulfilling; the harder bar is super-high-quality code no one has written before.
- Personally, he has enjoyed typing code for 40–50 years and will keep typing the parts he likes, happily farming out tests to AI; he finds reviewing harder than writing and expects AI to make code review more ergonomic.

### Thariq Shihipar's Perspective
- "Coding is largely solved" (a Boris tagline) means we no longer get stuck the way we used to — software was once so rare and failure-prone that most projects failed, but now it works far more often and can be applied everywhere.
- Being technical is still crucial: understand computers, programs, languages, memory allocation, caches, and what a back-end service is — you can only judge great software if you are a great software engineer.
- The unique work is deciding what to build, defining specs, and providing context; Claude absorbs the "glue work" (e.g., a Figma-to-React translation that has been done once shouldn't be redone).
- Internships shift from "write the React code" to discovering genuinely new problems (e.g., how to eval and measure model performance across millions of users) — more proactive and opportunistic than a pipeline task.
- Maintainability is being redefined: naming and stylistic opinions matter less; verification harnesses, skills, and ~100x more test code matter more; consider wholesale rewrites as models improve.
- Learning should still feel like effort (Karpathy): nodding along while Claude explains something is not the same as actually learning it.
- The "ticket to done" only works when the ticket is a complete spec; the real work is figuring out what you want and where the unknowns are.

## Related

- [[summary-20250501 - Industry Secrets We Wish We Knew Before Graduating (Staff Engs Talk at UCLA)]] — source summary
- [[AI as Amplifier]] — Steve Huynh's framework for AI's impact
- [[Career Growth]] — the context of career planning with AI
- [[Machine Learning]] — the field of AI itself
- [[Michael Novati]] — his LLM workflow and predictions
- [[summary-20250711 - Meta Senior Staff Eng (IC7)： Zuck Stories, Rapid Career Growth, Code Machine Archetype]] — source summary
- [[summary-20251215 - Boris Cherny (Creator of Claude Code) On What Grew His Career And Building at Anthropic]] — source summary (Boris)
- [[Boris Cherny]] — builds Claude Code
- [[Claude Code]] — the AI coding agent he created
- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — his perspective on AI and engineering careers
- [[summary-20260511 - Harvard Professor： CS50, What Matters More Than Programming Now, Lecturing Well ｜ David J Malan]] — source summary (Malan)
- [[David J. Malan]] — problem-solving over syntax
- [[CS50]] — the course teaching problem-solving
- [[Mitchell Hashimoto]] — renderer example (hand-written 100x vs agent 10x)
- [[Vibe Coding]] — one end of the agent-era spectrum
- [[Contributor Poker]] — how agents break contributor growth
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
- [[Anders Hejlsberg]] — AI can't write the compiler; don't hand AI the keys
- [[TypeScript]] — the AI adoption "knee"
- [[Porting vs Rewriting]] — deterministic tools vs stochastic AI
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[Thariq Shihipar]] — "coding is largely solved" and staying technical
- [[summary-20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar]] — source summary
- [[summary-20260909 - Creator of TypeScript & C#： AI Software Engineering Predictions ｜ Anders Hejlsberg]] — source summary
