import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestNavigateToForgotPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_forgot_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.delete_all_cookies()
        main_page.refresh_page()
        main_page.close_modal_if_present()
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_forgot_password()
        assert "/forgot-password" in login_page.get_current_url()