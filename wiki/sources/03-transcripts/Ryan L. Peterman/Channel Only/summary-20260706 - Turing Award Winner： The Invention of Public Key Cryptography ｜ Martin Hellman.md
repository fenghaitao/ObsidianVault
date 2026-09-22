---
title: "summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---
## Core Summary
Martin Hellman recounts how he and Whitfield Diffie invented public key cryptography in the mid-1970s in the face of government opposition, when the NSA argued that publishing cryptographic research in international journals violated ITAR export controls. The first "crypto war" followed a 1977 anonymous NSA letter to the IEEE and was fought over the freedom to publish and over the deliberately short 56-bit DES key size. Hellman explains the mechanics of key exchange and digital signatures, credits Ralph Merkle's independent invention, and reflects on losing the RSA patent war. The conversation then turns to his later work on nuclear risk, where he argues that nuclear weapons — and possibly AI — pose an existential threat to humanity.
## Key Points
- Cryptography (the study of codes and ciphers) barely existed in the open when Hellman began at IBM Research in 1968, where Horst Feistel was starting unclassified research; at MIT (1969–71) Peter Elias gave him Claude Shannon's 1949 paper connecting information theory to cryptography.
- Before public key work, only banks and mining companies encrypted (badly); NSA, GCHQ, and GRU were reading huge volumes of unencrypted traffic.
- In July 1977, a man later identified as an NSA employee wrote from his Maryland home to the IEEE claiming members were breaking the law by publishing papers; the IEEE replied and copied Hellman (as a Board of Governors member of the Information Theory Group).
- NSA's basis was ITAR (International Traffic in Arms Regulations), which classified anything cryptographic as an implement of war; Hellman took the letter to Stanford general counsel John Schwartz, who called the broad reading unconstitutional but said only a court could settle it.
- Hellman and Diffie objected to DES's 56-bit key, estimating around 1975 that a $10,000 machine could exhaustively search it in roughly a day (2^56 ≈ 10^17 keys; a million chips searching a million keys/sec ≈ 80,000–100,000 seconds).
- The first crypto war (late 1970s–early 1980s) was over the freedom to publish internationally and the DES key size; the second (1990s) centered on the Clipper Chip and key escrow; the third (San Bernardino/Apple) was key escrow rebranded as mandatory backdoors.
- Diffie-Hellman key exchange uses a commutative one-way function (modular exponentiation over a finite field): two parties each apply a secret exponent, and the operations commute, so they can agree on a shared key that an eavesdropper cannot derive.
- Hellman frames public key cryptography as the natural next step from the "trapdoor cipher" — a cipher an authorized party can use securely against an adversary who captures it — and grounds trapdoors in P vs NP (problems easy to check but hard to solve).
- Ralph Merkle independently invented the public key distribution half; his CACM submission was rejected before Diffie-Hellman's paper, and Hellman later recruited him to Stanford for his PhD.
- Digital signatures (Whitfield Diffie's contribution) and RSA (Rivest–Shamir–Adleman, the first public key cryptosystem, using mod N) enable authentication and software signing; GCHQ claims to have invented public key cryptography slightly earlier but had nothing on digital signatures.
- Asymmetric cryptography exchanges a key, then a fast symmetric cipher (AES) carries the bulk data; Apple signs only a hash of a software update with a secret key, while phones hold only the public key.
- On patents: Hellman and Diffie's patent was written by a Stanford law school intern and covered only one method, so RSA won the patent war and sold for $250 million while Stanford/Hellman made essentially nothing; Hellman later reconciled with RSA's Jim Bidzos and thinks Ron Rivest may have nominated them for the Turing Award.
- Hellman's later work ("rethinking national security") argues a child born today has worse-than-even odds of living out a natural life because of nuclear weapons alone; he works on HR 3564, a bill limiting sole presidential launch authority (it keeps a launch-on-warning exception to be passable).
- On AI, Hellman notes the split between Geoffrey Hinton/Yoshua Bengio (AI as existential threat) and Ed Feigenbaum/Raj Reddy (calling that ridiculous), while worrying AI is likely to be built into nuclear command and control.
- Personal philosophy: growing up Jewish in an Irish Catholic Bronx neighborhood made him a "street fighter" who was drawn to work others called crazy; his marriage was rescued through the Stanford-founded group Creative Initiative (Harry Rathbun), and he calls himself "a follower of Jesus" while remaining Jewish.
- He attributes near-simultaneous invention (Newton/Leibniz, Darwin/Wallace, Merkle/Diffie-Hellman, Liskov's independent East/West Coast discovery) to a mix of a shared "muse" and the technology simply becoming ready.
## Related
- [[Martin Hellman]] — co-inventor of public key cryptography
- [[Whitfield Diffie]] — co-inventor and collaborator
- [[Ralph Merkle]] — independent inventor of public key distribution
- [[Turing Award]] — the award Hellman won
- [[Stanford University]] — Hellman's institution
- [[NSA]] — the agency that opposed publication
- [[IBM]] — where Hellman first encountered unclassified cryptography
- [[Alan Turing]] — broke the Enigma machine
- [[Claude Shannon]] — linked information theory to cryptography
- [[Public Key Cryptography]] — the central invention
- [[Diffie-Hellman Key Exchange]] — the key exchange algorithm
- [[Digital Signatures]] — authentication half they enabled
- [[RSA]] — the first public key cryptosystem
- [[Data Encryption Standard]] — the 56-bit standard they criticized
- [[Advanced Encryption Standard]] — the modern symmetric cipher
- [[Crypto Wars]] — the conflicts with government
- [[Key Escrow]] — the backdoor debate
- [[Nuclear Risk]] — Hellman's later concern
- [[One-Way Functions]] — the trapdoor basis
- [[P vs NP]] — the hardness question beneath cryptography
