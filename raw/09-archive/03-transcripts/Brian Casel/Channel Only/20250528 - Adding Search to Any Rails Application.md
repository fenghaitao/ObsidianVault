---
title: "Adding Search to Any Rails Application"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Brian Casel"
---

# Adding Search to Any Rails Application

Just about every app that we ever use today has a search function, right? So today I want to show you how I go about designing and implementing a search feature in every Rails application that I build. You know, this week I'm actually building out the docs site for instrumental components, my components library for Ruby on Rails. And sure enough, I needed a search component. So I designed a search function, built it into my Rails app with the help of cursor of course, and then just like I do with every UI component I build these days, I extract it out into a component that I can use again and users of my instrumental components library can use as well. So let's get into it.

Here is an example application that I just spun up. Uh I created a model called posts. Of course, I used the instrumental scaffolding uh component for that. Very straightforward. Every post has a title. um and uh time that it was created.

I can go in and I can see the content. I can edit the content in this form. Okay. So, so far I've added four posts and I can click this icon to launch my search or I can use the keyboard shortcut for forward slash to launch the search function. Um most users expect that these days and of course you should be able to hit the escape key to close it out. So I like to put the search in its own modal popup uh right in the middle of the screen.

So then the user can just start typing and you know this field is autofocused by default. The user doesn't have to like click again. So I can just you know start typing the title of a post or any content in the excerpt or the content of the post to pull up the results and then I can use the keyboard up and down and I can just hit return to go to that post. Um or of course I could use the mouse as well. Let's see. So, uh, this this post has the word, um, clutch in it.

So, I'll I'll just copy that and I will, uh, actually search for that. So, I pasted in clutch and it brought up this post. So, as you can see, the search query is going to find a match if it's in the title or in the excerpt field or in the body content. And I was able to configure, you know, which columns and which associated records, like the rich text record that's associated with posts, um, which of those things are actually searchable. And one more little detail here. So, if I go into a form and when I'm in a form and one of the fields is is focused, I don't actually want to launch the modal if I type the key forward slash.

I want that to actually be part of whatever I'm typing in. It's really annoying if I if I'm trying to type into a field and I hit a key that would trigger a launch of a modal or something. So, the stimulusJS controller that I'm using, which I'll show you in a second, to launch the modal is smart enough to know if any field on the current page is currently focused. And if I defocus it and then I hit the the slash key, then it actually does launch the uh the modal. So, that's pretty cool. Okay, so that is the search function.

Let me tear it out of this application and I'll regenerate it. I'll reinstall it and I'll show you all the pieces and how to actually install it in your Rails application. Um, especially if you're using uh instrumental components, which makes it super easy. Okay, so off camera I just ripped it all out and now I'm going to reinstall my search component into this Rails app. As you can see, uh, we no longer have the search icon up here. We'll add that back in just a minute.

And if I hit the slash key, nothing happens. It's not launching anything. It's not even in the app. Okay. So, let's go ahead and uh go into our codebase and I'm going to run uh the instrumental command for installing the search component. So, I'm going to do rails g instrumental search.

And you can check out my other videos on how to actually install instrumental components. And you can get a license of course at instrumental.dev. So, this this one is about to install the search component. And it's showing me an overview before I install it. It also works with a couple of other components that it'll pull in. So that's all good to go.

I'm going to hit return to proceed with the installation. Okay, so now this this feature this search function needs a few pieces of information in order to wire it up, right? So the first thing that it's going to ask me is what's the name of the of the class that we're going to be searching. So in this case, I want my search feature to search for posts. So I'm going to actually type in post. Okay.

So now we need to set up the link that each search result is going to point to. And in this case that would be the posts show view. So typically it'll be the show view for whatever class or whatever model you are searching. Now, the way that uh we're going to need to wire this up and the way that the generator is going to do that for us, it's actually instructing me that um leave out the uh the parenthesis part of the path helper, right? So, normally the path helper to go to my posts path would be post path with the uh the post ID or the post slug in the URLs. That that's just how my routes are set up.

