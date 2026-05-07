import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
import time

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestOrderNumberInProgress:

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_in_progress(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login("test_v@pochta.ru", "123456")
        MainPage(driver).add_bun_to_order()
        MainPage(driver).click_order_button()
        time.sleep(3)
        order_number = "0" + MainPage(driver).get_order_number()
        time.sleep(2)
        main_page.click_order_feed()
        assert order_number in FeedPage(driver).get_in_progress_numbers()
