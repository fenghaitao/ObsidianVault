---
title: "How Notion built with Claude Managed Agents"
type: transcript
source: youtube
playlist: "Product Launches"
author: "Claude"
---

# How Notion built with Claude Managed Agents

Hi, I'm Eric. I'm a product manager at Notion and I work on our agents and agent orchestration. I had 30 tasks to make a prototype. I took all of that and just dragged it to start and it was like Claude running wild. I was like, oh, I don't need to watch this. So, I got like a snack.

I came back and like all the prototypes were made. That was sort of the unlock. We want Notion to be the agent orchestration platform. Notion is such a good place for human and agent collaboration. You bring the right agent together for the job and we help to manage all of your workflows. We were really excited about bringing managed agents into Notion because Claude is really good at complex long-running tasks.

If you were to roll it up yourself, it's like a mega brain engineering effort. You need like a PhD in all of this to make it work. And so, the managed agent product was great because it makes it really plug and play to bring in Claude. He runs the sessions in the cloud. We just pull in the API and it works. For our customers, what that means is that they can kick off a ton of jobs in Notion.

I'd love to show a use case of how we use managed agents to build agent orchestration in Notion. So, this example is something that a lot of our non-technical users do, which is they'll onboard clients. Let's take a fictitious client called Harbor and Pine. They are a lifestyle brand and now here are all the action items we have within Notion's a custom agent and we've basically given it all of the client databases and task boards. So, it has the full context to onboard and it helps us in the onboarding workflows for clients. Behind the scenes, this agent has Claude as well.

It is pulling in all the contexts within Notion to go and generate this. And so, what I want to do is call upon the client onboarding manager and then take these action items, turn them into tasks. You can see them, they're all in this task board. And this is what I like about it, like I can take all of this and just dump it here and you can see on this side that it kicks off a bunch of agent threads. And that all basically feeds into Claude and then Claude will then kick off a Claude session on that. And so now you can talk to that Claude session within Notion here, which mirrors the actual session that was kicked off.

So, if we go into the Claude platform, you can see that this session is running for Claude managed agents. It kind of gives you a different view of what's happening. It's useful for us on the development side, right, to go and see like what's happening, but also actually to feed all these traces to go and improve our agent. Having a harness that can do long-running tasks is really essential. You might need to run it for 20 minutes, an hour. That ability to continue to run it, to manage memory, to have high-quality outputs over time is a layer that's super critical on top of the model itself.

A lot of the tasks are completed already. This is what a example home page could look like and it is pulling in all the contexts within Notion to go and generate this. And if we wanted to iterate on that, we can talk to Claude directly here. That's how we used managed agents in Notion to help ourselves and help our customers. So, the managed agent product is like a playground for me. It's just really cool to be able to kick off all these jobs at the same time.

I just love building cool
