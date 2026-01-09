import pytest


class TestHomePage:
    """Test cases for Home Page"""
    
    def test_verify_home_page_loads_successfully(self, home_page):
        """
        Test Case 1: Verify Home Page Loads Successfully
        - Use implicit wait (implemented in BasePage)
        - Assert page title or visible element
        """
        print("\n=== Test Case 1: Verify Home Page Loads Successfully ===")
        print("Using IMPLICIT WAIT: driver.implicitly_wait(10)")
        print("Applied globally in BasePage.__init__()")
        
        # Implicit wait is already set in BasePage (10 seconds)
        # All find_element calls will wait up to 10 seconds
        
        # Verify home page loads
        assert home_page.verify_home_page_loaded(), "Home page did not load successfully"
        
        # Verify page title contains expected text
        assert "Automation Exercise" in home_page.driver.title, \
            f"Page title doesn't match. Actual: {home_page.driver.title}"
        
        print("✓ Home page loaded successfully")
        print(f"✓ Page title: {home_page.driver.title}")