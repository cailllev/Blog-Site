# My approach to Ace GIAC exams

1. Choose a SANS course that really interests you, I can only learn for stuff that I find interesting.
2. Attend the course and write minimal notes when the instructor summarises a page or explains the implications.
3. Re-read the book, highlight key words / phrases, stuff that you want to see when searching for it at exam date.
4. Also during the re-read, create your index with key words, about one key word per 3 pages for me.
5. Take a practice exam, if you are content with the result (min. 80%), you are done learning.

## Example 1 - NTLM Login Flow
Highlight important words like "nonce", "challenge", "signed", etc. and create the index entry.
Also, maybe the instructor mentioned Responder / Coerced Auth at this page and you created a small note. This might help too.

| Topic | Keyword | Page |
| --- | --- | --- |
| Lateral Movement | NTLM Login Flow | 3-42 |
<cap>Example 1</cap>

## Example 2 - Skeleton Key Attack
Highlight important words like "misc::skeleton", "must be done on all DCs", "one pw for all accounts"

| Topic | Keyword | Page |
| --- | --- | --- |
| Lateral Movement | NTLM Login Flow | 3-42 |
| Persistence | Skeleton Key Attack | 4-99|
<cap>Example 2</cap>

## Create the actual printed Index
Assuming we have a finished pre-index like this:

| Topic | Keyword | Page |
| --- | --- | --- |
| Lateral Movement | NTLM Login Flow | 3-42 |
| Lateral Movement | Coerced Auth Responder | 3-44 |
| Persistence | LSASS Dump | 4-87 |
| Persistence | LSA Protection | 4-95 |
| Persistence | Skeleton Key Attack | 4-99 |
<cap>Finished Pre-Index after reading all books</cap>

Then I create one index to sorted by topic, then keyword, and one index sorted by keyword only, like this:

### Topic Sorted
| Lateral Movement | Page |
| --- | --- |
| Coerced Auth Responder | 3-44 |
| NTLM Login Flow | 3-42 |
<cap>Index for topic Lateral Movement</cap>

| Persistence | Page |
| --- | --- |
| LSA Protection | 4-95 |
| LSASS Dump | 4-87 |
| Skeleton Key Attack | 4-99 |
<cap>Index for topic Persistence</cap>

### Keyword Sorted
| Keyword | Page |
| --- | --- |
| Coerced Auth Responder | 3-44 |
| LSA Protection | 4-95 |
| LSASS Dump | 4-87 |
| NTLM Login Flow | 3-42 |
| Skeleton Key Attack | 4-99 |
<cap>Index over all keywords - sorted only by Keyword</cap>

## Results
<div style="display:flex; gap:20px;">
  <img src="/static/sans/gcfa.png" alt="GCFA">
  <img src="/static/sans/gdat.png" alt="GDAT">
</div>
