from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage


class LoginPage(BasePage):
    """Login and Registration Page"""
    
    # Locators
    SIGNUP_NAME = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    MR_RADIO = (By.ID, "id_gender1")
    MRS_RADIO = (By.ID, "id_gender2")
    PASSWORD = (By.ID, "password")
    DAY_DROPDOWN = (By.ID, "days")
    MONTH_DROPDOWN = (By.ID, "months")
    YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[@data-qa='create-account']")
    ACCOUNT_CREATED_MSG = (By.XPATH, "//h2[@data-qa='account-created']")
    CONTINUE_BTN = (By.XPATH, "//a[@data-qa='continue-button']")
    
    def signup_new_user(self, name, email):
        """Start new user signup process"""
        self.send_keys(self.SIGNUP_NAME, name)
        self.send_keys(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)
        # After clicking signup, wait for account information form to load
        try:
            # DAY_DROPDOWN is part of the registration form; wait for it
            self.fluent_wait_for_element(self.DAY_DROPDOWN, timeout=15, poll_frequency=1)
        except Exception:
            # Let subsequent actions raise explicit errors if element not present
            pass
    
    def fill_account_information(self, user_data):
        """Fill account information form"""
        # Select title using explicit wait
        if user_data['title'] == 'Mr':
            self.click(self.MR_RADIO)
        else:
            self.click(self.MRS_RADIO)
        
        self.send_keys(self.PASSWORD, user_data['password'])
        
        # SELECT CLASS: Handling dropdowns using Select class
        self.select_day(user_data['day'])
        self.select_month(user_data['month'])
        self.select_year(user_data['year'])
        
        # Check checkboxes
        if user_data['newsletter']:
            self.click(self.NEWSLETTER_CHECKBOX)
        if user_data['offers']:
            self.click(self.OFFERS_CHECKBOX)
        
        self.send_keys(self.FIRST_NAME, user_data['first_name'])
        self.send_keys(self.LAST_NAME, user_data['last_name'])
        self.send_keys(self.COMPANY, user_data['company'])
        self.send_keys(self.ADDRESS1, user_data['address1'])
        self.send_keys(self.ADDRESS2, user_data['address2'])
        
        # Country dropdown using Select class
        self.select_country(user_data['country'])
        
        self.send_keys(self.STATE, user_data['state'])
        self.send_keys(self.CITY, user_data['city'])
        self.send_keys(self.ZIPCODE, user_data['zipcode'])
        self.send_keys(self.MOBILE_NUMBER, user_data['mobile'])
    
    def select_day(self, day_value):
        """Select day from dropdown using Select class"""
        day_dropdown = self.find_element(self.DAY_DROPDOWN)
        select = Select(day_dropdown)
        select.select_by_value(str(day_value))
        return select.first_selected_option.text
    
    def select_month(self, month_value):
        """Select month from dropdown using Select class"""
        month_dropdown = self.find_element(self.MONTH_DROPDOWN)
        select = Select(month_dropdown)
        select.select_by_value(str(month_value))
        return select.first_selected_option.text
    
    def select_year(self, year_value):
        """Select year from dropdown using Select class"""
        year_dropdown = self.find_element(self.YEAR_DROPDOWN)
        select = Select(year_dropdown)
        select.select_by_value(str(year_value))
        return select.first_selected_option.text
    
    def select_country(self, country_name):
        """Select country from dropdown using Select class"""
        country_dropdown = self.find_element(self.COUNTRY)
        select = Select(country_dropdown)
        select.select_by_visible_text(country_name)
        return select.first_selected_option.text
    
    def submit_account_creation(self):
        """Submit account creation form"""
        self.click(self.CREATE_ACCOUNT_BTN)
    
    def verify_account_created(self):
        """Verify account creation success"""
        return self.is_element_visible(self.ACCOUNT_CREATED_MSG)
    
    def continue_after_creation(self):
        """Click continue after account creation"""
        self.click(self.CONTINUE_BTN)