---
title: "Data Encryption Standard"
type: concept
tags: [cryptography, symmetric, standard]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

DES (Data Encryption Standard) is a 1975 symmetric block cipher with a 56-bit key that Martin Hellman and Whitfield Diffie argued was dangerously short.

## Key Information

- Announced in March 1975; the key size was influenced by two NSA people who had moved over to NBS (National Bureau of Standards).
- Hellman and Diffie estimated around 1975–76 that a roughly $10,000 machine could exhaustively search 2^56 ≈ 10^17 keys in about a day (one million chips each searching a million keys per second → roughly 80,000–100,000 seconds).
- The government wanted fewer bits so a publicly available standard would remain breakable by NSA; the short key acted as a "crude form of trapdoor" (NSA had both enough targets and enough money to keep such a machine fully loaded, while ordinary users did not).
- The 56-bit key size became a central flashpoint of the first crypto war.

## Related

- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary
- [[NSA]] — influenced the short key size
- [[Crypto Wars]] — the first war was partly over DES
- [[Advanced Encryption Standard]] — the longer-key successor
- [[Martin Hellman]] — criticized the key size
- [[Whitfield Diffie]] — co-critic
- [[Key Escrow]] — the later regulatory debate
