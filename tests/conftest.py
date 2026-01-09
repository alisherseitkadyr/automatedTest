import pytest
from selenium import webdriver
from utils.driver_manager import DriverManager


@pytest.fixture(scope="function")
def driver():
    """WebDriver fixture for each test"""
    driver = DriverManager.get_chrome_driver()
    driver.get("https://automationexercise.com/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(driver):
    """Home page fixture"""
    from pages.home_page import HomePage
    return HomePage(driver)


@pytest.fixture(scope="function")
def login_page(driver):
    """Login page fixture"""
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture(scope="function")
def products_page(driver):
    """Products page fixture"""
    from pages.products_page import ProductsPage
    return ProductsPage(driver)


@pytest.fixture(scope="function")
def cart_page(driver):
    """Cart page fixture"""
    from pages.cart_page import CartPage
    return CartPage(driver)