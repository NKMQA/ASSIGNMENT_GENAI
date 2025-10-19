from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_heading = page.locator(".oxd-text.oxd-text--h6")

    def title_text(self) -> str:
        return self.dashboard_heading.text_content() or ""