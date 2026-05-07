import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
import time

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestOrderHistoryInFeed:

    @allure.title("Заказы из «Истории заказов» отображаются в «Ленте заказов»")
    def test_order_history_in_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login("test_v@pochta.ru", "123456")
        MainPage(driver).add_bun_to_order()
        MainPage(driver).click_order_button()
        time.sleep(2)
        MainPage(driver).click_personal_account()
        ProfilePage(driver).click_order_history()
        time.sleep(3)
        order_in_history = ProfilePage(driver).get_first_order_number()
        MainPage(driver).click_order_feed()
        main_page.close_modal_if_present()
        FeedPage(driver).click_order_card()
        assert order_in_history == FeedPage(driver).get_modal_order_number()
