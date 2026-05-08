import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Ввод email для восстановления пароля")
    def input_email(self, email):
        self.input_text(ForgotPasswordLocators.FIELD_EMAIL, email)

    @allure.step("Клик на кнопку «Восстановить»")
    def click_recover(self):
        self.click_element(ForgotPasswordLocators.BTN_RECOVER)

    @allure.step("Клик на ссылку «Войти»")
    def click_login_link(self):
        self.click_element(ForgotPasswordLocators.LINK_LOGIN)
