---
title: "Meta"
type: entity
tags: [company, FAANG, tech, social-media]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Feb 2024).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20241101 - Job Hopping to Staff at Airbnb by Age 26 ｜ Zach Wilson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250301 - Amazon Principal Engineer (L7)： Layoffs, Interviewing & Career Growth ｜ Steve Huynh.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250523 - OpenAI & Meta Distinguished Engineer (IC9)： Working With Zuck, Carmack & Career Growth ｜ Philip Su.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250501 - Industry Secrets We Wish We Knew Before Graduating (Staff Engs Talk at UCLA).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260104 - Anthropic Eng Leader： Mentorship Advice, Microsoft vs Facebook, Career Learnings ｜ Fiona Fung.md"]
last_updated: 2026-09-14
---

## Definition

Meta (formerly Facebook) is a multinational technology conglomerate and one of the FAANG companies, known for social media platforms, advertising, and virtual reality.

## Key Information

- Ryan L. Peterman went from E3 to E6 at Meta in three years, one of the fastest trajectories
- Rahul similarly went from E3 to E6 at Meta in three years
- Zach was hired into a junior role at Facebook after being a mid-level engineer at a startup, but received an 80% pay bump despite the title drop. He was hired as an IC3 Data Engineer and promoted to IC4 in just 5 months because Facebook recognized he was mis-leveled. Zach worked on the Growth team (Notifications) under manager Jender, where he developed the Reachability metric, built the first cross-app growth dashboard, and made the notification ML pipeline 90% cheaper. He received two consecutive Greatly Exceeds ratings as IC4 but was denied E5 because management questioned sustainability of his performance. Facebook had a separate Data Engineer (DE) track from the Software Engineer (SWE) track, with DEs receiving 30-40% less equity at the same level. Facebook used Boot Camp for onboarding, described by Zach as feeling like Disneyland. The company used PSC (Performance Summary Cycle) for half-year reviews.
- Meta's leveling system: E3 (entry level), E4 (mid-level), E5 (senior), E6 (staff), E7 (senior staff)
- Meta used to have Boot Camp for onboarding — new engineers entered undeclared, completed tasks for various teams, and then chose which team to join (now replaced by Team Match)
- Evan King joined Meta through Boot Camp and initially explored cyber security teams before choosing the Content Integrity org, specifically the terrorism team
- Content Integrity is a Meta org that builds ML models to identify and take action on violating content (hate speech, graphic violence, suicide, terrorism, child exploitation imagery, pornography)
- The Content Integrity org had a culture of young, relatable engineers; the Seattle office team was hidden on the second floor in the corner due to the sensitive nature of content they worked with
- Evan King's first Meta project was called Estuary, a multi-staged funnel for detecting terrorist content using crude checks, expensive models, photo matching, and human review
- After the Christchurch shooting in March 2019, Meta created the Realtime Integrity team to detect live-streamed atrocities in real time
- The Realtime Integrity team developed Golden Set Recall, an evaluation system that restreamed past atrocity content through Bots on real Facebook infrastructure to holistically test detection systems
- Live suicide detection recall improved from 9% to mid-90s through a combination of the Golden Set Recall evaluation system and incorporating comment signals into models
- Evan King's IC6 promo timeline: promoted from IC3 to IC4 in 1 half, IC4 to IC5 in 2 halves, IC5 to IC6 in 3 halves
- Meta's culture rewards impact over difficulty — a one-line change with massive impact is valued more than a complex year-long project; this incentivizes finding the simplest path to impact
- Meta engineers' levels are not publicly visible, which forces influence without authority and requires earning credibility through being right consistently
- Evan King noted that Meta's impact-driven culture had a downside: it encouraged a "ship it and run" mentality that discouraged deep technical understanding of how things actually worked
- Ryan Peterman worked on Instagram infrastructure at Meta, choosing the product vs infrastructure split based on infrastructure sounding "technical and cool"
- Ryan Peterman's staff promotion project was a compute efficiency optimization for Instagram video encoding that eliminated redundant work
- Ryan Peterman transitioned to TLM (Tech Lead Manager) at Meta, then to full management, partly because he felt IC7 would make him a "snowflake" with limited transferability
- Meta's monorepo meant the entire codebase was at every engineer's fingertips; being good at code search was a significant accelerator for both junior and senior engineers
- Panelists noted that titles at startups are often inflated relative to Meta's leveling
- Ryan Peterman's staff promotion project was a large efficiency project that made video processing at Instagram 94% cheaper for basic encodings
- Rahul's staff promotion at Meta came from an internal debug-ability tool (saving thousands of engineering hours/year) and re-architecting a calling system
- Lee worked at Meta as an L6 Staff Engineer but had a difficult experience and moved to Google after about a year and a half
- Meta uses Workplace (internal version of Facebook) for communication and sharing work updates
- Mark Zuckerberg predicted in 2025 that AI would be able to produce mid-level engineer code later that year; Steve Huynh expressed skepticism about the timeline, noting that if it were already true, the prediction would target senior/staff levels instead
- Meta was on a hiring spree in early 2025, with inflows significantly larger than outflows, making the "low performers leaving" policy less concerning for most employees
- Steve Huynh noted that many former Amazon engineers who couldn't make the SDE3 to Principal jump at Amazon went to Meta and thrived at high levels
- Rahul Pandey joined Meta as IC5 (senior) from Pinterest, then achieved IC6 (staff) while working on the Portal hardware device
- Building 8 (later Portal) was Meta's hardware division developing a standalone video calling device running a forked version of Android with ~30 custom apps
- Portal used Buck, Meta's custom build system, which was significantly different from standard Android development
- Meta's code review culture was much lighter than Pinterest's: usually only one accept (LGTM) was needed to land code, compared to Pinterest's two-reviewer requirement with herald rules
- Meta's culture was more direct than Pinterest's — people were more willing to say "this doesn't make sense, let's cut it or kill it"
- Meta had a more aggressive PIP culture compared to Pinterest
- Rahul's IC6 promotion at Meta came from two projects: a debug tool for Portal engineers (saving hundreds of engineering hours/month) and migrating Portal's video calling infrastructure back to Messenger's shared RTC infrastructure
- Rahul served as TLM at Meta before leaving to found Taro
- Meta's Portal team grew from an experimental project to hundreds of engineers
- The Android build at Meta for Portal was uniquely complex: building all 30 apps would take 3-4 hours, so engineers only built the specific app they were working on
- Philip Su was one of the few engineers promoted to IC9 (Distinguished Engineer) at Meta, and was the second person hired in Meta Seattle (Meta's first office outside Palo Alto)
- Philip Su was promoted to E9 as Site Director of Meta London, growing the office from 12 engineers to ~400-500 people over 4-5 years
- When Philip Su joined Facebook, it had 500 engineers globally; the median age was 27, making him (at 33) the oldest person in the Seattle office for seven months
- Philip Su built Meta London using a landing team of 12 people who committed to two years minimum, selected from ~50 volunteers for their culture-carrying ability
- Philip Su deliberately sought and received a demotion from E9 to E7 when switching from Site Director to IC at Oculus
- The IC9 level was invented partly to accommodate exceptional individual contributors like John Carmack, who was so prolific at coding that no existing level captured his contribution
- When Meta first considered promoting engineers to E9 (when the company was several thousand people), only three engineers were being considered
- Philip Su created "The Great Post Explorer" internally to rank and expose timeless Workplace posts
- Philip Su bought coffee for the entire company multiple times, including spending over $23,000 on his departure
- Scott Renfro was a high-level IC at Meta described as a "force multiplier" for teams, with peer feedback consistently saying "Scott takes time out of his day to make me great"
- Philip noted that Mark Zuckerberg and Bosworth both impressed with deliberate, visible personal growth and self-improvement over their years leading the company
- At the UCLA talk, Meta's stock was noted as "ripping recently," which explained why Meta compensation numbers on Levels.FYI were significantly higher than Google's at the time
- Ryan Peterman noted he had five interns at Meta and described the difference between rock stars (ask questions, propose improvements) and low performers (quiet, struggle alone, make no progress)

### Fiona Fung's Reality Labs Chapter
- Worked on RL (Reality Labs) VR/AR at Meta, shipping Quest 2 during COVID and incubating Ray-Ban Stories (later Ray-Ban Meta) and Horizon OS
- Held weekly leadership dogfooding sessions (with a PM and a design partner) to give fast feedback on features about to ship
- Treated hands-on debugging of hard-to-reproduce Horizon OS issues as her "maker time" (e.g., floor-height bugs)
- Left a happy VR role at Meta to join Anthropic, drawn by its mission-driven culture

### Adrien Friggeri's Meta Chapter ([[summary-20260112 - New Grad to Principal Engineer (IC8) at Meta (Career Story) ｜ Adrien Friggeri]])
- Joined Facebook's ~20-person "data science" team in 2011-12, which built the A/B testing and data-measurement infrastructure before the "data scientist" title was repurposed for product analytics around 2014.
- Built Bento, Meta's Jupyter-based notebook platform, seeding adoption through new-hire boot camp/data camp and legacy-system support.
- Pivoted from "the data guy" to product/hardware, leading all user "experiences" on an unreleased smart-glasses line, and earned IC8 (Principal Engineer) by pairing impact with consensus built ahead of calibration.

### Igor's Meta Experience ([[summary-20260123 - Meta Senior Staff (IC7) Eng's Honest Demotion Story]])
- Joined as a senior staff (E7) and felt Meta's senior space was crowded; Meta had begun managing out the lowest ~10% of performers.
- Meta had no process for demoting an IC within the same job family, which surfaced when he asked to drop from E7.
- Described Meta's culture as setting arbitrary, aggressive deadlines with constant leadership status updates that people eventually dismissed.

## Related

- [[Fiona Fung]] — VR/AR leader at Meta, then left for Anthropic
- [[Facebook Marketplace]] — Meta/Facebook product she helped build
- [[summary-20260104 - Anthropic Eng Leader： Mentorship Advice, Microsoft vs Facebook, Career Learnings ｜ Fiona Fung]] — source summary
- [[Dogfooding]] — her signature leadership practice
- [[summary-20241101 - Job Hopping to Staff at Airbnb by Age 26 ｜ Zach Wilson]] — source summary
- [[summary-20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Feb 2024)]] — source summary
- [[summary-20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023)]] — source summary
- [[summary-20250301 - Amazon Principal Engineer (L7)： Layoffs, Interviewing & Career Growth ｜ Steve Huynh]] — source summary
- [[Ryan L. Peterman]] — went E3 to E6 at Meta
- [[Rahul]] — went E3 to E6 at Meta
- [[Zach Wilson]] — hired at Facebook as junior from mid-level startup role
- [[Lee]] — worked at Meta as L6 Staff Engineer
- [[Steve Huynh]] — referenced Meta's hiring and AI predictions
- [[Instagram]] — product at Meta
- [[Workplace]] — internal communication tool at Meta
- [[Staff Engineer]] — the E6 level at Meta
- [[Down-Leveling]] — title adjustment when entering Meta from startups
- [[FAANG]] — the group of companies Meta belongs to
- [[Jender]] — Zach's manager on the Growth team
- [[Boot Camp]] — onboarding program at Facebook
- [[Performance Review]] — the PSC process at Facebook
- [[Mis-Leveling]] — Zach's experience being hired at the wrong level
- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[AI as Amplifier]] — Steve's framework for AI's impact on engineering
- [[summary-20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey]] — source summary
- [[Portal (Meta)]] — hardware device developed at Meta
- [[Building 8]] — Meta's hardware division
- [[Buck]] — Meta's custom build system
- [[Messenger]] — Meta's messaging platform
- [[RTC]] — the video calling infrastructure team
- [[Code Review Culture]] — differences between Meta and Pinterest
- [[Alex]] — Rahul's co-founder, met at Meta
- [[summary-20250523 - OpenAI & Meta Distinguished Engineer (IC9)： Working With Zuck, Carmack & Career Growth ｜ Philip Su]] — source summary
- [[Philip Su]] — IC9 at Meta, built London office
- [[Mark Zuckerberg]] — CEO observed by Philip Su
- [[John Carmack]] — legendary IC at Oculus/Meta
- [[Scott Renfro]] — force multiplier IC at Meta
- [[Bosworth]] — former CTO, Philip's first manager
- [[Shrep]] — former CTO, Philip's manager during London years
- [[Oculus]] — VR division of Meta
- [[The Great Post Explorer]] — internal tool built by Philip Su
- [[Ben Matthews]] — member of Meta London landing team
- [[Landing Teams]] — Philip's approach to building Meta London
