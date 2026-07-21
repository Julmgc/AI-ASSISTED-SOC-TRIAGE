# Alert 07 — Encoded PowerShell Command

## Manual classification

- **Classification:** suspicious
- **Risk level:** high
- **Confidence:** medium to high

## Evidence reviewed

- PowerShell process execution
- Encoded or obfuscated command-line content
- PowerShell command-line flags
- Parent process
- User and host context
- Available Sysmon process telemetry

## Analyst reasoning

The alert shows PowerShell executing an encoded or obfuscated command.

Encoded PowerShell is security-relevant because attackers frequently use encoding to conceal command content, bypass simple detections, or make analysis more difficult. However, encoding can also be used by legitimate scripts, deployment tools, and administrative automation.

The presence of an encoded command materially increases the risk compared with ordinary PowerShell execution. The payload should be decoded and reviewed before a final determination is made.

Without decoding the content, it is not possible to determine precisely what actions were attempted or whether the execution resulted in compromise.

## MITRE ATT&CK assessment

- **Technique:** T1059.001 — Command and Scripting Interpreter: PowerShell
- **Possible technique:** T1027 — Obfuscated Files or Information
- **Mapping confidence:** high for PowerShell
- **Mapping confidence:** medium to high for obfuscation

The PowerShell mapping is directly supported by the process telemetry. The obfuscation mapping is supported if the command uses encoding to conceal its content.

## Recommended next steps

- Preserve the original encoded command.
- Decode the payload in a safe analysis environment.
- Review the decoded content for downloads, persistence, credential access, or execution.
- Identify the parent process and initiating user.
- Check whether the command was part of an approved script or deployment.
- Review child processes and network connections.
- Search for the same encoded command across other hosts.
- Isolate the endpoint if the decoded payload is malicious.

## Final assessment

Encoded PowerShell activity is strongly suspicious and warrants immediate investigation. A final malicious classification depends on the decoded command and surrounding telemetry.

- **Final classification:** suspicious
- **Final risk level:** high
