import time

from selenium import webdriver

link_one = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link_one)
try:
    input_first_name = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input_last_name.send_keys("Ivanov")
    input_email = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input_email.send_keys("Ivanov@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()