# Kredily HRMS — QA Assessment Submission

A GitHub-ready QA assessment repository for the Kredily HRMS Android application.

## Repository contents

```text
Kredily_QA_Assessment_Submission/
├── test-cases/
│   ├── test-cases.csv
│   └── README.md
├── bug-reports/
│   ├── BUG-001.md
│   ├── BUG-002.md
│   └── README.md
├── automation/
│   ├── conftest.py
│   ├── test_kredily.py
│   ├── requirements.txt
│   └── README.md
├── api/
│   ├── Kredily_API_Collection.postman_collection.json
│   └── README.md
├── ai-assisted-qa/
│   └── AI_ASSISTED_QA.md
├── evidence/
│   └── screenshots/
└── reports/
    ├── final_qa_summary.md
    └── observations.md
```

## Test case execution
Open `test-cases/test-cases.csv`. Exactly 20 functional test cases are included, covering positive, negative and edge scenarios.

## Bug reports
Two bugs are directly supported by the supplied screenshots. No unsupported defects have been presented as genuine bugs.

## Mobile automation
The Appium + Python + pytest framework is under `automation/`.

### Prerequisites
- Android SDK / emulator or physical Android device
- Appium 2 + UiAutomator2
- Python 3.10+
- Kredily APK
- Valid test credentials

### Run
```bash
cd automation
pip install -r requirements.txt
# Set the APK path and test password in the Python files
pytest -v
```

## API testing
The Postman collection is under `api/`. The actual API host and routes must be captured from the test environment before execution; placeholders are intentionally used instead of invented endpoints.

## AI-assisted QA
See `ai-assisted-qa/AI_ASSISTED_QA.md` for the prompt, AI-generated output summary, and human validation changes.

## Evidence
All eight screenshots supplied for this assessment are included under `evidence/screenshots/`.

## QA conclusion
The evidence demonstrates coverage of major visible HRMS workflows and two defensible defects. Live APK execution is still required to complete unexecuted test cases, finalize Appium locators, capture execution reports/videos, and discover the real API endpoints.
