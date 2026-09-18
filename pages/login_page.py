import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Войти в аккаунт')
    def login(self, email, password):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_via_script(LoginPageLocators.LOGIN_BUTTON)

