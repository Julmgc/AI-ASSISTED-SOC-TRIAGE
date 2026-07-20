````markdown
# AI-Assisted SOC Triage with Splunk, Sysmon, Python, and OpenAI

This project evaluates how an LLM can assist with early-stage SOC triage.

The lab uses **Splunk**, **Sysmon**, **Windows Event Logs**, **Python**, and the **OpenAI API** to process SOC-style alerts, generate structured triage analysis, suggest MITRE ATT&CK mappings, and compare AI output against manual analyst validation.

The goal is not to replace analyst judgment. The goal is to test where AI can help analysts move faster while still avoiding unsupported conclusions.

## Project Overview

The workflow follows a realistic SOC triage process:

```text
Windows telemetry / sample alerts
        ↓
Splunk investigation context
        ↓
Alert JSON files
        ↓
Python triage workflow
        ↓
OpenAI structured analysis
        ↓
Manual analyst validation
        ↓
Human vs AI comparison
```
````

The LLM is used as a triage assistant. It summarizes evidence, extracts observables, suggests possible MITRE ATT&CK mappings, generates triage questions, and identifies unsupported assumptions.

The final classification remains with the analyst.

## Tools Used

- **Splunk Enterprise** — SIEM and investigation layer
- **Splunk Universal Forwarder** — Windows log forwarding
- **Sysmon** — endpoint telemetry
- **Windows Security Event Logs** — authentication and account-management events
- **Python** — alert parsing and API workflow
- **OpenAI API** — structured LLM triage output
- **MITRE ATT&CK** — technique mapping and analyst validation

## Alert Dataset

The project includes eight SOC-style alerts:

| Alert    | Scenario                         | Purpose                                                                                     |
| -------- | -------------------------------- | ------------------------------------------------------------------------------------------- |
| Alert 01 | Suspicious PowerShell execution  | Test whether the model identifies suspicious command-line flags without assuming compromise |
| Alert 02 | Benign administrative PowerShell | Test whether the model overclassifies normal admin activity                                 |
| Alert 03 | Failed login burst               | Test authentication and brute-force triage reasoning                                        |
| Alert 04 | SQL injection-style web request  | Test web attack interpretation                                                              |
| Alert 05 | New local user created           | Test account-management and persistence reasoning                                           |
| Alert 06 | Suspicious outbound connection   | Test process and network context analysis                                                   |
| Alert 07 | Encoded PowerShell command       | Test higher-risk endpoint behavior                                                          |
| Alert 08 | Noisy false positive             | Test whether the model can acknowledge weak evidence                                        |

## Repository Structure

```text
ai-assisted-soc-triage/
├── alerts/
│   ├── alert_01_suspicious_powershell.json
│   ├── alert_02_admin_powershell_benign.json
│   ├── alert_03_failed_logins.json
│   ├── alert_04_sqli_web_attack.json
│   ├── alert_05_new_user_created.json
│   ├── alert_06_suspicious_outbound_connection.json
│   ├── alert_07_encoded_powershell.json
│   └── alert_08_false_positive.json
│
├── prompts/
│   └── triage_prompt_v1.md
│
├── results/
│   ├── ai_outputs/
│   ├── manual_analysis/
│   └── comparison_table.md
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Example Alert

Example: Alert 05 — New local user created.

```json
{
  "alert_id": "alert_05",
  "source": "Windows Security Event Log collected in Splunk",
  "event": {
    "event_type": "User Created",
    "windows_event_code": 4720,
    "actor_user": "DESKTOP-HRMT55O\\jules",
    "target_user": "lab_backup",
    "command_line": "net user lab_backup P@ssw0rd123 /add"
  },
  "detection": {
    "rule_name": "New local user account created",
    "severity": "medium"
  }
}
```

This alert tests whether the LLM can identify possible persistence behavior without assuming compromise when authorization context is missing.

## How It Works

The Python script:

1. Loads an alert JSON file.
2. Inserts the alert context into a structured SOC triage prompt.
3. Sends the prompt to the OpenAI API.
4. Saves the AI-generated triage output.
5. Allows comparison against manual analyst notes.

Example command:

```bash
python main.py --alert alerts/alert_05_new_user_created.json
```

Output is saved to:

```text
results/ai_outputs/
```

## Setup

Clone the repository:

```bash
git clone https://github.com/Julmgc/AI-ASSISTED-SOC-TRIAGE.git
cd AI-ASSISTED-SOC-TRIAGE
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```bash
cp .env.example .env
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.5
```

Do not commit `.env` to GitHub.

## Usage

Run triage for one alert:

```bash
python main.py --alert alerts/alert_01_suspicious_powershell.json
```

Run another alert:

```bash
python main.py --alert alerts/alert_05_new_user_created.json
```

Validate JSON files before running:

```bash
python3 -m json.tool alerts/alert_05_new_user_created.json > /dev/null
```

## Example AI Output

For the new local user alert, the LLM should identify:

```text
Risk level: medium
Classification: suspicious or needs_review
Possible MITRE mapping: T1136.001 — Create Account: Local Account
```

The important part is whether the model avoids unsupported assumptions.

A good triage output should not claim:

- confirmed compromise
- malware execution
- lateral movement
- credential theft
- exfiltration

unless those facts are present in the evidence.

## Manual Analyst Validation

Each AI output is manually reviewed using the same evidence.

The manual review checks:

- Was the classification supported?
- Was the MITRE mapping appropriate?
- Did the model overclassify the alert?
- Did the model invent attacker intent or impact?
- Did it ask useful triage questions?
- Did it identify missing context?

Example manual assessment:

```text
Alert 05: New local user created

Manual classification: needs_review
Risk level: medium

Reasoning:
A new local user account can indicate persistence, but the alert does not prove compromise by itself. There is no evidence that the account was added to the local Administrators group, used for lateral movement, or tied to malware execution. Additional context is required.
```

## Human vs AI Comparison

The project compares AI classifications against manual analyst validation.

| Alert                          | AI Classification | Manual Classification   | Result            |
| ------------------------------ | ----------------- | ----------------------- | ----------------- |
| Suspicious PowerShell          | Needs review      | Needs review            | Correct           |
| Benign admin PowerShell        | Suspicious        | Benign / Needs review   | Partially correct |
| Failed login burst             | Suspicious        | Suspicious              | Correct           |
| SQL injection-style request    | Suspicious        | Suspicious              | Correct           |
| New local user created         | Suspicious        | Needs review            | Partially correct |
| Suspicious outbound connection | Needs review      | Needs review            | Correct           |
| Encoded PowerShell             | Suspicious        | Suspicious              | Correct           |
| Noisy false positive           | Suspicious        | Benign / False positive | Incorrect         |

## Key Findings

The LLM was useful for:

- summarizing noisy alert data
- extracting key observables
- suggesting triage questions
- producing consistent first-pass notes
- suggesting possible MITRE ATT&CK mappings

The LLM was risky when:

- evidence was weak or ambiguous
- suspicious behavior also had a legitimate explanation
- environmental context was missing
- MITRE mappings were plausible but not fully supported

## Skills Demonstrated

This project demonstrates:

- SOC triage methodology
- Splunk search and investigation
- Windows telemetry analysis
- Sysmon and Windows Event Log interpretation
- Python scripting
- OpenAI API integration
- MITRE ATT&CK mapping
- alert classification
- false-positive reasoning
- human validation of AI-generated security analysis

## Main Lesson

AI can help with first-pass SOC triage, but it should not be treated as the final decision-maker.

The safest role for an LLM in this workflow is:

> Assist the analyst, but do not replace analyst judgment.
