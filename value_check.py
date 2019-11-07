from selenium import webdriver
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value_picture = browser.find_element_by_id("treasure")
    value_picture_1 = value_picture.get_attribute("valuex")
    
    x = value_picture_1
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

