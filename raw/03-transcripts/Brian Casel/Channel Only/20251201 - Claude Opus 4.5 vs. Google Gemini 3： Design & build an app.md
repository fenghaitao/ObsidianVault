---
title: "Claude Opus 4.5 vs. Google Gemini 3： Design & build an app"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Brian Casel"
---

# Claude Opus 4.5 vs. Google Gemini 3： Design & build an app

Here we go again. Last week, we had another Frontier model drop. Two of them, actually. Claude Opus 4.5 and Google's Gemini 3. And at this point, keeping up with every new release feels like a full-time job. So, in this video, I want to share how I actually think about evaluating new models when they drop.

And we'll put these two heavyweights, Opus 4.5 and Gemini 3, through a realworld test by building the same app with both of them. Now, let me be clear. There's really no way to deliver a final verdict on any model from a single test because a single demo, whether it's by me or by you or someone else, doesn't represent the full range of projects and tasks that we throw at these models day-to-day. Planning a new feature looks different from debugging an issue on production. And green field development is different from refactoring legacy code. You know, I tend to find that some models are better suited for different phases of the product development cycle than others.

But even that is a very personal preference. My workflow and style might be different from yours. So, one model might fit me like a glove, but you not so much. So, when a new model drops and I want to get a feel for it, I think the move is to try it out on the types of projects and tasks that are most important to you. Now, for me, I care most about planning and designing new products and rapidly building them so that I can deploy to first customers or start using it myself. I care about long-term maintenance, too, but I won't really know how models perform there until I've used them for months.

So, when we're in week one with a new model or two new models like we are today, I like to put them through their paces on a fresh green field project, something simple but real. And that's exactly what we're going to do today. We're going to build an invoicing app and we're going to build it twice. Once using Opus 4.5 and again using Gemini 3. Same spec, same requirements, head-to-head. We'll go from planning to design to building it out.

And if you're looking to upgrade your process for how you build with AI, then I want to send you my builder briefing. It's a five-minute read that I send every week to cut through the noise and help you keep a pulse on what's actually working for professional builders. You can get yours by going to buildermethods.com. And if you want to go deeper and connect with other builders, my builder methods pro membership is currently still on sale for Black Friday. That's where I share projectbased training, live workshops, and we have a community of builders who are figuring this out together. Now's a great time to join us by going to buildermethods.com/pro.

All right, let's build this thing. Okay, so what we're going to do is build the same app twice. So I've fired up two separate codebases. The first one here I named invoicy opus and then the other one is named invoiceicy gemini. So these are both rub on rails with inertia and react and we'll be using Tailwind CSS and some shad CN components. Now, the process for designing and building this app is going to be sort of a a speedrun version of what I usually do.

I I usually take a much more methodical approach, but for the purpose of this demo, I want to get through the entire design process and the building process for a simple client invoicing application. Now, what I've done in both of these is I've added a folder called plan. And inside that, I have a product overview file. And this is basically just an overview of the simple invoicing app that we're going to build. You know, I've got this information up here, some information about the like the shell of the application. We're going to have a dashboard view.

We're going to have a a view for managing clients, a view for managing invoices, uh the ability to have like a sharable invoice view that we can send to a client, and then I just gave it some information on the tech stack that we're working with. So, I'm going to reference this product overview when I give it the prompts. And I also prepared two prompts that we're going to be using because we're going to break this very simple design and build project into two phases. The first phase, I want to see how these models can handle designing a a professional front-end interface for for the views in this app. And then the second prompt is where we will, you know, wire up the back end and make it a functional product. The other thing that I'll be looking to do throughout this process is to see how Opus 4.5 compares to Gemini when it comes to planning and asking clarifying questions.

So let's get started with this Opus project and see how it can handle the first phase which is planning and designing this application. So, I'm going to run claude code. And first I'm going to say uh reference product overview for an overview of what we will be building. And then I'm going to go into this prompt. And I guess I could just like reference this prompt file as well, but I'll just copy and paste it. And so to show you what I just pasted in for this first prompt is let's start with the front-end design.

