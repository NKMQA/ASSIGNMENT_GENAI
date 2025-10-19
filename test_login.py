import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def setup_page(page: Page):
    # Navigate to OrangeHRM demo site
    page.goto("https://opensource-demo.orangehrmlive.com/")
    yield page
    page.close()

class TestLogin:
    def test_successful_login(self, setup_page):
        """Test successful login with valid credentials"""
        page = setup_page
        
        # Fill login form with demo credentials
        page.fill("input[name='username']", "Admin")
        page.fill("input[name='password']", "admin123")
        
        # Click login button
        page.click("button[type='submit']")
        
        # Assert successful login by checking dashboard element
        expect(page.locator(".oxd-text.oxd-text--h6")).to_contain_text("Dashboard")

    def test_invalid_credentials(self, setup_page):
        """Test login failure with invalid credentials"""
        page = setup_page
        
        # Fill login form with invalid credentials
        page.fill("input[name='username']", "invalid_user")
        page.fill("input[name='password']", "wrong_password")
        
        # Click login button
        page.click("button[type='submit']")
        
        # Assert error message
        expect(page.locator(".oxd-alert-content-text")).to_contain_text("Invalid credentials")

    def test_empty_fields(self, setup_page):
        """Test login with empty fields"""
        page = setup_page
        
        # Click login button without filling fields
        page.click("button[type='submit']")
        
        # Assert validation messages
        expect(page.locator(".oxd-input-field-error-message")).to_be_visible()

    def test_password_masking(self, setup_page):
        """Test password field masking"""
        page = setup_page
        
        # Check password field type
        password_field = page.locator("input[name='password']")
        expect(password_field).to_have_attribute("type", "password")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context"""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080
        },
        "record_video_dir": "test-results/videos"
    }