# Ransomware Detection Rates by modern EDRs
TL;DR: EDRs still suck at detecting malicious PowerShell scripts. Sources see [github.com/cailllev/VT2](https://github.com/cailllev/VT2/blob/main/paper/VT2-EDR-Detection-Bypass.pdf)

## Intro
My project implemented a test framework to boot up a VM, execute a malicious PowerShell script, measure the impact of the script and reset the VM for the next run.

## Method
1. Select and develop malicious script types -> account access removal, data destruction, data encryption, data theft and service stop.
2. Select and develop bypass strategies -> rename variables, escape strings, in-memory (IEX), encoded command (enc), file handles and random delays.
3. Build a framework to boot a VM, execute and measure the impact of the script, and reset the VM.
4. Execute tests and note results.

![framework](/static/ransomware-detection-rate/framework.png)
<cap>The VT2 Framework</cap>

1. start (or reset) the VM
2. check if the service (to run the tests) exists
3. create a clean snapshot (only required once)
4. write the next config to test
5. monitor for a new test run
6. execute the test runner, write true to is-running.txt
7. execute the chosen test
8. check the impact, write the result to res.txt, write false to is-running.txt
9. monitor is-running.txt, get the results when is-running.txt contains false

## Results
The columns display the tested scripts (1). The rows display the bypass strategies (2).
The numbers indicate how many EDRs blocked the attack, out of **4 tested EDRs**.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-q7w7{background-color:#F9CB9C;border-color:#000000;text-align:center;vertical-align:top}
.tg .tg-umej{background-color:#FFE599;border-color:#000000;text-align:center;vertical-align:top}
.tg .tg-f7v4{background-color:#c0c0c0;border-color:#000000;text-align:left;vertical-align:top}
.tg .tg-0l2h{background-color:#EA9999;border-color:#000000;text-align:center;vertical-align:top}
.tg .tg-ezs6{background-color:#B7B7B7;border-color:#000000;text-align:center;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 555px"><colgroup>
<col style="width: 85px">
<col style="width: 68px">
<col style="width: 67px">
<col style="width: 67px">
<col style="width: 67px">
<col style="width: 67px">
<col style="width: 67px">
<col style="width: 67px">
</colgroup>
<thead>
  <tr>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Script &gt;</span><br><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">V Strategy</span></th>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Account </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Access </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Removal</span></th>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Data De</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">struction</span></th>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Data De-</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">struction </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Minimal</span></th>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Data En-</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">cryption</span></th>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Data En-</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">cryption </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">BadWare</span></th>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Data </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Theft</span></th>
    <th class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Service </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">Stop</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">original </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">script</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
  </tr>
  <tr>
    <td class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">renaming </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">variables</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
  </tr>
  <tr>
    <td class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">string </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">escaping</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
  </tr>
  <tr>
    <td class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">in-memory </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">loader</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
  </tr>
  <tr>
    <td class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">encoded </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">command</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-ezs6"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nA</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
  </tr>
  <tr>
    <td class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">open file </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">handles</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
  </tr>
  <tr>
    <td class="tg-f7v4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">random </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000">delays</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-q7w7"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0l2h"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0</span></td>
    <td class="tg-umej"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
  </tr>
</tbody></table>
<!-- generated by https://www.tablesgenerator.com/html_tables, very nice -->
<cap>Results over all EDRs - x out of 4 blocked attacks</cap>

## Conclusion
Jugding maliciousness for an unknown PowerShell script is nearly impossible. Neiter static nor runtime detections protect systems from silly things happening.

