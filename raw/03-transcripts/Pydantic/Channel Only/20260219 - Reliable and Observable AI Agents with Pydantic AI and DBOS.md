---
title: "Reliable and Observable AI Agents with Pydantic AI and DBOS"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Pydantic"
---

# Reliable and Observable AI Agents with Pydantic AI and DBOS

Uh hello. I'm here today with Shan Lee, co-founder of DB Boss. Welcome. &gt;&gt; Hi. Nice to meet everyone. And we're going to talk about durable execution and deboss.

So, Pedria just released an integration with Deboss that makes AI agents reliable by default. So, let's flash. Uh, Shen, what is DBOS? &gt;&gt; Yeah. So, Deboss is a lightweight durable execution library that is built on top of Postgress. So, you can use it directly in your existing applications without rearchitecting your code.

And um what are the benefits of using deboss over any other durable execution solutions in the market right now? &gt;&gt; Yeah. So I think the main benefit of deboss is that it's really lightweight. Uh often the time people come to us saying they can integrate deboss seamlessly into their applications because they are already using a Postgress database and they just need to add a few Python decorators to their functions and then their uh their applications become durable. So they don't need to host a separate orchestration server and they don't need to host dedicated workers for that. Hence lightweight.

&gt;&gt; Yes. So it's very similar to the philosophy of panic AI where it's also a very lightweight and flexible library. &gt;&gt; Yes. Yes indeed. Very good. Um so since we we started talking about pentic AI then so penti lets you express agent logic and tools and structured outputs without introducing a separate agent runtime.

Um can you explain to me what are the benefits of using deboss for reliability? &gt;&gt; Yeah. So by using deboss together uh with padic AI uh you can we can automatically checkpoint the the output of the progress of your workflows your agenic workflows. For example every time you call an external service we'll checkpoint a result and every time you call the external tool we can checkpoint the result of that too. So that if your server crashes or something happened in the middle or you redeploy your applications, you don't have to restart from the very beginning. So you can save the amount of tokens you burned on those requests and you can save a lot of time uh instead of because instead of running from the very beginning, you continue from where you left off using the checkpoint.

&gt;&gt; That sounds like a very useful thing for deep research agents. So actually I can show you the code for like a fun uh deep research agent uh I built with panic AI and deboss. So we published this demo under deboss demo apps python panic research agent. So the setup is really easy. You install UV you set up your uh API keys for panic AI gateway. You set up logfire and deboss conductor.

And then the main logic is just in one single file. So you just need to define three agents. Uh this the first is a planning agent. It basically analyzes the query and designs a plan for deep research uh to answer the query. And then we'll use the search agent to search the web and find related results. And finally we'll use an analysis agent to aggregate results uh and then provide a final report.

So as you can see, Pyenic AI makes it really simple to define those agents using different models, using different prompts and because thanks to structured output, you will get a very clean report uh and a very clean uh agent interactions across different agents. And then once you define those agents, you can simply wrap those agents as deboss agents. just one line you you define your agent using pyen AI and then you use the py deboss integration called a deboss agent now you have a durable agent and then what's more when you actually want to call the agents instead of calling the original agent you call the deboss agent and for sub aent calling it's even simpler so we define an extra search tool on this analysis agent by calling the deboss search agent. So this uh analysis agent will do a sub aent call and then everything is recorded through deboss. So even sub aents can be traced and checkpointed correctly to the database. So you will never lose progress.

And finally this is the main deep research workflow. So we can see that we first use the plan agent to get results and then for each plan step we use deba start workflow async. So we can search we can start those search workflows in parallel so we can fan out to parallel workflows and then at after that we can collect results later on so that you get the benefit of concurrency and parallelism. So it increases the speed of processing and finally once we collect all the information we'll put it to the deboss analysis agent and then finally we get the result. So everything every step every model calling will be recorded in the database. So you can crash anywhere in between and your agent will come back right online.

Very cool. Are you going to run this example for SD today? Sure. Uh so before running that um we can talk about the logfire integration. So in this demo if it detects a logfire token it will just configure logfire and then instrument pinic AI. And the benefit is that so deboss automatically generate traces.

