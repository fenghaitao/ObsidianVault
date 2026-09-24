---
title: "Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations"
type: transcript
source: youtube
playlist: "Channel Only"
author: "Ryan L. Peterman"
---

# Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations

talk and I think there's also a paper behind it of this idea that uh one sizefits all database systems not optimal one size actually fits none and that what you really want is database solutions that target specific needs what database offerings you see today that are one-sizefits-all in 2004 when I wrote the paper we had an academic project which was building what became streambase And so a stream processing engine looks nothing like a relational database. And we had the gist of an idea for column stores for the for data warehouses which was popularized by Vertica looks nothing like a row store. So here were three wildly different implementations that had no resemblance to each other and in each case they were an order of magnitude faster than the other guys. So it's pretty clear that one side, you know, that in with those three instances, you give up an order of magnitude uh when you're running a database system that isn't architected for your kind of stuff. I think that's still true. I mean, I think Clickhouse is a column store.

Pine cone is faster than userdefined types on on textbased vector processing. And so I think it's it's still very much the case [snorts] and I think there's no difficulty putting a common parser on top of multiple implementations. uh Postgress has so far chosen not to do that. they don't implement a column store and so I think they are not they are not competitive you know on sizable data warehouses they also don't have multi-node support again for people with big data warehouses that's table stakes so I think it's just as true today as it ever was I think that what is true is that if you want to get going, you have a database problem, you know, the answer is choose Postgress [snorts] and there's a huge programming community, all kinds of all kinds of, you know, data type implementations. it's free uh and you can find Postgress talent easily and get going and and so I think it's it's it's a great choice for lowest common denominator and until you're trying to do [snorts] a million transactions a second it works just fine until you're trying to support a pedibyte data warehouse it it I say at the low end it it's absolutely Absolutely the right one sizefits all at the low end it's postgress at the high end that's just not true >> GPUs do they make available some new opportunities to optimize databases probably but I think the the big challenge is that GPUs are you know sumd sim you know single instruction multi- data and that's the anathema of indexing And so whenever indexing is the right answer, they're probably not a good idea. And I think uh also you've got to architect them so that the so that the bandwidth from storage is is not not the bottleneck.

And so if they're an add-on to the CPU as often as not the bus connecting it to the the GPU to the CPU is a bottleneck. >> Can you explain why indexing would be not as effective when there's SIMD? >> So let's let's say I'm I'm [snorts] looking for Ryan's I'm looking for Ryan's salary and I have a B tree. So you go to the root of the B tree. You find you find the divider that has both sides of Ryan. You follow the pointer.

That's a memory access for sure. Then you do it all again and you do this like three or four times. So that doesn't parallelize well. So the answer is indexing doesn't parallelize well. You mentioned B trees. When you first implemented uh that first version of ingress, did you write all of that by hand?

Because I imagine there's probably not some existing B tree library or something. >> Yeah, we wrote the original version of ingress was all written from scratch. >> What was the hardest part of that implementation? >> Uh query optimizer. >> And why was that hard? >> It's tough.

It's it's just algorithmically difficult.
