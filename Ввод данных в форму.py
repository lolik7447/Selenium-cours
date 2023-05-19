from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    link = browser.find_element(By.PARTIAL_LINK_TEXT, link_text)
    link.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Kuzya")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Khabarovsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
