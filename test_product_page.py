import pytest
from pages.product_page import ProductPage
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207'


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)             # инициализация PageObject, передача экземпляр драйвера и url адрес
    page.open()                                   # открываем страницу
    obj = page.should_be_bottom_basket()          # проверка корректности страницы
    obj.click()                                   # кликаем по корзине
    page.should_not_be_success_message()          # проверяем что нет сообщения об успехе (False)


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)             # инициализация PageObject, передача экземпляр драйвера и url адрес
    page.open()                                   # открываем страницу
    page.should_not_be_success_message()          # проверяем что нет сообщения об успехе (True)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
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
