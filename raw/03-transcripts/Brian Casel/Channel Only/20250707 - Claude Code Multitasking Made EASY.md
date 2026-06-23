---
title: "Claude Code Multitasking Made EASY"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Brian Casel"
---

# Claude Code Multitasking Made EASY

So, it's pretty clear that right now Claude Code seems to be the most capable tool for professionals who are building with AI and I'm more and more impressed with it by the day. But when it comes to my workflow of working with Claude Code every day, there's still one thing that kind of bothers me. So, I'll give Cloud Code a big task to work on. I'll let it run and then I wait. Still waiting, watching it. It's doing its thing.

waiting. And while Claude is working, I can't really do much because Claude code is working on the same git branch that I'm currently working on. So if I want to keep making progress on this feature over here while Claude is doing its thing over there, or if I want to spin up multiple cloud code agents, it's all going to be on the same branch and that'll result in a lot of conflicts and that'll just be a mess. In this video, I'll show you the right way to do it using Git work trees. More importantly, we're going to set up a workflow that's fast and easy to be able to spin up multiple cloud code agents working in parallel anytime we need to so that we can stay in the flow, keep making progress, and ship our products way faster. So, in my last video on this channel, I made the case for Cloud Code and where it fits in alongside other agentic coding tools like cursor.

And in that video, I showed you how Cloud Code really shines as an autonomous coding agent. And that's why multitasking with Cloud Code seems like the most obvious next step. So, if you're a subscriber to this channel, then you know that I'm talking to pros like you and me. We want to stay ahead of the curve when it comes to building with AI. And I'm also sending a weekly newsletter called the builder briefing. It's free.

It's a five-minute read to help you stay sharp as a builder. You can get your builder briefing by going to buildermethods.com and subscribers will be the first to know about my Claude Code course coming later this year. Now, you might be wondering, why can't we just open up multiple Claude Code instances on separate terminal tabs? Well, as long as we're working in the same codebase, then all of your terminal tabs are going to be working on the same Git branch. That's even the case if you have multiple applications that can run terminal. Now that might seem obvious, but I just want to make it clear that if you and other people on your team or other agents are all working in the same files in the same codebase on the same git branch, then that can obviously lead to conflicts.

So how does anthropic actually suggest we solve this problem? Well, in the cloud code docs, kind of buried under this common workflows page, there's this section on running parallel cloud code sessions using git work trees. What are git work trees? Well, instead of just creating another branch, which would allow you to work on the same set of files as others, a git work tree will copy your entire codebase, all the files, all the folders into another directory on your system. And by doing that, it enables you or the agent to work on its own branch in the copied codebase. Meaning the work is getting done on entirely different set of files than your main codebase.

And when the work is done on that copied codebase on the work tree branch, you can merge it back into the main branch just like you normally would. All right, let's see this in action. All right, we're going to start with a simple example first and then we'll get into automating the whole workflow so that it's fast and easy to spin up multiple agents using git work trees. Now, today I'm working on an example Rails app. It's called Music Shop. It's just going to be a simple app to uh sort of track inventory for different musical instruments.

Um, so far I've just added guitars and I can, you know, create a new guitar and give it a name and edit it and view the guitar. Super simple little CRUD app here. And throughout this video, we're going to be adding to this by adding other instruments into our uh, inventory tracker, if you will. So, we're going to start by just understanding how git work trees work, right? So, as you can see here, I'm on the main branch of my uh, project here, and I'm going to just open it in Finder. So, inside this temp folder on my system, I've got music shop.

This is our actual codebase. Uh, and you know, you can see all the files and folders for the app here. Now, before I can create a git work tree, I need to create a folder on my system where we want to place the copied code base or code bases into as we create more and more work trees, right? So, I'll just put it on my system uh inside my temp folder. And what I like to do is create a work trees folder that is adjacent to my projects folder. So again, my my project folder was named music shop.

So I'm going to do music shop dash work trees. Let's take a look at the folder now. So now I have my main application and I just created this directory music shop work trees. As you can see, they're right next to each other. So that'll just make it easy for me to like see each project and see the the related work trees. Okay, so now we can spin up the git work tree.

So I'm going to do get work tree add. And we also want to create a branch for this. We'll call this feature name. And then we need to specify the destination for where we're going to copy the files to. We're going to sort of back out one level into that music shop work trees directory. And then I need to name the folder for the copied codebase.

I like to keep it the same as the branch name. So, we're just going to do feature name. Okay. So, that just created a work tree. Let's take a look at our folder. And so, now we have our main music shop project.

