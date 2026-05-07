class ResetPasswordLocators:
    FIELD_PASSWORD = ("css selector", "input[name='Введите новый пароль']")
    FIELD_CODE = ("css selector", "input[name='name']")
    BTN_SAVE = ("xpath", "//button[text()='Сохранить']")
    ICON_EYE = ("css selector", "div.input__icon-action")
    FIELD_ACTIVE = ("css selector", "div.input_status_active")