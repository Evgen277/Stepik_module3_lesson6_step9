import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_buy_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.implicitly_wait(10)
    button = browser.find_element_by_class_name("btn")
    assert button, "Кнопка не найдена"
    
