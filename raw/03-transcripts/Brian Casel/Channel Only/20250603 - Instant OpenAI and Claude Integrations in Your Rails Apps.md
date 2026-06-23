---
title: "Instant OpenAI and Claude Integrations in Your Rails Apps"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Brian Casel"
---

# Instant OpenAI and Claude Integrations in Your Rails Apps

These days when you're building apps with Ruby on Rails, more times than not, you need to integrate with the AI providers like OpenAI, the makers of ChatgBT or Anthropic, the makers of Claude. You know, bringing in these integrations into your Rails app enables you to build AI powered features like, you know, generating content, generating text, responding to prompts or instructions from the users. There's so many different possibilities. Frankly, these are like essential features in today's products and software being built. So, I want to make this video to show how I go about integrating with OpenAI and Anthropic in all of the Rails apps that I build. And of course, I turned these into two new components that I've added to instrumental components to make it really fast and really easy to get up and running with an OpenAI integration and a Cloud integration in your Rails app.

So, let's get right into it. and I'm going to show you how you can fire this up really fast. So, I have spun up a new Rails app. I used some of the generators that come with instrumental components to to get here a fresh Rails app. I've got authentication and some account stuff built in. But in this video, I just want to show you how I can generate and install two new components which will give us two integrations.

One with OpenAI and the other with Claude or Anthropic if you will. Now, of course, in this video, I am showing my components library, instrumental components, which you can learn more about at instrumental.dev, and that is what is actually powering the generators that I'm going to use to install the OpenAI and Anthropic integrations. But I am going to show you under the hood and show you the codebase to show you what these generators actually place into your Rails application code so that you can see how it all works. Okay. And I'm going to start with the OpenAI integration. I'll run rails g instrumental open aai.

And as always, that's going to give us like an overview of what's about to be installed. So I'm going to proceed with this. So for this integration, we are adding an initializer, a couple of controllers, a service, actually one controller, a service class, and some views. So So that's all set. And here is the recap. Again, we have those files added to our project.

We are going to be making use of the Ruby OpenAI gem that has been automatically added to our gem file and we added some routes for the example implementation. Also, we have some some localization stuff now built into all the components with instrumental components. Okay, so that is all set. Let's run bundle to get that gem installed. Now, in order for this to work, we are going to need to connect to our OpenAI account using the OpenAI API credentials. So, in order to do that, we need to add some credentials to our to our Rails credentials file.

So, I have a shortcut to open up my credentials. And in the docs on instrumental components, you can go into the AI docs here. I'm going to go into OpenAI. And we've already run the generator. Now, this is what we're going to need to add into our credentials. And it's going to need an access token like our API key and the organization ID.

So you can get those from your OpenAI account. I believe it's at platform.openai.com. Now you're going to need to get your credentials from your OpenAI account. So you can, you know, sign up for an account over there. Get your credentials there and then drop them in here. I'm going to do that now off camera and then I'll close this out.

Okay. So I've saved that and the next step is we need to go to the OpenAI initializer. So, one of the files that was just installed with this generator was this initializer, and that's what pulls in those API keys that we've saved in credentials. All we need to do here is uncomment the code that's all ready for you and ready to go. Now, what did this actually install aside from the initializer? Well, let's look at our application.

Number one is in services. We have this OpenAI service. This is essentially the new tool that you now have in your Rails application that you can use to interact with the OpenAI API. It's it's pretty flexible. You can, you know, send it a prompt along with several options like the system message, system instructions, which model you want to use, some max tokens, bunch of other options here, parameters if you will, like temperature and some other stuff. And then it's going to respond with the response or like the generated response from the LLM.

You know, we've got several models available. As you're working with this and as they're releasing more models, you can of course add to this array and keep this updated. And we at Instrumental Components, by we, I probably mean me. I'm going to be keeping this up to date as well. Okay, so this is the service object, the service class that we're going to be using whenever we're interacting with it. But to make this even easier, this component comes with an example implementation.

So you will find under controllers, we now have OpenAI prompt controller. And in views, we have OpenAI prompt. We also added some routes right here. OpenAI prompt. So let's go ahead and start our server. I have a shortcut for that.

And I'm going to need to log back in that uses our authentication component. Okay. So now I'm in. Now we can get to our open AI prompt at this route. And you know what? I'm going to actually add a navigation link to my main navigation to make that easier.

So this uses our navigation layout that's in that comes included with instrumental. Let's see. Yeah, I think that's it. Yep. Okay. So we have the OpenAI prompt feature.

This isn't, you know, this is just a very basic implementation. All it does is it lets you type in instructions, anything that you want. And then we have some optional additional fields here. You can, you know, put in some system instructions or the advanced options as well. You know, selecting which model you want to use, max tokens, temperature, and whatnot. So, this is really just like an example imple implementation so that you can see what's going to happen.

Let's actually just go ahead and try it out. Tell me a joke. generate response. And this actually uses a Rails turbo response. And just like that, we have why don't scientists trust atoms? Because they make everything up.

Well done. So, you know, it's also spinning back some usage details. It tells me what my prompt was. And in this case, I did not give it any system instructions. You know, you can do things like, tell me a joke. Everything you say should be in Spanish.

Let's generate that again. And there you go. I don't even really speak Spanish so well, but something about Facebook and Twitter there. Maybe you can tell me in the comments what that actually says. So, this again is just like an example implementation, and you can check it out by going into that controller. And you can see when we create a new response, we are opening up a new instance of the OpenAI service and then we're sending it the prompt and then we're sending it whatever options we put into the form and then it's getting the response, sending it back and we are rendering that with a turbo stream.

