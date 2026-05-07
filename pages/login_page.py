from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):
    def input_email(self, email):
        self.input_text(LoginPageLocators.FIELD_EMAIL, email)

    def input_password(self, password):
        self.input_text(LoginPageLocators.FIELD_PASSWORD, password)

    def click_login(self):
        self.click_element(LoginPageLocators.BTN_LOGIN)

    def click_forgot_password(self):
        self.click_element(LoginPageLocators.LINK_FORGOT_PASSWORD)

    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login()
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.BTN_ORDER))
        import time; time.sleep(1)
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
        time.sleep(0.5)
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
