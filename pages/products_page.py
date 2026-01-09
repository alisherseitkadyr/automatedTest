from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage


class ProductsPage(BasePage):
    """Products Page for product interactions"""
    
    # Locators
    ALL_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'All Products')]")
    SEARCH_PRODUCT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCT_ITEM = (By.CLASS_NAME, "product-image-wrapper")
    PRODUCT_INFO = (By.CLASS_NAME, "productinfo")
    ADD_TO_CART_BTN = (By.XPATH, ".//a[contains(@class, 'add-to-cart')]")
    VIEW_CART_BTN = (By.XPATH, "//u[contains(text(),'View Cart')]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")
    MODAL_TITLE = (By.XPATH, "//h4[contains(text(),'Added!')]")
    
    def verify_products_page_loaded(self):
        """Verify products page is loaded"""
        return self.is_element_visible(self.ALL_PRODUCTS_TEXT)
    
    def hover_over_product(self, product_index=0):
        """
        Hover over a product using ActionChains
        Args:
            product_index: Index of product to hover (default 0)
        """
        products = self.find_elements(self.PRODUCT_ITEM)
        if product_index < len(products):
            product = products[product_index]
            # ACTIONCHAINS: Creating hover action
            actions = ActionChains(self.driver)
            actions.move_to_element(product).perform()
            return True
        return False
    
    def add_product_to_cart_with_hover(self, product_index=0):
        """
        Hover over product and click Add to Cart using ActionChains
        Args:
            product_index: Index of product to add (default 0)
        """
        products = self.find_elements(self.PRODUCT_ITEM)
        if product_index < len(products):
            product = products[product_index]
            
            # ACTIONCHAINS: Complex hover and click action
            actions = ActionChains(self.driver)
            
            # Move to product wrapper and perform hover
            actions.move_to_element(product).perform()

            # Find add to cart button within the hovered product
            add_to_cart_btn = product.find_element(By.XPATH, ".//a[contains(@class, 'add-to-cart')]")

            # Move to button and click using ActionChains
            actions.move_to_element(add_to_cart_btn).click().perform()

            # Wait for modal to appear: sometimes the modal title isn't present,
            # so wait for one of the modal buttons (View Cart or Continue Shopping)
            try:
                self.fluent_wait_for_element(self.VIEW_CART_BTN, timeout=10, poll_frequency=1)
            except Exception:
                try:
                    self.fluent_wait_for_element(self.CONTINUE_SHOPPING_BTN, timeout=10, poll_frequency=1)
                except Exception:
                    # final attempt: wait for modal title
                    self.fluent_wait_for_element(self.MODAL_TITLE, timeout=5, poll_frequency=1)

            return True
        return False
    
    def continue_shopping(self):
        """Click continue shopping button in modal"""
        self.click(self.CONTINUE_SHOPPING_BTN)
    
    def view_cart(self):
        """Click view cart button in modal"""
        self.click(self.VIEW_CART_BTN)