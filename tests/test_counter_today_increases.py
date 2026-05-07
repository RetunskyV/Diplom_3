import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestCounterTodayIncreases:

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_counter_today_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_order_feed()
        old = FeedPage(driver).get_counter_today()
        main_page.click_personal_account()
        LoginPage(driver).login("test_v@pochta.ru", "123456")
        MainPage(driver).add_bun_to_order()
        MainPage(driver).click_order_button()
        import time; time.sleep(2)
        main_page.click_order_feed()
        new = FeedPage(driver).get_counter_today()
        assert int(new) > int(old)
