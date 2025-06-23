from selenium.webdriver.common.by import By

from Pageobjects.checkout_confirmation import CheckOutConfirmation


class ShopPage:

    def __init__(self,driver):
        self.driver = driver
        self.shop_link = (By.LINK_TEXT, "Shop")
        self.products_carts=(By.XPATH, "//div[@class='card h-100']")
        self.button=(By.CLASS_NAME, "btn-primary")




    def add_product_cart(self,productname):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.products_carts)

        for product in products:
            product_name = product.find_element(By.XPATH, 'div/h4/a').text
            if product_name == productname:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.button).click()

        checkout_confirm=CheckOutConfirmation(self.driver)
        return checkout_confirm
