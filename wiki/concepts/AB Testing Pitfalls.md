---
title: "AB Testing Pitfalls"
type: concept
tags: [ab-testing, experimentation, product, statistics]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/30 - The surprising advice from a founder who built 2 unicorns ｜ Jason Cohen (WP Engine).md"]
last_updated: 2026-07-10
---

## Definition

AB Testing Pitfalls is Jason Cohen's critique that most AB testing is ineffective because: (1) it can't test the important things (strategy, vision, insights), and (2) even for mundane details, most positive results are false positives. Cohen argues that unless you're highly sophisticated, AB testing is largely a waste of time.

## Key Arguments

### 1. Can't Test What Matters

You cannot AB test whether Uber is a good idea. Strategy, vision, insights, and anything actually important to the company's success cannot be A/B tested. The things you can test (button color, copy variations) are the things that matter least.

### 2. Most Results Are False Positives

Even when the statistical tool says a result is significant, false positives dominate because:
- The tools are not statistically accurate
- When the effect you're looking for is rare (most AB test improvements are), false positives occur more often than genuine effects
- Even at 95% statistical confidence, most "winners" are noise

### 3. The Stacking Problem

People find a "winner," implement it, find another "winner," implement it... and a year later, conversion rates are unchanged. The expected cumulative improvement from stacking all these "winners" never materializes because most were false positives.

### 4. The Shopify Evidence

Shopify's CTO (on Lenny's Podcast) revealed that their team of ~100 people uses holdout groups to verify AB test results. About a third of their positive test results simply disappear over time — and this is with a large, sophisticated team. If Shopify can't make it work reliably, most companies can't.

## When AB Testing Might Work

- At massive scale where a 1% improvement is worth millions
- With highly sophisticated teams that understand statistical nuance
- For very specific, narrow optimizations (not strategic decisions)
- If you don't know who the sucker at the poker table is, it's you

## Related

- [[summary-30 - The surprising advice from a founder who built 2 unicorns ｜ Jason Cohen (WP Engine)]] — source episode
- [[Jason Cohen]] — creator
- [[Shopify]] — holdout group evidence
