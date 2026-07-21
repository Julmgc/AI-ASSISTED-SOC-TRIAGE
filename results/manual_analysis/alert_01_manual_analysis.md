# Alert 01 — Suspicious PowerShell Execution

## Manual classification

- **Classification:** needs_review
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- PowerShell process execution
- Command-line arguments associated with the process
- Parent process information
- User and host context
- Available Windows or Sysmon process telemetry

## Analyst reasoning

The alert shows PowerShell executing with characteristics that may be associated with suspicious activity.

PowerShell is a legitimate administrative tool, so its presence alone does not establish malicious behavior. The assessment therefore depends on the command-line arguments, the initiating user, the parent process, and whether the activity was expected in this environment.

The available evidence justifies further investigation, but it does not independently confirm malware execution, credential theft, persistence, lateral movement, or data exfiltration.

The event should not be classified as a confirmed compromise without additional supporting telemetry.

## MITRE ATT&CK assessment

- **Possible technique:** T1059.001 — Command and Scripting Interpreter: PowerShell
- **Mapping confidence:** medium

The mapping is appropriate if the evidence confirms that PowerShell was used to execute commands. However, an ATT&CK mapping describes observed behavior and does not prove malicious intent.

## Recommended next steps

- Review the complete PowerShell command line.
- Identify the parent process that launched PowerShell.
- Determine whether the user normally performs this activity.
- Check for encoded, downloaded, or obfuscated content.
- Review related network connections and child processes.
- Correlate the event with other endpoint alerts.
- Confirm whether the activity was authorized.

## Final assessment

The PowerShell execution is security-relevant and warrants investigation. However, the available evidence is insufficient to classify it as confirmed malicious activity.

- **Final classification:** needs_review
- **Final risk level:** medium
