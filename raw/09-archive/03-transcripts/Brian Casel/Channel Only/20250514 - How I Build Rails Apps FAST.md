---
title: "How I Build Rails Apps FAST"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Brian Casel"
---

# How I Build Rails Apps FAST

Let me show you version one of instrumental components. It's my toolkit that I've always wanted when building out my apps with Ruby on Rails. So whether I'm vibe coding in cursor or hand coding, I'm usually doing a hybrid of both. I find that building with my components helps me ship highquality products fast and pack in a lot of power with just a few commands. So let me show you how it works. So once you're inside, you'll find uh documentation and instructions on how to install instrumental components.

You have two options here. You can install the gem, which lets you install individual components into your project on an as needed basis, or you can use our starter kit, which gives you a fresh Rails application that comes with instrumental components and all of the components pre-installed for you. I'm going to walk through the process of installing the gem. So, if you haven't done it already, you'll need to start up a new Rails application. The only hard requirement here is that we're using Tailwind version 4 or up. So I'm going to Rails new demo app.

That's what we'll call it. And we will add Tailwind. Then you'll want to CD into your project. From there you can pop in our installer gem into your gem file. and run bundle install. Finally, you'll want to copy this oneliner down here.

This will install our component generators and register your license all in one shot. We'll just run that. Okay, so that was successful. Now, you might see these red messages here. That just means that your project doesn't yet meet the base requirements to run instrumental components. That is we need active storage installed and active and action text installed.

Let's get those and we'll db migrate those. Let's run bin dev and we should have our rail screen up and running. Cool. Now, typically the very first component that I like to install is our simplest component and that is just to install a root page. Instead of the rail screen, we just want a hello world page with a controller and a view and put that into our routes file. So, let's run rails g instrumental root page.

And that's how all of the commands in instrumental components work. Rails generate or rails g instrumental colon the component name. And with every generator, it's going to start with an overview of what's about to be installed into your project. This is a super simple one, but some of them are more complex, and you'll see a long list of of tasks that it's about to run. So, you'll just approve that to proceed. I'll hit return.

And then you're going to watch the terminal go step by step installing these files into your project. And then when it's done, you'll see a message like this in green, which gives you an overview of everything that just happened. In this case, we've added two files, a controller and a view. We've added one line to our routes, and we are all good to go. See what our site is looking like. It's not going to be exciting.

It's just going to be a hello world. Okay. So, we've got our first component installed into our project. All right. Now, let's really get our project going. I'm going to install four components that I always use on every project.

We want to start with authentication, so login along with a user signup flow. Then I'm going to install the teams component, which sets up accounts and users, an invitations system for team members. Then I'm going to install a back-end dashboard for me and my team to manage users and accounts in my product. And finally, I'll install instrumental commerce. That's our Stripe integration so that I can start charging for this SAS product that I'm going to build here. Now we'll start with authentication.

That's railsg instrumental authentication. And actually this is going to fail because it's going to check requirements and first it's going to tell me that we actually need to install the core rails authentication generator that came with rails 8 and so our authentication layer is built on top of that. So we want to run rails g authentication. So this is starting with the core rails authentication which just gives us you know like a login flow and we can migrate. Okay. So now we'll be ready to run the same command again.

Rails g instrumental authentication and once again we have an overview of the component that we're about to install. Now most of these components actually pull in multiple components all in one shot. Right? So, our authentication component also makes use of all these other ones like the logo component, the menus, drop downs, buttons, tool tips, and a whole bunch of stuff. So, it's going to give you a list of everything that it's about to install along with this. We want to proceed.

Now, part of this is it's going to actually install a layout into our application. And when we install a layout, it asks whether we want to make that our default application layout or give it another name. In this case, yeah, we'll use the application layout. So, I'll approve that. Okay. Okay, so now it's going to step through the installations of, you know, 15 different components and you can see it making progress.

Um, the blue lines kind of give us like an update on which step in the process that we're at. You'll see these green lines which means that another component has successfully been added to the project. Now, by default, this is happening in slow mode, right? Where we can sort of watch it happen step by step. You can just add the the fast flag to make this go all in one shot. And you can even add that to your config file for instrumental uh so that it uses fast mode every time.

Okay, so that's all set. When it's finished, it gives us this recap which in this case it shows 58 new files have been inserted into our project. We can go through those and review those later on. And it also did some code insertions which means it it took some some existing files, it left its code intact and it just added a bit of functionality and methods and things um to those. In this case, we did add a migration. So we'll need to migrate that.

