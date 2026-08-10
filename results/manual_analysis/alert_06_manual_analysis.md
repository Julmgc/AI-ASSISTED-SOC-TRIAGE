# Alert 06 — Suspicious Outbound Connection

## Manual classification

- **Classification:** needs_review
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- Sysmon network connection telemetry
- Source host: `DESKTOP-HRMT55O`
- User: `DESKTOP-HRMT55O\jules`
- Initiating process: `powershell.exe`
- Full PowerShell command line
- Destination IP: `203.0.113.50`
- Destination port: `80`
- Requested resource: `/update.txt`
- Destination described as a lab documentation IP
- No evidence that the requested content was saved or executed

## Manual reasoning

The event shows PowerShell making an outbound HTTP request with:

```powershell
Invoke-WebRequest http://203.0.113.50/update.txt
```

The use of PowerShell for an outbound web request is relevant for review, but the available evidence does not establish malicious behavior.

The destination is described as an external documentation IP used for lab testing, and the alert does not show whether the request succeeded, whether a file was written to disk, or whether any downloaded content was executed.

There is also no evidence of command-and-control activity, persistence, credential access, lateral movement, or data exfiltration.

Because the request could represent legitimate lab activity but the full execution context is not available, the evidence supports a `needs_review` classification.

## MITRE ATT&CK assessment

- **Possible technique:** T1059.001 — Command and Scripting Interpreter: PowerShell
- **Mapping confidence:** high

PowerShell was directly observed executing the web request, so this mapping is well supported.

- **Possible technique:** T1105 — Ingress Tool Transfer
- **Mapping confidence:** low

`Invoke-WebRequest` was used to request a remote resource, which could be consistent with file retrieval. However, the available evidence does not confirm that the resource was downloaded, saved, or executed.

## Recommended next steps

- Confirm whether the PowerShell request was part of expected lab activity.
- Review the parent process and surrounding PowerShell process events.
- Determine whether the HTTP request completed successfully.
- Check for file creation associated with `update.txt`.
- Review available network or proxy telemetry for the connection.
- Look for follow-on process or network activity after the request.
- Confirm that `203.0.113.50` was intentionally used in the lab scenario.

## Final assessment

The event shows a PowerShell-initiated HTTP request to an external lab destination, but the available evidence does not confirm malicious activity or follow-on execution.

- **Final classification:** needs_review
- **Final risk level:** medium
