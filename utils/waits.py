from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class FluentWait:
    """
    Custom Fluent Wait implementation
    FLUENT WAIT: Wait with configurable polling and ignored exceptions
    """
    
    def __init__(self, driver, timeout=30, poll_frequency=2, ignored_exceptions=None):
        """
        Initialize fluent wait
        
        Args:
            driver: WebDriver instance
            timeout: Maximum time to wait in seconds (default 30)
            poll_frequency: How often to check in seconds (default 2)
            ignored_exceptions: List of exceptions to ignore (default [NoSuchElementException])
        """
        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency
        
        if ignored_exceptions is None:
            ignored_exceptions = [NoSuchElementException]
        
        self.wait = WebDriverWait(
            driver, 
            timeout, 
            poll_frequency=poll_frequency,
            ignored_exceptions=ignored_exceptions
        )
    
    def until_visible(self, locator):
        """Wait until element is visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def until_clickable(self, locator):
        """Wait until element is clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def until_present(self, locator):
        """Wait until element is present in DOM"""
        return self.wait.until(EC.presence_of_element_located(locator))