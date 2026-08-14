# Alert 03 — Noisy False Positive

## Manual classification

- **Classification:** benign
- **Risk level:** low
- **Confidence:** high

## Evidence reviewed

- Sysmon Event ID `1`
- Process: `cmd.exe`
- Command line: `cmd.exe /c whoami`
- Parent process: `explorer.exe`
- User: `DESKTOP-HRMT55O\jules`
- Host: `DESKTOP-HRMT55O`
- Detection severity: low
- Known lab activity: manual testing of command execution visibility in Splunk
- No additional suspicious indicators provided

## Manual reasoning

The event shows `cmd.exe` launched from `explorer.exe` to execute:

```cmd
whoami
```

The command only returns the current user context. The provided lab context states that `jules` was manually testing command execution visibility in Splunk.

There is no evidence of unauthorized access, malware execution, persistence, credential access, lateral movement, command-and-control activity, or data exfiltration.

Because both the command and the surrounding context are consistent with the documented lab activity, the event is best classified as benign.

## MITRE ATT&CK assessment

- **Possible technique:** T1059.003 — Windows Command Shell
- **Mapping confidence:** medium

The mapping describes the use of `cmd.exe`, but in this case the execution is consistent with benign lab activity.

- **Possible technique:** T1033 — System Owner/User Discovery
- **Mapping confidence:** medium

The `whoami` command retrieves the current user identity, which corresponds to user discovery behavior. However, the available context does not support malicious intent.

## Recommended next steps

- Confirm that the command was part of the documented Splunk visibility test.
- Review nearby process events only if additional context is required.
- If confirmed, document the event as benign lab activity.
- Consider whether the detection should be tuned to reduce noise from known test activity.

## Detection-tuning notes

A detection based only on `cmd.exe` or `whoami` can generate low-value alerts because both are commonly used in legitimate administration and testing.

Potential tuning could include:

- requiring additional suspicious command-line indicators;
- considering unusual parent-child process relationships;
- correlating the command with other suspicious activity;
- adding narrowly scoped exclusions for documented lab testing.

Any exclusion should remain specific enough to avoid suppressing meaningful command-shell activity.

## Final assessment

The event is consistent with documented lab testing and does not contain supporting evidence of malicious behavior.

- **Final classification:** benign
- **Final risk level:** low