And then inside music shop work trees, we have this folder called feature name. And inside that is our entire app. Again, all the files and folders, the whole codebase has been copied here, including git. So, it's going to be tracked. So going forward now I can just create more and more work trees for every new big feature that either I'm going to work on or an individual cloud code agent can work on. So this folder is just going to keep like building up with work trees unless I you know remove the work trees which we can do later.

Now here we can do get work tree list to see the list of all of the work trees that we currently have. As you can see we have the main branch here and then it gives us the location of this other uh work tree. Now, you might be wondering, why did I create this music shop work trees folder outside of the main project folder, right? Like, why didn't I just create this inside as like a subfolder to have the the work trees inside the main project? And actually, I asked Claude that very question to get a good understanding of what the best practice is here. And Claude recommends that it is not recommended for several reasons.

One is, you know, git will track all the workree directories unless you add it to your git ignore, which you could do. that could be errorprone. You could accidentally commit these entire copied code bases to your repository. You know, git and various tools could sort of get confused with like nested repositories. And also like depending on your codebase and your IDE, various tooling um that stuff can like depend and and recursively uh scan directories in your project. So if again if it's scanning your main directory and then a whole copy inside it, that can sort sort of become a mess.

So, you know, the better approach here, of course, is to have your project and then have a work trees directory. In this case, it's sort of suggesting just create other directories right next to it. I like to put them inside a folder called work trees, you know, because uh when I have my like active projects, I'm going to have like many projects in here. So, each project should have the main folder and its work trees folder and then in there um that's where I put all the trees. So, you know, that's just like my method of of organizing it. Okay, so now I'm in the feature name uh branch and my terminal is set up to show me my current branch.

And so this would be fine. Like I I could run Claude right here and have Claude work on that branch inside the feature name codebase. That would work fine. But one thing that could trip you up is that here in cursor, if we want to like review the the work that Claude did or review some file changes from the feature name uh branch and codebase, that's not going to be found here because here these files are still in my main music shop folder. So what I do is I actually open up a second cursor window. So I'm going to do this and then I can just open up the folder.

And so now here, this is a second cursor window. I've got that copied codebase and the terminal and branch for that. And this is where I can run Claude. And what I actually like to do, I'm one of those weirdos who likes to use a single monitor, believe it or not. Um, I'll throw this into a second desktop, and then I can switch between my main branch here, music shop, and then here I am in the feature name branch. Just like that.

And later we'll we'll do this like three, four times, and I'll have, you know, different uh different branches going. Now that whole process of course was a lot of leg work. We don't want to have to do that every time we want to spin up a new cloud code agent on a new git work tree. So let's automate it. So my first idea of course is to use cloud code itself to handle the task of spinning up a work tree and setting itself up so that it can start to work on a task on its own workree branch. So for that we could try creating a custom slash command for cloud code.

Let's see how far we get with that. All right. All right. So to create a custom slash command, you'll go into the claude folder. If you don't have one already, create a cloud folder. Inside that, create commands.

And then inside that, we're going to create a file called create worktree.md. All right. So this is where we will put in the instructions that cloud code can follow every time we call this command. And so I already prepared these. It just says follow these steps to create a git work tree. Get the current project folders name.

So in this case, it would get the name music shop. Create a new folder adjacent to the current projects folder and name it with that project's folder name-work trees. I gave it an example for how to do that. And then create a git work tree and a branch. And we're going to pass it an argument. This will be the branch name and the folder name that we want to use.

And it'll save it inside that folder. And then I'm asking Cloud Code to go ahead and CD into that uh folder created inside the workre folder. All right, so I'm going to fire up Claude. Of course, I could use the built-in Claude integration with cursor, but I actually like using it in the terminal a little bit better for whatever reason. All right, so I'm going to go ahead and uh use our new command that's create workree. It's right here at the top.

So I'm going to tab and then I'm going to put in the name of the branch. This is the argument that I'm passing into the slash command. We'll call this example feature. All right. So, I'm going to let that run and let's see how we do. I'm going to turn on autoedits so that it can just go ahead and do it.

Looks like it got the project folder name. That's good. All right. So, we created the adjacent folder and it's creating the git workree. Aha. What's this?

All right. So, we ran into a little bit of a hitch here. We actually got pretty far. We did get the folder name. We created our work trees folder and in this case that folder had already been created. It was able to create the git work tree and inside it I can see example feature.

So you know again it did copy the whole codebase. So it got it got that far but claude itself can't cd into that folder because we're currently working within the confines of the main project folder. So, you know, Claude doesn't have the security permissions to back out of that folder and go elsewhere on my file system. Claude can only operate within the main project folder and into the subfolders. And so, that's what this error is is telling us here. And, you know, that's sort of like the conclusion that Claude gave us right here.

