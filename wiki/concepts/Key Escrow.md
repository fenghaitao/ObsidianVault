---
title: "Key Escrow"
type: concept
tags: [cryptography, policy, backdoor]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

Key escrow is a mechanism in which a third party (often the government) retains a copy of encryption keys so it can decrypt with legal authority, at the cost of weakening security.

## Key Information

- Central to the second crypto war (the Clipper Chip) and the third crypto war (San Bernardino/Apple).
- The 1995 National Research Council "CRISIS" committee (formally "Cryptography's Role in Securing the Information Society") concluded it saw no way to solve key escrow's problems — e.g., who holds the keys when parties span France/United States or Russia/United States — and recommended the government experiment with it; the government never returned with a solution.
- Hellman's objection: if Apple could recover one key, it could recover any, and repeated demands plus leakage risk making "all of Apple's devices insecure" — the "keys under doormats" problem.
- He would like to grant access for legitimate government use while withholding it from illegitimate use, but argues there is no technical way to do both selectively.

## Related

- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary
- [[Crypto Wars]] — the second and third wars centered on escrow
- [[Advanced Encryption Standard]] — the encryption whose keys would be escrowed
- [[Digital Signatures]] — the signing keys at issue
- [[NSA]] — the agency seeking access
- [[RSA]] — its co-author Rivest wrote "Keys Under Doormats"
