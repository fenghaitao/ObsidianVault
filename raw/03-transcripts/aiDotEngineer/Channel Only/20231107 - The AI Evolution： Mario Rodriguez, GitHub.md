---
title: "The AI Evolution： Mario Rodriguez, GitHub"
type: transcript
source: youtube
playlist: "Channel Only"
author: "aiDotEngineer"
---

# The AI Evolution： Mario Rodriguez, GitHub

I don't know about you, but I've been having a blast at this conference. Um I've been enjoying a lot of great conversations about how to build AI products and how to kind of advance humanity forward at the same time. This is hard. Like it's not easy to do. Um so I really enjoy kind of being part of this community and I'm kind of sharing kind of the best practices, the failures, and everything else. I also want to give a shout out to Ben and Swyx.

Let's hear it for them for an amazing day one. I will tell you one thing, putting together conferences is also not an easy job. Um it's kind of a lot of hard work um and a lot of people end up criticizing and things go wrong. It's kind of like a wedding at times, you know, it's like so but they have not been priceless or anything like that. Um okay, so who am I? My name is Mario Rodriguez and I am VP of product at GitHub and I oversee uh what is called our productivity suite.

Um that includes repositories, so where you store your code, um our pull request product, issues, projects, our mobile app, our CLI. And then kind of since January of this year, I had the privilege of also leading the Copilot team and the AI strategy at GitHub. Um I'm not one of those that invented Copilot and put it on Twitter or anything like that. So but I am kind of overseeing uh what that strategy is at the moment and thankful for everyone that did um made it happen before. So I actually want to start with a little bit of um what I call insider info. Like if you were not at GitHub that moment, um you would not have known this.

But I would say a catalyst, at least in my opinion, uh for Copilot's existence came around August 2020. And there was a paper circulated at GitHub. Uga, Alber, and a couple of other people, probably more than a couple of people, ended up writing that paper. And it was called this, an automated AI programmer, fact or fiction. Again, this is 2020. This is before the hype of ChatGPT and everything else that you know about.

This is before the existence of having able to actually have this conference. And one of the things in my opinion that paper had was what I call polarity. And polarity for me is is not a choice because you can choose A and B. Polarity for me is is those choices are interconnected and related as well. So there were a lot of people that said that it was fiction. For example, is this fact or fiction?

You probably will say it's fiction. If you ask my, you know, 4-year-old or 3-year-old, they'll tell you it's fact. They love this thing. They play with it and all of those other things. It's kind of scary that the dinosaurs with the kids there, but it's a good dinosaur, right? So, so it kind of had this thing of like is it fact or is it fiction?

And you we we went through a lot of conversations about what is this product really going to be like? And the product kind of failed at the beginning. We were trying it first in the PR flow as an example. And and it was not good in there. But then something happened and we started kind of seeing traction. And that traction ended up with us shipping the product in 2021.

And that was the first AI at scale AI programmer in the world. Um, and it has continued to grow since then. We were the first Copilot before everything happened. And today, if you actually ask out there, we get used by over 20,000 organizations. There's 1 million plus developers using the product as well. We'll release new stats very soon on that, too.

We got a lot of studies or what we're doing and what's the impact that is having. You see things like 46% of the code written. That's really just tap tap and kind of completions. Copilot does a pretty good job at times depending on the language and multi-line completions overall. So we were the first one and we're kind of our extending that. So if I ask you you know Copilot is also a business.

There was a recent report that you know we're losing money and that's not true but regardless of that. So how much do you think of ARR Copilot has today? And ARR is kind of like the annualized revenue that we have. So raise your hands if you think it's over 25 million in ARR. Okay. Fair amount.

I'm going to bring you to the board meetings. What about 50 million ARR? Raise your hand if you think it's that. Okay. Pretty good too. So you're mostly right.

Copilot today is over 100 million ARR product. That's what it is today. I can't give you the latest numbers because the SEC will go after me but it's a pretty darn successful business. You know we builders dream about building things that have that impact. Forget about actually even the money that it brings because at the end we really actually are making Copilot for you. When I say for you I mean the essence of GitHub is developers.

It's AI engineers. You're a developer too but they kind of specialize on that end. But the essence of us is developers. That's why we wake up every single day is to kind of bring you Copilot so you could actually enjoy the work you do overall and based on yesterday's conversation maybe Lindy, Flow, Lindy and Copilot maybe can you know help at the end Milton as well. So like I said you know we're building Copilot for the sake of developer happiness. You know for me the definition of success of Copilot is this.

It's it's not lines of code I said that or that's a pretty good metric overall. Um it is fundamentally we are raising all the boilerplate that you're creating. All of these things that kind of don't keep you in the flow. And what I want you to experience of Copilot is the feeling of flow at the end. Um it's not only about conversational. Now we have inline chat.

There's other modalities that we'll end up trying. The the chat box is not all. Um you know, and in code completion kind of we have proven that as well. But you know, this is what generates happy developers from in my end is kind of that flow. Um and happy developers write better software. You know, Milton doesn't write a lot of good software overall.

