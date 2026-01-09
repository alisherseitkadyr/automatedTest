from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Cart Page for verifying added products"""
    
    # Locators
    CART_TITLE = (By.XPATH, "//li[contains(text(),'Shopping Cart')]")
    CART_ITEMS = (By.XPATH, "//tbody/tr")
    PRODUCT_NAME = (By.CLASS_NAME, "cart_description")
    PRODUCT_PRICE = (By.CLASS_NAME, "cart_price")
    PRODUCT_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    PRODUCT_TOTAL = (By.CLASS_NAME, "cart_total")
    
    def verify_cart_page_loaded(self):
        """Verify cart page is loaded"""
        return self.is_element_visible(self.CART_TITLE)
    
    def get_cart_items_count(self):
        """Get count of items in cart"""
        items = self.find_elements(self.CART_ITEMS)
        return len(items)
    
    def get_first_product_name(self):
        """Get name of first product in cart"""
        try:
            return self.find_element(self.PRODUCT_NAME).text
        except:
            return None