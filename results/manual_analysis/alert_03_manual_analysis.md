# Alert 03 — Failed Login Burst

## Manual classification

- **Classification:** suspicious
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- Windows Security Event ID `4625`
- 12 failed authentication attempts within 5 minutes
- Target account: `administrator`
- Source IP: `192.168.20.50`
- Logon Type `3` (network logon)
- Internal lab network context
- No successful login reported after the failures

## Manual reasoning

The alert shows 12 failed network logon attempts against the `administrator` account within a five-minute window, all originating from `192.168.20.50`.

The frequency of the failures and the use of a privileged account make the activity suspicious. Possible explanations include password guessing, incorrect credentials, a misconfigured service or script, or authorized testing in the lab.

The available evidence does not show that authentication succeeded or that the account was compromised. Additional context about the source host and surrounding authentication activity would be needed to determine the cause.

A successful login from the same source following the failures would materially change the assessment because it could indicate that the authentication attempts eventually succeeded.

## MITRE ATT&CK assessment

- **Possible technique:** T1110 — Brute Force
- **Possible sub-technique:** T1110.001 — Password Guessing
- **Mapping confidence:** medium

The repeated failures against the same privileged account are consistent with password-guessing behavior.

However, the evidence does not establish intent, and the source is an internal lab address whose role is not identified. The mapping therefore remains provisional.

## Recommended next steps

- Identify the host or user associated with `192.168.20.50`.
- Confirm whether that source is expected to authenticate to `DESKTOP-HRMT55O`.
- Search for additional Event ID `4625` activity from the same source.
- Check for successful logons before or after the failed attempts.
- Review account lockout events involving the `administrator` account.
- Determine whether the activity was part of authorized lab testing or administrative troubleshooting.
- Review nearby authentication and remote-access events on the target host.

## Final assessment

The repeated failed logons against the `administrator` account are suspicious and consistent with possible password-guessing activity.

The evidence does not show successful authentication or account compromise.

- **Final classification:** suspicious
- **Final risk level:** medium
