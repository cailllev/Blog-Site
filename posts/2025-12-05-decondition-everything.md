# Decondition Everything
## Alternate Titles
* Cross-Process Deconditioning
* Reversing Defenders Behavioural Engine
* Bypass Every EDR if you find the correct Rule
* This is why your malware gets detected

## Acknowlegdements
The following theory and pseudo-code is based on my and [Dobins](https://blog.deeb.ch) experience and exchange on the matter.

## Related Work
If you don't know what a behavioural engine or behavioural tracking is, have a look at [Detection Engines](/posts/2025-12-05-defender-detection-engines) first.<br>
If you do not believe the results, see [Temporal Detections](/post/2025-12-02-defender-temporal-detections) where the observations stem from.<br>

## My Work
### Remarks
1. A.exe and A'.exe are lsass dumpers.
2. A.exe and A'.exe are compiled at the same time, same machine, same import function, and share most of their code.
3. EDRs have some "process identification" mechanism. This might be `hash(code_section)`, `imphash(x.exe)` or `metadata(x.exe)`. This allows to store only the identifier for lookups.

### Definitions
1. Let's call this process identification `PI(x.exe)`, for now it does not matter how it works exactly.

### Observations
1. A.exe is executed, it does some deconditioning (dump 20 other procs), then A.exe dumps lsass. -> <b>undetected</b> -> expected
2. A'.exe is executed, directly dumps lsass. -> <b>UNDETECTED</b> -> unexpected!
3. <i>Wait some time (~1h), or let A'.exe raise a non-behaviour alert (i.e. signature, memory, ..., does not matter how).</i>
4. A'.exe is executed again, directly dumps lsass. -> <b>detected</b> -> expected
5. A.exe is executed again, deconditioning, then dumps lsass.exe -> <b>DETECTED</b> -> unexpected!

### Lemmas
1. From the remarks it follows that `A.exe != A'.exe`
2. But from observations it follows that `PI(A.exe) == PI(A'.exe)`

### Claims
1. Defender has a cutoff for tracking behaviours, like process dumping (else observation 1 would not dump lsass)
2. Defender uses a form of process identification (else observation 2 would not match result in observation 1, and 5 not 4)

## New Behavior Tracking Theory
This is pseudo-code and based only on the above.
```python
class Rule:
    name: str      # lsass-dump
    input: [event] # open_proc, open_file
    trigger: func  # proc == lsass

anti_lsass_dump = Rule("lsass-dump", [event.open_proc, event.open_file], event.target_proc == lsass)
...

rules = [anti_lass_dump, ...]
cache = {} # caching of all processed events (detection results) for performance increase

def get_rules_based_on_event(event):
    return filter(rules: if r.input == event.type)

def PI(process):
    return imphash(process.code) # or metadata(process.file) or hash(process.code)

def behaviour_handler(event):
    process_identity = PI(event.process)

    # which behaviour rules are subscribed to this event, e.g. event open process -> lsass-dump
    rules = get_rules_based_on_event(event)
    for r.name, r.trigger:
        if cache[r.name][process_identity] == -1: # previously detected
            return true # ALERT!

        elif cache[r.name][process_identity]++ < cutoff:
            detection = r.trigger(event)
            if detection:
                cache[r.name][process_identity] = -1 # store as known bad
                return true # ALERT!

# example, "A.exe" opens a proc, but non malicious
a_pi = PI("a.exe")
cache = {
    anti_lsass_dump: {
        a_pi: 1
    }
}
# repeat 10x
cache = {
    anti_lsass_dump: {
        a_pi: 10
    }
}
# now (speculated) cutoff is reached, anti_lsass_dump on a_pi will always return non malicious
```

## Conclusions
1. If your malware is detected when doing X, find the associated rule and decondition it
2. ??
3. ??
4. Profit

## Further Research
* Do the cache cutoffs depend on [rule] and [process_identity], or only on rule? It should depend on both, else A.exe can decondition the EDR, and EVERY proc on the system is now whitelisted for proc dumping.
* Can the exact PI function be found? Is it really imphash? 
* Find more rules besides this `anti_lsass_dump` and [C2 Loaders (SirAllocALot)](https://github.com/dobin/SuperMega?tab=readme-ov-file#anti-emulation) 
