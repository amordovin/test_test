from selenium import webdriver
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    browser.execute_script("window.scrollBy(0, 130);")
    
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()