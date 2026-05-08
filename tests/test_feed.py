import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from data import BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD


class TestFeed:

    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_order_modal_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_order_feed()
        main_page.close_modal_if_present()
        FeedPage(driver).click_order_card()
        assert FeedPage(driver).is_modal_order_displayed()

    @allure.title("Заказы из «Истории заказов» отображаются в «Ленте заказов»")
    def test_order_history_in_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page.add_bun_to_order()
        main_page.click_order_button()
        main_page.wait_for_order_number()
        main_page.click_personal_account()
        ProfilePage(driver).click_order_history()
        order_in_history = ProfilePage(driver).get_first_order_number()
        main_page.click_order_feed()
        main_page.close_modal_if_present()
        FeedPage(driver).click_order_card()
        assert order_in_history == FeedPage(driver).get_modal_order_number()

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_counter_all_time_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_order_feed()
        feed_page = FeedPage(driver)
        old = feed_page.get_counter_all_time()
        main_page.click_personal_account()
        LoginPage(driver).login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page.add_bun_to_order()
        main_page.click_order_button()
        main_page.wait_for_order_number()
        main_page.click_order_feed()
        feed_page.wait_for_counter_update(old, feed_page.get_counter_all_time)
        assert int(feed_page.get_counter_all_time()) > int(old)

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_counter_today_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_order_feed()
        feed_page = FeedPage(driver)
        old = feed_page.get_counter_today()
        main_page.click_personal_account()
        LoginPage(driver).login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page.add_bun_to_order()
        main_page.click_order_button()
        main_page.wait_for_order_number()
        main_page.click_order_feed()
        feed_page.wait_for_counter_update(old, feed_page.get_counter_today)
        assert int(feed_page.get_counter_today()) > int(old)

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_in_progress(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_personal_account()
        LoginPage(driver).login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page.add_bun_to_order()
        main_page.click_order_button()
        main_page.wait_for_order_number()
        order_number = "0" + main_page.get_order_number()
        main_page.click_order_feed()
        main_page.wait_for_order_in_progress(order_number)
        assert order_number in FeedPage(driver).get_in_progress_numbers()
