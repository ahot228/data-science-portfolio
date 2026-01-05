# Python Anomaly Detector

## Overview
This project automates **data quality checks** for datasets using Python.  
It detects **missing values, duplicates, schema mismatches, and outliers** to ensure data consistency in analytics workflows.

## Tech Stack
- Python • Pandas • PyTest
- GitHub Actions (for CI/CD integration)

## ⚙️ Features
- Automated validation tests for key data quality dimensions.
- Unit tests using PyTest for modular testing.
- GitHub Actions workflow to run tests on every commit.

## 📁 Project Structure
```
src/
├── anomaly_detector.py
tests/
├── test_anomaly_detector.py
├── test_report.txt
data/
├── *raw csv files*
requirements.txt
README.md
```

## How to Run
```bash
pip3 install -r requirements.txt
pytest
```

## Learnings
- Built robust testing for data pipelines.
- Practiced CI/CD automation using GitHub Actions.
