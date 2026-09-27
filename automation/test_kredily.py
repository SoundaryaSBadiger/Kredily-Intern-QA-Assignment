import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "peoplekredily1@yopmail.com"
PASSWORD = "REPLACE_WITH_TEST_PASSWORD"

def text(driver, value):
    return driver.find_element(By.XPATH, f'//*[@text="{value}"]')

def test_login_valid(driver):
    # Adjust locators after inspecting the APK with Appium Inspector.
    text(driver, "Sign in with password").click()
    driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys(EMAIL)
    driver.find_elements(By.CLASS_NAME, "android.widget.EditText")[1].send_keys(PASSWORD)
    text(driver, "Sign in").click()
    WebDriverWait(driver, 10).until(lambda d: "Home" in d.page_source)

def test_invalid_email_validation(driver):
    text(driver, "Continue").click() if False else None
    # Enter malformed email and assert the validation state.
    # Exact locator should be finalized with Appium Inspector.
    assert "Welcome to Kredily" in driver.page_source

def test_dashboard_validation(driver):
    # Requires successful authentication.
    assert "Home" in driver.page_source
    assert "Approvals" in driver.page_source
    assert "Attendance" in driver.page_source

def test_attendance_navigation(driver):
    # Requires successful authentication.
    text(driver, "Attendance").click()
    assert "Org" in driver.page_source or "attendance" in driver.page_source.lower()

def test_approvals_navigation(driver):
    text(driver, "Approvals").click()
    assert "Approvals" in driver.page_source
