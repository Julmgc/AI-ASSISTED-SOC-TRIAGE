# Alert 06 — Suspicious Outbound Connection

## Manual classification

- **Classification:** needs_review
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- Outbound network connection
- Source host
- Initiating process
- Destination IP address or hostname
- Destination port
- User context
- Available Sysmon or network telemetry

## Analyst reasoning

The alert shows an outbound connection that may be unusual for the initiating process, destination, or port.

An outbound connection is not inherently malicious. Legitimate applications frequently communicate with external services, update servers, cloud providers, content-delivery networks, and internal infrastructure.

The risk depends on whether the destination is expected, whether the initiating process is legitimate, whether the binary is trusted, and whether similar activity normally occurs on the host.

The evidence does not independently confirm command-and-control traffic, malware activity, data exfiltration, or unauthorized remote access.

## MITRE ATT&CK assessment

- **Possible technique:** T1071 — Application Layer Protocol
- **Possible technique:** T1041 — Exfiltration Over C2 Channel
- **Mapping confidence:** low

These mappings should only be retained if the protocol and surrounding evidence support them. A network connection alone is not enough to establish command-and-control or exfiltration.

## Recommended next steps

- Identify and validate the initiating process.
- Check the file path, digital signature, and file hash.
- Investigate the destination IP address or domain.
- Determine whether the destination is expected for the application.
- Review DNS queries associated with the connection.
- Check for repeated or periodic outbound communication.
- Review transferred byte counts where available.
- Correlate the connection with process creation and user activity.

## Final assessment

The connection is potentially suspicious but cannot be classified as malicious without additional process, destination, and environmental context.

- **Final classification:** needs_review
- **Final risk level:** medium