you just need to point the trace to uh you just need to enable the trace in the deboss config. So once you enable the trace uh deboss will automatically export everything to lock file. Okay. So what about if I want to configure my spans using DOS? Is it is that possible? Uh so for the spans in your agent tools so like if you have any specific tools you want to create a special span then you can just use span here directly.

Do you want to see the demo now? Yes please. Cool. So we actually built a front end. It's uh built with TypeScript but you can see if we just have the front end uh it doesn't run anything because we don't have the back end. And so let's get started to run the back end.

So we simply need to uv run python main.py. Just run that python file. It will load up and you can see I've run some queries before because everything is stored in the database. When it starts up, it will just load whatever is stored there before. &gt;&gt; So what is the what's this interesting question there? Find me a list of Python AI conferences in 26.

Let's go. So you can see in this demo uh there are three stages for this agent. The first stage is planning. So it will call the planning agent. It's running. &gt;&gt; Very good.

&gt;&gt; And then we start five concurrent search workflows. By the way, you will be able to find see all the workflows on the deboss console. You can see all the console there. Five workflows running in parallel. And then we can kill the agent. I would like to see that on log fire too.

Oh, sure. So, let's see. So, those are the traced agent run on lockfire for now. But I stopped agent. So currently it got stuck in analysis agent. &gt;&gt; So let's just restart it and you'll see it comes all back online and instead of repeating this all the search agents it directly jumps to the analysis agents and continue the workflows.

You can see the workflow details here and analysis agent is still running in progress and on logfire you will see it continues with the analysis agent and you can see on the this side it didn't go through all the planning and search phase it's continues with anal analyzing phase has finished completed and we'll see comprehensive report and very nice yep I I guess it skipped the PI AI conference. It should &gt;&gt; not there. I don't like this. &gt;&gt; So sometimes you might want to restart the workflow. Maybe you want to um for example you want to fork the workflow and run it again. So we'll keep running.

We able to see it? Oh, we're able to fork the workflow through deboss. So instead of going to a planning agent, we fork from the searching step. So now we're re we're searching it again and now analyzing it again and hopefully we'll get some better results for this time. Fingers crossed. But I was when we fart um we fart just from the search.

Uh so we're not rerunning the entire workflow. We're just rerunning the section um that we're interested on. Yes, exactly. So when we fork a workflow, we'll keep the checkpoints from the previous one up to a certain point and then we'll kind of explore an alternative path from there. So hopefully this time we'll get some new results. &gt;&gt; Absolutely.

And we can continue to uh monitor the cost and everything. &gt;&gt; Blockfire &gt;&gt; still running. &gt;&gt; It's cost something two cents. Now it's done. &gt;&gt; And now it's done indeed. &gt;&gt; Whoa.

&gt;&gt; 10 cents. &gt;&gt; 10 cent. &gt;&gt; Still no P AI com, but it's okay. I accepted. &gt;&gt; Okay. I'm sure in the previous run I actually searched PI AI so it's not really stable.

Sometimes when you asked the agents the same question they will give you different results. So I think the benefit of using deboss is also using deboss and uh panic is that you can explore different options. You can observe what happened in the past and then you can do more auditing on what agents have done and how the decisions were made based on the previous output based on certain like basically you can get the context for your agent runs &gt;&gt; and running sections as well which is quite important if you're trying to debug and understand in which section of my AI workflow is the hallucination happening um or any other bias. Wonderful. So for more information, we have a gist with this code. We also have a blog post which with much more detail of everything that we just talked about.

And if anybody wants to keep in contact with you or learn more about deboss where they should go, uh visit our website at dbos.dev. And uh you can also read the uh deboss integration docs on the panic AI uh docs page. Uh yeah, feel free to reach out and we're always here to answer questions and help you with uh reliable agents. &gt;&gt; Wonderful. Thank you so much. This is very good.

Thank you. Um and that's it. Well, AI stateless engineering. Thank you.