All right, let's keep it going. So more inside information. Like what made it successful? If you ask me um what made Copilot V1 successful? And that is I would say the code completion product that you use today. And there's four key components on it.

Number one, it was the ghost text. Believe it or not, that completely changed the game when we were trying the Codex model. And Codex was the first um model that um shipped with Copilot. When we were trying that model, having the ability to actually generate either from natural language, you know, you could just put a comment and have it generate, or just normal as you're typing, having something in there to remind you is this what you want or not. Having that in the UX was one of the key elements. The second thing is it had to be fast.

It's not like you know, people don't like if I want to keep you in the flow and you're waiting seconds for that, that's not a good experience, right? So what do we want? We want to make it fast. So we worked a lot you know, be- um just recently by the way we switched to GPT-3.5 Turbo behind. So we're no longer using uh Codex. But you know, Codex is a very fast model.

So you end up with less than 100 milliseconds in latency many of the times. Then the other thing is, you know, the Codex model was like anything we have seen before. You know, hats off to OpenAI on that, but that model really changed the experience that we were having. We were always tinkering with AI at GitHub, but once we actually pair ghost tags with a low latency with an amazing model, then that's when the magic happened. And then at the end, you know, there's people that say prompt engineering is not a true thing. At least from where I'm standing, prompt engineering is a very true thing.

So, if you're really gifted at that, I have a job offer for you at the end of this. Um because like it takes a long I could create a demo for you all probably within 30 seconds. Making AI product that actually gets used by millions of people that you could sell out there to companies, that takes a lot of hard work. Um and it takes a lot of engineering. Takes a lot of people like you continuing and innovating as well. All right.

So, let's um go to the next one. The main point that I really want to make at the end over here is UX matters in what we're doing. Don't think that you're just going to get something out there. The UX that you end up choosing the modality you end up choosing with that AI application can either make or break it. Um and we have seen that a lot as well. All right.

So, what are the things? Um the other thing that I want to tell you is once you actually hit a little bit of that product market fit, get used to a very fast pace. If you think right now you're fast paced, things go kind of through the other side once you're having success with a business in AI. There's a lot of questions coming at you, a lot of things that you have to handle both internally and then externally. So, some things that are also learnings from inside. Number one is, and you probably know this, syntax is not software.

Just because you could read Java doesn't make you a Java developer. Um so, on that end, same thing for AI. Just just because AI can actually understand some of the syntax, it does not make it a developer. You have to do a lot of work from a semantic perspective for that AI to end up generating the right code. Um so, just remember that syntax is not software if you're going to be in this space. Uh the The stuff is you need a global presence if you're going to have a global product.

We have deployments all around the world in order to keep that 150 milliseconds many times. So, we are in Japan, we are in Europe, we're in North America um in multiple data centers in order to guarantee that first time to buy it overall is very very fast. The other stuff is set up score cards for quality. You could mess up your deployment very quickly uh uh on a like you think you actually have something that it works and then you go to production meaning your offline evaluations, right? So, in your offline evals everything's working, you go to prod and your online evals kind of tank. So, be ready for that.

Score cards are very very helpful because what sometimes works in offline is not really going to work in online. So, if I have one thing to tell you at scale is set up your offline and online evaluations so you could actually end up iterating quickly cuz you're going to have to increase the the ability for you to ship. All right. So, what else? Um the other thing that we have learned and there's a saying that says trust grows at the speed of coconut but falls at the speed um coconut tree but falls at the speed of a coconut. Um and really what I want to tell you on that is once you go into companies so if you're going to take your product and go to B2B overall, you're going to have to care about three things.

Number one is security. Please don't store anything at rest. Usually that's not going to be a good thing for you or any of your prompts or any of the customer data. Um please don't train other data without their you know their approval and all of the those type of things. Um you're not going to get far. The second thing there's a lot of legal things that you have to take care about.

You know, for example for us we provide indemnification to our customers just in case there's anything happening. So, you know, and as you could probably imagine from the legal perspective today there's a lot of you know regulations and things that we're talking about with many of the countries. And the last thing is what we call responsible AI. Um you could see I think yesterday's um and and someone told me this but I think yesterday's opening AI demo failed, but it mainly failed on that. It failed on their uh um their ability to actually have, you know, not security, but trust and trustworthiness into what they're doing and the responsible AI aspect of it. Um so, the same for us.

We invest a fair amount in making sure that the AI is be is doing the right thing for the user and it's not harming the user. So, I encourage you to continue to think from that ethics perspective because it's really important. We're creating this to advance, you know, human progress forward, not really taking it back. All right. So, now I want to kind of explore I'm going to shift it from okay, some lessons learned um into a little bit more about the future. So, from a future, what what gets me out of bed?

Well, fundamentally transforming how the world builds software together, but what does that kind of mean? Like, where's Copilot going? Um there's a talk by Bret Victor uh that is called the future of programming and I want you to watch it because I think it you know, it happened a long time ago, but really talks about the struggles that we have in software going forward that are still present there. Um and the first prompt actually um well, we'll put it like this. The first prompt that I want to give you is the following. What does it look like to move from procedures to goals and constraints?

