""" Retrieve all the Users and password related information and store it 
    in Sheet named "User credentials" in a excel file.
    User ID, User Name, Password """
import weblauch as web
import pandas as pd
from selenium.webdriver.common.by import By

def retrieve_user_credentials():
    """
    Retrieves the usernames and passwords from a web page.

    Returns:
        usernames (list): List of usernames.
        pass_words (list): List of passwords.
    """
    driver = web.weblauch()

    element = driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
    text = element.text
    usernames = text.split("\n")[1:]

    pass_word = driver.find_element(By.XPATH, '//div[@class="login_password"]')
    text1 = pass_word.text
    pass_words = text1.split("\n")[1:]

    driver.quit()

    return usernames, pass_words

def save_user_credentials(usernames, pass_words):
    """
    Saves the usernames and passwords to an Excel file.

    Args:
        usernames (list): List of usernames.
        pass_words (list): List of passwords.
    """
    data = {"User ID": range(1, len(usernames) + 1),
            "User Name": usernames,
            "Password": pass_words * len(usernames)}

    df = pd.DataFrame(data)
    df.to_excel("User credentials.xlsx",sheet_name="User Details", index=False)

def main():
    """Main function to retrieve and save user credentials."""
    usernames, pass_words = retrieve_user_credentials()
    save_user_credentials(usernames, pass_words)

if __name__ == "__main__":
    main()
