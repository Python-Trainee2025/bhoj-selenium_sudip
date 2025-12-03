import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Updated Logging Configuration

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s'
)
logger = logging.getLogger(__name__)


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request):
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

        # Launch Chrome
        self.driver = webdriver.Chrome(options=chrome_options)
        logger.info("Chrome launched successfully.")

        # FOR PYTEST-HTML SCREENSHOTS
        #request.node._driver = self.driver

        # Credentials
        self.cred = {
            "base_url": "https://www.bhojdeals.com/",
            "email": "chelseasudip430@gmail.com",
            "password": "Protectmy@ccount11"
        }

        self.email = self.cred["email"]
        self.password = self.cred["password"]

        yield

        logger.info("Closing Chrome browser.")
        self.driver.quit()

    # Optional utility
    def open_url(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)
