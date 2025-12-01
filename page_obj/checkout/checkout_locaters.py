from selenium.webdriver.common.by import By


class CheckoutLocators(object):
    CHECKOUT_BUTTON=(By.XPATH,"//button[normalize-space()='Proceed to check out']")
    ADD_DELIVERY_BUTTON=(By.XPATH,"//a[@class='addnew-btn']")
    DELIVERY_ADDRESS=(By.XPATH,"//div[@class='address-map']//label//input")
    CLOSE_ADDRESS_POPUP=(By.XPATH,"//img[@alt='cross']")
    CONFIRMATION_CALL=(By.XPATH,"//label[@for='call-yes']")
    DELIVERY_DAY=(By.XPATH,"//a[normalize-space()='Tomorrow']")
    DELIVERY_NOTE=(By.XPATH,"//div[contains(text(),'Driver Note')]/textarea")
    PAYMENT_METHOD=(By.XPATH,"//label[@for='radiobtn']")