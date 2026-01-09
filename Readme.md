# Blinkit Web Automation (Selenium – Python)

This project is a low-level end-to-end UI automation of a real user flow on the Blinkit website using Selenium with Python.
It simulates how an actual user interacts with the platform — from opening the site to adding multiple items to the cart and verifying the final cart price.

The goal of this project is learning and practicing website testing fundamentals, not building a production-grade framework.

## Warning
From the Constants Folder, Change the Constants of your project to your phone_number.



# Final Aim of the Project

The main objective is to automate and validate the following user journey:
1. Open the Blinkit website

2. Set delivery location

3. Log in using the available authentication flow

4. Navigate to the Fruits & Vegetables section

5. Add multiple items (10–20) to the cart

6. Open the cart

7. Extract and print the final total price in the terminal

Checkout and payment are intentionally excluded, as Blinkit restricts order completion to the mobile app.

# Project Structure
>blinkit-selenium-automation/
>│
>├── pages/
>│   ├── constants.py
>│   ├── login_page.py
>│   ├── location_page.py
>│   ├── home_page.py
>│   ├── fruits_vegetables_page.py
>│   ├── cart_page.py
>│
>├── test_results/
>│   └── execution_result.xlsx
>│
>├── run.py
>├── requirements.txt
>└── README.md

## Folder Explanation
<ul> 
<li> <b> pages/ </b> <br>
Contains Page Object Model (POM) classes for different parts of the website. </li>

<li> <b> constants.py </b> <br>
Stores reusable constants like:
<ul> 
 <li> Website URL </li>

<li>Items to add to cart </li>

<li>Quantity per item </li>

</ul>

Since this is a personal learning project, this file is kept simple and not over-engineered.</li>

<li> <b>run.py </b> <br>
Entry point of the project. <br>
Executes the complete automation flow from start to finish.  </li>



<li> <b> test_results/ </b> <br>
Stores test execution output in Excel format. </li>
</ul>


#  How to Run the Project

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies
> pip install -r requirements.txt


### 3. Run Automation
> py run.py


# Output
Test result would be printed in execution_result.xlsx. But the final cart price would be printed at the terminal directly.