And we also added a gem. It pulled in our icons component which uses the loose rails gem. Okay. So, oh, and we added a few routes to our routes file. Let's go ahead and get this migrated. We want to run bundle.

Let's see how we're doing. Okay. So, here is our new and improved login flow and our authentication flow. Actually also gave us a sign up and registration flow. Inside it gives us like user profiles and avatars and time zones and a whole bunch of other stuff. Um, but before I actually sign up for an account, I want to make sure that I set up my accounts model and users and teams and the association between those.

And that's where our teams component is going to come in. So, I'm going to stop the server and I'm going to run rails gin instrumental teams. And this time I'm going to use the fast command to make sure that we just run through this much faster. Now, we always start with our overview. In this case, we're going to install the teams component plus these additional components. But it also found that 11 other components that would be used by the teams component are already installed in our project.

So we're not going to install them again. All right, let's proceed. Okay, so that was much faster this time. Of course, here is the recap of everything that was just installed with the teams component. 40 more files have been inserted into our project. We've got controllers, you know, views, partials, couple code insertions.

Uh there are some new migrations. Again, we set up the the accounts model and the route and the users and a whole invitation system. So, we're going to migrate that and we added the page gem that adds uh pageionation and we have all the styling built in for that as well. And we added a couple of routes. All right. So, let's get this stuff migrated.

Bundle. Cool. I'm going to start the server. I've got a shortcut for that. All right. So, I'm going to sign up for my account and I'm dropped into the application.

This is our application layout and we have a few different layouts that we can install with instrumental components, but this is the one that came with our uh our early installations. Up here, I've I have a user menu. I've got my account settings. I've got my user profile settings, password. Here is my team section. So, I can actually uh send an invite to other team members and give them another role.

The the mailers are all wired up for that. So, they receive an email, they accept the invite, then they have a flow for them to come in. I can add additional accounts and then I can even have like an account switcher up here. So all of that is now installed into my project. Good to go. All right.

The next thing I want is an admin dashboard where I can manage things on the back end like users, accounts, and later on managing products and things for my product. So let's stop the server. I'm going to do Rails G instrumental admin. Let's use fast mode. Actually, you know what? Instead of instead of manually adding that every time, I'm going to go into my config, go into instrumental YAML, and these are the configuration options for how your instrumental components work.

So the first thing is I'm going to turn fast mode to true. So it just uses that every single time. Now, while I'm here, let me tell you about the prevent overwrites list. you know, building with components. What typically happens is you'll install some components and then you'll go into the components themselves and customize them and actually adapt them to your project. So, as we're installing lots of components and reinstalling and updating components, you want to be sure that you're not overwriting your customizations.

So, that's where the prevent overwrites list comes in. You can just list out the files in your project that you've made some customizations to or that are really important that you don't want to overwrite and we will prevent the overwrites. And if you ever need to grab some of the updated code from the new improved components that come out throughout the year, you can always go into our starter kit and find the PR and and grab the individual pieces of code and import them into your project. Okay, so let's go ahead and get our admin component installed. I'm not going to use the fast flag because that should happen automatically. So here is the overview.

the admin component plus a plus two new components will be installed and it uses 12 other components that we already have including buttons, icons, breadcrumbs, logo, toggle, and you know, a bunch of other stuff. Okay, so we're going to proceed and that's all done. So now we have our recap. Bunch of files were overwritten because they were not in our skip overwrites list. That's okay. We inserted some code into things like our application controller and a couple other places.

And we did add a migration and a couple of routes. We'll run the migration. Now, in order to actually use the admin panel that we've just installed, I have to make my user an admin. That's like, think of it like a super admin in your application. That happens directly in your database. So, you could do that in Rails console or I like to use table plus on Mac and I have a shortcut to launch it.

Um, and so I'm going to go into my user record that I had registered earlier and we're going to change this admin flag to true. and I'll restart the server. Okay, so now that I've made myself an admin, that gives me a special link here. All right, so here I am in my backend admin panel for my product. It uses the secondary color, so it's a little bit different from the main application. So I know that I'm here in the admin.

Now, out of the box, we have, you know, a main dashboard. We can add stuff to this later. I've got my users list and I've got my accounts list. I can inspect any individual account. I can see which users are in each account. And this one happens to be myself.

But if I were viewing another user, we'd have a button here and I can impersonate that user. That's really helpful for customer support. And as the app grows, we can add more things to our admin dashboard that we need to manage like commerce, like our products and purchases and orders and subscriptions and customers. And that's actually what we're going to install next. Let's get into it. All right.

