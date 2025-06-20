import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Comment this line if you want to see the browser
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_typing_full_book_title_shows_correct_result(driver):
    # TC_110 - Typing full book title shows correct result

    driver.get("https://demoqa.com/books")
    time.sleep(2)  # Let the page load

    search_box = driver.find_element(By.ID, "searchBox")
    full_title = "Git Pocket Guide"
    search_box.send_keys(full_title)
    time.sleep(2)  # Wait for filtering

    rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
    visible_books = [row.text for row in rows if row.text.strip() != ""]

    assert len(visible_books) == 1, f"Expected 1 result, got {len(visible_books)}"
    assert full_title in visible_books[0], f"Book title '{full_title}' not found in result"
