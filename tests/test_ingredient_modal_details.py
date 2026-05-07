import allure
from pages.main_page import MainPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestIngredientModalDetails:

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_ingredient_modal_details(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        page.click_ingredient()
        assert page.is_modal_ingredient_displayed()
        assert page.get_modal_ingredient_name() != ""