I'm going to stop the server. And now I'm going to install instrumental commerce. That is our Stripe integration. Let's get to it. Rails G instrumental commerce. Okay, so this one is going to install a couple of new components, including our drag and drop reorder component, our FAQ component, some copy to clipboard stuff.

All right, we're going to proceed. That's all done. This was a really big one. So, um, you know, we've added 165 new files into our project. Um, lots of stuff. you know, there's like products and prices and subscriptions and payment methods and checkout flows and um you know, user payment history and you know, all this stuff is it's it's a it's a full commerce system for selling subscriptions and one-time product with a pricing table and checkout flows and everything.

So, um a lot of stuff happened. We have a bunch of migrations to run. We added the Stripe gem and we added the positioning gem along with a bunch of routes. All right. So, let's get the all migrated bundle. Okay.

So, let's see how we're doing here. Now, again, I'm I'm viewing my admin panel. If I refresh now, we've just added commerce into our admin panel. So, here in the commerce section is where I can set up my products, my prices, plans. Um, you know, I can also see purchase activity, payments, subscriptions. Now, I'm going to have a totally separate video and a bunch of guides on commerce because it really goes deep.

I don't I don't want to waste time here in this demo, but you know, as we can see, it's all here. Um, I'm going to go back to my app. All right, one more thing before I wrap up this demo. Let's actually start building our product, like our features, right? So, let's use the instrumental scaffolding component to scaffold a model and some views. I'm going to use this app as like a place to list my guitars, right?

So, let's do this. I'm going to stop the server. I'm going to do rails gin instrumental scaffold. And this works just like a rail scaffold except it's a little bit better. We're going to call this guitars. Each one is going to have a name, a brand purchased.

That'll be a datetime. And how about favorite? That's a boolean. All right, let's run that once again. And here's the overview. We're going to proceed.

It's going to ask us which column is actually going to define the name. This, you know, it's going to use that when it sets up the controllers and things. We also have the option to give each guitar a unique slug like in the URL. And yes, I want to do that. And we can actually generate that from the name of the guitar or generate a random one. We do want to generate it from a field.

We'll choose the uh the name field. And uh yes, we want to pageionate the index of guitars. So I'm going to agree to that. Okay, so um it just ran through the whole process very fast. Here is the recap. We installed some components and it did add a migration for guitars.

Let's run that. Restart the server. Let's go to guitars. Instead of needing to update the URL directly, I want to actually update my main navigation. I'm going to update global nav. So this partial handles handles the side navigation.

And you can see some sample code in here which will actually give us like a a top level and a suble navigation. I'm just going to add a second one here and that's going to link to guitars path. We'll give it an icon. See how we're doing. Okay. So there is our guitars link.

It takes us into our guitar section. Cool. Let's add a new guitar. All right. So here, you know, it just gives you a form. Uh, very simple.

Show view um, edit. And now we're back on an index. These are totally customizable. We've got some like settings drop downs here for each one. We can delete one. Let's add another one.

Now, of course, everything is mobile optimized. So, you can take a look at that. We've got a mobile menu all built in and everything is dark mode friendly. So, all of that is all set for you as well. Let's take a look at our routes. You know, we've installed a bunch of routes.

It's nicely organized. You can go in here and and organize it however you want. Let's check out that guitars controller. You know, it added a whole bunch of controllers and billing code and commerce code and admin panels and name spaces and all that stuff is just organized for you. It's all here. You can check it out.

We're using Tailwind version 4. You can customize all of your colors. So, if we look into views under shared components, this is where most of the components live. So, for example, here's the drop-own component, and all of this has been meticulously built out to be fully customizable. These are just basic Rails ERB partials. You can pass a whole bunch of options and attributes into them and change them up um without uh without changing the core component.

But if you need to, all of your component code is right here in your project. You own it. You're it's good to go. We've got some layouts that we've installed like the authentication layout, the application layout, the admin layout. We built out an invitation system and you can check out all these things. We we follow um common patterns across the project using a lot of Rails conventions which makes it really easy for you and your team to maintain and also for LLMs like and and using tools like cursor and wind surf when you're vibe coding.

It's all standard Rails stuff. So uh you know it it makes it really um easy to build out applications really fast. So that's a look at instrumental components. There are many more components already included and I'm releasing new ones all the time. So check out instrumental.dev. Thanks for watching.
