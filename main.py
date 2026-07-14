import argparse
import json
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent
PROMPT_PATH = BASE_DIR / "prompts" / "triage_prompt_v1.md"
OUTPUT_DIR = BASE_DIR / "results" / "ai_outputs"


def load_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Alert file not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_prompt(prompt_template: str, alert_data: dict) -> str:
    alert_json = json.dumps(alert_data, indent=2)
    return prompt_template.replace("{{ALERT_JSON}}", alert_json)


def run_triage(alert_path: Path) -> dict:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-5.5")

    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is missing. Add it to your .env file.")

    client = OpenAI(api_key=api_key)

    alert_data = load_json(alert_path)
    prompt_template = load_text(PROMPT_PATH)
    prompt = build_prompt(prompt_template, alert_data)

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    output_text = response.output_text

    result = {
        "alert_file": str(alert_path),
        "model": model,
        "generated_at": datetime.now().isoformat(),
        "ai_output": output_text,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    alert_id = alert_data.get("alert_id", alert_path.stem)
    output_path = OUTPUT_DIR / f"{alert_id}_ai_triage.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)

    print(f"[+] AI triage saved to: {output_path}")
    print()
    print(output_text)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Run LLM-assisted SOC triage for one alert."
    )
    parser.add_argument(
        "--alert",
        required=True,
        help="Path to the alert JSON file."
    )
    args = parser.parse_args()

    alert_path = Path(args.alert)
    run_triage(alert_path)


if __name__ == "__main__":
    main()
