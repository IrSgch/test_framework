import time

def test_time(driver):
    start = time.time()
    driver.get("https://example.com")
    end = time.time()
    load_time = end - start
    assert load_time < 3, f"Page load takes too long time: {load_time:.3f} sec"

