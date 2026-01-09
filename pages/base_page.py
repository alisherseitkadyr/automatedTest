from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.waits import FluentWait


class BasePage:
    """Base page with common functionality for all pages"""
    
    def __init__(self, driver):
        self.driver = driver
        # IMPLICIT WAIT: Applied to all elements automatically
        # This is a global wait that applies to all find_element calls
        self.driver.implicitly_wait(10)  # 10 seconds implicit wait
        
    def find_element(self, locator):
        """Find single element with explicit wait"""
        try:
            # EXPLICIT WAIT: Wait for specific element to be visible
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element with locator {locator} not found")
    
    def find_elements(self, locator):
        """Find multiple elements"""
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        """Click element with explicit wait"""
        element = self.find_element(locator)
        element.click()
    
    def send_keys(self, locator, text):
        """Send text to element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def fluent_wait_for_element(self, locator, timeout=30, poll_frequency=2, ignored_exceptions=None):
        """
        FLUENT WAIT: Custom wait with configurable polling and ignored exceptions
        Args:
            locator: Element locator
            timeout: Maximum time to wait (default 30s)
            poll_frequency: How often to check (default 2s)
            ignored_exceptions: Exceptions to ignore during polling
        """
        wait = FluentWait(self.driver, timeout, poll_frequency, ignored_exceptions)
        return wait.until_visible(locator)