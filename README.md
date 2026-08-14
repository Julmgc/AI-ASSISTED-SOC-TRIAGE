````markdown
# AI-Assisted SOC Triage with Splunk, Sysmon, Python, and OpenAI

This project evaluates how an LLM can support initial security alert triage.

The lab uses **Splunk**, **Sysmon**, **Windows Event Logs**, **Python**, and the **OpenAI API** to process three representative alert scenarios, generate structured assessments, suggest MITRE ATT&CK mappings, and compare the LLM output with a manual review.

The goal is to evaluate where an LLM can help structure alert analysis while keeping conclusions limited to the available evidence.

## Project Overview

The lab follows this workflow:

```text
Windows telemetry
        ↓
Splunk investigation
        ↓
Structured alert JSON
        ↓
Python workflow
        ↓
OpenAI structured assessment
        ↓
Manual review
        ↓
AI vs. manual comparison
```

The LLM is used to:

- summarize available evidence;
- extract relevant observables;
- suggest MITRE ATT&CK mappings;
- identify missing context;
- generate triage questions;
- provide a structured classification and risk level.

The LLM output is then compared with a manual assessment based on the same evidence.

## Tools Used

- **Splunk Enterprise** — SIEM and event investigation
- **Splunk Universal Forwarder** — Windows log forwarding
- **Sysmon** — endpoint telemetry
- **Windows Security Event Logs** — authentication and account-management events
- **Python** — alert parsing and API workflow
- **OpenAI API** — structured LLM assessment
- **MITRE ATT&CK** — technique mapping

## Alert Dataset

The project contains three representative alert scenarios:

| Alert        | Scenario                        | Purpose                                                                                             |
| ------------ | ------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Alert 01** | New local user created          | Test account-creation reasoning when authorization context is missing                               |
| **Alert 02** | Suspicious PowerShell execution | Test whether the model recognizes relevant command-line characteristics without assuming compromise |
| **Alert 03** | Noisy false positive            | Test whether the model avoids treating weak evidence as malicious activity                          |

## Repository Structure

```text
ai-assisted-soc-triage/
├── alerts/
│   ├── alert_01_new_user_created.json
│   ├── alert_02_suspicious_powershell.json
│   └── alert_03_false_positive.json
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

Alert 01 represents the creation of a new local Windows account.

```json
{
  "alert_id": "alert_01",
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

This scenario tests whether the LLM can identify the security relevance of local account creation without assuming compromise when authorization context is unavailable.

## How It Works

The Python workflow:

1. loads an alert JSON file;
2. inserts the available evidence into a structured triage prompt;
3. sends the prompt to the OpenAI API;
4. saves the structured LLM output;
5. compares the result with a manual assessment.

Example:

```bash
python main.py --alert alerts/alert_01_new_user_created.json
```

AI output is saved under:

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

Add your OpenAI API configuration:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.5
```

Do not commit `.env` or API credentials to GitHub.

## Usage

Run Alert 01:

```bash
python main.py --alert alerts/alert_01_new_user_created.json
```

Run Alert 02:

```bash
python main.py --alert alerts/alert_02_suspicious_powershell.json
```

Run Alert 03:

```bash
python main.py --alert alerts/alert_03_false_positive.json
```

Validate an alert JSON file before running it:

```bash
python3 -m json.tool alerts/alert_01_new_user_created.json > /dev/null
```

## Alert 01 — New Local User Created

The scenario uses Windows Security Event ID `4720` and Sysmon process creation telemetry related to the creation of the `lab_backup` account.

The LLM assessment included:

```text
Classification: needs_review
Risk level: medium
MITRE ATT&CK: T1136.001 — Create Account: Local Account
```

The manual assessment reached the same classification and risk level.

The evidence confirmed that a new account had been created but did not establish whether the action was authorized or malicious.

Additional context would be required, such as:

- whether the account creation was approved;
- whether the account was added to a privileged group;
- whether the account was later used to log in;
- whether related suspicious activity occurred on the endpoint.

## Alert 02 — Suspicious PowerShell

The scenario contains a PowerShell execution using:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Test-NetConnection 192.168.20.45 -Port 9997"
```

Both assessments classified the event as:

```text
Classification: needs_review
```

The LLM assigned a `low` risk level, while the manual assessment assigned `medium`.

The difference came from how much weight was given to the combination of `ExecutionPolicy Bypass` and network connectivity activity.

The command was not treated as evidence of compromise on its own.

## Alert 03 — Noisy False Positive

The third scenario uses:

```cmd
cmd.exe /c whoami
```

The command was part of a documented test used to confirm command-execution visibility in Splunk.

Both the LLM and the manual assessment classified the event as:

```text
Classification: benign
Risk level: low
```

The LLM did not treat the use of `cmd.exe` or `whoami` alone as evidence of malicious activity.

## AI vs. Manual Comparison

| Alert                         | AI Classification | AI Risk | Manual Classification | Manual Risk | Comparison        |
| ----------------------------- | ----------------- | ------- | --------------------- | ----------- | ----------------- |
| **Alert 01 — New local user** | Needs review      | Medium  | Needs review          | Medium      | Aligned           |
| **Alert 02 — PowerShell**     | Needs review      | Low     | Needs review          | Medium      | Partially aligned |
| **Alert 03 — False positive** | Benign            | Low     | Benign                | Low         | Aligned           |

The main difference appeared in Alert 02, where the classification was the same but the assigned risk level differed.

## Key Findings

Across the three scenarios, the LLM was useful for:

- summarizing evidence;
- extracting relevant observables;
- identifying missing context;
- generating useful triage questions;
- suggesting MITRE ATT&CK mappings;
- producing consistent structured assessments.

The main limitation was its dependence on the context included in the alert.

Information such as authorization, process relationships, execution results, related events, and expected endpoint behavior can significantly affect the final assessment.

## Skills Demonstrated

This project demonstrates hands-on work with:

- Splunk searches and event investigation;
- Windows Security Event Logs;
- Sysmon process telemetry;
- structured alert analysis;
- Python scripting;
- OpenAI API integration;
- MITRE ATT&CK mapping;
- alert classification;
- false-positive reasoning;
- comparison of LLM output with manual assessment.

## Main Lesson

The LLM was most useful as a tool for structuring the initial review rather than making autonomous security decisions.

Its conclusions were most reliable when they remained limited to the evidence provided.

> **Use AI to structure the analysis, not to replace evidence-based judgment.**
````
