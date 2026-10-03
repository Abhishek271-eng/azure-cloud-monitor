import json
from pathlib import Path

from app.monitor import evaluate_metrics
from app.report import save_report


BASE_DIR = Path(__file__).resolve().parent.parent


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    thresholds = load_json(
        BASE_DIR / "config" / "thresholds.json"
    )

    metrics = load_json(
        BASE_DIR / "data" / "sample_metrics.json"
    )

    results = []

    for resource in metrics:
        result = evaluate_metrics(resource, thresholds)
        results.append(result)

        print(
            f"{result['resource']}: "
            f"{result['status']}"
        )

    save_report(results)


if __name__ == "__main__":
    main()