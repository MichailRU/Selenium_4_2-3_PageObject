from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):  # проверка, что есть поля формы регистрации и сама регистрация
        reg_email = self.is_element_present(*LoginPageLocators.REGISTER_EMAIL)
        assert reg_email, 'Email field is not presented on the registration form'
        reg_email.send_keys(email)
        reg_pwd1 = self.is_element_present(*LoginPageLocators.REGISTER_PWD1)
        assert reg_pwd1, 'Password-1 field is not presented on the registration form'
        reg_pwd1.send_keys(password)
        reg_pwd2 = self.is_element_present(*LoginPageLocators.REGISTER_PWD2)
        assert reg_pwd2, 'Password-2 field is not presented on the registration form'
        reg_pwd2.send_keys(password)
        reg_btn = self.is_element_present(*LoginPageLocators.REGISTER_BUTTON)
        assert reg_btn, 'Register button is not presented on the registration form'
        reg_btn.click()

    def should_be_login_form(self):    # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_login_page(self):    # проверка, что есть страница логина (url + формы регистрации и логина)
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):    # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, 'Login url is not correct'

    def should_be_register_form(self):    # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