Um, but in this case, we just want to include the part without the parenthesis. So, we'll do post path. I know that's a little bit confusing. That's just how the instrumental generator works. Then afterward, we can go in and inspect it and and tweak it if we need to. Okay.

So, next we need to select the set of searchable columns on the posts table that we'll want to search the content for. So, um, first of course, we want to search the titles of posts. So, we'll select the title. And yes, I want to add another column. Uh, next we want to select the excerpt column. And I'm done adding searchable columns for now.

Um, but you'll remember that we're also searching the content of posts. Now, that's not actually one of the columns on the actual posts database table because the content of the post is a rich text field which uses the action text uh, you know, column in the database. So that's what we call an associated record with posts. So in this case it's asking me would I like to add any associated records to search by and in this case I do. And then it's going to ask is that associated record a rich text field because we sort of need to treat that a little bit uh differently when we build out the code. Uh so yes it is.

And what's the name of that rich text field? So I can take a look at my post model and I have this has rich text um field here which I'm calling content. That's like the content of the post, right? So I'm going to say the name of that rich text field is content. And you know I I could add other associations like for example if I have like tags or categories and I want to include the names of those tags or categories um in the searchable content. In this case I don't.

We're keeping it simple. So, I'm done adding uh associated records to search by. Just a couple more questions for me here. So, when I get the search results, uh each result is going to be a link to a post and each of those search result is going to have a title. So, it's asking me which column on the post table do we want to actually use as the title. And of course, we want to use the post title column.

So, I'm going to select that. And then the other thing if you remember underneath each title I'm displaying like a descriptive text. Um in this case I do want to des uh I do want to show that and we're going to use that excerpt text. Okay. So it got all the information that it needed and now uh the component is being fully installed and now it's all done. So uh I've installed the component.

Instrumental components tells me that uh six files have been added. We're going to take a look at those in just a second. So um it did add my stimulus controller which handles all the JavaScript for this search feature. It added a new service object called search service. Added a couple partials to build out the actual search modal and the search results. And then we have a search controller and we're doing a little bit of uh of turbo responses here as well.

We did add one new route to our routes file for uh processing the search and uh there we go. Okay. So um that is all set. Now, let's see if it just works right out of the box. I'm going to run bend dev to restart my server. And I'll refresh my page.

And you'll notice I don't have the icon here. And if I hit the the keyboard shortcut for slash, it's not actually launching anything. So, why isn't it working? Well, there's one more step that we need to do to get this fully working. And that's to actually install the search component in our layout where we're going to have the search uh available. you know that this this last step is not actually part of the generator because your layout in each project may vary.

So let me show you how to um finish up this implementation and then we'll look at all the code that's involved here. All right. So I'm going to go into my application layout. Uh that's the layout that is powering this page and all the other pages that I'm currently working with. So I'm going to go to the body tag on that layout. And the first thing is I want to add the stimulus controller to the body tag.

Now, the body tag might already have a data controller. If it does, then you'll want to add a second one by adding a space. If it doesn't, then you'll want to add a data controller to your body tag. And the stimulus controller that was installed is in JavaScript controllers inside components. That's where all of uh instrumentals stimulus controllers uh get installed. We added search controller under here.

So um since it is namespaced under components we'll do components dash dash search. Okay. So then the other thing we need to wire up here is the keyboard shortcut. Right. So um in order for that to work, we're going to need to add data action because my body tag doesn't yet have any uh data actions. And it's it actually uh remembered that from when I worked with it earlier.

So on the key down event, we want to use the component search controller and we're going to call keyboard launch. That is the method that handles uh launching of the uh of the modal. So let's try this out now. And I'm going to refresh. And you'll still notice that nothing is happening. Why is that?

Well, there's one more piece that we need to do. And that is to actually render the search uh partial. So in if we go into views the uh search component added this search folder and this search partial that that handles the actual modal popup that that pops up. We need to include that or render that out in uh the layout. So that should work. Let's uh just restart the server.

