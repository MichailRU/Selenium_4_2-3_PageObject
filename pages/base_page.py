class BasePage:
    def __init__(self, browser, url):    # конструктор с созданием переменных экземпляра класса
        self.browser = browser
        self.url = url

    def open(self):    # открытие необходимой страницы по url, указанному при создании экземпляра
        self.browser.get(self.url)
