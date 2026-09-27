# Mobile Automation

Framework: **Appium + Python + pytest + UiAutomator2**.

## Important
The supplied evidence contains screenshots, not the APK binary. Therefore this repository contains the automation implementation and locator strategy, but it does **not** claim that the tests were executed against the APK.

## Setup
1. Install Android Studio/SDK and enable USB debugging on a test device/emulator.
2. Install Appium 2 and UiAutomator2 driver.
3. Install Python dependencies:
   `pip install -r requirements.txt`
4. Set `options.app` in `conftest.py` to the local APK path.
5. Start Appium server on port 4723.
6. Replace `REPLACE_WITH_TEST_PASSWORD` with a valid test credential.
7. Inspect and refine locators with Appium Inspector.
8. Run:
   `pytest -v`

## Journeys covered
- Valid login
- Invalid/malformed login validation
- Dashboard validation
- Attendance navigation
- Approvals navigation
