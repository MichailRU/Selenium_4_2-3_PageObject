from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_of_empty_basket(self):    # проверка, что есть сообщение о пустой корзине
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), 'Not message of empty basket'

    def should_be_not_item_in_basket(self):    # проверка, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), 'Not items in Basket'
