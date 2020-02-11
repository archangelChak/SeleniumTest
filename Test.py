from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    f_name = browser.find_element(By.CSS_SELECTOR, 'div.container > form > div.first_block > div.form-group.first_class > input')
    f_name.send_keys('Ihor')
    l_name = browser.find_element(By.CSS_SELECTOR, 'div.container > form > div.first_block > div.form-group.second_class > input')
    l_name.send_keys('Myhorsky')
    e_mail = browser.find_element(By.CSS_SELECTOR, 'body > div.container > form > div.first_block > div.form-group.third_class > input')
    e_mail.send_keys('mail')



    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully pegistered!" == welcome_text


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

