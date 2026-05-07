from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_constructor(self):
        self.click_element(MainPageLocators.BTN_CONSTRUCTOR)

    def click_order_feed(self):
        self.click_element(MainPageLocators.BTN_ORDER_FEED)

    def click_personal_account(self):
        self.click_element(MainPageLocators.BTN_PERSONAL_ACCOUNT)

    def click_login_button(self):
        self.click_element(MainPageLocators.BTN_LOGIN)

    def click_order_button(self):
        self.click_element(MainPageLocators.BTN_ORDER)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    def is_modal_ingredient_displayed(self):
        return self.is_displayed(MainPageLocators.MODAL_INGREDIENT)

    def get_modal_ingredient_name(self):
        return self.get_text(MainPageLocators.MODAL_INGREDIENT_NAME)

    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE)

    def is_modal_closed(self):
        return self.wait.until(EC.invisibility_of_element_located(MainPageLocators.MODAL_INGREDIENT))

    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    def add_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.BASKET_TOP_BUN)

    def close_modal_if_present(self):
        try:
            self.click_element(MainPageLocators.MODAL_CLOSE)
        except:
            pass

    def wait_for_order_number(self):
        import time; time.sleep(2)
