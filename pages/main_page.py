from pages.base_page import BasePage
from pages.locators import MainPageLocators


# Класс описываемый конкретную страницу и наследуемый от BasePage
class MainPage(BasePage):
    def should_be_login_link(self):
        # Проверка наличия ссылки
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

    def go_to_login_page(self):
        # Переход на страницу login
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)    # ищем элемент
        login_link.click()    # кликаем по нему
