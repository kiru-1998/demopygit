from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckOutConfirmation:


    def __init__(self,driver):
        self.driver = driver
        self.checkout_btn = (By.CSS_SELECTOR, ".btn.btn-success")
        self.country = (By.ID, "country")
        self.country_option=(By.LINK_TEXT, "India")
        self.submit_btn=(By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
        self.success_message=(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")


    def Checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

    def delivery_address(self,countryName):
        self.driver.find_element(*self.country).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.submit_btn).click()


    def validate(self):
        msg = self.driver.find_element(*self.success_message).text
        assert 'Success! Thank you!' in msg






