from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "This Login link is not valid"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "There is no Login form on this link"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "There is no Register form on this link"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_FORM)
        reg_email.send_keys(email)
        reg_pswrd1 = self.browser.find_element(*LoginPageLocators.PASS_REGISTRATION_FORM1)
        reg_pswrd1.send_keys(password)
        reg_pswrd2 = self.browser.find_element(*LoginPageLocators.PASS_REGISTRATION_FORM2)
        reg_pswrd2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        reg_btn.click()