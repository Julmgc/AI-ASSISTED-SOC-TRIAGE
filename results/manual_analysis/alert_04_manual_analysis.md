# Alert 04 — SQL Injection-Style Web Request

## Manual classification

- **Classification:** suspicious
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- HTTP `GET` request
- Target host: `WEB-LAB-01`
- Source IP: `192.168.20.60`
- Request URI: `/products?id=1' OR '1'='1`
- HTTP status code: `400`
- Request marked as blocked
- No evidence of successful exploitation
- Lab web application context

## Manual reasoning

The request contains the SQL injection-style expression:

```text
/products?id=1' OR '1'='1
```

The payload is consistent with an attempt to manipulate a SQL query through a web parameter, which makes the activity suspicious.

However, the request returned HTTP `400`, was marked as blocked, and the available evidence does not show that the payload was successfully processed by the application or database.

The activity could represent unauthorized probing, automated scanning, authorized security testing, or other lab activity. Additional context about the source and surrounding web requests would be needed to determine its purpose.

## MITRE ATT&CK assessment

- **Possible technique:** T1190 — Exploit Public-Facing Application
- **Mapping confidence:** medium

The mapping is reasonable because the request contains an injection-style payload targeting a web application.

However, the evidence supports an attempted interaction with the application rather than confirmed exploitation. There is no evidence of successful database access, code execution, or data exposure.

## Recommended next steps

- Identify the system or user associated with `192.168.20.60`.
- Confirm whether the source was performing authorized lab or security testing.
- Search for additional requests from the same source.
- Check whether similar payloads received successful HTTP responses.
- Review application logs for errors or unusual behavior around the event.
- Review available database logs for related activity.
- Verify that the blocking control behaved as expected.

## Final assessment

The request is suspicious because it contains a recognizable SQL injection-style payload.

The available evidence shows that the request was blocked and does not confirm successful exploitation.

- **Final classification:** suspicious
- **Final risk level:** medium
