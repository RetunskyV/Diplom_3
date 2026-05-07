class LoginPageLocators:
    FIELD_EMAIL = ("css selector", "input[name='name']")
    FIELD_PASSWORD = ("css selector", "input[name='Пароль']")
    BTN_LOGIN = ("xpath", "//button[text()='Войти']")
    LINK_REGISTER = ("css selector", "a[href='/register']")
    LINK_FORGOT_PASSWORD = ("css selector", "a[href='/forgot-password']")