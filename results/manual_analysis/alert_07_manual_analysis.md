# Alert 07 — Encoded PowerShell Command

## Manual classification

- **Classification:** needs_review
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- Sysmon Event ID `1`
- PowerShell process execution
- Parent process: `cmd.exe`
- User: `DESKTOP-HRMT55O\jules`
- Command-line flags:
  - `-NoProfile`
  - `-ExecutionPolicy Bypass`
  - `-EncodedCommand`
- Encoded command value
- No decoded payload provided
- No execution result provided

## Manual reasoning

The event shows PowerShell launched from `cmd.exe` with both `-ExecutionPolicy Bypass` and `-EncodedCommand`.

The use of an encoded PowerShell command is security-relevant because encoding can obscure the underlying command content. However, encoded commands can also appear in legitimate automation, administrative scripts, installers, and controlled lab activity.

The available evidence does not include the decoded payload or the result of the execution. Because of that, it is not possible to determine whether the command performed a malicious action.

There is also no evidence in the alert of persistence, credential access, lateral movement, malware execution, or data exfiltration.

The event therefore requires additional context and payload review before it can be classified as benign or malicious.

## MITRE ATT&CK assessment

- **Technique:** T1059.001 — Command and Scripting Interpreter: PowerShell
- **Mapping confidence:** high

The PowerShell mapping is directly supported by the process telemetry.

- **Possible technique:** T1027 — Obfuscated Files or Information
- **Mapping confidence:** medium

The use of `-EncodedCommand` supports an obfuscation-related mapping, but the decoded content is not available in the evidence. The mapping should therefore remain tentative.

## Recommended next steps

- Preserve the original encoded command.
- Decode and review the payload in a safe analysis workflow.
- Review the parent process and surrounding process tree.
- Check for child processes, file creation, registry changes, or network connections associated with the PowerShell process.
- Review available PowerShell logs for additional command or script content.
- Confirm whether the activity was expected in the lab.
- Escalate only if the decoded payload or follow-on telemetry shows malicious behavior.

## Final assessment

The combination of `-ExecutionPolicy Bypass` and `-EncodedCommand` makes the event security-relevant, but the available evidence does not establish malicious execution.

- **Final classification:** needs_review
- **Final risk level:** medium
