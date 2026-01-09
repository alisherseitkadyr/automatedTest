import pytest
import time
from data.test_data import TestData


class TestRegistration:
    """Test cases for User Registration"""
    
    def test_user_registration_flow(self, home_page, login_page):
        """
        Test Case 2: User Registration Flow
        - Navigate to Signup/Login
        - Fill form with user data
        - Use explicit wait for elements
        - Assert successful account creation
        """
        print("\n=== Test Case 2: User Registration Flow ===")
        print("Using EXPLICIT WAIT: WebDriverWait + expected_conditions")
        
        # Step 1: Navigate to Signup/Login page
        home_page.navigate_to_signup_login()
        print("✓ Navigated to Signup/Login page")
        
        # Step 2: Fill signup form
        # Using explicit wait in find_element method
        login_page.signup_new_user(TestData.NAME, TestData.EMAIL)
        print("✓ Filled signup form with name and email")
        
        # Step 3: Fill account information
        # EXPLICIT WAIT: Each form field uses explicit wait via find_element
        selected_day = login_page.select_day(TestData.DAY)
        selected_month = login_page.select_month(TestData.MONTH)
        selected_year = login_page.select_year(TestData.YEAR)
        
        # Fill rest of the form
        login_page.fill_account_information({
            'title': TestData.TITLE,
            'password': TestData.PASSWORD,
            'day': TestData.DAY,
            'month': TestData.MONTH,
            'year': TestData.YEAR,
            'newsletter': True,
            'offers': True,
            'first_name': TestData.FIRST_NAME,
            'last_name': TestData.LAST_NAME,
            'company': TestData.COMPANY,
            'address1': TestData.ADDRESS1,
            'address2': TestData.ADDRESS2,
            'country': TestData.COUNTRY,
            'state': TestData.STATE,
            'city': TestData.CITY,
            'zipcode': TestData.ZIPCODE,
            'mobile': TestData.MOBILE_NUMBER
        })
        
        print(f"✓ Selected date: {selected_day}/{selected_month}/{selected_year}")
        print("✓ Filled all account information")
        
        # Step 4: Submit account creation
        login_page.submit_account_creation()
        print("✓ Submitted account creation form")
        
        # Step 5: Verify account created
        # EXPLICIT WAIT: Waiting for success message
        assert login_page.verify_account_created(), "Account creation failed"
        print("✓ Account created successfully")
        
        # Step 6: Continue to home page
        login_page.continue_after_creation()
        print("✓ Continued to home page")
        
        # Step 7: Verify user is logged in
        # Using explicit wait via find_element
        assert home_page.is_logged_in(), "User is not logged in"
        print("✓ User successfully logged in")
        
        print("✓ Registration flow completed successfully")