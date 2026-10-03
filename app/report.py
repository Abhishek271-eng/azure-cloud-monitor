import json
from datetime import datetime
from pathlib import Path


def save_report(results):
    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    history_folder = reports_folder / "history"
    history_folder.mkdir(exist_ok=True)

    generated_at = datetime.now()

    report_data = {
        "generated_at": generated_at.isoformat(),
        "summary": {
            "total_resources": len(results),
            "healthy": sum(
                1 for result in results
                if result["status"] == "HEALTHY"
            ),
            "warning": sum(
                1 for result in results
                if result["status"] == "WARNING"
            ),
            "critical": sum(
                1 for result in results
                if result["status"] == "CRITICAL"
            )
        },
        "resources": results
    }

    # Current/latest report
    report_file = reports_folder / "infrastructure_report.json"

    with open(report_file, "w") as file:
        json.dump(report_data, file, indent=4)

    # Historical copy
    timestamp = generated_at.strftime("%Y-%m-%d_%H-%M-%S")
    history_file = history_folder / f"{timestamp}.json"

    with open(history_file, "w") as file:
        json.dump(report_data, file, indent=4)

    print(f"Report generated: {report_file}")
    print(f"History saved: {history_file}")