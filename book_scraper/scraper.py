import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

try:
    browser.maximize_window()
    browser.get('https://www.goodreads.com/book/show/18373.Flowers_for_Algernon?ref=nav_sb_ss_1_20')
    time.sleep(5)

    summary = browser.find_element(By.CLASS_NAME, "BookPageMetadataSection__description").text
    time.sleep(2)
    more_info_button = browser.find_element(By.XPATH, "//*[text()='Book details & editions']")
    more_info_button.click()

    edition_details = browser.find_element(By.CLASS_NAME, "EditionDetails").text
    print(summary)
except:
    pass
finally:
    browser.close()
    browser.quit()