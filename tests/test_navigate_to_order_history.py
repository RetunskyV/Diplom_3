import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestNavigateToOrderHistory:

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login("test_v@pochta.ru", "123456")
        MainPage(driver).click_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        assert "/account/order-history" in profile_page.get_current_url()
