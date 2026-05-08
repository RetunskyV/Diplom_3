import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data import BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD


class TestProfile:

    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_navigate_to_profile(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        MainPage(driver).click_personal_account()
        assert ProfilePage(driver).is_profile_page()

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        MainPage(driver).click_personal_account()
        ProfilePage(driver).click_order_history()
        assert "/account/order-history" in ProfilePage(driver).get_current_url()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        MainPage(driver).click_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        profile_page.wait_for_url("/login")
        assert "/login" in profile_page.get_current_url()