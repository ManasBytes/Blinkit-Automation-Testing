from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .constants import PHONE_NUMBER

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)  # max 2 minutes

    def login(self):
        # 1. Click Login button on home page
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[normalize-space()='Login']")
            )
        )
        login_button.click()

        # 2. Enter phone number
        phone_input = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='tel']")
            )
        )
        phone_input.send_keys(PHONE_NUMBER)

        # 3. Click Continue
        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Continue']")
            )
        )
        continue_button.click()

        # 4. WAIT for OTP login to complete (manual)
        # Login button should disappear after successful login
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[normalize-space()='Login']")
            )
        )
