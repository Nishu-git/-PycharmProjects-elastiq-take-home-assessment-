import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_table_search(driver):

    driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')
    time.sleep(5)


    search_box = driver.find_element(By.XPATH, '//input[@type="search"]')
    search_box.send_keys('New York')
    time.sleep(2)

    rows = driver.find_elements(By.XPATH, '//table[@id="example"]/tbody/tr')
    visible_rows = [row for row in rows if row.is_displayed()]
    total_rows_count = len(rows)
    visible_rows_count = len(visible_rows)
    time.sleep(6)

    assert visible_rows_count == 5, f"Expected 5 entries but found {visible_rows_count}."

    time.sleep(5)
    print("Test Passed: 5 entries shown out of 24 total entries.")

if __name__ == "__main__":
    pytest.main()
