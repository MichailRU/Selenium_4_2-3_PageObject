import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from pages.locators import BasePageLocators


# абстрактный класс с вспомогательными методами для работы с драйвером
class BasePage:
    def __init__(self, browser, url):
        # Конструктор с созданием переменных экземпляра класса
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        # Переход на страницу login
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)    # ищем элемент
        login_link.click()                                                      # кликаем по нему

    def go_to_basket_page(self):
        # Переход на страницу basket (корзина)
        basket_link = self.is_element_present(*BasePageLocators.BUTTON_BASKET)
        assert basket_link, 'Button basket is not presented'
        basket_link.click()

    def is_disappeared(self, *locator,  timeout=4):
        # Метод, проверяющий, что какой-то элемент исчезает в течение заданного времени.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, *locator, timeout=10):
        # Проверка наличия элемента на странице. Возвращает элемент по заданному локатору.
        # Если элемент отсутствует или превышено время ожидания timeout - возвращается False.
        # Для проводящих код-ревью: метод написан изначально на основе явного ожидания и похож на
        # написанный ниже is_not_element_present - возвращаемое значение not (is_not_element_present).
        try:
            out = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            out = False
        return out

    def is_not_element_present(self, *locator, timeout=4):
        # Метод, который проверяет, что элемент не появляется на странице в течение заданного времени.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def open(self):
        # Открытие необходимой страницы по url, указанному при создании экземпляра
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        # Проверка того, что пользователь прошел авторизацию
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User icon is not presented, probably unauthorised'

    def should_be_login_link(self):
        # Проверка наличия ссылки на страницу login
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def solve_quiz_and_get_code(self):
        # Получение проверочного кода - метод возвращает код или False в случае ошибки
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            return False
