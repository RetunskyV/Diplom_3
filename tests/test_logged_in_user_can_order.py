import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestLoggedInUserCanOrder:

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(f"{BASE_URL}/login")
        login_page.login("test_v@pochta.ru", "123456")
        page = MainPage(driver)
        page.add_bun_to_order()
        page.click_order_button()
        assert page.get_order_number().isdigit()