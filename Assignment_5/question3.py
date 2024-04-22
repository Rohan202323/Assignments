""" Login using the "standard_user" and retrieve all the product related information for every listed product. 
    Write this information into a separate sheet named "Product Details" in the same excel file.
    Product ID, Product Name, Description, Price """

import time
import pandas as pd
import weblauch as web
from selenium.webdriver.common.by import By

def retrieve_product_details():
    """
    Retrieves the product details from a web page and saves them to an Excel file.
    """
    driver = web.weblauch()

    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    time.sleep(2)
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    time.sleep(4)
    # Retrieve product information
    product_elements = driver.find_elements(By.XPATH, "//div[@class='inventory_item']")

    product_details = []

    for product_element in product_elements:
        product_id = product_element.find_element(By.XPATH, ".//div[@class='inventory_item_img']/a").get_attribute(
            "href").split("=")[-1]
        product_name = product_element.find_element(By.XPATH, ".//div[@class='inventory_item_name']").text
        product_description = product_element.find_element(By.XPATH, ".//div[@class='inventory_item_desc']").text
        product_price = product_element.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text

        product_details.append({
            "Product ID": product_id,
            "Product Name": product_name,
            "Description": product_description,
            "Price": product_price
        })

    # Close the driver
    driver.quit()

    df_product_details = pd.DataFrame(product_details)

    with pd.ExcelWriter("User credentials.xlsx", mode="a", engine="openpyxl") as writer:
        df_product_details.to_excel(writer, sheet_name="Product Details", index=False)

if __name__ == "__main__":
    retrieve_product_details()

