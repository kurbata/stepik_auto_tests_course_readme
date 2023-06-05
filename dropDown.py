import select

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    x_num = int(x)
    y = browser.find_element(By.ID, "num2").text
    y_num = int(y)
    result = str(str(y_num+x_num))
    answer = browser.find_element(By.ID, "dropdown").send_keys(result)
    submit = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']") .click()



finally:
    time.sleep(30)
    browser.quit