I have a shortcut for that. I'm going to refresh here. And there we go. So now this modal exists in the layout and we were able to call it using the keyboard shortcut. Now you'll notice that I don't have the icon in the top of my of my layout here. So let me show you how to add that piece.

So I want to add it right here. And this whole top section is handled in the top uh partial. And all of this is documented in the instrumental components documentation at at instrumental.dev. So um you can follow along there but I just wanted to demonstrate it here in this video. So uh this partial is handling basically this whole block right here. And I want to find this area and that is right here.

And so it actually already is set up for flex items. So I can add like an additional item right here. And you'll actually have this uh cut and paste uh snippet provided to you in the docs. So I just added this. This is just a div um with some T1 CSS classes. And then uh inside it we are rendering the search icon and that is um powered by our icons helper which comes with uh instrumental components which then you know brings in uh lucide icons.

So the search icon is there. We've got this div and you'll also notice that we have data action and that's a click event so that we can actually click that icon and that's going to call our components search launch method. So, let's uh refresh that. And there's our search icon. And if I click it, it launches our search. So, we're good to go.

And then, of course, uh it should work. Oops, I hit escape to It's just a habit of hitting escape there. Uh post. And I can use the arrow keys to go up and down. Okay. So, let's take let's unpack the actual code that powers all of this.

Um I'm not doing anything fancy with this search implementation. I'm not using an outside service. So I'm not using any special gems. All I'm using is a Postgress database and some functionality that you get for free with Ruby and Rails and Postgress. It's super simple. Um great for a a starter application.

You can really go a pretty far way with just a simple implementation like this. So um let's start from the front and then we'll work our way to the back end. So on the front end, I already showed you kind of the markup. We're going to get into the actual stimulus uh stimulusJS controller. All that action is happening in search controller JS. So we've got a couple of targets uh the search modal the input field and then the results.

Um we've got the launch method which is called uh in two ways. One is using the keyboard launch and that is triggered uh when we you know hit the the slash key. Um, and this is only going to work if it's the slash key. And then this is that special code that's checking for whether um a any field on the page is currently focused. And if it is, then it would be considered is editable and we are not going to actually launch because we don't want to disrupt the typing into a into a form. Right?

So that's handled there. Um, this launch action is is hit directly when we uh when we click that search icon. You can see s um launch. We're hitting that there. Okay. So, uh moving down uh we have the close functionality which which can be done a few different ways.

You can escape it just by hitting the escape button and that will close or you can click outside and hide. So, let's take a look at the actual uh search partial. So this gets a little bit complex but we are adding some data attributes on the actual search modal. So um if I go like that and we inspect this let me open this up. We inspect the actual modal you can see uh where is it? Um this is the the main container which actually goes around the whole page and that's where you can see data action click um click outside and hide and what that does as you can see if if I have it open and if I click outside of it then it's going to hide.

So that's one really common UX thing that we want to make sure that we have. So I'm going to look at the search controller again. Click outside and hide. That's looking for the click event. Then it's going to check if that click event is inside of the actual search modal box. So let me show you that one more time.

If I click in here, anywhere in this white box, it's not going to close it. But as soon as I click just outside of it, it is going to close it. And that's exactly what we want. Um, next thing is the um keyboard close. And that's looking for the escape key event. So only this will only fire if the escape key is is hit and only if the search modal is already open and if it is then it's going to close it.

So this close and then we close and then we reset. So we have a reset function down here which will um hide the modal target. It'll reset the input field back to empty, right? because you don't want it to to be like, you know, test and then um and then close it and then reopen it and it still says test. We want it to be fully reset, right? So, uh that's what that does.

Um and then it also clears out uh the results. Okay, so now now we start to get into the interesting stuff, the actual searching, right? So when I start to type, every time I type in any letter, it's going to hit my server again to check for um search results. And so that search action is happening on the search input field. So here is the text field and that's wrapped in our wrapper which comes with instrumental components which you know styles up search field or styles up any form field um like that. Okay.

Okay. So, here's the the text field. We've got some, you know, it is autofocused uh by default. And then we've got this data attribute here. Um it is the input target. And then the action is search.

