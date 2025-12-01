from page_obj.login.login_locaters import  LoginLocator


class LoginProperties:

    @property
    def nav_login_btn(self):
        return self.driver.find_element(*LoginLocator.LOGIN_BTN_NAV)

    @property
    def email(self):
        return self.driver.find_element(*LoginLocator.EMAIL_INPUT)

    @property
    def password(self):
        return self.driver.find_element(*LoginLocator.PASSWORD_INPUT)

    @property
    def submit_btn(self):
        return self.driver.find_element(*LoginLocator.LOGIN_SUBMIT)

    @property
    def error_message(self):
        return self.driver.find_element(*LoginLocator.LOGIN_ERROR)

    @property
    def logout_btn(self):
        return self.driver.find_element(*LoginLocator.LOGOUT_BTN)

    @property
    def forgot_password_link(self):
        return self.driver.find_element(*LoginLocator.FORGOT_PASSWORD_LINK)

    @property
    def my_account_btn(self):
        return self.driver.find_element(*LoginLocator.MY_ACCOUNT_BTN)

    @property
    def edit_profile_btn(self):
        return self.driver.find_element(*LoginLocator.EDIT_PROFILE_BTN)

    @property
    def profile_username_input(self):
        return self.driver.find_element(*LoginLocator.PROFILE_USERNAME_INPUT)

    @property
    def profile_submit_btn(self):
        return self.driver.find_element(*LoginLocator.PROFILE_SUBMIT_BTN)

