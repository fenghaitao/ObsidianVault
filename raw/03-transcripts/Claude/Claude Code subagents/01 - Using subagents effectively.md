---
title: "Using subagents effectively"
type: transcript
source: youtube
playlist: "Claude Code subagents"
author: "Claude"
---

# Using subagents effectively

You know how to create sub agents and design them well. Now, let's cover when they actually help and when they get in the way. Simply put, the difference comes down to whether the intermediate work matters to your main thread. When exploration is separate from execution, sub agents shine. When each step depends on what the previous step discovered, well, information gets lost in the handoff process. Sub agents excel at research tasks where you just need an answer, not the journey.

Consider investigating how authentication works in an unfamiliar code base. Well, the main thread might need to know where is the JWT validated, but doesn't need to see every file that was searched. A research sub agent can read dozens of files, trace through function calls, and explore different code paths. All that exploration stays in the sub agent's context. Your main thread receives JWT validation happens in middleware/auth.js at line 42, called from the Express router and route/api.js, or something like that. Claude reviews work more effectively when the code is presented as being authored by someone else.

If you build a feature over many turns with your main thread, asking the main thread to then review it often doesn't give the best feedback. Claude was involved in creating it, so it has trouble seeing it with fresh eyes. A reviewer sub agent sees the changes in a separate context. It runs get diff, reads the modified files, and applies its specialized review criteria without the history of how the code was written. And this separation also lets you encode project-specific review standards in the sub agent system prompt, ensuring consistent review criteria across the team. Claude Code's default system prompt emphasizes concise, code-focused response.

And this works great for coding, but not for everything. So, one is a copywriting sub-agent with instructions about tone, audience, and style. This will produce better marketing text than the main thread would. Claude Code's default prompt tends towards concise, technical writing, which really isn't what you want for a landing page or email campaign, unless you want to put your customers to sleep. A copywriting sub-agent can have completely different instructions about voice and structure. A styling sub-agent that at mentions your design system files will apply consistent CSS patterns.

When the sub-agent runs, those files load into the context automatically, so it knows your color variables, spacing conventions, and component patterns before it even starts writing any CSS. Sub-agents that claim expertise rarely help. Prompts like, "You are a Python expert." or "You are a Kubernetes specialist." add no value because Claude already has that knowledge. The overhead of launching a sub-agent, losing visibility into its work, and compressing its findings into a summary only makes sense when the sub-agent does something that the main thread can't. Like applying a custom system prompt or keeping exploratory work isolated. Sequential sub-agent pipelines create problems.

Consider a three-agent flow. One to reproduce a bug, one to debug it, and one to fix it. Pipelines work when tasks are truly independent. They fail when each step depends on discoveries from the previous step. Test runner sub-agents tend to hide information you need. When tests fail, you want the full output to diagnose issues.

A sub-agent that returns a test failed forces you to create additional debug scripts to get details that would have been visible in direct output. Testing has showed that the test runner pattern performed worse among all configurations. Across the series, we covered how sub-agents work as isolated threads that return summaries. How to create them with the /agents command, and how to design them with structured outputs and specific descriptions. Use them for research, reviews, and tasks needing custom system prompts. But, avoid them for expert claims, multi-step pipelines, and test runners.

The key question, does the intermediate work matter? If not, then delegate it.