So, that's a good start. And, you know, maybe you can get something like this working for you. But in my opinion, there's still a few more steps that we need to handle, like opening up a new window and cding into it and just getting ready to go. I'd like all of it to be automated in one shot, much faster than all this. So, my next idea is to use a terminal alias with a script that can do all of that stuff and even fire up a new window for us and CD into it. And so, to get that script going, why don't we just have Claude write it for us, right?

So, for this kind of thing, like a standalone script that I'm going to, you know, install on my system, instead of using cursor or claude code, I like to just go straight into uh Claude itself or sometimes I'll use chat GPT and I'll drop in my prompt here and I and I'll get this little standalone script created for me right here. Okay, so here is the prompt that I'm giving it. Uh, I'm using ZSH. So, create a script for my ZSHRC file so that I can run an alias like this. I want it to be WT space branch name and I'm explaining that that should do the following. Basically what we've been doing like create a folder adjacent to the current projects folder get the project name it accordingly um and then create a git work tree and branch using the name that is passed via the alias argument and then open the new feature name work tree folder in a new window using cursor and I'm asking it to add a comment above every line in the script so that I can sort of read through it and understand what it built.

All right. So, it's using a clawed artifact. Cool. So, this pretty much looks good. I just wanted to sort of like demonstrate the process of working with claw to create little scripts like this. I do this kind of thing all the time.

And I actually already created my own version of this. So, I'm not going to use this one. I'm going to use the one that I already have. You know, you're going to want to custom and tweak it to your particular system and the types of projects that you work on, of course. But, you know, just to show you mine, this is my uh Zshrc file on my system. So this is my WT alias and the script.

You know, it's basically doing all those things. It creates the folder, gets the parent folder name, names it accordingly. But this part is actually important. You'll probably have to do some version of this in your script. One is to copy over the.env file if if you have that, you know, because that file won't be copied into the workree folders by default. So I'm actually having the script handle that piece.

I'm also making sure that these other hidden folders, if they exist, also should be copied in. I want to get the claude folder. I want to get the cursor folder so that my rules and settings from claude and andor cursor are also copied in. I use my instrumental components library for Ruby on Rails. So, um, if you're a Rails person, you might find that interesting. And I'm starting to use a thing that I built called AgentOS.

And I'm going to have another video about agent OS coming very soon. That's a whole operating system for delegating large projects to agents. I'll have more on that later, but that that's going to have its own folder as well. So, I want to make sure that all that stuff gets copied into the workree folder and that's what this block handles. Everything else is pretty much the same and then it gives me sort of a success message. So, let's go ahead and try it out.

And when we do this, let's actually start to create some new features in our music shop project here. So, I've already added guitars. I want to add drums, keyboards, and basses as the other three instruments that we want to inventory here in this app. And to build those out, I'm going to use my new work tree script to fire up the work tree. Then I'm going to open up Claude Code in each of those work trees, and I'm going to have those three different instances of Cloud Code, all adding the uh additional features to this project. All right, so I'm going to use my script WT.

Let's start with drums. Okay, so that happened super fast. You might not have caught that, but that actually opened up a second cursor window. And I'm going to use my um my raycast shortcut to throw that window into another desktop, another raycast shortcut to fit it to the size. And so now I can use my Mac OS shortcut to just, you know, go between this uh music shop. This is like my main project folder.

And then here is the drums folder. So let's check out our folder now. So now we see under work trees that these were the examples from earlier and now we have another one called drums. Again it's the whole codebase copied into it. That looks good. So here I'm looking at my main folder.

I'm on the main branch. And then here I'm on the drums folder. And you can see in the terminal I'm on the drums branch. Cool. Let's go ahead and do the same thing for bases. All right.

So, I'm going to throw this into yet another desktop. So, now I can go like that. This is desktop one. This is my main folder. This is desktop two. I've got uh the drums folder and the drums branch.

And then this is desktop 3. Here's bases. And uh here is um the bases branch. Let's do one more. I'm going to do I'm going to clear this. Do WT again.

This will be keyboards. All right. So, here is my keyboards window. I'm going to throw that into another desktop. All right. So, now I've got here I'm back to one.

So, here is my main folder, music shop. Here is two. This is drums. Here's three bases. And here's four keyboards. All right.

So, now I'm going to go to the drums. And I'm going to fire up Claude Code. I'll just type Claude. And by the way, we have copied in here, you know, that command from earlier, which we're not really going to use for now. Um, it did copy in my settings. So, the permissions that I had granted earlier, those will now already be pre-granted here.

