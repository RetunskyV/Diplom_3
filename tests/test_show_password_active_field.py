import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestShowPasswordActiveField:

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_active_field(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_url(f"{BASE_URL}/forgot-password")
        forgot_page.input_email("test_v@pochta.ru")
        forgot_page.click_recover()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_for_url("/reset-password")
        reset_page.click_eye_icon()
        assert reset_page.is_password_field_active()