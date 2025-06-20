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
    options.add_argument("--headless")  # Remove this line if you want to see the browser
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_login_valid_user(driver):
    driver.get("https://demoqa.com/login")

    wait = WebDriverWait(driver, 10)

    username = "validusername123"
    password = "Validpassword123!"

    # Find username and password fields
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    username_input.send_keys(username)
    password_input.send_keys(password)

    # Wait for login button to be clickable
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))

    # Scroll button into view
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    time.sleep(0.5)  # small pause to stabilize

    try:
        login_button.click()
    except Exception:
        # fallback to JS click if normal click fails
        driver.execute_script("arguments[0].click();", login_button)

    # Wait for profile username to appear after login
    profile_username = wait.until(EC.visibility_of_element_located((By.ID, "userName-value"))).text

    assert profile_username == username, f"Expected username '{username}' after login, got '{profile_username}'"
