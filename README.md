<div align="center">

<img src="https://img.shields.io/badge/AZURE-CLOUD%20MONITORING-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Azure Cloud Monitoring"/>

# ☁️ Azure Cloud Infrastructure  
# Monitoring & Alerting System

<p>
  <strong>A Python-based infrastructure monitoring system designed around Azure cloud monitoring concepts.</strong>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/JSON-Configuration-000000?style=flat-square&logo=json&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pytest-Tested-0A9EDC?style=flat-square&logo=pytest&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=flat-square&logo=git&logoColor=white"/>
  <img src="https://img.shields.io/badge/Azure-Monitoring%20Concepts-0078D4?style=flat-square&logo=microsoftazure&logoColor=white"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/Monitoring-Continuous-00A98F?style=flat-square"/>
  <img src="https://img.shields.io/badge/Reports-JSON-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Tests-6%20Passed-brightgreen?style=flat-square"/>
</p>

</div>

---

## 🚀 Overview

<table>
<tr>
<td width="60%">

This project demonstrates the core workflow of a **cloud infrastructure monitoring and alerting system**.

The application continuously evaluates infrastructure health using three key indicators:

- 🖥️ **CPU Utilization**
- 💾 **Disk Utilization**
- 🟢 **Resource Availability**

Each monitored resource is classified into one of three health states:

**HEALTHY → WARNING → CRITICAL**

The system also generates structured alerts, creates JSON reports, and maintains timestamped monitoring history.

</td>

<td width="40%">

### 🎯 Project Focus

```text
Infrastructure
      ↓
Metric Evaluation
      ↓
Threshold Checking
      ↓
Health Classification
      ↓
Alert Generation
      ↓
JSON Reporting
      ↓
Monitoring History
```

</td>
</tr>
</table>

---

## 🧠 Why This Project?

Cloud infrastructure needs continuous monitoring to identify performance problems before they become larger incidents.

This project focuses on implementing the fundamental monitoring workflow:

> **Collect → Evaluate → Classify → Alert → Report → Track History**

The monitoring engine is intentionally separated from the metric source so that simulated metrics can later be replaced with real cloud monitoring data.

---

## 🏗️ System Architecture

<div align="center">

```text
                     ☁️ CLOUD INFRASTRUCTURE
                              │
                              ▼
                  ┌───────────────────────┐
                  │   Infrastructure      │
                  │       Metrics         │
                  └───────────┬───────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        🖥️ CPU Utilization         💾 Disk Utilization
                 │                         │
                 └────────────┬────────────┘
                              │
                              ▼
                    🟢 Availability Check
                              │
                              ▼
                  ┌───────────────────────┐
                  │   Monitoring Engine   │
                  │     monitor.py       │
                  └───────────┬───────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │ Threshold Evaluation  │
                  └───────────┬───────────┘
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
          🟢 HEALTHY      🟡 WARNING       🔴 CRITICAL
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                    🚨 Alert Generation
                              │
                              ▼
                  ┌───────────────────────┐
                  │     Report Engine     │
                  │       report.py       │
                  └───────────┬───────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             📄 Latest Report      🕘 History
             JSON Report           JSON Files
```

</div>

---

## 📊 Monitoring Metrics

<table>
<tr>
<th>Metric</th>
<th>Purpose</th>
<th>Healthy</th>
<th>Warning</th>
<th>Critical</th>
</tr>

<tr>
<td>🖥️ CPU</td>
<td>Detect high processor utilization</td>
<td>&lt; 70%</td>
<td>70–84%</td>
<td>≥ 85%</td>
</tr>

<tr>
<td>💾 Disk</td>
<td>Detect high storage utilization</td>
<td>&lt; 75%</td>
<td>75–89%</td>
<td>≥ 90%</td>
</tr>

<tr>
<td>🟢 Availability</td>
<td>Check resource availability</td>
<td>Available</td>
<td>—</td>
<td>Unavailable</td>
</tr>

</table>

> **Note:** CPU and disk thresholds are project-configurable values stored in `config/thresholds.json`.

---

## ⚙️ Monitoring Workflow

