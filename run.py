from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

from pages.constants import BLINKIT_URL, ITEMS_TO_ADD, QUANTITY_PER_ITEM
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.fruits_vegetables_page import FruitsVegetablesPage
# from pages.groceries_page import GroceriesPage
from pages.cart_page import CartPage
from pages.location_page import LocationPage

results = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get(BLINKIT_URL)
    
    LocationPage(driver).set_location("Bandra Terminus")

    LoginPage(driver).login()
    HomePage(driver).go_to_fruits_and_vegetables()
    FruitsVegetablesPage(driver).add_items_to_cart(ITEMS_TO_ADD)
    CartPage(driver).open_cart()
    CartPage(driver).print_cart_total_price()

    results.append(["Add groceries and verify cart", "PASS"])

except Exception as e:
    print(e)
    results.append(["Add groceries and verify cart", "FAIL"])

finally:
    df = pd.DataFrame(results, columns=["Test Case", "Status"]) 
    # print (df)
    df.to_excel("test_results/execution_result.xlsx", index=False)
    driver.quit()
