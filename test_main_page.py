import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)      # инициализация PageObject, передаем экземпляр драйвера и url адрес
        page.open()                         # открываем страницу
        page.should_be_login_link()         # проверка существования линка логина
        page.go_to_login_page()             # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()   # проверка url, форм логина и регистрации

    def test_guest_should_see_login_link(self, browser):
        # Проверка, что есть ссылка, которая ведет на логин
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)                   # инициализация PageObject, передаем экземпляр драйвера и url адрес
    page.open()                                      # открываем страницу
    page.go_to_basket_page()                         # проверка существования кнопки корзины и переход по ней
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_item_in_basket()       # проверка, что в корзине нет товаров
    basket_page.should_be_message_of_empty_basket()  # проверка, что существует сообщение о пустой корзине
