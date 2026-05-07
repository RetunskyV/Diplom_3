from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    def input_email(self, email):
        self.input_text(ForgotPasswordLocators.FIELD_EMAIL, email)

    def click_recover(self):
        self.click_element(ForgotPasswordLocators.BTN_RECOVER)

    def click_login_link(self):
        self.click_element(ForgotPasswordLocators.LINK_LOGIN)

    from locators.main_page_locators import MainPageLocators

    def close_modal_if_present(self):
        try:
            self.click_element(MainPageLocators.MODAL_CLOSE)
        except:
            pass