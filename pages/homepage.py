class HomePage:
    URL = "https://example.com"
    def __init__(self, driver):
        self.driver = driver
    def load(self):
        self.driver.get(self.URL)
    def get_title(self):
        return self.driver.title
    def page_contains_text(self, text):
        return text in self.driver.page_source