And, you know, this list can can grow over time. It also copied in my Claude MD. Now, this is something that I actually didn't cover in the beginning of the video here, but in a new project, whenever I'm start using cloud code, it's always a good idea to do claude init. and and Claude will actually do its own uh sort of spidering through your codebase and write its own claude MD file to sort of get oriented with how everything works in the codebase. So it did that on the main project and then when we created the workree folder, it copied that in here in the drums project. And then same thing over here.

Let's fire up claude for bases. And then we'll fire up another Claude for keyboards. So now I have three instances of cloud code all fired up on three different branches inside three different code bases. Again, just to really illustrate this, let's look at our folder. This is music shop. This is my main project folder.

This is our work trees folder. And inside we have bases, drums, and keyboards. Three different copies of the codebase. Okay. So, I'm in the drums work tree here, and I'm going to give Claude Code uh the prompt for creating the drums resource in my app. I already prepared these prompts for adding drums and bases and keyboards.

It's not quite as relevant for this video, but basically what I'm doing here for each one is I'm I'm telling it to use my instrumental components component generator library for Ruby on Rails. It's a Rails thing. That's sort of a separate topic for another day. But I'm I'm actually instructing it to use that to create uh our uh drums resource and that will you know fire up the the routes and the controllers and the models and the views run the migrations. I'm also asking it to add the drums to um this navigation. So each of those branches should be adding another one to the navigation.

Now, we might run into some some conflicts there and we can deal with those, but uh yeah, let's go ahead and do that. Okay, so that is starting up. I'm going to go ahead and fire up the other one. So, here is bases. So, I'm going to go into bases and I'm going to paste that in and start that up. And then the last one was keyboards.

And that's starting up as well. And make sure auto accept edits is on. Okay, so it looks like the task of adding drums has completed and the bases task has also been completed and the keyboards has been completed. So now let's go back to the drums codebase here and in a separate terminal. I want to check it out and take a look. Right?

So this is another tip is to run the server on a different port than your original server. Right? So, if I go back here and um and if I'm running, you know, music shop, I have a shortcut to run my my Rails server. Um that's going to run on port 3000, right? So, if I look at this, I'm looking at the music shop, the the main project folder here, which only has guitars. But here in drums, again, I have a shortcut to do that, which is going to run my rail server on uh port 3002, right?

So this will be like our second one. So if I go back to my Chrome and go to two or 3002, it's a separate database. So I'm going to need to actually create a separate user. Okay, cool. Actually, that that worked really well. It added the the drums navigation item here.

And I can, you know, create a new drum. And yeah, that's looking good. So now I've got guitars and drums. Sweet. All right, let's go to bases. So I'm going to open up another terminal here.

I'm going to do RR3. That's my alias uh on my system running the rail server on port 3003. So if I go back here and do localhost 3003 again it's a separate database. Okay. So this one has guitars and basses. This one has guitars and drums.

And this one only has guitars. To to finish this out I will um take a look at keyboards. for that we'll do RR4. So that's going to be running my server on port 3004. Okay, so here are keyboards and I can create another keyboard. Looks good.

So again, we have our main folder which still only has guitars. So we need to merge these three into our main project. All right. So first on the drums branch, let's stop that server and let's commit. And let's also commit the work for bases before we we forget. I'm going to do added bases.

Again, I have uh terminal shortcuts for this and keyboards. Cool. All right. Now, let's go back to our main branch here. You know, normally you might want to do a pull request, but just to to keep it fast for this demo, let's go ahead and merge drums. Okay, so we have merged the drums and now I'm running the server on localhost 3000.

That's the main folder for the project. I now have home, guitar, and drums. Okay, so now let's go ahead and merge uh the other two, bases and keyboards. Okay, so um this was sort of expected. Uh there there is a merge conflict when I'm adding bases. And so let's uh take a look and resolve these just like we would need to resolve any merge conflicts, you know, when working with a team member who just contributed something, right?

So, and I'm going to clean this up a little bit. I'm cursor sort of uh corrected the rest there for bases, and we should be good to go. Let's take a look. Yep. All right. So, there's bases.

So, now we have guitars, drums, bases. Last one is keyboards. We're probably going to need to go through the same uh song and dance there. Let's do get merge keyboards. All right. So, we're all set there.

Now, we have all of our instruments uh all set up in our main codebase. So, that's how you can multitask with Claude code running multiple agents in parallel. It's pretty powerful stuff. So, right after you hit subscribe on this channel, I've got another video where I go into the movement that Claude Code has introduced into the picture for us as professional builders. We're entering into agentic development. It's really exciting, really interesting.

Things are moving super fast. So, I'll see you over there.
