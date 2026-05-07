import allure
from pages.main_page import MainPage

BASE_URL = "https://qa-stellarburgers.education-services.ru"


class TestIngredientCounterIncreases:

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open_url(BASE_URL)
        initial = page.get_ingredient_counter()
        page.add_bun_to_order()
        assert page.get_ingredient_counter() != initial