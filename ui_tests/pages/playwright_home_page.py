from pages.base_page import BasePage
from playwright.sync_api import expect


class PlaywrightHomePage(BasePage):

    def open(self):
        self.navigate("https://playwright.dev")

    def click_get_started(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.get_by_role("link", name="Get started").click()

    def is_installation_visible(self):
        installation_heading = self.page.get_by_role("heading", name="Installation")
        expect(installation_heading).to_be_visible(timeout=10000)