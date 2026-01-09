from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_cart(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'CartButton__Text')]")
            )
        )
        cart_button.click()

    def print_cart_total_price(self):
        total_price_element = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'CheckoutStrip__NetPriceText')]"
                )
            )
        )

        total_price = total_price_element.text
        print(f"\n Cart Total Price: {total_price}\n")

        return total_price
