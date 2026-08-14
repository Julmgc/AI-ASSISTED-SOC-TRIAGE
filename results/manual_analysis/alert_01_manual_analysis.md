# Alert 01 — New Local User Created

## Manual classification

- **Classification:** needs_review
- **Risk level:** medium
- **Confidence:** high

## Evidence reviewed

- Windows Security Event ID `4720`
- Actor account: `DESKTOP-HRMT55O\jules`
- Target account: `lab_backup`
- Sysmon Event ID `1`
- Process images: `net.exe` and `net1.exe`
- Parent process: `powershell.exe`
- Command line used to create the local account
- Account not reported as added to the local Administrators group
- No change ticket or known administrative context provided

## Manual reasoning

Windows Security Event ID `4720` confirms that a new local account named `lab_backup` was created on the endpoint.

Sysmon Event ID `1` adds process context, showing PowerShell launching `net.exe`, which then invoked `net1.exe` with the command used to create the account.

Local account creation can be legitimate administrative activity, but it can also be associated with persistence when performed without authorization.

The available evidence confirms the account-creation action but does not establish whether it was expected or approved. The account was not reported as added to the local Administrators group, and there is no evidence of subsequent login activity, malware execution, credential access, lateral movement, or data exfiltration.

Because the authorization context is missing, the evidence supports a `needs_review` classification rather than a benign or malicious conclusion.

## MITRE ATT&CK assessment

- **Technique:** T1136.001 — Create Account: Local Account
- **Mapping confidence:** high

The mapping is directly supported by the observed creation of a local Windows account.

The ATT&CK mapping describes the behavior that occurred, but it does not establish whether the action was malicious.

## Recommended next steps

- Confirm whether the creation of `lab_backup` was authorized.
- Check for an approved change record, administrative request, or lab instruction.
- Review the account's local group memberships.
- Search for subsequent logons using `lab_backup`.
- Review nearby account-management events for additional changes.
- Determine whether the account was later modified, enabled, disabled, or deleted.
- Review surrounding process activity for additional context.
- If the account was not authorized, disable or remove it according to the applicable procedure.

## Final assessment

The evidence confirms that `lab_backup` was created as a local account, but it does not establish whether the action was authorized or malicious.

- **Final classification:** needs_review
- **Final risk level:** medium
