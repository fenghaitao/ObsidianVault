---
title: "CRUSH Your Backlog With Background Agents in Cursor"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Brian Casel"
---

# CRUSH Your Backlog With Background Agents in Cursor

Why does actually shipping our apps always end up taking longer than we think it should? It's because every time we want to focus on building that next big feature in our road map, we're ambushed by our backlog. The bug fixes, the quick requests, or the endless just one more thing. Well, that changes today. Enter background agents. This past month, Cursor just launched their background agents feature, and OpenAI launched their codeex product.

And both of these tools are aimed at letting us offload certain tasks to background agents so that we can focus our time and our mental cycles on the more important things in our road map. So in this video, I'll show you how I spin up background agents in cursor and how to be selective about which jobs are best for background agents to handle for us. Look, I'm not here for the hype. After 20 years of writing full stack code by hand, today I'm building with AI for the leverage. I want to ship more ambitious software faster and I want to erase all the busy work that often makes my craft feel like a grind. Background agents feel like the multiplier that we've been waiting for.

Now, in my last video on this channel, I showed you a new workflow that professionals are using to take an active approach to working with AI agents on largecale projects. In this video, we're gaining efficiency in our backlog by delegating those tasks to background agents. By the way, I'll be teaching a workshop soon, so drop a comment below with your top question about building with AI and I'll make sure you get in on that. All right, let's get into it. So, here is an app that I just built yesterday. It's a habit tracker app.

It's built with Ruby on Rails and Inertia and React. I built it in cursor with agent mode. Pretty simple. It's not quite ready for prime time yet, but it's coming along. And so up here, I can track my 14-day streak of how I'm doing on my habits. Of course, I have a zero day streak right now because I just built this app yesterday.

And then I can create these habits down here that I want to track and I can mark them off as complete every day and keep the streak going. Now, I want to speed up my road map and push some of my backlog to background agents. So, how should we think about this? Well, I'm looking for tasks that I don't want to babysit. I want them to get done, but while they're getting done, I need to be working on something else. Now, I've been testing background agents this week, and I'm realizing that there's a pitfall that we should try to avoid.

You know, the tendency is to want to delegate the larger, more complex tasks to background agents because they're so timeconuming. But while a background agent can execute most tasks the same way that a foreground agent can, the more complex the task is, the more likely it's not going to be 100% perfect in one shot. So then you'll probably need to take your tasks back to your foreground agent, give it some feedback and tweaks and finish it off. And that's possible using cursor's background agents feature and I'll show you that here. But it sort of defeats the purpose of delegating to the background agent in the first place. Right?

So my advice here might seem a little counterintuitive. But when it comes to picking tasks to give to your background agent, I think you should pick the ones that are easier, smaller, more predictable because even though you could knock those out pretty quickly, they really add up and you should be focusing your time on the bigger, more important pieces in your road map. And by delegating the easier tasks that a background agent can crush in one shot, that's how you start to see the efficiency gains. All right. So, in this project, here are three chores that I'm am glad to have a background agent tackle for me. The first is going to be a simple design tweak.

You see this mark complete button? I don't really like how it doesn't really look like a button. It looks more like an alert or something. So, we need to make that a more solid button. And also, I don't like how the text is to the left. It should be centered.

So, we'll get that cleaned up. I also noticed a bug. So, if I try to delete a habit, we're running into this error. So, we'll let the background agent handle that. And the last one is an accessibility task. So currently, if my system was in dark mode, the app does not display in dark mode.

And so we should add that dark mode support. So let me show you how I'm setting up these background agents in cursor. Now the first thing is you need to make sure that you have privacy mode turned off in cursor. So you'll go to settings and under general, you've got privacy mode. That needs to be disabled in order to use the background agents feature. I don't know if it'll always be that way in the future, but currently it is.

So, just make sure you have that disabled. Another thing, and this gets into the costs of running background agents in your cursor account, you do need to make sure that you have usage based spending turned on and you'll need to fund it with $10 or $20 at least. And I really hope that they change this as the feature comes out of beta because even if you haven't used up all of your included requests, the background agents are always going to use your usagebased spending. And if the background agents are using max mode, which cursor encourages you to do, each request might use 10, 25 cents. I've seen some use up about 50 cents. As you can see, I've been using it a lot this past week.

