import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="function")
def page(browser):
    p = browser.new_page()
    yield p
    p.close()

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page: Page):
    return DashboardPage(page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": "test-results/videos"
    }