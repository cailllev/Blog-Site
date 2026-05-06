# EDRs' Impossible Job

## Theory
EDRs should not block everything that looks or acts like malware, as this will block a considerable part of legitimate software, but only blocking known malware is a bad idea too. A balance must be found between not blocking most legitimate software and still trying to catch every possible malware. 

## Impact
This however means that some malware is classified as legit software, when it is "similar" enough to legit software.

## Visualized
The diagram below illustrates this dilemma. The xs represent the effectively unknown border between software and malware. The horizontal lines display possible strategies for EDR developers. Choosing the right line means correctly classifying all legit software as legit software, but also wrongly classifying some malware as legit software, represented by the dots. Choosing the left line means correctly classifying all malware as malware, but wrongly classifying some legit software as malware, represented by the minuses. As classifying legit software as malware has too much impact on stability and reliability of systems, EDR developers usually choose a strategy close to the first approach. 
```text
┌──────────────────────────────────┐
│              │x...│              │
│ legit         -x..   malware     │
│ software     │--x.│              │
│               ---x               │
│              │--x.│              │
│               -x..               │
│              │--x.│              │
└──────────────────────────────────┘
```