Now, the bottom line here is I don't think that using background agents is cost prohibitive in most cases, but it is a bit pricier than using a normal AI agent. So that's another reason why you want to be more selective with the types of tasks that you delegate to your background agent versus the ones that you handle in your foreground agent. Okay, let's set up our first background agent. So in cursor, you can get to your background agents a few different ways. You can click this icon up here or I prefer the keyboard shortcut that's commande and that'll launch this here. So this is where you can, you know, create a background agent or I can escape out of that and I can also start a background agent using the main chat window.

By default, it's on agent mode, but I can switch that to background. And then it's like the same thing. I'm creating a background agent here. One thing you'll notice is it'll automatically switch the model to a model that uses max mode. So again, that does use up more credits than the non-max models. So, you know, pricing is something to keep in mind.

When I was using this earlier, it actually didn't even let me use a non-max model. But now, I actually can switch it, but they're still just going to like recommend that we use a max model. I think that's because they're assuming that a background agent needs a really large context to complete a large task. Again, my recommendation is to keep the tasks tight and simple. So maybe a max mode isn't always required, but you know, you'll need to experiment with it and see what works for you. So same thing over here, you can select the model.

Now, another thing that tripped me up a few times is you do need to be aware of which branch you're working off of. It's always going to default to your main branch, even if you were previously working in a different branch. So, if I was on another feature branch and there's a bug on this feature, but it's not actually in the main branch yet, then I would need to make sure that I switch to that branch here, so that when the background agent starts up, it starts off of that branch. Now, it will create its own branch to make the change and then we'll see the PR that we can merge back in. But here, you do need to set the branch that you want as your starting point. This is just a demo app.

I only have the main branch, so we'll go with that for now. All right, let's get that first prompt in. You know, again, I'm just asking it to tweak the design of the mark complete button so that the button is more of a solid green color, a bit larger, and the button text is centered in the button. All right, so the first time you do this, it'll ask you to connect your background agent to the GitHub repository for this project. I'm going to click connect. That's going to take me over to GitHub.

You'll need to make sure that you're adding the repository. I'll save that. I can close that. And there we go. That should just start right up. Now, if you run into GitHub connection issues, and I have ran into a few while I was testing this, you'll need to go into cursor settings, and you can go to background agents, and under here, you'll see GitHub access.

You might need to refresh it, reconnect it. Another thing that I found is restarting cursor also helps because I know that cursor caches a lot of these settings. So, if you change things up on your GitHub repository, you'll need to restart. Anyway, that's where you can troubleshoot things. But looks like we have our first background agent up and running. It created a new environment and then it actually creates like an interface that essentially is like another cursor inside of cursor, right?

And so here we go. The background agent is doing its thing in the chat window here. I don't need to do anything. I can just get out of this and I can work on something else now, right? And actually, I'm going to let that work and we're going to start up another background agent. So, let's take care of that bug with the delete button.

I'm just going to recreate that error. So, I'm going to hit delete and we run into the error there. So, now we have the error in our logs and I'm just going to highlight that. Now, I can add to the chat, right? So, now we have that in the context window. And instead of just asking the agent to fix this bug, I'm going to push it to the background agent.

Just like that. Please fix. We can delete a habit. All right. So let's open this up again. And so this is the second background environment that's being spun up by the background agent.

Now up here we can see my two tabs, right? So now I have two different background tasks that are set up here. This one is just getting underway. This one is actually showing the green check mark which means it's all done. We're going to come back to that. We're going to look at the results in just a minute.

But first I want to add a third background agent. And again that third one was to implement dark mode for our app. So, I'm going to start up another background agent. I'm going to give it this prompt where I'm asking it to support dark mode so that when a user's system is set to dark mode, all of our colors in the app will show the dark versions that are in the app. I'm also telling it like, hey, we don't yet need to implement a toggle switch for light and dark mode. That's something that I can add later and maybe consider giving it to another background agent.

