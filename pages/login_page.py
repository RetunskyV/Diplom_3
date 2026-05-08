import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):
    @allure.step("Ввод email")
    def input_email(self, email):
        self.input_text(LoginPageLocators.FIELD_EMAIL, email)

    @allure.step("Ввод пароля")
    def input_password(self, password):
        self.input_text(LoginPageLocators.FIELD_PASSWORD, password)

    @allure.step("Клик на кнопку «Войти»")
    def click_login(self):
        self.click_element(LoginPageLocators.BTN_LOGIN)

    @allure.step("Клик на ссылку «Восстановить пароль»")
    def click_forgot_password(self):
        self.click_element(LoginPageLocators.LINK_FORGOT_PASSWORD)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login()
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.BTN_ORDER))
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