So, what does that mean? Well, coding today is procedures, text files, and sequential programming. This is how you do things. Um you know, our CEO went and programmed an Octo Arcade demo, a snake demo. So, if your CEO can actually program, that's always great, right? Although in technology company, hopefully all of them can.

Um but it's it's this, right? Like, he did it in JavaScript. I was kind of trolling him a little bit on hey, can you just do it in TypeScript and can we have Copilot do that for you? But it's just a lit it's just procedures, text file, and sequential. And And is that really what AI should help you with? It should be doing going forward?

I think no. I think I think a future of copilot really goes on operating on goals and constraints. Um and then the repple that the actual programming environment that you have will need to change. This is what we want to do. We just don't want to play to the status quo of what it is today. We want to have AI actually change it and it kind of do a step up going forward.

So, what do I want the future to be? I want the future to be create me an app, use remix, Redis and Postgres, have a magic state machine, go and use for this UI library, and then host it in my cloud. And then once we get there, I think you're going to kind of be unstoppable. You're going to be able to go and say, "You know what? I'm going to go in and evaluate all of the vector databases, all of the embeddings kind of models, and everything else that have to do to actually make this AI product work." Um but that's what the future looks like for me. It's kind of the semantic workspace at the end.

So, two, what it is to have reasoning on code. So, what would be for the AI to reason on code? Well, our brain has the ability to actually do reasoning very well, by the way. And And it does that through summarization many times. So, here's an example. Let's try this.

So, imagine you need to add a feature flag in a code base you're not familiar with. What would you search for? Like, just ask yourself that right now and try to see what your brain gives you back. Okay. Congratulations, you just did rag on your brain. That's what you did.

You went and you ended up putting a bunch of things together and into a query string. And let me tell you, your brain is freaking phenomenal at that. The AI that we have today, not even close. If not, I could retire probably. So, but your brain is really good. So, we're going to have to think about what it actually means to actually do summarization that fast with high quality to advance this going forward.

So, here's another one, another test. So, this, many of you, if not all of you, are going to see a blue car. There's actually not a shade of blue in there. There is The car is gray, but your brain putting blue there because it knows that it needs to, you know, it thinks that it's overexposed, and it adds a little bit of that for you. You're used to strawberries being, you know, red, etc., etc. So, it adds that.

Um So, this is what it might look like in the future as you three centered code. And Amelia, who is a speaker that is coming, I think, two after this, did this project while she was at GitHub. But think about a little bit more about what does it mean to actually have these broken down into many parts, and then be able to reason and summarize them very quickly. So, I'm very excited. We're doing a lot of, in I would say, the GitHub next team is doing a lot of innovation in that space as well. So, think about, you know, a model, architectural advancing in rags, and then visualizations to help you with reasoning on code.

Uh What's problem number three? So, what does it look like to create software together with a copilot and others? A lot of the UX that you have today is was not was not meant to have an AI collaborator. That's why we're all trying to put a sidebar with a shot thing on it. It's because like the paradigms today, that's kind of what they could afford. But that's not what the future should be if AI is really going to be with you helping you get something done.

Um so, the way that developers collaborate haven't really changed in a long time. So, what I want to What I want to get to at the end is something like this. So, I'm getting an issue, and it's assigned to you. Actually, this is more what it looks like today more than later. So, you get an issue assigned to you. You meet to chat and discuss.

You code with copilot. You open a PR. Um I don't I don't many chat suites you have. We have a lot of GitHub. It's kind of love and hate. Um and then you merge and deploy before Friday.

Majority of you do not want to actually deploy on Friday. Although, if you are at Vercel, they tell you that they're the best cloud to do it. So, you yolo to production with them anytime you want, okay? Um Tell Tell me, Guillermo, that's the best way to do it. Um okay. So, what what would that UI in the future look like if it is actually designed for both human and AI collaboration?

What What does it have What would allow you to do if you could then steer the UI the the AI and even the other humans in it to collaborate on that code? And how can you do it so things that you need to ignore are ignored and things that need to be verified are verified? These are the things that we're trying to tackle at the moment. It's not only about code completion. It's not only about chat. It's not about having, you know, training your own models.

It's really about advancing how we code and how the world codes together. So, um I'm going to speed up because I promised Ben that I was going to end up very quickly. Um but what I really wanted to do with that is kind of make meaning transparent along the way and what this ends up going. Um I cannot give you a sneak peek yet, but I I just want you to think about an immersive experience and this is just kind of the beginning of that. An immersive experience that you could go in and out together with AI and other humans. So, we're excited about that.

Not going to do prompt four. That security is top of mind for all of us. What would it look like? So, you could imagine I I could do five, six, seven, eight prompts overall um on how to continue to push, you know, what we do every day forward. So, the last thing that I want to leave you with is GitHub today is no longer the home of open source and it's no longer the best version control system on Earth. We have worked a lot to actually make it into a platform.

We have an AI you know, CI CD system with actions. We have packages. We have Copilot. We have code spaces. So, it's really an you know, end-to-end platform. And we're going to infuse that platform with AI.

And with that, I want to end it and thank you all for entertaining this. And have an amazing conference.