So let me show you another example of how we can actually use this in our application. I'm going to show you a little bit of like building out a new feature that might use the OpenAI integration. So, let's go ahead and scaffold out a new model in our app, just a posts model, like a blog post model. I'm going to go ahead and stop the server. You can use a regular Rails scaffold, but I'm going to use the instrumental Rails scaffold, which is like a scaffold on steroids. We have I have another whole video that covered that in depth.

So, here we go. I'm going to do Rails G instrumental scaffold. And let's call it post. And we'll give each post a title. We're going to keep it super simple. I could add like a lot more attributes here, but I'm just going to do posts and titles.

And later on we can add like rich text and all that kind of stuff, but this is just an example. Okay. So, we are going to install. We're actually using the scaffolds component to install a uh a post. And we have some questions here to configure our new post that's being generated. Again, my other video on the instrumental scaffolding system goes into this stuff in depth, but you can sort of see what's going on here.

And we also has have a fast mode for instrumental components which would run through this like instantly. So, I really probably should should enable that on the next run. Okay, so we have set up our posts model. Got a bunch of views and controllers and some routes. And we also added a migration. So, let's do rails db migrate.

Let's go back to our navigation and add it into our navigation as well. Let's let's put it up here. Post path. I think that should work. Let's see. Oh, I have to actually start the server.

Okay, so we've just scaffolded out this basic posts path. Hello world. I'm a post. Great. So, I just created a post. All it has is a title and a slug.

Now, that obviously did not use AI. So, how can we AIify the post model a little bit? This is just a madeup example. But let's imagine we want to set up a system where every time we create a new post, we use AI to rewrite the title of the post and make it a silly rhyme or something, right? I'm just making stuff up as I go along here. So, I'm going to go ahead and come back in here.

I'm going to go to my post model and we want to after create we want to rewrite title and then we're going to define that. Now, obviously, I could it's it's already suggesting the OpenAI service, but I'm going to kind of show you a little bit of vibe coding here to I what I really want to demonstrate is how well instrumental components and Ruby on Rails in general works with vibe coding or using AI or prompting AI in a tool like cursor because it's really just Rails stuff. Like a service class is just Rails stuff. So, I can do this. I can just highlight this empty method here and go into my AI chat and say I want this call back to rewrite the title of the new post by turning it in into a funny rhyme. Oops.

And then I'm going to instruct it to use our existing open AI service. So, you know, cloud force sonnet is going to be smart enough to find that file in our codebase and then it's going to use that file to build out the functionality. So, let's go ahead and get that going. Okay, so it filled out our our callback method here. I'm going to accept that and we can see what it did. We'll close up the chat here.

So, it created this prompt like take this title, the title that the post initially has, rewrite it as a funny, catchy rhyme, keep it short and snappy, return only the rhyming title and nothing else. So, you know, cursor and claude just came up with this, which is exactly what I wanted. It also added some system instructions. You are a creative writer who specializes in. All right. So, then we are opening up the open AI service which calls it here.

We are sending it the prompt and we're sending it the system instructions and these options for temperature and max tokens. Then we have a response and we're going to update the title on the post. Okay, so let's try it out. I'm going to get this. I'm going to create a new post. Post about baseball.

Let's see what it comes up with. It called it batting banter, a ball game blabber. I don't even know what that means, but as you can see, it came up with something, right? So, I'm not going to say that this is the like the killer app of the year, but it just goes to show how you can start to integrate AI into your app. Now, that's using the OpenAI API, but of course, the Claude API from Anthropic is just as popular, if not more popular when it comes to AI integration. So, we have another component from instrumental components.

It works almost exactly the same except it integrates with the anthropic API instead. So let's just get that installed just to show you how that works. All right. So I'm going to stop this. We're essentially going to do exactly what we did before. We're going to do rails g instrumental and this time anthropic.

And I'm going to also use the fast flag to make this go a lot faster this time. So we are going to install the anthropic component. I want to proceed with that. And that's all done. So again, it looks very similar. You can see that we have an initializer for anthropic, anthropic prompt controller, anthropic service.

Okay, so we're going to and we did add the Ruby anthropic gem and we're going to bundle this up. And once again, I'm going to open my Rails credentials and add my anthropic API key into there. So I'm going to do that off camera. Okay, I saved my Anthropic API key, which I got from my Anthropic account. And I'm also going to go into Anthropic RB. That's the new file that was added under initializers.

Same deal. Just need to uncomment that. And that is good to go. And so now, and again, we can just see, you know, the new stuff that has been added. Again, just like we added the anthropic the OpenAI interface, now we have a very similar anthropic interface to use as a nice example. Let's go ahead and go to the navigation and just add an easy link to it and let's start the server.

Okay, so now we have anthropic prompt. I'm going to go here. It literally works exactly the same way except we're using clawed models instead of OpenAI. And you know, we're going to be adding the latest models to this as we go along, but again, we can just go ahead and tell a funny joke. And there you go. Here is Claude's response.

It's a little bit more verbose here, but you know, all the same information. It just, you know, serves as a good example for you. So, overall, I think that that gives you a look at how you can get these popular AI LLMs integrated into your Rails applications with these easy components from instrumental components. Now, if you found this helpful and if you want to learn more about instrumental components, I have a number of other videos. The one I want to point you to actually next is our commerce component that will install a stripe integration so that you can charge for your SAS application, charge customers to use it, especially if you are using AI integrations which are going to cost you money as the business owner. They, you know, they use your tokens from your OpenAI and your anthropic account.

So, you know, you don't want to necessarily just, you know, launch these free applications and let people draw down on your tokens. So, you'll want to charge customers to use your SAS. And to do that, you will probably need to use the commerce component from instrumental components. I've got a deep dive video on that. If you have any questions or any requests for future videos, I'm going to be doing a lot more videos on using Cursor to build with AI and some new workflows on building software much faster. I'm excited to get into that.

But yeah, thank you for watching.
