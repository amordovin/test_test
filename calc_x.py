import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

link_one = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link_one)
try:
    
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
   
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()