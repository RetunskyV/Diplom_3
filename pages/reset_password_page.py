from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):
    def click_eye_icon(self):
        self.click_element(ResetPasswordLocators.ICON_EYE)

    def is_password_field_active(self):
        return self.is_displayed(ResetPasswordLocators.FIELD_ACTIVE)