We won't be building the full API backend functionality just yet. Start by stubbing out these routes and views for the dashboard, clients, invoices, invoice editor, and sharable invoice. And then I'm saying use your front-end design skill to design a clean professional front-end design. So on my system in my home directory, I have installed a cloud code skill called front-end design. And a couple weeks ago, the team at Anthropic shared this uh skill in this blog post called improving front-end design through skills. And I've been using this on a bunch of recent projects, and it works really great.

So, you can see my previous video about claude code skills and what they are and and how they work. Uh but the team actually provided a specific skill skill that they call front-end design. And I have that installed in my home directory in my claw directory in skills. And you can see front-end design and it's this simple build.md file. Anyway, you can read more about that from their blog post. I just copied it as is and it works really great.

So, it just adds a little bit of design muscle to cla code. So, we're going to use that in cloud code and I'm also going to reference the same skill in Gemini 3 when we do that. It it's easy to do. So, we'll get into that as well. So, so I'm telling it to use that front-end design skill. I gave it a few more requirements about, you know, I want it to be mobile responsive.

I wanted to support light and dark modes. Some information about how we're using Tailwind, Google Fonts, Lucide icons. When finished, just give me like the five uh route URLs so that I can easily preview them in the browser and we can see what they what they look like. All right. And and also I'm asking it to start by asking me clarifying questions to inform your plan for this. And you know what?

I'm actually going to toggle into plan mode. Specdriven development can take many different forms. And today we're going to take probably like the simplest possible approach to this. So I always like to start in plan mode and really dial in the plan. Specifically, I want to see how Opus 4.5 is going to ask me constructive clarifying questions to make sure that we're set up for success here. All right, so I'm going to send that prompt and let's get going.

Okay. And by the way, in the latest versions of Cloud Code, I really like how they've added this question and answer interface, which makes it really easy for me to, you know, select answers to these uh questions that the agent is posing back to me. I love this pattern of having the agent ask me back questions. It's such a powerful underrated, I think, aspect to the planning phase when it comes to building stuff with AI. All right, so what Google font would you like to use? I'm just going to use it's since this is a simpler app with just a few pages, we'll go with a top navbar for the sharable invoice page.

Yes, this should be a standalone layout. Okay, I'll submit those answers. So, just evaluating Opus 4.5's ability to plan and ask questions. I'd say I was pretty happy with those questions. They all seemed pretty accurate and constructive. So, something I like to see.

All right, let's see how it does with putting together an implementation plan here. By the way, Claude Code has started actually saving its plans. Yeah, you can see here. Um, it it gives it these weird names. Mutable greeting fog. What's kind of weird to me is that it it actually saves those plans in in the home directory in Claude in the cloud directory.

And then you can see inside plans, you'll find it here, you know, with these kind of cryptic names. I kind of wish that it would have just saved the plan into my codebase into my project. I guess I could like instruct it to do that, but it just seems weird. I would rather have the plan in the actual project where the plan happens. But anyway, here is the plan. Yeah, that looks pretty good.

I see some design decisions. It's going to stub out some routes. It's going to create these page components. You know, in a normal typical project, I would spend a lot more time reviewing this line by line, but I think I think this is looking good. And yeah, let's go ahead and have it um let's go ahead and have it design these these front ends for our app. Okay, so Opus 4.5 and cloud code has completed its work.

I'd say that took about 10 minutes or so and and here is its final report. Implementation complete and it gave me the list of URLs exactly as I asked for. We're going to take a look at those in just a second. We've got a list of components that was built. Um, so I'm going to go ahead and start my server. [clears throat] Okay, so here is the the dashboard view.

This was created by Opus 4.5. And so, uh, yeah, it went with that like emerald green color. I do like I I do kind of like this navigation centered across the top. That's interesting. Created a nice little icon and text logo there. One thing I don't love is the double up of this button.