But again, my goal is to keep these tasks tight and simple and easy to complete in one shot. So, let's go ahead with this one. And we're spinning up our third background agent. And so, now I can toggle between my three different background agent jobs. And the first two now show that they've been completed and the dark mode task is doing its thing. So, again, while that works, I'm going to go take a walk, maybe grab a coffee, do some other work, might even do some marketing work for a change.

Okay. Okay. Now, while the dark mode task is still working, let's take a look to see how we did on the other two tasks since they both seem to be done now. So, let's go to that first one where we tweaked the design of the mark complete button. So, when it's all set, you'll see the green check mark and I can, you know, go back and review all the history from this background agent. I can review the file changes.

This was a pretty simple one. Looks like just one line change here with a bunch of new tailwind styling. So over here we have a couple options. I can create a pull request which I'm going to do in a minute. But first I actually want to check it out locally so that I can take a look. Right.

So I'm going to click this. And what this does is it actually checks out the branch that cursor created. So my terminal is set up to show me which branch I'm currently on. And I can see that I'm on this branch. So cursor creates a new branch named cursor slash the name of the task. And that's where it does all of its work.

So it's separate from, you know, whatever other code you have going on in your project. So now that I have it checked out locally, I can run my server and take a look to see how it did. Okay, so this is actually much better. I can see the mark complete button. It actually looks like a button now. The text is centered and yeah, that's working well.

I'm going to complete this habit because I actually did do my exercise this morning. All right, so I've got a little little bit of a streak here. It's getting a little choppy, but that's okay. All right, let's see how we're doing on the other tasks. So, our dark mode task is still in progress, but the fix for deleting habits appears to be all set. So, here it is.

I can again review the code. Looks like a simple fix here. I've got the summary from the agent and I am going to check it out locally so that I can test it out to make sure that it works. So, I'll click that. Okay, so now we're on that branch and I'm going to start my server. I can sort of take a look and see what happened here.

I can look at the file itself and I can see the changes. It was a simple fix. So, I'm going to refresh and let's try to delete a habit. There we go. It works. Good to go.

Now, before we check the work on implementing dark mode, the next step after you've taken a look at the results of your background agents work is you can create a pull request. So, I'll close this. So once you see the green check mark, you'll have this ability to create a pull request and that'll open up GitHub. It'll write up a whole pull request with all the details. You can go ahead and create that and then you or someone on your team or maybe another AI agent can actually review the code and then merge it into your project when you're ready. So now I'm in the other background task for improving the mark complete button.

That one needs a pull request. So I'll go ahead and click that. And here it is. It wrote it up with all the details. Very cool. So that's all set to go and we can merge that in a little bit later.

All right. Finally, let's go into our dark mode implementation. And our AI has given us sort of a summary. It made a bunch of changes. So this one actually made quite a few changes to multiple files and it added, you know, all the dark variants to all the tail and CSS colors. So let's take a look at that.

I have checked out that branch. I'm going to refresh my server. This probably isn't even necessary. It's just sort of a habit, especially when I'm making like a CSS changes. So, I'm going to refresh now. I'm going to set my system to dark mode.

And hey, there we go. So, we're in dark mode. Nice. It actually did a pretty good job of finding every single color on the page and giving it like a dark mode variant. Now, I'll probably want to tweak this hover state. That looks a little bit weird, but you know, I can get to that a little bit later.

Maybe in a separate task, maybe even for a background agent. So, that works. I'm going to go ahead and create that pull request. There it is. Add dark mode support. Got all the details.

I'll create the pull request. And then when our app is ready for each of these fixes or new features to be merged in, we just need to go into the pull request and merge it up. All right. I've got a challenge for you. I want you to think about your current project that you're working on this week. pick out one task that you would like to delegate to a background agent and then leave a comment and tell us what your project is and what that task is.

I want us to like create a big list of task ideas that we can all start to think about as things that we can get off of our plates, delegate them to background agents, and we can become more productive. Now, when you want to take a more active approach to leveraging AI in your big important projects, you'll need a better approach than just vibe coding and spinning your wheels. So, check out my other video where I show you how professionals are building with AI right now. See you there.
