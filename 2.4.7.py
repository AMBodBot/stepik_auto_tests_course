from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from math import log, sin

try:
    #Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))

    #Нажать на кнопку "Book"
    browser.find_element(By.ID, "book").click()

    #Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = int(browser.find_element(By.ID, "input_value").text)
    f = log(abs(12 * sin(x)))
    browser.find_element(By.ID, "answer").send_keys(f)
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)

finally:
    browser.quit()