```text
       START
         │
         ▼
┌─────────────────┐
│ Load Thresholds │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Obtain Metrics  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Evaluate CPU    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Evaluate Disk   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Check Available │
└────────┬────────┘
         │
         ▼
┌──────────────────────┐
│ Determine Overall    │
│ Resource Health      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Generate Alerts      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Generate JSON Report │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Save Monitoring      │
│ History              │
└──────────┬───────────┘
           │
           ▼
      WAIT 10 SEC
           │
           └──────────────► REPEAT
```

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔍 Infrastructure Monitoring

- CPU utilization monitoring
- Disk utilization monitoring
- Resource availability checking
- Continuous monitoring cycles

</td>

<td width="50%">

### 🚨 Alerting

- Threshold-based detection
- Warning-level alerts
- Critical-level alerts
- Recommended actions

</td>
</tr>

<tr>
<td>

### 📄 Reporting

- JSON infrastructure reports
- Monitoring timestamps
- Resource-level results
- Health summary

</td>

<td>

### 🕘 Monitoring History

- Timestamped historical reports
- One report per monitoring cycle
- Historical health tracking
- Latest + historical reports

</td>
</tr>

<tr>
<td>

### 🛡️ Reliability

- JSON validation
- Missing-file handling
- Application-level error handling
- Graceful termination

</td>

<td>

### 🧪 Testing

- Automated pytest tests
- Healthy-state validation
- CPU threshold validation
- Disk threshold validation
- Availability validation

</td>
</tr>
</table>

---

## 🗂️ Project Structure

```text
azure-cloud-monitor/
│
├── 📁 app/
│   ├── __init__.py
│   ├── main.py
│   ├── monitor.py
│   └── report.py
│
├── 📁 config/
│   └── thresholds.json
│
├── 📁 data/
│   └── sample_metrics.json
│
├── 📁 reports/
│   ├── infrastructure_report.json
│   └── 📁 history/
│       └── *.json
│
├── 📁 tests/
│   └── test_monitor.py
│
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
└── 📁 venv/              ← ignored by Git
```

---

## 🧩 Application Components

### `main.py`

<div align="center">

**Application Controller**

</div>

Responsible for coordinating the monitoring workflow.

```text
Load Configuration
       ↓
Obtain Metrics
       ↓
Run Monitoring Engine
       ↓
Generate Results
       ↓
Create Reports
       ↓
Repeat Monitoring Cycle
```

---

### `monitor.py`

<div align="center">

**Core Monitoring Engine**

</div>

Contains the main infrastructure health evaluation logic.

Responsibilities:

- CPU threshold evaluation
- Disk threshold evaluation
- Availability checking
- Overall health classification
- Alert generation
- Recommended actions

---

### `report.py`

<div align="center">

**Reporting & History Engine**

</div>

Responsible for:

- Generating the latest report
- Calculating health summaries
- Adding timestamps
- Saving historical reports

---

### `thresholds.json`

Central configuration for monitoring thresholds.

```json
{
    "cpu": {
        "warning": 70,
        "critical": 85
    },
    "disk": {
        "warning": 75,
        "critical": 90
    }
}
```

This allows thresholds to be changed without modifying the monitoring logic.

---

### `test_monitor.py`

Contains automated tests for the monitoring engine.

### Test Scenarios

| # | Scenario | Expected Result |
|---|---|---|
| 1 | Normal resource | 🟢 HEALTHY |
| 2 | High CPU | 🟡 WARNING |
| 3 | Critical CPU | 🔴 CRITICAL |
| 4 | High disk | 🟡 WARNING |
| 5 | Critical disk | 🔴 CRITICAL |
| 6 | Resource unavailable | 🔴 CRITICAL |

---

## 🔄 Simulated Monitoring

Because the project was developed without an active Azure subscription, infrastructure metrics are currently simulated locally.

The simulation demonstrates changing infrastructure conditions:

```text
Cycle 1
   ↓
🟢 HEALTHY

Cycle 2
   ↓
🟡 WARNING

Cycle 3
   ↓
🔴 CRITICAL

Cycle 4
   ↓
🟢 RECOVERY
```

This allows the monitoring and alerting logic to be tested without requiring paid cloud resources.

---

## 📄 Reporting

### Latest Report

```text
reports/infrastructure_report.json
```

Contains:

