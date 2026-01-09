from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_fruits_and_vegetables(self):
        category = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[contains(@alt,'Fruits')]")
            )
        )
        self.driver.execute_script("arguments[0].click();", category)
