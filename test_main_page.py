from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/'


def test_can_go_to_login_page(browser):
    browser.get(link)                                                   # открываем страницу по адресу link
    login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')   # ищем элемент
    login_link.click()                                                  # кликаем по нему
