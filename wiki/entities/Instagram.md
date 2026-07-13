---
title: "Instagram"
type: entity
tags: [company, product, social-media, meta]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/05 - The hidden pattern behind successful products ｜ Mark Pincus (FarmVille, Words with Friends, & more).md"]
last_updated: 2026-07-10
---

## Definition

Instagram is a photo/video-sharing social media platform owned by [[Meta]], led by [[Adam Mosseri]] since ~2018. As of this interview, it has over three billion monthly users (roughly one in three people alive).

## Key Information

- Founded by [[Kevin Systrom]] and [[Mike Krieger]]; [[Adam Mosseri]] took over as head of Instagram roughly 8 years before this interview.
- In 2026, Instagram/Meta product teams have shifted from large specialist teams (~13 people: multiple Android/iOS/server engineers, PM, designer, data scientist, researcher) to small generalist "[[Pods|pods]]" (4-7 people) built around a new "[[Product Staff|product staff]]" role. See [[Pods]] and [[Product Staff]].
- Instagram's ranking/recommendation algorithm relies heavily on illegible embedding vectors rather than detailed semantic understanding of user interests. A new feature, "[[Your Algorithm|Your Algorithm]]," uses an LLM to translate a user's embedding-space interest cluster into a human-readable description (e.g., "deep pour-over coffee snobbery") and lets users see and adjust it.
- Deliberately avoids pure chronological feeds by default: testing showed that when chronological is the default, both usage and overall satisfaction decline, because (a) it rewards high-frequency posting (publishers/companies crowd out friends) and (b) recency is only one input to relevance.
- Investing heavily in exploration-based ranking (surfacing niche/breakout creators a user might like but doesn't know yet) as opposed to pure exploitation-based ranking, an area Mosseri credits [[TikTok]] with pioneering; Instagram says it has caught up and leads in some areas as of this interview. See [[Exploration Based Ranking]].
- Stance on AI-generated content: won't filter AI content out, but plans to let users know whether content (and possibly accounts) is AI-generated. Likely to prioritize labeling non-AI ("camera captured") content over labeling AI content long-term, given detection reliability concerns. See [[AI Content Labeling]].
- Views the rise of abundant synthetic/AI content as a net tailwind because it expects people to increasingly seek out human creativity, authenticity, and individual points of view — reinforcing Instagram's long-standing strategic bet on creators (a broad definition including journalists, artists, small sellers, not just influencers).
- No token-spend leaderboards for engineers; AI compute/token budgets are managed like any other constrained resource (GPUs, CPUs, storage, headcount, opex). See [[Token Budgeting]].
- Product history discussed: [[Reels]] was originally built on top of [[Stories]] in 2019, which under-exposed it (low Stories read-through rate) and left Instagram out of position when [[TikTok]] surged during the COVID-19 pandemic in 2020.
- A 2021 test (4% of iOS users) that combined a video-viewer redesign, more Reels emphasis, and more recommended (non-followed) content triggered a major creator/press backlash even though it was never intended to launch broadly; Instagram has since continued investing in video, ranking, and recommendations regardless.
- Historically tied to major controversy episodes (e.g., the Cambridge Analytica lawsuit era) as part of Meta's broader public scrutiny.
- Per [[Mark Pincus]]: also cited as an example of social media that has "lost the adrenaline" — quitting Instagram has become a point of pride rather than a source of FOMO. Pincus cites NPS (net promoter score) data showing people who quit Facebook/Instagram swung from a +35 to a -35 score, describing it as feeling "like they just quit smoking."
- Also referenced (per Pincus) as a best-of-breed proven camera/photo UX pattern worth mastering before attempting to "innovate on the camera" (alongside Apple and Snapchat).

## Related

- [[summary-02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG)]] — source summary
- [[summary-05 - The hidden pattern behind successful products ｜ Mark Pincus (FarmVille, Words with Friends, & more)]] — source summary
- [[Adam Mosseri]] — Head of Instagram
- [[Meta]] — parent company
- [[Kevin Systrom]] — co-founder
- [[Mike Krieger]] — co-founder
- [[Pods]] — new team structure
- [[Product Staff]] — new generalist role
- [[Your Algorithm]] — the interest-transparency feature
- [[Exploration Based Ranking]] — ranking philosophy compared against TikTok
- [[AI Content Labeling]] — content/account labeling stance
- [[Token Budgeting]] — approach to AI compute cost
- [[Reels]] — short-video product
- [[Stories]] — ephemeral content product
- [[TikTok]] — primary competitor referenced throughout
- [[Facebook]] — grouped together in the NPS/adrenaline-loss discussion
- [[Cocktail Party Distribution]] — concept the NPS example illustrates
