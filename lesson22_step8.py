import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys('ds')
    last = browser.find_element(By.NAME, 'lastname')
    last.send_keys('ds')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('ds')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(3)
    browser.quit()