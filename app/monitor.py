def evaluate_metrics(metrics, thresholds):
    alerts = []
    overall_status = "HEALTHY"

    # Check CPU
    cpu = metrics["cpu"]

    if cpu >= thresholds["cpu"]["critical"]:
        overall_status = "CRITICAL"

        alerts.append({
            "metric": "cpu",
            "value": cpu,
            "severity": "CRITICAL",
            "message": "CPU utilization is critically high",
            "recommended_action": "Investigate high CPU processes and workload"
        })

    elif cpu >= thresholds["cpu"]["warning"]:
        overall_status = "WARNING"

        alerts.append({
            "metric": "cpu",
            "value": cpu,
            "severity": "WARNING",
            "message": "CPU utilization is above warning threshold",
            "recommended_action": "Investigate CPU-consuming processes"
        })

    # Check disk
    disk = metrics["disk"]

    if disk >= thresholds["disk"]["critical"]:
        overall_status = "CRITICAL"

        alerts.append({
            "metric": "disk",
            "value": disk,
            "severity": "CRITICAL",
            "message": "Disk utilization is critically high",
            "recommended_action": "Review disk usage or increase storage capacity"
        })

    elif disk >= thresholds["disk"]["warning"]:
        if overall_status != "CRITICAL":
            overall_status = "WARNING"

        alerts.append({
            "metric": "disk",
            "value": disk,
            "severity": "WARNING",
            "message": "Disk utilization is above warning threshold",
            "recommended_action": "Review disk usage and unnecessary files"
        })

    # Check availability
    if not metrics["availability"]:
        overall_status = "CRITICAL"

        alerts.append({
            "metric": "availability",
            "value": False,
            "severity": "CRITICAL",
            "message": "Resource is unavailable",
            "recommended_action": "Check resource health, networking and service status"
        })

    return {
        "resource": metrics["resource"],
        "status": overall_status,
        "metrics": metrics,
        "alerts": alerts
    }