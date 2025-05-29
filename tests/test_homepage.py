from pages.homepage import HomePage

def test_homepage_title(driver):
    home = HomePage(driver)
    home.load()
    assert "Example Domain" in home.get_title()

def test_homepage_has_expected_text(driver):
    home = HomePage(driver)
    home.load()
    assert home.page_contains_text("This domain is for use in illustrative examples")

# def test_homepage_more_information(driver):
#     home = HomePage(driver)
#     home.load()
#     assert "More information" in home.page_contains_text()
#
# def test_homepage_metadata():
#     response = requests.get("https://example.com")
#     assert title is not None, "Title tag is missing"
#     assert description is not None, "Meta description is missing"
#     assert keywords is not None, "Meta keywords are missing"
#     in response.headers
