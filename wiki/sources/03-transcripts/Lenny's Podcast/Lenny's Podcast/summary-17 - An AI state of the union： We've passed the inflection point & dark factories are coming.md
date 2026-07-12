---
title: "Summary: An AI state of the union： We've passed the inflection point & dark factories are coming"
type: source-summary
source: "17 - An AI state of the union： We've passed the inflection point & dark factories are coming"
playlist: "Lenny's Podcast"
author: "Lenny Rachitsky"
guest: "Simon Wilson (Simon Willison)"
date: 2026
---

# Summary: An AI state of the union： We've passed the inflection point & dark factories are coming

## Core Thesis

**November 2025 was the inflection point for AI coding.** GPT-5.1 and Claude Opus 4.5 crossed a threshold where coding agents went from "mostly works" to "almost always does what you tell it." This shift fundamentally changes how software is built. Code is now cheap, prototyping is nearly free, and the bottleneck has shifted from writing code to everything else — ideation, testing, quality assurance, and security. The next frontier is the "dark factory" pattern, where software is built without anyone directly reading or writing code, relying instead on automated testing, simulated QA swarms, and security penetration testing by AI. Simon Wilson (Simon Willison), co-creator of Django and the person who coined "prompt injection," "AI slop," and "agentic engineering," lays out the patterns for effective agentic engineering, warns about the "lethal trifecta" security risk, and predicts a "Challenger disaster of AI" as we normalize deviance around unsafe AI usage.

## Key Topics

### 1. The November 2025 Inflection Point
- Throughout 2025, Anthropic and OpenAI focused all training efforts on coding, using reinforcement learning and reasoning models.
- In November 2025, GPT-5.1 and Claude Opus 4.5 crossed a threshold: previously agents would "mostly work" but required close attention; now they "almost always do what you told them."
- Software engineers who tinkered over the holidays had a realization: "Oh, wow, this stuff actually works now. I can tell it to build code and if I describe that code well enough, it'll follow the instructions."
- The reverberations are still shaking software engineering. "A lot of people woke up in January and February and started realizing, 'Oh, wow, this technology which I'd been kind of paying attention to, suddenly it's got really, really good.'"
- Code is easier than other knowledge work because code is "obviously right or wrong" — you can run it and see. Other fields (law, essays) have much harder verification.