So, I assume that this is going to be like a global button shown on all pages. And here, since we're on the dashboard, I've got like a new client and a new invoice. So, just visually, I don't like seeing these two things together on the same page like that. Um, but that's that can be tweaked. Got this nice got this nice metrics layout. Don't know if I love the weird padding on those, but that's okay.

Just the the designer in me is being a little nitpicky, but I guess that's the the point of this whole exercise, right? This is a nice touch. I like this like great progress this month. Uh something I did not ask for, but that's an interesting interesting one. This stuff does actually follow the instruction that I gave it in terms of what I want to see on this page. So, I did ask it to support light mode and dark mode, and it actually didn't do that this time.

Interestingly, I did a test run of this project off camera earlier, and it and it did handle dark mode that time, but this time during recording, it it did not. So, you know, that's just another example of how you can run the same prompt twice, even with the exact same model, and sometimes it'll just, you know, perform a little bit better than others. I did ask it to make it mobile responsive. So, let's see how it did with that. And that's that's looking pretty good. Everything Everything does break down.

Everything does break down uh pretty good. Although, I'm seeing some some side scrolling bleed when we get to a really small screen size there. Got a nice mobile mobile slideout menu there. That's That's kind of cool. Okay. Pretty impressive.

All right. So, that's the dashboard view. Let's take a look at the other views. Do these link? Yes. Okay.

So, here is the uh client list. Looking pretty good. I don't love this this handling of the padding. A little bit too close to the edge there for my taste. Um once again, like the two green buttons here a little bit competing for my attention. Okay.

So, we got some nice menus here, some nice sample data. That's looking pretty good. Okay, it actually uh gave me like a new client modal popup. Now, normally I would like really plan out all these little details during the spec and the planning phase, but again, we're doing sort of like a a speedrun uh test here. So, here's the invoices view. Again, like this this left padding is a little bit tight for my taste.

Um we do have the filter, which is nice. Something that I did ask for. A little bit hard to read these numbers, but that's okay. Let's let's see how that works on mobile. This is so this is good. So, you know, this is actually a hard thing to do is to make a list like this collapse down to a mobile view.

And it it seemed to do a really good job on that. Okay. So, here is the invoice editor view. We can select a client. We can add some invoice items. Looks good.

And let's see the preview. Okay. So, that one doesn't link, but I believe that it did actually create that. So, here is that URL. And that's okay that it doesn't link because really I only asked it to to do the mock-ups for now. We're going to do the back end wiring up here in just a second.

So here is the uh sharable invoice which you know does look nice and professional, nice and clean. One thing I'm noticing again just a small detail is like there's this extra space due to the looks like it's due to the rounded corner. Um and this gradient really should go all the way to the top. Just being very nitpicky about this, of course. Um, and let's see how we look on mobile. Okay.

Yeah, it breaks down nicely. So, overall, I'm I'm pretty impressed. And there are some some little details that I would normally like spend a little bit of time polishing up with with Claude. But, but yeah, I think that's a really good test run. Okay. So now let's jump over to our project with Gemini 3 and we'll run the same process of starting with the design of the front-end views for this new uh invoicing app.

When I use Gemini or any other model that is not a cloud model, I'll use cursors agent mode for that. So that's what we're going to do when we're in this Gemini project. I'll just make this a little bit bigger and I'm going to switch the agent to Gemini 3 Pro and I'm going to start in plan mode just like I did in Claude Code. Cursor also has a very nice and capable plan mode here. Now, just like in the Opus project, I also have this plan folder here in the Gemini project. It has the same product overview that I had over there and I have the same prompt one and prompt two, which we'll get to in a little bit.

