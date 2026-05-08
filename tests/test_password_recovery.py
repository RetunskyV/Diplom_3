import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from data import BASE_URL, TEST_USER_EMAIL


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_forgot_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.prepare_clean_session()
        main_page.click_login_button()
        LoginPage(driver).click_forgot_password()
        assert "/forgot-password" in driver.current_url

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_recover_password_with_email(self, driver):
        page = ForgotPasswordPage(driver)
        page.open_url(f"{BASE_URL}/forgot-password")
        page.input_email(TEST_USER_EMAIL)
        page.click_recover()
        page.wait_for_url("/reset-password")
        assert "/reset-password" in page.get_current_url()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_active_field(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_url(f"{BASE_URL}/forgot-password")
        forgot_page.input_email(TEST_USER_EMAIL)
        forgot_page.click_recover()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_for_url("/reset-password")
        reset_page.click_eye_icon()
        assert reset_page.is_password_field_active()
