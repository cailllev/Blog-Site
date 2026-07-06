# DoLLM - Denial of LLM
*Weaponizing vendor compliance for a new type of Denial of Service*

## What
A new kind of theoretical attack, to terminate others LLM licenses.

## Requirements
* an attacker with a malicious input, that is against the vendors ToS
* a hoster with an open LLM prompt
* a vendor that terminates LLM licenses given enough malicious inputs 

## Idea
Now or in the near future some websites may check the users uploads (images, texts, etc.) for compliance. If the user is able to get the LLM to detect malicious input, like prompt injection or "dangerous" prompts, the LLM vendor might block the hoster's license.

## Other Attacks
* Compared to DoS: This is not a traditional resource based DoS, no CPU or bandwith is exhausted.
* Compared to DoW: This is also not an attack against the LLM budget of the hoster.

## Acknowlegements
I heard the idea first at x33fcon 2026, where adding a classical prompt injection into your malware will get analysts' licenses blocked, and also [here](https://www.linkedin.com/posts/malwaretech_the-first-thing-llm-based-malware-analysis-share-7470805192699981826-24Dm/).

## Conclusion
You've heard it here first. KTHXBY