Now the only difference here in the Gemini project is that I added this front-end design skill.m MD. So this is literally that Claude code skill for the front-end design that I used in Claude code. I want to make the same skill or that same design muscle available to Gemini to try to put them on, you know, equal playing field here. So, so I'm going to start by saying refer to product overview for an overview of what we will be building. And then I'm going to go to prompt one and I'm going to copy that in. Again, I guess I could just, you know, reference it as well, but I just want to make it clear that that's the prompt.

We're going to start with the front-end design. We're going to have it stub out these routes and views. I gave it a few requirements and and that's good. Now, here is just one thing I want to tweak for Gemini. Since it doesn't quite have that claude code skills feature, I'm going to rewrite this part. Um, refer to front-end design skills.

So, I'm literally referring to this file right here and use that skill set to design a clean, professional front-end design, UIUX for these views. So, hopefully that will be good. Now again, we're still in plan mode, and I'm just going to ask it to ask me clarifying questions to inform its plan. So, cursor in plan mode also has a very nice question and answer interface, just like Claude Code does. I love how all these tools are really starting to converge on the same set sets of features and the same paradigms. I think that's that's really great for all of us.

So, here's the first question. So, it's asking me like which design aesthetic should it lean toward? That that's an interesting question. a little bit different from what Opus was asking me. Yeah, let's go with modern SAS. What's your preferred navigation layout?

Similar question to what Opus asked me. Uh, we'll go with the top bar navigation since this is like a simpler app with just a few links. How would you like me to handle dummy data for these views? That's a really interesting question because it's part of a new design process that I'm that I've been tinkering with myself is uh generating sample data first. Again, it's a little bit, you know, again, that was just a little bit too much process for this simple demo. But Gemini 3 is is sort of thinking along the same lines as how I'm thinking about my my new design process.

So, yeah, let's go with a centralized mock data. That's that's good. Shall I add more SHA shad CN? Yes. And install the standard ones. Okay.

So, these were very good questions. I would say I was pretty impressed with uh Gemini's thoughtful, constructive planning questions here. Okay, so that plan is all set and I can I can review it here. One of the nice things I like about plan mode in cursor is I can just click this button to save it to the workspace and it does that. It puts it right into the actual workspace into the project unlike cloud code which for some reason puts it in my home directory. I do wish it would just save it automatically or if there was a setting for that, but at least it's it's right here.

And I also like that the that it has a more relevant name for the plan or this this is essentially a spec, if you will. So, yeah, here it is. Here's the plan. Looks pretty good. And interestingly, you know, I've seen I've seen it do this before. I don't know if this is a Gemini 3 thing or maybe an issue with cursor, but it actually didn't create to-dos.

Uh, sometimes I need to give it a little bit of a nudge. Create your to-do list for this plan. And I've only started seeing it do that since I've started experimenting with Gemini 3. So, that's that's an interesting quirk. Okay, so now it added its 10step to-do list to its plan. And uh, yeah, that's all looking good.

So, I guess sometimes you just got to give it a little nudge, right? So, I'm going to go ahead and press the build button to have it start designing the frontends. And I do have Gemini 3 Pro selected as the model for that. So let's go ahead. [clears throat] Okay, so it's completed its work now. And I would say it took about half the time that Opus 4.5 in Claude Code took to do the same task.

But I don't know if that's a Gemini thing or a cursor thing because I have noticed that when I run Claude models in cursors agent mode, they actually execute a lot faster than they do in cloud code. I think cloud code just might generally be slower to execute things for whatever reason, whatever magic is happening under the hood there. So, here is the final message and it gave me the list of URLs and let's let's go ahead and take a look at that. So, I'm going to run my server. Okay, so the first thing I notic is that it doesn't actually work. So, when I view this this URL at dashboard, I'm seeing nothing.

So, let's see if we have any issues. Okay, so here we go. So, here is what I'm seeing. Let's Let's try out Gemini's ability to debug this. Seeing a blank screen and this error. Okay, I'll just restart the server and see how we're doing.

Huh. So, now we have a syntax error. Not off to a great start, Gemini. I'm using CleShot to to grab snapshots and easily paste them into the chat. I think that works great. Huh, this is interesting.

