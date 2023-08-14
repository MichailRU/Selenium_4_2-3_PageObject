from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# Класс описываемый конкретную страницу и наследуемый от BasePage
class MainPage(BasePage):
    def should_be_login_link(self):
        # Проверка наличия ссылки
        assert self.is_element_present(10, By.CSS_SELECTOR, '#login_link'), 'Login link is not presented'

    def go_to_login_page(self):
        # Переход на страницу login
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')    # ищем элемент
        login_link.click()    # кликаем по нему
