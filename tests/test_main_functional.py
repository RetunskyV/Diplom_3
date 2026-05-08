import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD


class TestMainFunctional:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_order_feed()
        page.click_constructor()
        assert page.get_current_url() == f"{BASE_URL}/"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_order_feed(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_order_feed()
        assert "/feed" in page.get_current_url()

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_ingredient_modal_details(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_ingredient()
        assert page.is_modal_ingredient_displayed()
        assert page.get_modal_ingredient_name() != ""

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_close(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_ingredient()
        page.close_modal()
        assert page.is_modal_closed()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        initial = page.get_ingredient_counter()
        page.add_bun_to_order()
        assert page.get_ingredient_counter() != initial

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(f"{BASE_URL}/login")
        login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        page = MainPage(driver)
        page.add_bun_to_order()
        page.click_order_button()
        assert page.get_order_number().isdigit()