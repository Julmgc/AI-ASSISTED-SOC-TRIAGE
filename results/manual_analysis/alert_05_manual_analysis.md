# Alert 05 — New Local User Created

## Manual classification

- **Classification:** needs_review
- **Risk level:** medium
- **Confidence:** high

## Evidence reviewed

- Windows Security Event ID 4720
- Actor account: `DESKTOP-HRMT55O\jules`
- Target account: `lab_backup`
- Sysmon Event ID 1 process telemetry
- Process images: `net.exe` and `net1.exe`
- Parent process: `powershell.exe`
- Command line used to add the local account

## Analyst reasoning

A new local user account named `lab_backup` was created on the Windows endpoint.

Windows Security Event ID 4720 confirms that the account-creation action occurred. Sysmon Event ID 1 provides additional process context, showing PowerShell launching `net.exe`, which then invoked `net1.exe` with the command used to add the account.

Local account creation can be legitimate administrative activity. It can also be associated with persistence when an account is created without authorization.

The available evidence confirms the activity but does not establish whether it was approved. There is no evidence in the alert that the account was added to the local Administrators group. There is also no evidence of subsequent login activity, malware execution, credential theft, lateral movement, or data exfiltration.

Because authorization cannot be determined from the available telemetry, the event requires analyst review.

## MITRE ATT&CK assessment

- **Technique:** T1136.001 — Create Account: Local Account
- **Mapping confidence:** high

The mapping is supported because the telemetry confirms the creation of a local Windows account. The mapping describes the observed behavior but does not by itself establish malicious intent.

## Recommended next steps

- Confirm whether the account creation was authorized.
- Check for a related change ticket or administrative request.
- Review the account’s local group membership.
- Determine whether the account was later enabled, modified, or deleted.
- Search for successful logins using `lab_backup`.
- Review subsequent processes and network activity associated with the account.
- Disable or remove the account if it was created without authorization.

## Final assessment

The account creation is security-relevant and requires validation. The evidence confirms that the account was created, but it does not prove that the action was malicious.

- **Final classification:** needs_review
- **Final risk level:** medium