Gemini said that it used layout logs from Lucid React, which does not exist or was a hallucination. I don't think I've ever seen an AI agent admit that it hallucinated. [laughter] That that is a first for me. [clears throat] Okay, so now now we're up and running. Let's see how we're doing. Okay, so this is this is looking pretty good.

I did notice there was like a a nice little fade in when I first loaded the page. A little subtle hover effect. Overall, this feels like a pretty pretty balanced design. It is much simpler than the one that Opus 4.5 created. It did give me some quick actions down here, which is something that I asked for. And I like the the navigation up top there.

Simple logo. Good. Let's see if it did dark mode. It did not. Again, like it it did this earlier, but it just didn't do it on on this run. So, if I go to mobile, let's see how we're doing there.

That's all looking looking pretty good. Although, this list it didn't really handle so well on the smallest size, but I think that's a common mistake, but something that I would hope to have worked. Something that we can clean up for sure. This Yeah, in that's kind of misaligned. And we do have a mobile menu, and that's working well. Okay, so not not so bad for the dashboard overall.

It's It's kind of clean and consistent. Here's the client's list. Okay. So, um it's fine, but yeah, I'm definitely seeing some issues. So, we've got a weird spacing issue up here that that probably shouldn't be there. Um this looks like a little bit too much top padding.

This is a little bit too close to the edge. So, again, these are little details that I could clean up. But to be honest, here at the end of 2025, I would expect that a Frontier model like Gemini 3, especially with all of the uh the fanfare around it, wouldn't make little design mistakes like this. But again, these are easy to clean up. Let's see how we're doing on mobile. Okay.

So, it did handle it like this is a sidescrolling and that's that's a common way to handle lists, but I did like the more creative and effective approach that Cloud Opus took to making sure that it's list actually stacks in a responsive way. All right. Now, here is the invoices list, which is basically the exact same layout with all of the same uh design issues. Um, I do like the consistency. I like how it it didn't just design a totally separate view from scratch. it it kept the same consistency across both, which is what I would want in an actual application.

So, that's good. Um, okay. So, I did ask it to create a an invoice editor view, and it did that. Um, this is simpler, and you know, I'll I'll just be honest, like overall my my general sense or my like the overall look and feel seem to be a little bit stronger from Opus 4.5, at least on this run. I mean, I've I've done a couple different runs, a couple different projects with these, and honestly, I've seen both perform really well and and perform a little bit worse than one another. They they really sort of trade off in that sense.

Here on this recording, it seemed like Opus' work just came out a little bit better than Gemini so far from what I'm seeing. Okay, so we've got like we can add new items. Okay, now I do want to see that sharable preview, the one that would be like sent to a client and that would be this one. Okay, so here is like that sharable view. Um, and this is interesting because like normally I would want this top navigation to not display since this is something that the client would see, not the not like the account user. So, and that's something that like Opus 4.5 figured out by default.

It had its own layout and actually if I remember it asked me a specific question about that during the upfront planning when I was working with Opus and then it got it right in the final implementation and this one Gemini did not ask me about should there be a separate layout for the sharable invoice and here here we are it actually got that wrong. So that's just a really good example of a the models being able to ask smart constructive questions upfront and b the value of really detail oriented planning up front leads to a successful outcome in the end. Okay, once again we've got like a spacing issue at the top and we've got some buttons here. You know, overall it's a clean look and feel. It It looks fairly professional, but a little bit more boring than the the nice clean one created by Opus 4.5. Let's see how we're doing on mobile.

Okay, that works. Super small. It gets a little bit squashed, but that's not too big of a deal. This gets cut off. And I don't even see the ability to sides scroll in there. So, that should stack a little bit better, but it doesn't.

