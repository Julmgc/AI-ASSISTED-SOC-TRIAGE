# Alert 03 — Failed Login Burst

## Manual classification

- **Classification:** suspicious
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- Multiple failed authentication attempts
- Source account or source address
- Target account or host
- Authentication timestamps
- Failure frequency within the observed time window
- Available Windows authentication telemetry

## Analyst reasoning

The alert shows repeated failed authentication attempts within a limited period.

A burst of failed logins may indicate password guessing, brute-force activity, a misconfigured service, an expired password, or a user repeatedly entering incorrect credentials. The behavior is suspicious because of its frequency, but failed logins alone do not prove that an attacker obtained access.

The evidence should be correlated with successful logins, source reputation, account lockouts, affected systems, and the normal behavior of the account.

If a successful authentication followed the failed attempts, the incident severity should be increased.

## MITRE ATT&CK assessment

- **Possible technique:** T1110 — Brute Force
- **Possible sub-technique:** T1110.001 — Password Guessing
- **Mapping confidence:** medium

This mapping is appropriate when the repeated failures represent attempts to guess a password. The evidence may also have a benign explanation, so the mapping should remain provisional until context is reviewed.

## Recommended next steps

- Identify the source IP address or host.
- Determine whether one or multiple accounts were targeted.
- Check whether any successful login followed the failures.
- Review account lockout events.
- Confirm whether the source is an expected internal system.
- Check whether the affected user recently changed a password.
- Review related activity on the target host.
- Block or contain the source if malicious activity is confirmed.

## Final assessment

The failed-login burst is suspicious and should be investigated. The current evidence supports possible password-guessing activity but does not confirm successful access.

- **Final classification:** suspicious
- **Final risk level:** medium
