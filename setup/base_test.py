import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class BaseTest:

    def setup_method(self):
        """Initialize Chrome driver with best recommended settings."""

        chrome_options = Options()

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--ignore-certificate-errors")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=chrome_options)
        logger.info("Chrome launched successfully.")

        # If no JSON, store credentials directly here or inside test
        self.email = "chelseasudip430@gmail.com"
        self.password = "Protectmy@ccount11"

    def teardown_method(self):
        """Close browser after each test."""
        self.driver.quit()

    def open_url(self, url):
        """Navigate to URL."""
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)
