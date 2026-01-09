import pytest


class TestProductInteraction:
    """Test cases for Product Interaction"""
    
    def test_product_interaction_with_actionchains(self, home_page, products_page, cart_page):
        """
        Test Case 3: Product Interaction with ActionChains
        - Navigate to products
        - Hover over a product using ActionChains
        - Click "Add to Cart" using ActionChains
        - Verify product added to cart
        """
        print("\n=== Test Case 3: Product Interaction with ActionChains ===")
        print("Using ACTIONCHAINS: hover, move_to_element, click")
        
        # Step 1: Navigate to products page
        home_page.navigate_to_products()
        assert products_page.verify_products_page_loaded(), "Products page not loaded"
        print("✓ Navigated to products page")
        
        # Step 2: Hover over first product using ActionChains
        assert products_page.hover_over_product(0), "Failed to hover over product"
        print("✓ Hovered over product using ActionChains")
        
        # Step 3: Add product to cart using ActionChains
        # ACTIONCHAINS: Complex hover and click action
        products_page.add_product_to_cart_with_hover(0)
        print("✓ Added product to cart using ActionChains")
        
        # Step 4: View cart
        products_page.view_cart()
        assert cart_page.verify_cart_page_loaded(), "Cart page not loaded"
        print("✓ Navigated to cart page")
        
        # Step 5: Verify product added to cart
        assert cart_page.get_cart_items_count() > 0, "No products in cart"
        print(f"✓ Product added to cart. Cart items: {cart_page.get_cart_items_count()}")
        
        print("✓ Product interaction with ActionChains completed successfully")