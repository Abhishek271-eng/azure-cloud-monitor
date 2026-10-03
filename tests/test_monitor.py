from app.monitor import evaluate_metrics


def test_healthy_resource():
    metrics = {
        "resource": "test-server",
        "cpu": 40,
        "disk": 50,
        "availability": True
    }

    thresholds = {
        "cpu": {
            "warning": 70,
            "critical": 85
        },
        "disk": {
            "warning": 75,
            "critical": 90
        }
    }

    result = evaluate_metrics(metrics, thresholds)

    assert result["status"] == "HEALTHY"


def test_warning_cpu():
    metrics = {
        "resource": "test-server",
        "cpu": 80,
        "disk": 50,
        "availability": True
    }

    thresholds = {
        "cpu": {
            "warning": 70,
            "critical": 85
        },
        "disk": {
            "warning": 75,
            "critical": 90
        }
    }

    result = evaluate_metrics(metrics, thresholds)

    assert result["status"] == "WARNING"


def test_critical_cpu():
    metrics = {
        "resource": "test-server",
        "cpu": 95,
        "disk": 50,
        "availability": True
    }

    thresholds = {
        "cpu": {
            "warning": 70,
            "critical": 85
        },
        "disk": {
            "warning": 75,
            "critical": 90
        }
    }

    result = evaluate_metrics(metrics, thresholds)

    assert result["status"] == "CRITICAL"