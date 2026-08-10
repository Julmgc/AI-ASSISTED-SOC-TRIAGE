# Alert 01 — Suspicious PowerShell Execution

## Manual classification

- **Classification:** needs_review
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- PowerShell process execution
- Full command line
- Parent process
- User and host context
- Sysmon process telemetry
- Internal destination `192.168.20.45:9997`

## Manual reasoning

The event shows PowerShell running with `-NoProfile` and `-ExecutionPolicy Bypass` to execute `Test-NetConnection` against the internal address `192.168.20.45` on port `9997`.

The use of `ExecutionPolicy Bypass` makes the command worth examining, but the observed action itself is a connectivity test to an internal Splunk receiver used in the lab.

The available evidence does not establish malware execution, persistence, credential access, lateral movement, or data exfiltration. Additional context would be needed to determine whether the command was expected administrative or lab activity.

## MITRE ATT&CK assessment

- **Possible technique:** T1059.001 — Command and Scripting Interpreter: PowerShell
- **Mapping confidence:** high

The mapping is supported because PowerShell was directly observed executing a command. This describes the observed technique and does not imply malicious intent.

A secondary mapping to `T1046 — Network Service Discovery` would be lower confidence because the evidence shows only a connectivity test to one known internal service.

## Recommended next steps

- Confirm whether the user was expected to test Splunk connectivity.
- Validate that `192.168.20.45:9997` is the intended Splunk receiver.
- Review surrounding PowerShell and process creation events.
- Check available network telemetry for the connection attempt.
- Review the parent process and nearby activity for additional context.

## Final assessment

The event requires context because it combines PowerShell with `ExecutionPolicy Bypass`, but the command itself is consistent with an internal connectivity test.

- **Final classification:** needs_review
- **Final risk level:** medium