Okay. You know, overall, I'm being a little bit nitpicky, and these are all things that could easily be uh cleaned up, which I which would normally be what I would do. Okay, so now that we've established all the front-end designs for all the key views and and routes in both applications, let's circle back and get the back end all wired up and get this into almost a shippable state, if you will. So, I'm going to go back to the application where we're building with Claude Opus 4.5 and I'm going to go ahead and run this prompt 2. And just to show you what that is, it all it is is like now that we've designed the front ends for these pages, let's make a plan to complete the full backend implementation for this app. Again, I'm going to refer to the product overview for an overview of everything that we're going for.

And I'm telling it like I want all buttons, navigation links, functionality should be fully functional and ready for me to test in a browser. And then finally, I'm asking it to ask me clarifying questions to dial in this plan. Okay. So I'm going to copy that and I'm going to give that to Claude code. Okay. So uh here is the first question.

Okay. So I I'll submit these questions. So Claude's plan is all set. And here is that plan summary implementation phases. Oh, you know what? I I realized I I think I actually wasn't in plan mode.

And sometimes I forget to toggle between them. So that's probably what happened was we actually started the planning of this, but I wasn't actually technically in plan mode. So it it did make a plan. It did ask me clarifying questions because I asked it to. So you can still do that even if you're not in plan mode. But since it wasn't in plan mode, it sort of just assumed that it was going to go ahead into implementation, which is perfectly fine.

So, all right, cloud code and Opus 4.5 is getting to work on the backend functionality. So, while that's cooking, I'm going to hop over to my other project. Now, we're back into working with Gemini, and we're going to do the same thing. So, I'm going to stay in the same chat that I've been working in, and I'm going to once again use prompt two. I'm going to copy that into my prompt here. Again, we're we're sort of picking up where we've left off.

We've designed the front ends. Now, we're going to do the backend implementation. Ask me clarifying questions. And you know what? This time, I will go into plan mode. Just making sure we're we're going to go through the actual motions here.

And I'm asking it to give me questions. And let's go ahead with that. All right. So, it's asking about the pay now button, which I've already instructed. It should be just a mocked up payment form. We're not going to go through uh the process of integr integrating payment processing at this time.

Um so we're just going to do mock only for that. Okay. So I didn't really see it work, but it did generate this this plan. But once again, we are missing the to-dos. So I'm going to give it one more nudge to to finish that that to-do list. Create a to-do list for this plan.

Again, I don't know if that's an issue with cursors agent mode or maybe Gemini 3 in cursors agent mode, but yeah, that seemed to happen a few times for me now. But it did go ahead and add the 10 to-do items to this plan. I'm going to go ahead and save the plan just cuz that's like a a common thing that I do. Okay, let's go ahead and have it have it build. I'm just going to switch to agent mode and proceed with building that plan. So yeah, actually the UI was a little funny there with cursor when I have it plan one thing, build that and then create a second like a follow-up plan while I'm still using the same agent.

Often times I would just start up a new agent. It depends on the project and the the day that I'm working. But yeah, that that little UI interaction I thought was a little confusing in in cursor. Okay, so now both Gemini 3 is cooking over here and Claude Code is still working over here. Okay, so uh they both took roughly about the same amount of time about 10 12 minutes. And looking at cloud code with Opus 4.5, here is the the implementation summary.

So that's all ready to go. And then I see the same thing from Gemini over here in cursor summary of changes. Here is everything. Okay, cool. So, let's go ahead and test out the Opus 4.5 buildout first. Okay.

So, here is the the dashboard for Invoiceicy. This is built by Opus 4.5. And you know, the front end still looks the same as before. Still looking consistent. And let's try out these buttons. I'll try new invoice here at the top.

And that that does take me to the new invoice page. Cool. I can view all invoices. That's all working fine from the dashboard. If I click new client, that links up. Very nice.

Uh let's go back to that client's list and let's see if we can search for a client. Yeah, so the search does seem to work. Nice. Be nice if I could use the keyboard, but I, you know, that's something that I can build out. I would have probably specked for that. Um let's go ahead and try creating a new client.

