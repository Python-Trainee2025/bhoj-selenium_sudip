import time
from setup.base_test import BaseTest
from page_obj.login_pom.login_page import LoginPage


class TestEditProfile(BaseTest):

    def test_edit_profile_name(self):
        # Step 1: Open website
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)

        # Step 2: Login
        login.login(self.email, self.password)
        time.sleep(4)

        # Step 3: Click My Account
        login.open_my_account()

        # Step 4: Open Edit Profile
        login.open_edit_profile()

        # Step 5: Change username to "Sudip Bhandari"
        login.edit_username("Sudip Bhandari")

        # Step 6: Submit profile
        login.submit_profile()

        # Step 7: Verify the username saved successfully
        updated_name = login.profile_username_input.get_attribute("value")

        assert updated_name == "Sudip Bhandari", "Profile name was NOT updated!"

        print("Profile name updated successfully:", updated_name)
