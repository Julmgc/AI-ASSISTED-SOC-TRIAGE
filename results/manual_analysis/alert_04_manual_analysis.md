# Alert 04 — SQL Injection-Style Web Request

## Manual classification

- **Classification:** suspicious
- **Risk level:** medium
- **Confidence:** medium

## Evidence reviewed

- HTTP request data
- Request path and query parameters
- SQL injection-style characters or expressions
- Source address
- Destination web application
- Available response or application context

## Analyst reasoning

The request contains syntax commonly associated with SQL injection testing or exploitation.

Examples may include SQL operators, quotation marks, comments, boolean conditions, or encoded payload fragments. This makes the request suspicious, but the request alone does not demonstrate that the application was vulnerable or that the attempted injection succeeded.

The activity may represent malicious probing, an automated vulnerability scanner, security testing, or malformed benign input. Confirmation requires application logs, database activity, server responses, and authorization context.

## MITRE ATT&CK assessment

- **Possible technique:** T1190 — Exploit Public-Facing Application
- **Mapping confidence:** medium

This mapping is appropriate if the request represents an attempt to exploit a web application. It should not be treated as a confirmed exploitation event without evidence that the application processed the payload successfully.

## Recommended next steps

- Review the complete request and decoded parameters.
- Check the HTTP response status and response body.
- Identify whether the source was an authorized scanner.
- Search for additional requests from the same source.
- Review web application and database logs.
- Check for database errors or unexpected queries.
- Verify whether the targeted parameter is properly sanitized.
- Block the source if the activity is confirmed as unauthorized and malicious.

## Final assessment

The request is consistent with an SQL injection attempt and should be investigated. The evidence supports suspicious web activity but does not confirm successful exploitation.

- **Final classification:** suspicious
- **Final risk level:** medium
