import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Remove if you want to see browser
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_login_invalid_user(driver):
    driver.get("https://demoqa.com/login")

    wait = WebDriverWait(driver, 10)

    # Invalid credentials
    username = "Invaliduser"
    password = "Invaliduser"

    username_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))

    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    time.sleep(0.5)

    try:
        login_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", login_button)

    # Wait for error message to appear
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "name"))).text

    # The login page URL should still be the login URL (no redirect)
    current_url = driver.current_url

    assert "Invalid username or password!" in error_message, f"Expected error message not found, got: {error_message}"
    assert "login" in current_url, f"Expected to stay on login page, but URL is {current_url}"
