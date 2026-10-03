import json
import time
from pathlib import Path

from app.monitor import evaluate_metrics
from app.report import save_report


BASE_DIR = Path(__file__).resolve().parent.parent


def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"ERROR: File not found - {file_path}")
        raise

    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON file - {file_path}")
        raise


def get_simulated_metrics(cycle):
    scenarios = [
        [
            {
                "resource": "web-server-01",
                "cpu": 45,
                "disk": 50,
                "availability": True
            },
            {
                "resource": "web-server-02",
                "cpu": 60,
                "disk": 65,
                "availability": True
            },
            {
                "resource": "web-server-03",
                "cpu": 75,
                "disk": 80,
                "availability": True
            },
            {
                "resource": "web-server-04",
                "cpu": 40,
                "disk": 40,
                "availability": True
            }
        ],

        [
            {
                "resource": "web-server-01",
                "cpu": 72,
                "disk": 50,
                "availability": True
            },
            {
                "resource": "web-server-02",
                "cpu": 65,
                "disk": 78,
                "availability": True
            },
            {
                "resource": "web-server-03",
                "cpu": 82,
                "disk": 85,
                "availability": True
            },
            {
                "resource": "web-server-04",
                "cpu": 40,
                "disk": 40,
                "availability": False
            }
        ],

        [
            {
                "resource": "web-server-01",
                "cpu": 91,
                "disk": 50,
                "availability": True
            },
            {
                "resource": "web-server-02",
                "cpu": 60,
                "disk": 92,
                "availability": True
            },
            {
                "resource": "web-server-03",
                "cpu": 95,
                "disk": 94,
                "availability": True
            },
            {
                "resource": "web-server-04",
                "cpu": 40,
                "disk": 40,
                "availability": False
            }
        ],

        [
            {
                "resource": "web-server-01",
                "cpu": 55,
                "disk": 55,
                "availability": True
            },
            {
                "resource": "web-server-02",
                "cpu": 50,
                "disk": 60,
                "availability": True
            },
            {
                "resource": "web-server-03",
                "cpu": 65,
                "disk": 70,
                "availability": True
            },
            {
                "resource": "web-server-04",
                "cpu": 45,
                "disk": 50,
                "availability": True
            }
        ]
    ]

    return scenarios[cycle % len(scenarios)]


def main():
    cycle = 0

    while True:
        try:
            thresholds = load_json(
                BASE_DIR / "config" / "thresholds.json"
            )

            metrics = get_simulated_metrics(cycle)

            results = []

            print(f"\n--- Monitoring Cycle {cycle + 1} ---")

            for resource in metrics:
                result = evaluate_metrics(resource, thresholds)
                results.append(result)

                print(
                    f"{result['resource']}: "
                    f"{result['status']}"
                )

            save_report(results)

            cycle += 1

            print("Next monitoring cycle in 10 seconds...\n")

            time.sleep(10)

        except (FileNotFoundError, json.JSONDecodeError):
            print(
                "Application stopped due to a configuration "
                "or data file error."
            )
            return


if __name__ == "__main__":
    main()