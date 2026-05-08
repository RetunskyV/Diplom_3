import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Клик на «Конструктор»")
    def click_constructor(self):
        self.click_element(MainPageLocators.BTN_CONSTRUCTOR)

    @allure.step("Клик на «Лента заказов»")
    def click_order_feed(self):
        self.click_element(MainPageLocators.BTN_ORDER_FEED)

    @allure.step("Клик на «Личный кабинет»")
    def click_personal_account(self):
        self.click_element(MainPageLocators.BTN_PERSONAL_ACCOUNT)

    @allure.step("Клик на кнопку «Войти в аккаунт»")
    def click_login_button(self):
        self.click_element(MainPageLocators.BTN_LOGIN)

    @allure.step("Клик на кнопку «Оформить заказ»")
    def click_order_button(self):
        self.click_element(MainPageLocators.BTN_ORDER)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step("Получение счётчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Проверка отображения модального окна ингредиента")
    def is_modal_ingredient_displayed(self):
        return self.is_displayed(MainPageLocators.MODAL_INGREDIENT)

    @allure.step("Получение названия ингредиента в модальном окне")
    def get_modal_ingredient_name(self):
        return self.get_text(MainPageLocators.MODAL_INGREDIENT_NAME)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE)

    @allure.step("Проверка, что модальное окно закрыто")
    def is_modal_closed(self):
        return self.wait.until(EC.invisibility_of_element_located(MainPageLocators.MODAL_INGREDIENT))

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Добавление булки в заказ")
    def add_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.BASKET_TOP_BUN)

    @allure.step("Закрытие модального окна, если оно есть")
    def close_modal_if_present(self):
        try:
            self.click_element(MainPageLocators.MODAL_CLOSE)
        except:
            pass

    @allure.step("Ожидание появления номера заказа")
    def wait_for_order_number(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER))
        self.wait.until(lambda d: self.get_order_number().isdigit() and len(self.get_order_number()) >= 4)

    @allure.step("Подготовка чистой сессии")
    def prepare_clean_session(self):
        self.delete_all_cookies()
        self.refresh_page()
        self.close_modal_if_present()

    @allure.step("Ожидание появления номера в разделе «В работе»")
    def wait_for_order_in_progress(self, order_number):
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
        self.refresh_page()
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
        from pages.feed_page import FeedPage
        FeedPage(self.driver).wait_for_order_in_progress(order_number)
