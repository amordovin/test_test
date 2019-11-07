﻿from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button1 = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
   
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()



finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()