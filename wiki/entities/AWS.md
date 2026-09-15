---
title: "AWS"
type: entity
tags: [company, cloud, Amazon, infrastructure]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260302 - Distinguished Eng： Stack Ranking, Competing with Bezos, Regrets ｜ Bryan Cantrill.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md"]
last_updated: 2026-09-14
---

## Definition

AWS (Amazon Web Services) is Amazon's cloud computing division, whose early EC2/S3/S3-stage moves Bryan Cantrill watched from Joyent while competing against it in public cloud.

## Key Information

- Amazon "hit the mother lode" by letting S3 and EC2 be developed and realizing it was onto cloud computing before anyone else had figured it out.
- Every AWS re:Invent in the ~2015 era brought a price cut plus new services; Cantrill credits this ruthless execution with making the cloud look like a terrible business to outsiders.
- Amazon did not break out AWS revenue, and analysts asking were told "we're not talking about that" — obscuring how profitable the business actually was.
- Cantrill, who competed with Amazon, says "the margins on this thing are great," and that AWS-era re:Invent no longer offers the same "can't live without" new services and price cuts.

### In the Kubernetes Origin Story
- At the time Kubernetes started, "AWS was dominant. They were there first and doing very well," while GCP was an up-and-coming third.
- Burns argued GCP should stop "tail light chasing" VMs and instead create a new playing field; he notes partners like Red Hat, Azure, and AWS could later "take a bet on Kubernetes" because of its independent governance.

### Marc Brooker on AWS Operations

- AWS Distinguished Engineer Marc Brooker read between 3,000 and 4,000 industry postmortems/Amazon COEs, and AWS runs a broad weekly COE-review meeting across engineers, leaders, and senior leaders — which he calls a core, almost causal factor in AWS's success.
- The collision of customer demand (serverless/container workloads) and the technical trend of block storage becoming the durability layer produced Aurora Serverless and Aurora D SQL, built on S3.

## Related

- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Kubernetes]] — the project positioned against AWS's dominance
- [[Google]] — the challenger (GCP)
- [[Thought Leadership]] — the strategy to compete
- [[summary-20260302 - Distinguished Eng： Stack Ranking, Competing with Bezos, Regrets ｜ Bryan Cantrill]] — source summary
- [[Amazon]] — the parent company
- [[Jeff Bezos]] — the executive behind the strategy
- [[Joyent]] — where Cantrill competed with AWS
- [[Bryan Cantrill]] — who describes AWS's economics
- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — Distinguished Engineer's operations/postmortem account
- [[Postmortems]] — the COE learning practice
- [[Amazon Aurora]] — the database work led by Brooker
