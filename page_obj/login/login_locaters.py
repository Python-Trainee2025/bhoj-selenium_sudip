from selenium.webdriver.common.by import By


class LoginLocator:
    LOGIN_BTN_NAV = (By.XPATH, "//a[text()='login']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(),'Login')]")
    LOGIN_ERROR = (By.CSS_SELECTOR, "div.alert.alert-dismissible.alert-danger")
    LOGOUT_BTN = (By.XPATH, '//*[@id="nav_collapse"]/ul/ul/li[2]/a')
    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        '//*[@id="mybhojapp"]/div[6]/section/div/div/div/div/form/div/div/div/div[1]/a[1]')
    MY_ACCOUNT_BTN = (By.XPATH, '//*[@id="nav_collapse"]/ul/ul/li[1]/a')
    EDIT_PROFILE_BTN = (By.XPATH, '//*[@id="mybhojapp"]/section/div/div/div[1]/div/ul/li[2]/a')
    PROFILE_USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    PROFILE_SUBMIT_BTN = (By.XPATH, '//*[@id="mybhojapp"]/section/div/div/div[2]/div/form/button')

    LOGIN_BTN_NAV = (By.XPATH, "//a[translate(text(),'LOGIN','login')='login']")

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@placeholder='Email' or @id='email' or @name='email' or contains(@class,'email')]"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@placeholder='Password' or @id='password' or @name='password' or contains(@class,'password')]"
    )

    LOGIN_SUBMIT = (
        By.XPATH,
        "//button[contains(text(),'Login') or @type='submit' or contains(@class,'login')]"
    )

    LOGIN_ERROR = (By.CSS_SELECTOR, "div.alert.alert-dismissible.alert-danger")



