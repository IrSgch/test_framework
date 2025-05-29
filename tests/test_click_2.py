from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_click_1(driver):
    try:
        driver.get("https://example.com")
        link = driver.find_element(By.CSS_SELECTOR, "a")
        #href = link.get_attribute("href")
        link.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Domains")))
        assert driver.current_url == "https://www.iana.org/help/example-domains"
        assert "example domains" in driver.title.lower()
    except Exception as e:
        driver.get_screenshot_as_file("test_failure.png")     #делает скриншот страницы на момент ошибки в папку энва
        raise e  # Rethrow the exception to mark the test as failed


    driver.quit()


#Перевірити, що посилання "More information..." веде на правильну сторінку і відкривається без помилок.