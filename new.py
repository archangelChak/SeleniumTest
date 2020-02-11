import time
import math
import pytest
from selenium import webdriver

list1=["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]

@pytest.fixture(scope="function")
def browser():
    browser=webdriver.Chrome()
    yield browser
    browser.quit()
@pytest.mark.parametrize('link',list1)
def test_pieces(browser,link):
    browser.get(link)
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_css_selector('.textarea.string-quiz__textarea.ember-text-area.ember-view')
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))
    button = browser.find_element_by_css_selector('button.submit-submission')
    button.click()
    check = browser.find_element_by_css_selector('pre.smart-hints__hint').text
    assert check == "Correct!", f"{check}"
    