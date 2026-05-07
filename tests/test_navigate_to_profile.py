import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestNavigateToProfile:

    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_navigate_to_profile(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login("test_v@pochta.ru", "123456")
        MainPage(driver).click_personal_account()
        assert ProfilePage(driver).is_profile_page()
