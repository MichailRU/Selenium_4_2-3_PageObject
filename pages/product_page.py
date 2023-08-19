from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_basket(self):    # добавить в корзину - нажатие кнопки
        self.is_element_present(*ProductPageLocators.BUTTON_BASKET_ADD).click()

    def should_be_button_basket(self):    # проверка нахождения на странице товара
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET_ADD), 'There is no add to cart button'
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), 'No books for sale'
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), 'There is no price of books sold'

    def should_be_correct_add_to_basket(self):    # проверка корректности добавления товара в корзину
        n1 = self.is_element_present(*ProductPageLocators.BOOK_NAME).text
        p1 = self.is_element_present(*ProductPageLocators.BOOK_PRICE).text
        n2 = self.is_element_present(*ProductPageLocators.ALERT_NAME).text
        p2 = self.is_element_present(*ProductPageLocators.ALERT_PRICE).text
        assert n1 == n2, f'The name of the book being added is "{n1}", in fact "{n2}"'
        assert p1 == p2, f'The price of the book being added is "{p1}", in fact "{p2}"'

    def should_disappeared_of_success_message(self):    # проверяем, что сообщение о добавлении товара исчезает
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout=10), 'Success message not disappeared'

    def should_not_be_success_message(self):    # проверяем что нет сообщения о добавлении товара в корзину
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented'