### 2. Vibe Coding vs. Agentic Engineering
- **Vibe coding** (Andrej Karpathy's term): When you don't look at the code, you just go on vibes. "Build me something that does X." Great for prototyping, personal projects, and non-programmers building tools. But not responsible for code that affects other people.
- **Agentic engineering**: When professional engineers use coding agents to write production-ready code that they review and verify. "The art of getting really good results out of this... is never going to be easy."
- Simon argues the term "vibe coding" should be reserved for the hands-off approach, not devalued by applying it to all AI-mediated coding.
- Today, ~95% of Simon's code is AI-generated. He writes much of it from his phone, walking the dog on the beach.

### 3. The Dark Factory / Software Factory Pattern
- Named after factory automation where "if your factory is so automated that you don't need any people there, you can turn the lights off."
- Two rules: (1) Nobody writes any code — all code must be AI-written. (2) Nobody reads the code.
- **StrongDM case study**: Security software company applied this pattern. Key innovations:
  - **Simulated QA swarm**: AI agents simulated thousands of end users making requests 24/7 in a simulated Slack channel, spending ~$10,000/day on tokens.
  - **Simulated API integrations**: Instead of testing against real Slack/Jira/Okta APIs (which have rate limits), they had AI build simulated versions of those APIs from public documentation.
  - The simulated Slack even had a fake UI they could use to observe what was happening.
- This raises the question: how do you know the software is good if you're not reviewing code? The answer might be better testing, security penetration testing by AI, and creative QA approaches.

### 4. Code Is Cheap — What Changes?
- The single biggest shock: "the thing that used to take the time takes way less time."
- Prototyping is nearly free. Simon now builds three different versions of a feature to explore which direction works best.
- Simon's career superpower was rapid prototyping — "that's gone. Anyone can do what I could do."
- But you still need to know when to prototype, how to think about prototyping, and how to use the tools to build useful prototypes.
- The implication: "We can test things so much faster now, because we can build workable prototypes so much quicker."

### 5. Where Human Brains Remain Valuable
- AI is great at the "first two-thirds" of brainstorming — generating the obvious ideas. The interesting part comes when you push for 20 more ideas and combine them in unusual ways.
- AI can combine weird fields: "I want ideas for marketing my new SaaS platform inspired by marine biology."
- For product design, the real value is still in usability testing with real humans — AI-simulated users aren't credible replacements.
- The bottleneck shifts from building to: ideation, testing, proving which options work, and deciding what to build.

### 6. Agentic Engineering Patterns (from Simon's Blog/Book)

#### A. Red/Green Test-Driven Development
- The most important thing: agents must run the tests. If they haven't run the code, "you're back to copying and pasting out of ChatGPT and crossing your fingers."
- Use "red/green TDD" — a concise jargon phrase that tells the agent to write the test first, watch it fail, implement the code, and watch it pass.
- Tests compound over time, giving confidence that new features won't break old ones.
- Simon's tolerance for verbose tests has increased because "updating 1,000 lines of tests is now the job of the coding agent."

#### B. Hoarding Things You Know How to Do
- Build a backlog of solved problems, techniques, and tools you've tried, so you can combine them for new problems.
- Simon has two public GitHub repos: `simonw/tools` (~193 HTML/JavaScript tools) and `simonw/research` (~75 AI-driven research projects with actual code and results).
- "You can tell an LLM to consult them and combine them." The agents can search across your entire hard drive of past work to find relevant examples.
- "It's hard to overstate how good these things are at reusing context that you can make available to them."

#### C. Start with a Good Template
- Coding agents are "phenomenally good at sticking to existing patterns in the code."
- Simon starts every new project with a thin skeleton template that has a single test (`1 + 1 = 2`), laid out in his preferred style.
- This is more effective than writing a long `claude.md` with paragraphs of instructions — the agent picks up the pattern from the code itself.

### 7. The Cognitive Exhaustion Problem
- "Using coding agents well is taking every inch of my 25 years of experience as a software engineer and it is mentally exhausting."
- Simon can fire up 4 agents in parallel and by 11:00 a.m. he is "wiped out for the day."
- "There is a limit on human cognition in how much... you can hold in your head at one time and it's very easy to pop that stack."
- Many people are losing sleep, staying up to set off more agents, waking up at 4:00 a.m. to check on them.
- "It's the most fun I've ever had with technology. It's so fun."
- Simon's New Year's resolution was the opposite of focusing: "Take on more stuff and be more ambitious."
- "It feels like the people that are most AI-pilled are working harder than they've ever worked." — an interesting contradiction to AI's promise of more leisure.

### 8. Mid-Level Engineer Squeeze
- **ThoughtWorks offsite conclusion**: AI amplifies senior engineers (they have expertise to leverage) and helps junior engineers (solves onboarding problems, gets them productive in a week instead of a month).
- **Cloudflare and Shopify** both hired 1,000 interns in 2025 because AI reduces onboarding costs.
- "The problem is the people in the middle." Mid-career engineers who aren't super senior but aren't new either are "probably in the most trouble."
- Advice: Lean into AI, use it to amplify your skills, take on more ambitious projects. "The only universal skill is being able to roll with the changes."

### 9. Prompt Injection and the Lethal Trifecta
- **Prompt injection**: A vulnerability in applications built on LLMs, not the models themselves. Untrusted text (from emails, websites) can override the system's instructions.
- Simon coined the term in 2022, before ChatGPT launched. He regrets the name because it implies the problem is solvable (like SQL injection), but it's fundamentally different.
- The **lethal trifecta**: A subset of prompt injection requiring three conditions:
  1. Access to private information
  2. Exposure to malicious instructions (someone can get their text into your system)
  3. Exfiltration capability (the agent can send data back to the attacker)
- Cut off any one leg to make the system safe. Usually, exfiltration is the easiest to cut.
- "You can get to like 97% effectiveness on those filters. I think that's a failing grade."
- The **CAMEL paper** (Google DeepMind) proposed a solution: split the agent into a privileged agent and a quarantined agent, with tainted data tracking and human-in-the-loop on high-risk actions.

### 10. The Challenger Disaster of AI
- Reference to the Space Shuttle Challenger and the sociological concept of "normalization of deviance."
- "Lots of people knew that those little O-rings were unreliable, but every single time you get away with launching a space shuttle without the O-rings failing, you institutionally feel more confident in what you're doing."
- "We've been using these systems in increasingly unsafe ways. This is going to catch up with us."
- Simon has been making this prediction every 6 months for 3 years — it hasn't happened yet, but the normalization of deviance continues.

### 11. Open Claw and Personal Digital Assistants
- Open Claw: first line of code written November 25, 2025. By the Super Bowl (~3.5 months later), there was a Super Bowl ad for a white-labeled Open Claw hosting provider.
- "Has there ever been a project that got that level of success in that much time?"
- It is "almost exactly the thing I most argue against existing" — a personal digital system with access to email and the ability to take actions.
- There have been catastrophic security failures (Bitcoin wallets lost), but hundreds of thousands of people still set it up.
- "The demand for a personal digital assistant is enormous."
- The biggest opportunity in AI: "If you can build safe Open Claw... that's a huge opportunity."
- Open Claw inspired a generic term: "claws" (Nano Claw, etc.). Simon predicts "building your own claw" will be the new "Hello World" of AI engineering.
- Spider-Man 2 reference: Doc Ock's AI-controlled claws with an inhibitor chip — when the chip breaks, the claws control him.

### 12. The Pelican Riding a Bicycle Benchmark
- Simon created a benchmark to make fun of numeric AI benchmarks: "Generate an SVG of a pelican riding a bicycle."
- It tests text models (not image models), since they output SVG code.
- "There appears to be a very strong correlation between how good their drawing of a pelican riding a bicycle is and how good they are at everything else."
- It has become a meme — AI labs are aware of it and compete on it. Gemini 3.1 released a video featuring an animated pelican on a bicycle.
- Simon has backup benchmarks (ocelot on a moped) to detect if labs specifically train on pelicans.
- "All I want from life is a really good picture of a pelican riding a bicycle."
- Simon lives near the world's second-largest mega roost of California brown pelicans.

### 13. AI Stack Preferences
- Simon primarily uses Claude Code (both desktop and Claude Code for Web on his phone).
- Claude Code for Web runs on Anthropic servers, so he can use YOLO/dangerously-skip-permissions mode safely — his code is all open source.
- Recently leaning toward GPT-5.4 (OpenAI Codex) because it's "on par with Claude Opus 4.6 and possibly even better" and cheaper.
- He keeps switching between ecosystems as models leapfrog each other.
- "This stuff's all so weird. It's a vibes all the way down."
- He turns off AI memory features because "as an AI researcher, I need to see what everyone else sees."
- For research, AI with search integration has replaced Google Search for him.

### 14. AI and Journalism
- Simon's day job: open-source tools for data journalism (Datasette).
- "Journalists deal with untrustworthy sources all the time... As long as the journalist treats the AI as yet another unreliable source, they're actually better equipped to work with AI than most other professions."
- Building tools that let journalists feed in PDFs of police reports, extract key details, build database tables, and run SQL queries.
- Goal: "I want somebody in the world to win a Pulitzer Prize where my software was like 3% of what they used."

### 15. Zero Deliverable Consulting
- Simon's consulting model: "I don't write a report, I don't write any code. You just get my time for an hour."
- He describes himself as "very lazy when it comes to actually making money" — doesn't want to find clients, invoice, or negotiate.
- Uses intermediaries to channel these one-hour calls.

### 16. AI's Impact on Software Engineering Careers
- 50% of engineers could have the majority of their code AI-written by the end of 2026.
- "The code is now good. It's good code... That's not justifiable anymore" to say you don't use AI because the code is bad.
- Different regions have different attitudes: Europeans are more AI-skeptic than Americans (based on Hacker News timezone patterns).
- On the job market: Tech companies are at the highest number of open engineering/PM roles in ~3.5 years (except the COVID peak), despite layoff headlines.
- The paradox: AI makes people more productive, but the most AI-pilled people are working harder than ever.

### 17. The Fun Factor
- "This space is inherently funny. It is ridiculous."
- "The fact that you could trick ChatGPT into telling you how to make napalm by saying that your grandmother worked at the napalm factory and you missed her... It's so silly."
- Simon embraces the "inherent ridiculousness of what we're trying to achieve with these things."
- Many people have finished their entire backlog of side projects from the past 10-15 years.
- "They almost feel a sort of sense of loss at the end where they're like, 'Well, okay, my backlog's gone. Now what am I going to build?'"

## Key Quotes

- "I can fire up four agents in parallel and have them work on four different problems. By 11:00 a.m., I am wiped out."
- "Today, probably 95% of the code that I produce, I didn't type it myself. I write so much of my code on my phone, it's wild."
- "Code is easier than almost every other problem that you pose these agents because code is obviously right or wrong."
- "Using coding agents well is taking every inch of my 25 years of experience as a software engineer."
- "The challenge is that understanding what's responsible and what isn't is in itself an expert-level skill."
- "There's a policy of nobody writes any code. The next rule though is nobody reads the code."
- "The reason we have to rethink how we build... is that the thing that used to take the time takes way less time."
- "I don't just want to build software that's good. I want us to build software that is better than we were building before."
- "You can get to like 97% effectiveness on those filters. I think that's a failing grade."
- "This space is inherently funny. It is ridiculous."
- "The only universal skill is being able to roll with the changes."
- "All I want from life is a really good picture of a pelican riding a bicycle."
- "The demand for a personal digital assistant is enormous."
- "I've been calling it a not a book because I don't want the pressure of building a book."
- "There is a rare parrot in New Zealand called the kakapo parrot... They are having a fantastic breeding season in 2026."

## Entities Referenced
- Simon Wilson (Simon Willison), Lenny Rachitsky, Andrej Karpathy, Boris Cherny, Sander Schulhoff, Jensen Huang, Dario Amodei, David Place, Alfred Molina
- Anthropic, OpenAI, Google DeepMind, StrongDM, ThoughtWorks, Cloudflare, Shopify, Mozilla, Block, Meta, Instagram, Spotify, Pinterest
- Claude Code, OpenAI Codex, ChatGPT, Claude, GPT-5.1, GPT-5.4, Claude Opus 4.5, Claude Opus 4.6, Gemini 3.1, Gemini Nano Banana
- Django, Datasette, Open Claw, Nano Claw, Playwright, Tesseract, Mozilla PDF.js, Docker, AppleScript, Redis, Node.js
- WorkOS, Vanta, Cursor, Vercel, Replit, Notion, Linear, Perplexity, Manas, GitHub, Slack, Jira, Okta, Google Search, Hacker News
- Kakapo parrot, Spider-Man 2, Space Shuttle Challenger, Super Bowl, California brown pelican

## Concepts
- November Inflection Point (AI Coding), Agentic Engineering, Dark Factory / Software Factory, Vibe Coding, Red/Green TDD, Hoarding Things You Know How to Do, Code is Cheap, Cognitive Exhaustion from AI, Mid-Level Engineer Squeeze, Lethal Trifecta, Prompt Injection, Challenger Disaster of AI, Normalization of Deviance, Pelican Riding a Bicycle Benchmark, YOLO Mode, Personal Digital Assistant, Zero Deliverable Consulting, AI for Journalism, AI Memory Features, AI as Amplifier, Coding Agents, Code Review (AI), AI Slop, Human Typing Speed Bottleneck, AI Safety Layers, Evals (Evaluation Metrics), Fast Feedback Loops
