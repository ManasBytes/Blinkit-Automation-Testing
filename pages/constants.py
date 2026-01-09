from dotenv import load_dotenv


load_dotenv()

import os


BLINKIT_URL = "https://www.blinkit.com"
PHONE_NUMBER = os.environ.get("PHONE")
ITEMS_TO_ADD = 10
QUANTITY_PER_ITEM = 2
