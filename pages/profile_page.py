from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def click_order_history(self):
        self.click_element(ProfilePageLocators.LINK_ORDER_HISTORY)

    def click_logout(self):
        self.click_element(ProfilePageLocators.BTN_LOGOUT)

    def is_profile_page(self):
        return self.is_displayed(ProfilePageLocators.FIELD_NAME)

    def open_profile_page(self):
        self.open_url("https://qa-stellarburgers.education-services.ru/account/profile")
        from selenium.webdriver.common.keys import Keys
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
        self.find_element(ProfilePageLocators.BTN_LOGOUT)

    def open_order_history_page(self):
        self.open_url("https://qa-stellarburgers.education-services.ru/account/order-history")

    def get_first_order_number(self):
        orders = self.driver.find_elements("xpath", "//p[contains(@class, 'text_type_digits-default') and contains(text(), '#')]")
        return orders[-1].text
