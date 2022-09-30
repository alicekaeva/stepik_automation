import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(int(x) + int(y))


try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = browser.find_element(By.ID, 'num1')
    x = value1.text
    value2 = browser.find_element(By.ID, 'num2')
    y = value2.text
    ans = calc(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(ans)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(7)
    browser.quit()
