import allure
from pages.main_page import MainPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestModalClose:

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_close(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_ingredient()
        page.close_modal()
        assert page.is_modal_closed()