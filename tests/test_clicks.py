from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_click_1(driver):
    driver.get("https://example.com")
    link = driver.find_element(By.CSS_SELECTOR, "a")
    href = link.get_attribute("href")
    link.click()
    # driver.window_handles()
    # WebDriverWait(driver, 50).until(lambda d: len(d.window_handles) > 1)
    # driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 50).until(EC.title_contains("IANA"))
    assert driver.current_url == href
    assert "iana.org" in driver.title.lower()


#Перевірити, що посилання "More information..." веде на правильну сторінку і відкривається без помилок.

