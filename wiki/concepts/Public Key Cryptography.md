---
title: "Public Key Cryptography"
type: concept
tags: [cryptography, public-key, key-exchange]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

Public key cryptography (asymmetric cryptography) uses two keys — a public key and a private (secret) key — so parties can communicate or sign messages without first sharing a secret key.

## Key Information

- Publicly invented in the mid-1970s by Martin Hellman and Whitfield Diffie, with Ralph Merkle independently contributing the key-distribution half; GCHQ claims to have invented it slightly earlier in secret but with nothing on digital signatures.
- Emerged logically from the "trapdoor cipher" — a cipher an authorized party could use securely even against an adversary who captures it — which Hellman calls "a general's dream."
- Before it, communicating securely required shared secret keys distributed by courier, workable only for militaries/banks, not for arbitrary clients over networks.
- Enables both key exchange (Diffie-Hellman) and digital signatures/RSA.
- In modern systems, asymmetric key exchange is used only at the start to establish a symmetric session key (e.g., AES), because public key cryptography is too slow for bulk data.

## Related

- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary
- [[Martin Hellman]] — co-inventor
- [[Whitfield Diffie]] — co-inventor
- [[Ralph Merkle]] — independent contributor
- [[Diffie-Hellman Key Exchange]] — the key exchange it enables
- [[Digital Signatures]] — the authentication it enables
- [[RSA]] — the first public key cryptosystem
- [[One-Way Functions]] — the trapdoor basis
- [[P vs NP]] — the hardness question beneath it
- [[Crypto Wars]] — the government opposition it provoked
- [[Advanced Encryption Standard]] — the symmetric cipher used after key exchange
