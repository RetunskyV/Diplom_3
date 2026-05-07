import allure
from pages.forgot_password_page import ForgotPasswordPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestRecoverPasswordWithEmail:

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_recover_password_with_email(self, driver):
        page = ForgotPasswordPage(driver)
        page.open_url(f"{BASE_URL}/forgot-password")
        page.close_modal_if_present()
        page.input_email("test_v@pochta.ru")
        page.click_recover()
        page.wait_for_url("/reset-password")
        assert "/reset-password" in page.get_current_url()