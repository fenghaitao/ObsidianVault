---
title: "summary-20260506 - Full Walkthrough： Writing & Using Skills — Nick Nisi and Zack Proser"
type: source
tags: [source, transcript, skills, agent-skills, skill-design, progressive-disclosure, confidence-scoring, skill-evals, sub-agents, workos]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - Full Walkthrough： Writing & Using Skills — Nick Nisi and Zack Proser.md"]
last_updated: 2026-06-29
---

## Core Summary

Nick Nisi and Zack Proser from WorkOS present a hands-on workshop on writing and using AI agent skills at scale. Skills are portable, composable markdown files (optionally with scripts) that encode domain knowledge, conventions, and workflows for LLM agents. Unlike Claude.md/agents.md (loaded every time), skills load on demand based on their description field, which acts as a routing rule for the LLM. The workshop covers skill structure, script interpolation for deterministic data injection, progressive disclosure for context efficiency, confidence scoring to force deeper reasoning, skill marketplaces and sharing mechanisms, eval frameworks, and skills beyond coding (recruiting, blog writing, image/video generation, Slack-Linear automation).

## Key Points

### Why Skills
- Every conversation with an LLM starts from zero context — skills avoid repeating yourself
- Claude.md/agents.md loads every time, bloating context; skills load only when relevant
- Skills are portable across projects, teams, and model providers (Claude, Codex, Cursor, Pi)
- As little as 30 lines of markdown can produce dramatically better, hyper-specific output
- Skills encode the DRY principle for the agentic era

### Skill Structure
- A skill is a folder containing skill.md (with YAML frontmatter) plus optional scripts, references, images
- Frontmatter: `name` and `description` — the description is a routing rule for the LLM to decide when to load the skill
- Constraints over prescriptions: providing constraints ("never be vague", "always cite code with line and commit reference") outperforms overly prescriptive instructions
- Common failure mode: bloviating in the middle of a markdown file

### Script Interpolation
- The `!`` (bang-backtick) syntax lets Claude execute shell commands and inline the output
- Deterministic data injection: instead of "go get the latest 10 commits", you provide the exact output
- Token-saving: avoids the LLM guessing or reading docs to figure out commands
- Ideal for morning reports, git status, stale TODO detection

### Progressive Disclosure
- Point to reference files only when needed: "if doing scoring, load scoring.md"
- Avoids bloating context with irrelevant information
- Enables scaling: WorkOS skill router references specific migration guides only when relevant
- Works across different audiences and use cases within the same skill

### Confidence Scoring
- Force the LLM to assess its own confidence before executing
- Nick's ideation plugin uses a 100-point confidence score across dimensions (problem clarity, goal definition, success criteria, scope boundaries, consistency)
- Below threshold (~95%), the agent asks clarifying questions rather than proceeding
- Value is in the iterative clarifying loop, not the mathematical precision

### Skill Marketplaces and Sharing
- Skills can be shared via: `.skill` files (renamed .zip), Claude Marketplace, MPX skills CLI, Git repos
- WorkOS publishes public skills at github.com/workos/skills
- Plugin marketplace architecture with versioning addresses team sharing challenges
- Non-technical users can drag `.skill` files into Claude Desktop

### Skills Beyond Coding
- Recruiting: formatting candidate info, pulling from Slack/Notion, generating reports
- Blog writing: encoding CMS knowledge, tone, format conventions
- Image generation: NanoBanana wrapper skill (static image → Veo animation)
- Video creation: Remotion skill (programmatic video from prompts)
- Context switching automation: Slack monitoring → Linear deduplication → ticket creation

### Evals for Skills
- Claude ships with a built-in eval framework (HTML reports, before/after comparisons)
- Nick's eval framework: runs task without skill vs with skill, grades both, requires 80%+ improvement
- Eval insights: overly prescriptive Next.js skill caused 30% accuracy drop — Claude was already good at Next.js
- Evals are like an Apple Watch: not perfectly accurate but provide a directional baseline

### Sub-Agents and Context Management
- Sub-agents handle bounded subtasks with fresh context, avoiding context pollution
- Used for adversarial verification: sub-agent checks main agent's work from fresh context
- Nick's ideation plugin uses sub-agents for code review loops
- Claude Agent SDK has best-in-class sub-agent support with bash access

### Meta-Skills and Iteration
- Claude's built-in skill-creator skill can critique and improve your skills
- Analyze conversation logs (JSONL files) to identify skill gaps and improvement areas
- Ask Claude: "analyze my week's worth of work — what skills should I split out?"
- Pre-LLM "disposable" context (failed attempts, frustrations) is now gold for skill refinement

### Q&A Highlights
- **Skills vs Claude.md**: Claude.md loads every time (keep it tiny); skills load on demand for specific tasks
- **Team sharing**: Use marketplace/plugin architecture with versioning; forks for personal modifications
- **Skill pickup failures**: Use explicit slash commands, ask Claude why it didn't pick a skill, improve description
- **Sub-agents vs skills**: Sub-agents for standalone context-heavy work; skills for encoding repeatable workflows
- **Memory**: Claude's built-in memory, OpenClaw's dreaming feature, Obsidian connector for daily notes

## Related

- [[NickNisi]] — speaker, WorkOS DX engineer
- [[ZackProser]] — speaker, WorkOS DX engineer
- [[WorkOS]] — employer, applied AI team
- [[Skills]] — the core concept
- [[ProgressiveDisclosure]] — context efficiency pattern
- [[SubAgents]] — context management via delegation
- [[AgenticLoop]] — the execution pattern skills enhance
- [[EvalEngineering]] — evaluating skill effectiveness
- [[ClaudeDesktop]] — non-technical skill usage
- [[Remotion]] — video creation skill example
- [[NanoBanana]] — image generation skill example
- [[Pi (coding agent)]] — skills support in Pi
- [[Vercel]] — skills-forward tooling (MPX)
- [[OpenClaw]] — memory/dreaming features
- [[WhisperFlow]] — dictation tool used in workflow
- [[SlideDev]] — slide creation tool
- [[ConfidenceScoring]] — forcing LLM self-assessment
- [[ScriptInterpolation]] — deterministic data injection in skills
- [[SkillDescription]] — description as routing rules
- [[SkillMarketplace]] — sharing and versioning skills
- [[SkillEvals]] — measuring skill effectiveness
- [[MetaSkills]] — skills that analyze/improve other skills
