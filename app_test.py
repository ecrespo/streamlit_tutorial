from app import calculate_sum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_user_interface():
    driver_path = r'../chromedriver'
    options = Options()
    options.add_argument('--headless')
    with webdriver.Chrome(driver_path,chrome_options=options) as driver:
        url = 'http://127.0.0.1:8501'
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        assert 'Add numbers' in html
        assert 'First number' in html
        assert 'Second number' in html

def test_logic():
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(2, 2) == 4
    assert calculate_sum(3, 2) == 5


if __name__ == '__main__':
    test_user_interface()
    test_logic()