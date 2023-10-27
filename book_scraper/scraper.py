import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

try:
    browser.maximize_window()
    browser.get('https://www.goodreads.com/book/show/44767458-dune')
    time.sleep(3)
    time.sleep(4)

    # Wait for the button to load (you might need to adjust the timeout)
    button = browser.find_element(By.CLASS_NAME, 'Button--buy')
    time.sleep(2)
    button.click()

    time.sleep(5)

    # Extract the link
    anchor_element = browser.find_element(By.CLASS_NAME, 'a-button-inner')

    # Extract the href attribute from the anchor element
    link = anchor_element.get_attribute('href')

    # Print the link
    print ("Link: ", link)


    # Print the link
    print("Link: ", link)

except Exception as e:
    print("Error: ", str(e))

finally:
    # Close the browser
    browser.quit()
