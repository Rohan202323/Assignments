"""Try login with all the Users provided on the website link https://www.saucedemo.com/v1/ and 
    record any error messages 
    displayed for a specific user. write this information to another sheet named "Login" 
    in the same excel file as above 
    in the following format.
    User ID, Login Message"""

import time
import weblauch as web
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def perform_login(user, password, driver):
    """
    Performs login using the provided user credentials.

    Args:
        user (str): Username.
        password (str): Password.
        driver: Selenium WebDriver instance.

    Returns:
        str: Error message if login fails, empty string otherwise.
    """
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    username_field.clear()
    password_field.clear()

    username_field.send_keys(user)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)
    driver.back()

    error_message = ""
    try:
        error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3').text
    except NoSuchElementException:
        pass

    return error_message

def login_user_credentials():
    """
    Login with user credentials and save the login results to an Excel file.
    """
    driver = web.weblauch()
    user_credentials = pd.read_excel("User credentials.xlsx")
    login_results = pd.DataFrame(columns=["User ID", "Login Message"])

    for index, row in user_credentials.iterrows():
        user_id = row["User ID"]
        user = row["User Name"]
        password = row["Password"]

        error_message = perform_login(user, password, driver)

        new_data = {"User ID": [user_id], "Login Message": [error_message]}
        new_df = pd.DataFrame(new_data)
        login_results = pd.concat([login_results, new_df])

    driver.quit()

    with pd.ExcelWriter("User credentials.xlsx", mode="a", engine="openpyxl") as writer:
        login_results.to_excel(writer, sheet_name="Login", index=False)

if __name__ == "__main__":
    login_user_credentials()
