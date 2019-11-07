from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os 
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input_name = browser.find_element_by_css_selector(".form-group :nth-child(2)")
    input_name.send_keys("Ivan")
    
    input_lastName = browser.find_element_by_css_selector(".form-group :nth-child(4)")
    input_lastName.send_keys("Petrov")
    
    input_email = browser.find_element_by_css_selector(".form-group :nth-child(6)")
    input_email.send_keys("aa@mail.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')
    
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    time.sleep(20)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()