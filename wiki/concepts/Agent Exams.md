---
title: "Agent Exams"
type: concept
tags: [evaluation, agents, testing, standardized, leaderboard, kaggle]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Agent Exams (originally called SATs — Standardized Agent Tests, renamed due to trademark issues) is Kaggle's platform for standardized agent evaluation. Users paste a one-line prompt for their agent, the agent takes an exam, and a score is returned on a leaderboard for comparison.

## Key Information

### How It Works
- User pastes a one-line prompt representing their agent
- The agent takes a standardized exam
- Score is returned and displayed on a leaderboard against other agents

### Why It Matters
- Research labs and enterprises use sophisticated eval setups (GrayTrust, state-of-the-art technology)
- Consumer agent builders (OpenClaw users, etc.) rarely test their agents before sending them into the real world — leading to incidents like 1,100 security advisories filed in a single morning
- Agent Exams provide a quick, accessible baseline for consumer agents
- Future direction: safety-focused exams for pre-deployment agent checks (before giving agents access to inbox, Amazon accounts, etc.)

### Launch and Traction
- Experimental MVP launched one week before the AI Engineering conference talk
- 500+ agents evaluated in the first week with minimal promotion
- Organic community content emerged: agent exam result sharing, even "SAE prep courses" on Mopbook
- Demonstrated clear demand for accessible agent evaluation among consumers

### Design Challenge
- **Difficulty spectrum**: Too difficult — nobody finishes the exam, no signal. Too easy — no meaningful differentiation between agents
- Must balance accessibility with sufficient challenge to produce useful signal

## Related
- [[AgenticEvaluations]] — broader evaluation paradigm
- [[Kaggle]] — platform hosting Agent Exams
- [[GoogleDeepMind]] — parent organization
- [[NicholasKang]] — presenter and product lead
- [[Eval Hackathons]] — complementary community engagement
- [[Game Arena]] — complementary Kaggle eval product
- [[OpenClaw]] — consumer agent platform where testing is needed
- [[AgentObservability]] — broader monitoring context
- [[summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind]] — source
