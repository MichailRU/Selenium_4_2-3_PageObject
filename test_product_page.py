import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207'


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207'
    page = ProductPage(browser, link)                # инициализация PageObject, передаем экземпляр драйвера и url адрес
    page.open()                                      # открываем страницу
    page.go_to_basket_page()                         # проверка существования кнопки корзины и переход по ней
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_item_in_basket()       # проверка, что в корзине нет товаров
    basket_page.should_be_message_of_empty_basket()  # проверка, что существует сообщение о пустой корзине


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207'
    page = ProductPage(browser, link)             # инициализация PageObject, передача экземпляр драйвера и url адрес
    page.open()                                   # открываем страницу
    obj = page.should_be_bottom_basket()          # проверка корректности страницы
    obj.click()                                   # кликаем по корзине
    page.should_not_be_success_message()          # проверяем что нет сообщения об успехе (False)


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207'
    page = ProductPage(browser, link)             # инициализация PageObject, передача экземпляр драйвера и url адрес
    page.open()                                   # открываем страницу
    page.should_not_be_success_message()          # проверяем что нет сообщения об успехе (True)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207'
    page = ProductPage(browser, link)             # инициализация PageObject, передача экземпляр драйвера и url адрес
    page.open()                                   # открываем страницу
    obj = page.should_be_bottom_basket()          # проверка корректности страницы
    obj.click()                                   # кликаем по корзине
    page.should_disappeared_of_success_message()  # проверяем, сообщения об успехе исчезает (False)


@pytest.mark.skip
@pytest.mark.parametrize('page', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, page):
    # Проверка функционала добавления товара в корзину
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{page}'
    page = ProductPage(browser, link)       # инициализация PageObject, передача экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    obj = page.should_be_bottom_basket()    # проверка корректности страницы
    obj.click()                             # кликаем по корзине
    kod = page.solve_quiz_and_get_code()    # получение проверочного кода
    page.should_be_correct_add_to_basket()  # проверка корректности добавления в корзину
    print(f'The received code = {kod}')
