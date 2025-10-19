import pytest
from playwright.sync_api import expect

class TestLogin:
    def test_successful_login(self, login_page, dashboard_page):
        login_page.navigate()
        login_page.login("Admin", "admin123")
        expect(dashboard_page.dashboard_heading).to_contain_text("Dashboard")

    def test_invalid_credentials(self, login_page):
        login_page.navigate()
        login_page.login("invalid_user", "wrong_password")
        expect(login_page.error_message).to_contain_text("Invalid credentials")

    def test_empty_fields(self, login_page):
        login_page.navigate()
        login_page.login("", "")
        expect(login_page.page.locator(".oxd-input-field-error-message")).to_be_visible()

    def test_password_masking(self, login_page):
        login_page.navigate()
        expect(login_page.password_input).to_have_attribute("type", "password")