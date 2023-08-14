import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException


# абстрактный класс с вспомогательными методами для работы с драйвером
class BasePage:
    def __init__(self, browser, url):
        # Конструктор с созданием переменных экземпляра класса
        self.browser = browser
        self.url = url

    def open(self):
        # Открытие необходимой страницы по url, указанному при создании экземпляра
        self.browser.get(self.url)

    def is_element_present(self, timeout, *locator):
        # Проверка наличия элемента на странице. Возвращает элемент по заданному локатору.
        # Если элемент отсутствует или превышено время ожидания timeout - возвращается False
        try:
            out = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            out = False
        return out

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