So anytime, so the event here is input. So anytime I'm inputting into the field, it's going to hit that which then um does this this fetch fetch query which is actually hitting my search route. So let's go to my routes and that is hitting this and that takes me to my search controller rails controller. That's the search action. Look how simple this is. It's just a few lines of code.

Of course, it there there's a bit more once we dig into the search service, but right here in the controller, um we are calling the search service. I'll I'll look at that in a second. Uh but we're passing to it the model that we're searching for. In this case, posts. And then these are the two columns on posts that we're going to search for. And then we have these searchable associations for rich text content.

So you can you can see now how the instrumental component generator asked me for each of these things. you know, the the class name, the column names, the rich text, the associated rich text. It pulled what it asked me for, and it automatically generated and inserted those values right into this controller. Did that for me right when I installed it. So, that's the kind of, you know, kind of power that you get when you're using instrumental components. It just sort of builds these files for you.

And then, of course, I can come in here and I can tweak things if I need to. All right, let's keep going a little bit. Essentially, that is going to give us some results and then we're going to kind of process and display those results using a turbo response. I'll get to that in a second. Let's go into that search service. And we have a bit more documentation right here inside the the codes.

It explains what it's expecting to to receive. So we want the record class. We want those searchable columns. Then optionally any um associated uh columns. Here is the code where we're actually uh running the I like query. Um and this is one of those features that comes with Postgress databases.

So this system actually will only work if you're using a Postgress database. It's not going to work with SQLite um or MySQL. Um uh so uh we are going to search first in those direct columns and then we're going to search in the associated columns and then it's going to sort of combine all of those conditions, join them together and then that sort of builds out the results and we return the results. Going back to our controller, we receive those results. Then we go to the turbo stream response and we're going to go into our views and you'll see search.turbo stream and then this is going to find the search results ID. So if we look at the uh search partial it's going to find this div which appears to be empty, right?

But this turbo stream update is going to fill it with search results if there are any. And if there's not then it's going to just display this. But if there are search results then it's going to display this partial which is for each individual search result. So um that is each of these you know each one of these is powered by this search result partial. Let's take a look at that. And there's actually quite a bit of um customization that you can build right into this.

So, for example, let's say I wanted to display an icon with each of these. Um I could do that. If I go back into the search result, I can add icon name and let's just use the book icon. And so now I'm going to search again. And so now we have a little icon there. So that's kind of cool.

Um we also have options for like if you're searching for users and each user has an avatar. Of course we have an avatars component. You might want to show like the user's name and their avatar um in the search results. So you can do all that using any of these customization options that we give you um built into this search result uh partial. So for now we're going to keep it simple. We're going to get rid of that icon and we're just going to display the title and even the description is optional.

You can you can get rid of that. But um again our generator automatically inserted the title column which we said like use the column named title and we said we specified that we want to use the excerpt. Um so result here represents a post right. So the results each result we want to look at the the excerpt and then remember that weird thing where we defined the um the the link path and I only typed in post path well our generator grabbed that and then it added its own uh parenthesis here to to build out you know it's because it's within this each loop that's why we had to do that that weird system. I might improve that in the future but that's how we did it. If your postpath link ends up being incorrect, if it throws an error, then you want to come into this file, this search.turbbor erb, and just fix that up and then you'll be good to go.

Oh yeah, one more thing and that is the uh navigation of the search results. So if I open this again and I get some search results again, I can use my arrow keys down and up to go through these and or come right back to the field. And all of that is handled again in our stimulus controller. We're going to kind of come full circle here. You can see navigate results. So that's looking for um arrow down or arrow up key events and then um and then it's going to sort of like cycle through each of the search results and it has some logic in there to make sure like if we're at the end, you know, don't keep going and and that sort of thing.

So all of that is handled. You get it all right out of the box when you install the search component from instrumental components. And if you have any questions about this or any questions about building with Rails or with AI or with components, uh, leave them in the comments. I would love to do more videos on how to build Rails apps with AI and cursor. And yeah, thanks for watching. See you.
