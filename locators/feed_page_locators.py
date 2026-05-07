class FeedPageLocators:
    TITLE_FEED = ("css selector", "h1.text_type_main-large")
    ORDER_CARD = ("css selector", "a.OrderHistory_link__1iNby")
    MODAL_ORDER = ("css selector", "div.Modal_orderBox__1xWdi")
    MODAL_ORDER_NUMBER = ("css selector", "div.Modal_orderBox__1xWdi p.text_type_digits-default")
    MODAL_CLOSE = ("css selector", "button.Modal_modal__close__TnseK")
    COUNTER_ALL_TIME = ("xpath", "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    COUNTER_TODAY = ("xpath", "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    IN_PROGRESS_LIST = ("xpath", "(//ul[contains(@class, 'OrderFeed_orderList__cBvyi')])[1]")
