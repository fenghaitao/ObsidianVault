---
title: "Diffie-Hellman Key Exchange"
type: concept
tags: [cryptography, key-exchange, algorithm]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

Diffie-Hellman key exchange (also called Diffie-Hellman-Merkle key exchange) is a method for two parties to agree on a shared secret over an insecure channel using a commutative one-way function.

## Key Information

- Martin Hellman came up with it in May 1976 and included it in a June 1976 paper presented at the IEEE Symposium on Information Theory in Ronneby, Sweden; it appeared in the November 1976 issue of IEEE Transactions on Information Theory (released February 1977).
- It relies on modular exponentiation over a finite field: raising alpha to X1 then to X2 gives the same result as X2 then X1, so both parties derive alpha^(X1·X2) while an eavesdropper cannot.
- Hellman's "strong box with two locks" analogy: each party adds or removes only their own lock (secret exponent) as the box (message) passes back and forth; it works because the operation is commutative.
- Ralph Merkle's earlier, independent "puzzle" method achieved public key distribution too, but required an eavesdropper to solve about half the puzzles — much more effort than the intended recipient.
- This is key exchange only — it does not provide signatures.

## Related

- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary
- [[Martin Hellman]] — inventor
- [[Whitfield Diffie]] — co-inventor
- [[Ralph Merkle]] — independent puzzle method
- [[Public Key Cryptography]] — the broader field
- [[One-Way Functions]] — the commutative one-way function it uses
- [[RSA]] — the cryptosystem that also provides signatures
