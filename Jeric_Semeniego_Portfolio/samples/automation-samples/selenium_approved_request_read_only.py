"""Representative Selenium sample for read-only validation after approval.

This is a simplified portfolio artifact, not a production-ready test framework.
"""

from selenium.webdriver.common.by import By


def open_request(driver, request_id: str) -> None:
    driver.get(f"https://example.test/purchase-requests/{request_id}")


def login(driver, username: str, password: str) -> None:
    driver.get("https://example.test/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "sign-in").click()


def approve_request(driver) -> None:
    driver.find_element(By.ID, "approve").click()


def test_approved_request_is_read_only(driver) -> None:
    login(driver, "approver_user", "password")
    open_request(driver, "PR-10025")
    approve_request(driver)

    login(driver, "requester_user", "password")
    open_request(driver, "PR-10025")

    amount = driver.find_element(By.ID, "amount")
    remarks = driver.find_element(By.ID, "remarks")

    assert amount.get_attribute("disabled") in ("true", "disabled")
    assert remarks.get_attribute("disabled") in ("true", "disabled")
