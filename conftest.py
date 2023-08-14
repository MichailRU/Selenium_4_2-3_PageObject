# учитывая наличие в тексте программы конструкции match/case необходимо наличие Python версии не ниже 3.10
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # парсер командной строки запускается перед всеми тестами
    parser.addoption('--language', action='store', default='en', help='Choose language')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser')


@pytest.fixture(scope='function')
def browser(request):
    my_language = request.config.getoption('language')
    my_browser = request.config.getoption('browser_name')
    # print(f'my_language = {my_language}, my_browser = {my_browser}')
    match my_browser:
        case 'firefox':
            from selenium.webdriver.firefox.options import Options
            options = Options()
            options.set_preference('intl.accept_languages', my_language)
            driver = webdriver.Firefox(options=options)
        case _:
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': my_language})
            driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
