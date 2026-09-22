---
title: "Advanced Encryption Standard"
type: concept
tags: [cryptography, symmetric, standard]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

AES (Advanced Encryption Standard) is a modern symmetric encryption standard with a minimum 128-bit key size, dramatically larger than DES's 56-bit key.

## Key Information

- Martin Hellman contrasts AES's ≥128-bit key with DES's 56-bit key: 2^128 is vastly larger than 2^56, making exhaustive search infeasible.
- In modern hybrid systems, public key cryptography is used only to establish/exchange a symmetric key, and AES then carries the bulk traffic quickly (public key cryptography is too slow for that).
- Example: Apple signs only a hash of a software update, then the actual update can be delivered/encrypted fast with a symmetric cipher like AES.

## Related

- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary
- [[Data Encryption Standard]] — the 56-bit predecessor it replaced
- [[Public Key Cryptography]] — used together in hybrid systems
- [[Diffie-Hellman Key Exchange]] — establishes the AES session key
- [[Digital Signatures]] — signs hashes before bulk use
- [[Key Escrow]] — the debate over government access to such keys
