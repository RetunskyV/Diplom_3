import allure
from pages.main_page import MainPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestNavigateToOrderFeed:

    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_order_feed(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_order_feed()
        assert "/feed" in page.get_current_url()
