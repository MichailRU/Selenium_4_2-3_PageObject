from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BOTTOM_BASKET_ADD = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    ALERT_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')
