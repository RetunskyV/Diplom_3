import allure
from pages.main_page import MainPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestNavigateToConstructor:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_order_feed()
        page.click_constructor()
        assert page.get_current_url() == f"{BASE_URL}/"
