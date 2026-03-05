class PlaywrightHomePage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://playwright.dev")

    def click_get_started(self):
        self.page.get_by_role("link", name="Get started").click()

    def is_installation_visible(self):
        return self.page.get_by_role("heading", name="Installation").is_visible()