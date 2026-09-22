---
title: "Digital Signatures"
type: concept
tags: [cryptography, authentication, public-key]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

A digital signature is a way to authenticate a message using a public key cryptosystem, typically by signing a hash with a private key that anyone can verify with the corresponding public key.

## Key Information

- Whitfield Diffie came up with the concept of digital signatures, complementing key exchange (privacy) with authentication.
- In RSA, the public and secret keys "undo one another" regardless of order, so a message signed (encrypted) with the secret key can be verified (decrypted) with the public key.
- Real-world example: Apple signs software updates with a secret key; phones hold only the public key, so someone who extracts the public key from a device still cannot forge future updates.
- In practice only a hash of the message is signed, not the entire message.
- GCHQ's claimed earlier invention of public key cryptography had nothing on digital signatures — only the privacy aspect.

## Related

- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary
- [[Whitfield Diffie]] — came up with the concept
- [[Public Key Cryptography]] — the framework
- [[RSA]] — the first instantiation
- [[Advanced Encryption Standard]] — the bulk cipher used after signing/handshake
- [[Martin Hellman]] — co-inventor of the underlying system
