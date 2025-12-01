import time
import logging
from setup.base_test import BaseTest
from page_obj.login.login_page import LoginPage


class TestEditProfile(BaseTest):

    def test_edit_profile_name(self):

        logging.info("Starting Edit Profile Test")

        # Step 1: Open website
        logging.info("Opening Bhojdeals website")
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)
        logging.info("LoginPage initialized for profile edit")

        # Step 2: Login
        logging.info(f"Logging in with email: {self.email}")
        login.login(self.email, self.password)
        time.sleep(4)

        # Step 3: Click My Account
        logging.info("Opening My Account page")
        login.open_my_account()

        # Step 4: Open Edit Profile
        logging.info("Opening Edit Profile page")
        login.open_edit_profile()

        # Step 5: Change username to 'Sudip Bhandari'
        logging.info("Editing username to 'Sudip Bhandari'")
        login.edit_username("Sudip Bhandari")

        # Step 6: Submit profile
        logging.info("Submitting updated profile")
        login.submit_profile()

        # Step 7: Verify the username saved successfully
        logging.info("Verifying updated username")
        updated_name = login.profile_username_input.get_attribute("value")

        assert updated_name == "Sudip Bhandari", "Profile name was NOT updated!"

        logging.info(f"Profile name updated successfully: {updated_name}")
