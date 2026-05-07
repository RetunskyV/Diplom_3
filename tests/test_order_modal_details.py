import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
import time

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestOrderModalDetails:

    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_order_modal_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_order_feed()
        time.sleep(3)
        main_page.close_modal_if_present()
        FeedPage(driver).click_order_card()
        time.sleep(2)
        assert FeedPage(driver).is_modal_order_displayed()
