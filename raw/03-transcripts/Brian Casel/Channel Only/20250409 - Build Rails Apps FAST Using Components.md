---
title: "Build Rails Apps FAST Using Components"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Brian Casel"
---

# Build Rails Apps FAST Using Components

Let me show you this app that I just spun up using instrumental components. It only took like four commands. So, here's a preview of instrumental components, which is launching very soon. Here's the finished app, and then I'll show you how I did it in just four commands. I scaffolded up a model for guitars. I can list out um each guitar.

It's got these uh drop-own menus. It's got a system for adding a new guitar and editing each guitar. As you can see, we have uh breadcrumbs up there. Up here I've got my uh user navigation where I can manage my account settings. I can even see all of my team members. So I can invite team members, they can accept invitations, I can create a new invitation and I can uh you know personalize it.

Give each person a role. I can even switch accounts. So I have multiple accounts here. I can use this account switcher up here to easily switch between my two accounts. And I even have a back office admin area. Uses a different color scheme.

And here I can see all of the users who've signed up for my app. I can see all the accounts that were created. And when I install our instrumental commerce component, I can manage all of my products and subscriptions and purchases all here in the back end. I can go into any user and I can even impersonate the user to uh you know run some customer support and seeing what's happening in their account. And I can stop impersonating right here and come right back into my admin dashboard. All of it is customizable.

And so now I've got all the table stakes installed in my new product here. And now all I need to do is start adding my core features and I'm off and running. So let me tear all this down and let's rebuild it in just a couple of commands using instrumental components. Okay, so I've just started over. I've got a fresh Rails app. The only thing that I've added so far is the Rails 8 authentication generator.

And all that did was it gave me a basic signin flow. So let's start using instrumental components to get this thing ready for prime time. First thing I want to do is add our authentication component, which is a layer on top of the Rails authentication, and it gives user profiles, a sign up and registration flow, user avatars, a panel for users to manage their profiles. We're going to do Rails instrumental authentication. First, it's going to check some requirements to make sure that we have the basics already installed, and we do. Then, it's going to give me a preview.

This one pulls in 14 other components from instrumental in the things that are about to be installed. So, we've got the logo component, uh, user menu, drop downs, flash forms, tool tips, buttons, icons, subnavs, avatars, breadcrumbs. So, um, let's get all that installed in one shot. I'm going to proceed. But before we actually get into it, it's going to ask a couple of questions about what I want to do. We want to make that our default layout.

So, I'll approve that. I can choose which icons library I want to use. I like to use Font Awesome. Okay, so now we are off to the races. We're going to now automatically install all of these components directly into the project itself. So, as you can see, you could watch the progress here.

It's adding files. It's adding controllers, views, partials, stimulus controllers, TWIN CSS styling. Um, it's it's adding functionality and wire wiring things up so that it all just works right out of the box, but it is putting these files directly in your project so that you can fully customize everything and everything is documented over at instrumental.dev. I can watch this progress happen or I can use fast mode and all this stuff will install instantly. But we'll fast forward a little bit here. Okay, so we have completed that installation and right here it gives us a little recap to sort of run down everything that happened.

So we've added 77 new files right into our project. Here's the list. Uh we've also inserted code into some existing files, keeping their existing code intact and just adding a few methods, helpers, some styling and whatnot. Um, this one did include one new migration, so it's giving us a reminder. We'll go ahead and do that. And we also added some new routes.

We'll take a look at those in in a minute. Let's see how we're doing so far. So, here's our new login screen. Much cleaner. It's all responsive. It's uh it uses our our form styling, our button styling.

We also have a signup form now. We have some social proof on there. All of this, of course, is customizable. Um, but you know, before I go ahead and register for a new account, I want to make sure that we have our accounts system and teams and and user system all squared away. So, we're going to add the instrumental teams component. Rails instrumental teams.

And so, what this is going to do is it's going to add a couple more components. And then it's also using a bunch of components that we already have installed in our project. It detected that. So, we're good to go. So, I'm going to proceed with this. And so, this is going to uh wire up our uh team member invitation system, a bunch of mailers for that, the way to track invitations and uh and being able to manage and different roles for different users in our accounts.

All right, here is the recap of that one. We've got all the files here and everything that happened. And by the way, we also have all this information stored in log instrumental. It gives you all the details of what exactly was installed, which components were installed and which files were added. So you always have a record of everything that was added into your project for you. So you're in complete control to manage and customize every single detail of what instrumental does.

And now let's go ahead and actually sign up for an account. Okay, so now we're logged in. We've got our flash message. It disappears there. It's using our minimal uh layout by default. And we've got our user profile and settings team member system all here.

But you know what? Let's upgrade the layout a little bit. I want this sidebar to be collapsible. I'm going to run rails gin instrumental layout. We're going to use collapsible sidebar. All right.

I'm going to refresh the server. And now we have a sidebar which can collapse. That's pretty cool. It even remembers the state that I leave it in. Pretty cool. All right.

So now let's start adding some features. I want to scaffold out uh a model. So I'm going to go ahead and run rails g instrumental scaffold. Let's do guitars. I'll give each one a name. We need a brand color strings integer uh purchased daytime.

That's good enough. We're going to proceed and get this stuff built out. So, a couple uh questions up front as it customizes how the guitars model and views are going to be integrated into our project. Which one defines its name? I do want to generate unique slugs for each guitar in the collection. I do want to pageionate the uh index view and yeah, it's going to get all that stuff wired up and installed into the project.

Okay, so there we go. I'm going to migrate that. Okay, we don't have any guitars yet. Even this little thing here is a little component for when we don't have any records, but let's go ahead and add the first guitar. And I can, you know, add more fields to it. This is uh just very basic kind of boilerplate stuff.

We've got our drop down all built in. Um, this is our listings component. By the way, everything, of course, is mobile optimized. We've got a a mobile uh menu all built in. And everything is dark mode ready as well. Let's go to my team members.

I just want to uh demo the uh user invitation. I can give the person a role. I'll send that invitation. It sends the invite as a mailer. The mailers are all wired up. I can accept that and open up in a different browser.

And so now I'm joining this team. It says I've been invited to join. I can set my password. I've logged in and it also notified the person who sent the invitation. So all of that stuff is wired up and ready to go. In my main account, I can track the status of each invitation and I can look at the list of my team members.

Pretty cool. I think the last piece is to add that admin backend dashboard. We're going to do Rails instrumental. You guessed it, admin. Okay, the admin has been installed. We're going to uh add that one column to the user table.

And I'm going to have to go directly into the database and set this user as the super admin for the app. So I've done that. And so now this user gets a special link called admin. I can click that takes me into the admin dashboard. It's using the secondary color scheme. Um, all of that is customizable in the Tailwind CSS settings that you have directly in your codebase.

Um, here you can see each of your users, the accounts. I can look at a user, I can impersonate the user. Um, and uh, all of this stuff is just wired up and ready to go. And as I add more features to my app, I can manage them here in the admin s such as instrumental commerce where I can uh manage purchases and subscriptions and payments with uh the users for my product. All of that can be managed here in the back end. So I'm back into my app and that is a quick look at instrumental components.

You can get on the early access list at instrumental.dev. Any questions or feedback, let me know. The
