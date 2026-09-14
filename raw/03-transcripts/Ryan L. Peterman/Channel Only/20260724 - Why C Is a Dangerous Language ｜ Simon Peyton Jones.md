---
title: "Why C Is a Dangerous Language ｜ Simon Peyton Jones"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Ryan L. Peterman"
---

# Why C Is a Dangerous Language ｜ Simon Peyton Jones

Then see, you program my mutation, so it's unsafe in the sense that any function can mutate any variables any time. It does a lot you you pass pointers around a lot and functions mutate the memory pointed to by those pointers. And moreover, typically they can mutate it anywhere. There's no array bounds checks or anything. So, it's kind of like super unsafe and in fact and this is demonstrated by the fact can you imagine that like all of these exploits that we get every day, right? Um that you know, MSRC is discovering in huge numbers, but but we've had you know Why is the internet so insecure?

Primarily because all of our software infrastructure is written in unsafe languages. If we I mean if we'd written all of our, you know, internet software and operating systems in Haskell or maybe in OCaml or ML 99% of all these exploits would be removed by construction. Like it's like we've built a boat out of paperclips and we're surprised that it's leaky. I mean, you shouldn't build boats out of paperclips, right? Because they have a holes in them. You should build it out of a secure substance.

Like but then it's too late. So, we spend incredible amounts of human ingenuity and effort patching the holes in our boat built of paperclips. It's tragic. It's tragic how much effort and ingenuity and money has been lost and waste of resources just because we wrote our you know computational infrastructure for the world in an insecure language. That's what I mean by unsafe. How many exploits are based on buffer overruns?

Or you know, pointer manipulation that's gone wrong. If you couldn't have a buffer overrun, you couldn't do pointer manipulation that go wrong. Those those exploits just wouldn't exist. >> What about more modern versions of those lower-level languages? >> Oh, much much better. Much much much better, right?

If we rewrote all of our software infrastructure in Rust things would be way way I I'm not actually even sure whether Rust has array bounds checks built in, but suppose it but it must have the ability to promise that you're not and actually out of bounds. I don't quite know quite know how, but if you compile all your code with that switched on, you're a way better situation. Way better. So, yes, this is not just functional programming, but you did ask about why I thought C was an insecure, unsafe language.
