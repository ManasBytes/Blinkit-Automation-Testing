import time

class LocationPage:
    def __init__(self, driver):
        self.driver = driver

    def set_location(self, location):
        location_input = self.driver.find_element(
            "xpath",
            '//*[@id="app"]/div/div/div[1]/header/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/input'
        )

        location_input.click()
        location_input.send_keys(location)
        time.sleep(2)

        # Find the exact "Bandra Terminus" option
        option = self.driver.find_element(
            "xpath",
            "//div[normalize-space()='Bandra Terminus']"
        )

        # JS click (more reliable for React)
        self.driver.execute_script("arguments[0].click();", option)

        time.sleep(3)
