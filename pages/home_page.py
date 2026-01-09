from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    """Home Page of Automation Exercise"""
    
    # Locators
    HOME_PAGE_TITLE = (By.CSS_SELECTOR, "title")
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    LOGGED_IN_AS = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    PRODUCTS_BTN = (By.XPATH, "//a[@href='/products']")
    CART_BTN = (By.XPATH, "//a[contains(text(),'Cart')]")
    CONTACT_US_BTN = (By.XPATH, "//a[contains(text(),'Contact us')]")
    
    def verify_home_page_loaded(self):
        """Verify home page loads successfully"""
        # Using implicit wait from base class
        return "Automation Exercise" in self.driver.title
    
    def navigate_to_signup_login(self):
        """Navigate to signup/login page"""
        self.click(self.SIGNUP_LOGIN_BTN)
        # Wait for the signup form to appear (dropdowns are part of the form)
        try:
            # Use fluent wait to allow the signup form to load fully
            self.fluent_wait_for_element((By.ID, "days"), timeout=15, poll_frequency=1)
        except Exception:
            # If waiting fails, continue — the tests will raise explicit errors later
            pass
    
    def navigate_to_products(self):
        """Navigate to products page"""
        self.click(self.PRODUCTS_BTN)
        # Wait for products page heading to appear
        try:
            self.fluent_wait_for_element(self.ALL_PRODUCTS_TEXT, timeout=15, poll_frequency=1)
        except Exception:
            # If wait fails, let tests assert the page state later
            pass
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return self.is_element_visible(self.LOGGED_IN_AS)
    
    def navigate_to_cart(self):
        """Navigate to cart page"""
        self.click(self.CART_BTN)