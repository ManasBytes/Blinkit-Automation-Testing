import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class FruitsVegetablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def add_items_to_cart(self, item_count):
        added = 0
        index = 0

        while added < item_count:
            try:
                # Re-fetch ADD buttons every loop (React-safe)
                add_buttons = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, "//div[normalize-space()='ADD']")
                    )
                )

                if index >= len(add_buttons):
                    break

                add_btn = add_buttons[index]

                # Bring into view
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", add_btn
                )
                time.sleep(0.4)

                # Click ADD (JS click = safest)
                self.driver.execute_script("arguments[0].click();", add_btn)
                time.sleep(0.4)

                added += 1
                index += 1

            except StaleElementReferenceException as e:
                print(f'{index},{e}')
                continue

            except Exception as e:
                print(f'{index},{e}')
                index += 1
                continue
