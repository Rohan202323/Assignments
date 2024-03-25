"""function"""
from selenium import webdriver

def weblauch():
    """It will lauch the web"""
    
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    return driver