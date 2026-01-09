import pytest
from data.test_data import TestData


class TestDropdownSelection:
    """Test cases for Dropdown Selection"""
    
    def test_dropdown_selection_with_select_class(self, home_page, login_page):
        """
        Test Case 4: Dropdown Selection using Select class
        - Navigate to Signup form
        - Select Day, Month, Year from dropdowns using Select class
        - Assert selected values
        """
        print("\n=== Test Case 4: Dropdown Selection with Select Class ===")
        print("Using SELECT CLASS: Select(dropdown_element)")
        
        # Step 1: Navigate to signup page
        home_page.navigate_to_signup_login()
        print("✓ Navigated to signup page")

        # Step 2: Start signup process (use unique test data email)
        login_page.signup_new_user(TestData.NAME, TestData.EMAIL)
        print("✓ Started signup process")
        
        # Step 3: Use SELECT CLASS to handle dropdowns
        # SELECT CLASS: Creating Select object for dropdown
        selected_day = login_page.select_day(TestData.DAY)
        selected_month = login_page.select_month(TestData.MONTH)
        selected_year = login_page.select_year(TestData.YEAR)
        
        print(f"✓ Selected Day: {selected_day}")
        print(f"✓ Selected Month: {selected_month}")
        print(f"✓ Selected Year: {selected_year}")
        
        # Step 4: Assert selected values
        assert selected_day != "", "Day not selected"
        assert selected_month != "", "Month not selected"
        assert selected_year != "", "Year not selected"
        
        print(f"✓ Asserted selected values: {selected_day}/{selected_month}/{selected_year}")
        
        # Step 5: Test country dropdown using Select class
        selected_country = login_page.select_country(TestData.COUNTRY)
        print(f"✓ Selected Country: {selected_country}")
        assert selected_country == TestData.COUNTRY, f"Country not selected correctly"
        
        print("✓ Dropdown selection with Select class completed successfully")
    
    def test_fluent_wait_implementation(self, home_page):
        """
        Test Case 5: Fluent Wait Implementation
        - Wait for dynamically loaded element
        - Use polling frequency
        - Handle NoSuchElementException
        """
        print("\n=== Test Case 5: Fluent Wait Implementation ===")
        print("Using FLUENT WAIT: WebDriverWait with custom polling and ignored exceptions")
        
        # FLUENT WAIT: Custom wait implementation
        # In a real scenario, we would wait for a dynamically loaded element
        # For demo, we'll simulate waiting for an element with specific conditions
        
        # Using fluent wait from base page
        # This demonstrates waiting with custom polling frequency
        
        # First, let's ensure page is loaded
        assert home_page.verify_home_page_loaded(), "Home page not loaded"
        
        # FLUENT WAIT EXAMPLE: 
        # Wait for Signup/Login button with specific polling
        print("Setting up Fluent Wait with:")
        print("  - Timeout: 30 seconds")
        print("  - Polling Frequency: 2 seconds")
        print("  - Ignored Exceptions: NoSuchElementException")
        
        try:
            # In real scenario, this would wait for a dynamically appearing element
            # For this demo, we'll use it on an existing element to show the pattern
            from selenium.common.exceptions import NoSuchElementException
            
            # Create a locator for demonstration
            demo_locator = home_page.SIGNUP_LOGIN_BTN
            
            # Use fluent wait from base page
            element = home_page.fluent_wait_for_element(
                demo_locator,
                timeout=30,
                poll_frequency=2,
                ignored_exceptions=[NoSuchElementException]
            )
            
            assert element is not None, "Element not found with fluent wait"
            print("✓ Fluent wait successfully found the element")
            print("✓ Element text:", element.text)
            
        except Exception as e:
            print(f"✗ Fluent wait failed: {e}")
            raise
        
        print("✓ Fluent wait implementation verified successfully")