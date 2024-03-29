﻿from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.implicitly_wait(5)
    
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_id("book")
    button.click()
    
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button1 = browser.find_element_by_id("solve")
    button1.click()
    
finally:
       time.sleep(15)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
       browser.quit()