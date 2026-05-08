import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from data import PROFILE_URL, ORDER_HISTORY_URL


class ProfilePage(BasePage):
    @allure.step("Клик на «История заказов»")
    def click_order_history(self):
        self.click_element(ProfilePageLocators.LINK_ORDER_HISTORY)

    @allure.step("Клик на кнопку «Выход»")
    def click_logout(self):
        self.click_element(ProfilePageLocators.BTN_LOGOUT)

    @allure.step("Проверка, что открыта страница профиля")
    def is_profile_page(self):
        return self.is_displayed(ProfilePageLocators.FIELD_NAME)

    @allure.step("Открытие страницы профиля")
    def open_profile_page(self):
        self.open_url(PROFILE_URL)
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
        self.find_element(ProfilePageLocators.BTN_LOGOUT)

    @allure.step("Открытие истории заказов")
    def open_order_history_page(self):
        self.open_url(ORDER_HISTORY_URL)

    @allure.step("Получение номера первого заказа")
    def get_first_order_number(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'text_type_digits-default') and contains(text(), '#')]"))
        )
        orders = self.driver.find_elements(By.XPATH, "//p[contains(@class, 'text_type_digits-default') and contains(text(), '#')]")
        return orders[-1].text
