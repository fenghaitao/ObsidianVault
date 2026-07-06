---
title: "summary-2026-01-26 - How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code"
type: source
tags: [source, marketing, claude-code, internal-use, skills]
sources: ["raw/01-articles/claude/2026-01-26 - How Anthropic&#39;s Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Austin Lau, a non-technical growth marketer at Anthropic who had never opened a terminal before Claude Code, built two workflows that cut ad creation time from 30 minutes to 30 seconds: a [[Figma]] plugin generating ad creative variants in one click, and a Google Ads copy workflow combining campaign data with Agent Skills for brand voice and RSA best practices, exporting upload-ready CSVs.

## Key Points

- **Figma plugin**: took ~45-60 minutes to build; eliminates repetitive copy-paste across Figma and Google Docs when producing ad variants across multiple aspect ratios — paste headline copy once, click a button, get all permutations for a creative.
- **Google Ads copy workflow**: a custom `/rsa` slash command asks for campaign data, existing copy, and keywords, then cross-references inputs against Skills Austin built for Anthropic's brand tone/voice, product accuracy, and Google Ads RSA (responsive search ad) best practices — Google's RSAs require 15 unique headlines under strict character limits. Output still requires human refinement and manual review before upload; the skills' underlying copy/examples were written in partnership with product marketing and copywriting teams.
- **Getting started approach**: started with a throwaway calculator app just to see how Claude responded, before tackling real workflows — start small and repetitive, stay curious, talk to Claude like explaining a problem to a colleague (no coding vocabulary needed), and build on existing resources (pointed Claude Code at Figma's own API docs for the plugin).
- **Broader marketing-org results at Anthropic**: Influencer Marketing frees 100+ hours/month writing scripts; Customer Marketing drafts case studies in 30 minutes instead of 2.5 hours (10 hours/week saved); Digital Marketing's web-development workflows lifted productivity 5x year-over-year; Product Marketing uses Skills and Projects for launch briefs (5-10 hours saved per launch); Partner Marketing built self-serve event enablement cutting trade-show prep time 40%.
- Frames the growth-marketer role as evolving toward product-manager-like scope: not just executing campaigns, but building the tools that achieve marketing targets.

## Related

- [[ClaudeCode]] — the tool underlying both workflows
- [[Figma]] — plugin platform automated for ad-creative generation
- [[ClaudeCodeSkills]] — Skills used for brand voice/tone and RSA best practices
- [[Anthropic]] — the company whose Growth Marketing team is profiled
