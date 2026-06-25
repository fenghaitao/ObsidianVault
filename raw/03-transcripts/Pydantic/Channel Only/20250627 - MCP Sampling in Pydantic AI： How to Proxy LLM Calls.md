---
title: "MCP Sampling in Pydantic AI： How to Proxy LLM Calls"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Pydantic"
---

# MCP Sampling in Pydantic AI： How to Proxy LLM Calls

MCP sampling landed in Pantic AI last week. Let's explain what it is and how to use it. So I actually talked about MCP sampling at AI engineer a few weeks ago. This diagram kind of explains how it works. So when we make a call to an MCP server, that MCP server can make calls to an LLM instead of having to but instead of having to make those calls directly, it can proxy them via the MCP client, which means you don't have to provision your servers with res with LLM resources, etc. instead they can use the LLM available on the client.

Let's have a look at what that looks like in Pance AI. So here we have a very simple example of an app using Panti. So we have a bit of bit of code here to configure observability with logfire. Then we have uh an MCP server running over standard IO. This is going to call the generate SVG uh file as I'll show you in a minute. We have our agent which is going to use OpenAI 4.1 GBT 4.1.

And then this is the core of our application where we're basically going to run our MCP servers and then make a request to the agent uh asking it to create an image of a robot uh in a punk style that should be pink. The point here is that our generate SVG MCP server is going to register one tool with our agent which is called uh image generator. This in turn is going to take care of converting a subject and a style into an SVG image. In particular, this is the clever bit here where our agent, our pilanti agent here uses the model MCP sampling model which has access to MCP context and therefore can make an LLM call proxied through the client. Um, and then we're going to we'll save the image and return the path. Uh, notably Pantic AI automatically enables sampling if it's run as a client.

You can disable it if you want. Let's go and run this example and see what it looks like. So, we see uh logs start to print out and we come over here to log fire. We can see requests ongoing. See our agent running. uh when GPT40 responds as it has done now we should be able to see exactly what happened.

So you'll see here that we have uh our outer agent run uh which called the tool as we would have expected and then that returned uh details of the image that's been generated. We can see pricing on this but notably you see here we have distributed tracing. So we see when we make the tool call, it goes uh from the client into the server, then back to the client to make the call to GP40 um and ultimately finished and output um a summary of what happened. And indeed, we can go and have a look at the image that generated. It's not great on this occasion, but MCP sampling worked correctly.
