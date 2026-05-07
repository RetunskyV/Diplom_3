from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def click_order_card(self):
        self.click_element(FeedPageLocators.ORDER_CARD)

    def is_modal_order_displayed(self):
        return self.is_displayed(FeedPageLocators.MODAL_ORDER)

    def get_modal_order_number(self):
        return self.get_text(FeedPageLocators.MODAL_ORDER_NUMBER)

    def close_modal(self):
        self.click_element(FeedPageLocators.MODAL_CLOSE)

    def get_counter_all_time(self):
        return self.get_text(FeedPageLocators.COUNTER_ALL_TIME)

    def get_counter_today(self):
        return self.get_text(FeedPageLocators.COUNTER_TODAY)

    def get_in_progress_numbers(self):
        return self.get_text(FeedPageLocators.IN_PROGRESS_LIST)