- Generation timestamp
- Total monitored resources
- Healthy resources
- Warning resources
- Critical resources
- Individual resource results
- Generated alerts

### Historical Reports

```text
reports/history/
```

Example:

```text
2026-10-03_23-45-12.json
2026-10-03_23-45-22.json
2026-10-03_23-45-32.json
```

Each file represents one monitoring cycle.

---

## 🧪 Testing

The project uses **pytest** for automated testing.

### Run Tests

```bash
python -m pytest
```

### Expected Result

```text
6 passed
```

### Test Coverage

```text
             Monitoring Engine
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
      CPU          Disk      Availability
       │            │            │
       ▼            ▼            ▼
    Warning      Warning      Available
    Critical     Critical     Unavailable
```

---

## 🛠️ Technology Stack

<div align="center">

| Technology | Purpose |
|---|---|
| 🐍 Python | Monitoring engine and application logic |
| 📋 JSON | Configuration, metrics and reports |
| 🧪 Pytest | Automated testing |
| ☁️ Azure Concepts | Cloud infrastructure monitoring architecture |
| 🔧 Git | Version control |
| 🐙 GitHub | Source code hosting |
| 🖥️ Linux / Windows | Development environment |

</div>

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2️⃣ Enter the Project

```bash
cd azure-cloud-monitor
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Tests

```bash
python -m pytest
```

### 5️⃣ Start Monitoring

```bash
python -m app.main
```

The application performs a monitoring cycle every **10 seconds**.

### 6️⃣ Stop Monitoring

```text
Ctrl + C
```

---

## 🔐 Error Handling

The application handles common configuration and data errors.

### Missing File

```text
ERROR: File not found
Application stopped due to a configuration or data file error.
```

### Invalid JSON

```text
ERROR: Invalid JSON file
Application stopped due to a configuration or data file error.
```

This prevents the application from continuing with invalid monitoring configuration or metric data.

---

## ☁️ Azure Integration Path

The current version uses simulated metrics.

The intended production-style architecture is:

```text
             CURRENT VERSION

      Simulated Infrastructure Data
                    │
                    ▼
            Monitoring Engine
                    │
                    ▼
             Alert + Report


             FUTURE VERSION

              Azure Monitor
                    │
                    ▼
         CPU / Disk / Availability
                    │
                    ▼
            Monitoring Engine
                    │
                    ▼
             Alert + Report
```

The monitoring logic can therefore remain separated from the source of the metrics.

---

## 🎯 Project Scope

This project intentionally focuses on three infrastructure indicators:

```text
🖥️ CPU
💾 Disk
🟢 Availability
```

The goal is to demonstrate the fundamental concepts of:

- Infrastructure monitoring
- Threshold-based alerting
- Incident identification
- Health classification
- Monitoring history
- Structured reporting
- Automated testing
- Error handling

Rather than attempting to monitor every possible cloud metric, the project keeps the implementation focused and understandable.

---

## 🔮 Future Enhancements

If an active Azure environment becomes available, the project could be extended with:

- ☁️ Azure Monitor metric integration
- 🔐 Azure authentication
- 📊 Dashboard visualization
- 📈 Historical metric trends
- 🚨 Email / notification alerts
- 🗄️ Persistent monitoring database
- 🌐 REST API for monitoring results
- 📦 Containerized deployment

---

## 💡 What I Learned

Through this project, I practiced:

- Python application structure
- File and JSON handling
- Threshold-based monitoring
- Exception handling
- Automated testing with pytest
- Continuous monitoring workflows
- Report generation
- Monitoring history
- Git and GitHub version control
- Cloud infrastructure monitoring concepts

---

## 👨‍💻 Author

<div align="center">

### Abhishek Devanagaon

**Computer Science Engineering Student**

Interested in:

`☁️ Cloud Computing` · `🐍 Python` · `🌐 Networking` · `⚙️ Infrastructure` · `🔧 Automation`

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

<br>

<img src="https://img.shields.io/badge/Built%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Cloud-Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
<img src="https://img.shields.io/badge/Tested-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white"/>

</div>
```

### One important thing, bro

I intentionally **didn't put fake claims** like:

```text
❌ Real-time Azure Monitor integration
❌ Azure VM deployed
❌ Production cloud monitoring
❌ Live Azure alerts
```
