import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FeedPage(BasePage):
    @allure.step("Клик на карточку заказа")
    def click_order_card(self):
        self.click_element(FeedPageLocators.ORDER_CARD)

    @allure.step("Проверка отображения модального окна заказа")
    def is_modal_order_displayed(self):
        return self.is_displayed(FeedPageLocators.MODAL_ORDER)

    @allure.step("Получение номера заказа в модальном окне")
    def get_modal_order_number(self):
        return self.get_text(FeedPageLocators.MODAL_ORDER_NUMBER)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click_element(FeedPageLocators.MODAL_CLOSE)

    @allure.step("Получение счётчика «Выполнено за всё время»")
    def get_counter_all_time(self):
        return self.get_text(FeedPageLocators.COUNTER_ALL_TIME)

    @allure.step("Получение счётчика «Выполнено за сегодня»")
    def get_counter_today(self):
        return self.get_text(FeedPageLocators.COUNTER_TODAY)

    @allure.step("Получение номеров заказов в работе")
    def get_in_progress_numbers(self):
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_LIST)
        return ' '.join([el.text for el in elements])

    @allure.step("Ожидание обновления счётчика заказов")
    def wait_for_counter_update(self, old_counter, get_counter_method):
        WebDriverWait(self.driver, 20).until(
            lambda d: int(get_counter_method()) > int(old_counter)
        )

    @allure.step("Ожидание появления номера заказа в разделе «В работе»")
    def wait_for_order_in_progress(self, order_number):
        self.wait.until(EC.visibility_of_element_located(FeedPageLocators.IN_PROGRESS_LIST))
        WebDriverWait(self.driver, 60).until(
            lambda d: order_number in self.get_in_progress_numbers()
        )
