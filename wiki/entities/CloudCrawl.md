---
title: "CloudCrawl"
type: entity
tags: [product, web-scraping, bright-data, crawler, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - From MCP to Scale： Pipelines That Build Themselves — Rafael Levi, Bright Data.md"]
last_updated: 2026-06-30
---

## Definition
CloudCrawl is Bright Data's crawling infrastructure product that enables large-scale web data collection through the Bright Data MCP. It handles anti-bot systems, captcha solving, and proxy rotation, allowing agents to access any public website without getting blocked.

## Key Information
- Part of Bright Data's web data platform
- Rafael Levi prefers CloudCrawl over Crawlera because it "gives less headache"
- Used to build self-healing scrapers: agent explores page via MCP, identifies selectors, builds scraper, CloudCrawl executes it
- Enables scheduled/recurring data collection (e.g., every 30 minutes) with automatic validation and repair
- Can run thousands of remote browsers on Bright Data servers
- Supports geo-targeted IPs for region-restricted content
- Browsers mimic human behavior with pre-recorded mouse movements and variable typing
- Accessible through the Bright Data MCP's 66 tools

## Related
- [[Bright Data]] — parent company
- [[Crawlera]] — alternative Bright Data crawler product
- [[Rafael Levi]] — speaker who demonstrated CloudCrawl
- [[Web Scraping Pipelines]] — pipeline approach enabled by CloudCrawl
- [[Self-Healing Pipelines]] — automated maintenance of CloudCrawl scrapers
- [[Remote Browser Infrastructure]] — underlying browser farm
- [[summary-20260607 - From MCP to Scale： Pipelines That Build Themselves — Rafael Levi, Bright Data]] — primary source
