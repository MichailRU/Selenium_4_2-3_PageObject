from selenium.webdriver.common.by import By


class BasePageLocators:
    BOTTOM_BASKET = (By.CSS_SELECTOR, '.btn-group a')
    LOGIN_LINK = (By.ID, 'login_link')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ALERT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    ALERT_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BOTTOM_BASKET_ADD = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    ITEM_IN_BASKET = (By.CSS_SELECTOR, '#basket_formset')