Good. That that worked. I had a little typo there. That's no big deal. Got a warning modal, a warning alert. That's good.

All right. Let's go ahead and create an invoice for a client. Okay. So, I I would have liked it to automatically select the client, but it didn't do that even though I had selected it from the client list. Not a big deal. It generated an invoice number.

Calculates, you know, the quantity and the and the amount correctly. Let's add another one. Okay, looking good. What happens if I click saved draft? And uh Okay, so I do see an issue here. It didn't actually save those line items.

So this is so I think that was invoice 9 and I see amount is zero and uh yeah we don't have those line items saved. So that is one issue with the implementation from opus. Let's see if we can search invoices. Yeah I can search by client name and I can search by invoice ID. So that's nice. Okay so mostly good.

There are a few issues that would need to be worked out, but that's, you know, it it's basically all wired up and Opus did a pretty good job on that, I think. Now, normally I would go through a bit of a code review to see how it structured everything, but that would be a little bit boring for this YouTube video. And and also, you know, the the code style and the tech stack is is just different for everyone. Um, but I I wanted to kind of demonstrate the ability for it to build out a back a backend and get it functional. So, that's mostly working. Let's hop over to the app that is built with Gemini.

Okay, so now I'm running the app that was built with Gemini 3. Here is the dashboard for that one. We see total revenue and I can see that that number is correct because it's adding up uh just the paid invoices and not the pending and the draft. So that's that's good. And then yeah, outstanding includes these two. Uh we've got some active clients.

That's all looking good. If we create a new invoice, we can get to that from here. We can add a new client from here. Good. Let's go to the clients list. Let's see if the search works.

It doesn't seem to work. Okay. So, it did not actually wire up that search. I didn't specifically tell it to do that, but I did specifically say I wanted all functionality and, you know, features to be functional and ready for me to test in the browser. So, you know, that's something that it didn't quite follow my instruction on. Um, yeah.

So, these these are actually not functional either. So, these actions, nothing happens. Let's try creating a new client. Okay, we've got an issue when we uh try to create a new client. We've got an error there. Let's just go ahead and and try to create a new invoice.

I can select a client. I'll create a line item. We've got a little overlapping UI issue there. That's not great. I would want to clean that up. Okay, so we have the total and that appears to be correct.

Let's save that. And yeah, once again, we have an issue with with saving. So, I'm going to try to have it debug that. Let's Let's try to do it. So, what I did was I cleared my server logs. I'm going to try to create I get the error and not much is showing there.

error when trying to create an invoice. Same happens when creating a client. So hopefully I can fix both of those in one shot. Now I want to be clear this entire design and build process was very uh abbreviated and and fast build out uh really just for demo purposes. Normally I would spend a lot more time upfront in the planning and the spec and architectural uh phase and that would prevent a lot of these issues when we when we come down the line to a final implementation and that's really the whole essence of spec driven development. But for the purpose of this video I wanted to just sort of like quickly design and build an app with both Opus and Gemini 3.

Okay. So it says that it has fixed the error. Let's see about that and I will refresh and let's Okay, so that does seem to have saved. Okay, so that basically works. So in the end on my first run, I must say these newest models don't seem noticeably different, but I expect that their true power will be revealed as I use them dayto-day going forward. I think my real takeaway from this is that these Frontier models are converging.

They're all incredibly capable now and they're only going to keep getting better, which means the gap between the models matters less and less over time. What matters more is you and me. It's our ability to leverage these tools, our product instincts, our architectural decisions, our taste. That's the real unfair advantage in this new era. Not which model we're using, but how skilled we are at directing them. And that's exactly why I made a video breaking down the five essential skills that matter most for builders.

Now, for some of them, you might already have an unfair advantage. A few of them are totally new domains that didn't even exist a year or two ago. So, right after you hit subscribe on this channel, I'll see you over there next. Let's keep building.
