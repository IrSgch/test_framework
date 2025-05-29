# import requests

def test_metadata(driver):
    driver.get("https://example.com")
    meta = driver.find_element("xpath","//meta[@charset='utf-8']")
    assert meta is not None #що дані присутні і не можуть бути незаповненими (не пусті)

def test_metadata_2(driver):
    driver.get("https://example.com")
    meta = driver.find_element("xpath","//meta[@name='viewport']")
    assert meta is not None


