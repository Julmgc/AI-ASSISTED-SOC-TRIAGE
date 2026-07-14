# Human vs AI Comparison

| Alert | AI Classification | Manual Classification | AI Correct? | Notes |
|---|---|---|---|---|
| Alert 01 — Suspicious PowerShell | Needs review | Needs review | Yes | The AI correctly identified suspicious PowerShell flags and suggested a valid PowerShell MITRE mapping. It also avoided assuming malware or compromise. The T1046 mapping was reasonable but should remain low-confidence because the command tested one known internal Splunk port rather than broad service discovery. |
