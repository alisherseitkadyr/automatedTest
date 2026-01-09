from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os


class DriverManager:
    """Manages WebDriver instances for different browsers"""
    
    @staticmethod
    def get_chrome_driver():
        """Initialize Chrome WebDriver with options"""
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-extensions')
        # Uncomment for headless execution
        # options.add_argument('--headless')
        
        # webdriver-manager sometimes returns a path to a non-executable
        # file (for example a LICENSE or THIRD_PARTY_NOTICES file) instead
        # of the actual chromedriver binary. Resolve the returned path and
        # prefer the real 'chromedriver' executable when present in the
        # same directory.
        installed_path = ChromeDriverManager().install()
        # If the returned name is not the actual binary, look for one
        bin_dir = os.path.dirname(installed_path)
        candidate = os.path.join(bin_dir, 'chromedriver')
        if os.path.exists(candidate) and os.access(candidate, os.X_OK):
            driver_path = candidate
        else:
            # fall back to whatever webdriver-manager returned
            driver_path = installed_path

        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    
    @staticmethod
    def get_firefox_driver():
        """Initialize Firefox WebDriver with options"""
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        return driver