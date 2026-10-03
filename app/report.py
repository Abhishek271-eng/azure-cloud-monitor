import json
from pathlib import Path


def save_report(results):
    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    report_file = reports_folder / "infrastructure_report.json"

    with open(report_file, "w") as file:
        json.dump(results, file, indent=4)

    print(f"Report generated: {report_file}")