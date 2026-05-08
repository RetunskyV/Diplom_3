class ProfilePageLocators:
    FIELD_NAME = ("css selector", "input[name='Name']")
    FIELD_EMAIL = ("xpath", "//input[@name='name' and @type='text']")
    FIELD_PASSWORD = ("css selector", "input[type='password']")
    BTN_SAVE = ("xpath", "//button[text()='Сохранить']")
    BTN_LOGOUT = ("css selector", "button.Account_button__14Yp3")
    LINK_ORDER_HISTORY = ("css selector", "a[href='/account/order-history']")