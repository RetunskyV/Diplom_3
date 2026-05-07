import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestLogout:

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login("test_v@pochta.ru", "123456")
        MainPage(driver).click_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        profile_page.wait_for_url("/login")
        assert "/login" in profile_page.get_current_url()
