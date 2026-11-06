from selenium.webdriver.common.by import By


class Locators:

    # Главная страница

    LOGIN_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти в аккаунт')]"
    )

    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//a[contains(@href, '/account')]"
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[contains(text(), 'Конструктор')]"
    )

    LOGO = (
        By.XPATH,
        "//a[@href='/']"
    )

    # Страница регистрации

    REGISTER_NAME_INPUT = (
        By.XPATH,
        "//input[@name='name']"
    )

    REGISTER_EMAIL_INPUT = (
        By.XPATH,
        "(//input[@type='text'])[2]"
    )

    REGISTER_PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    REGISTER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Зарегистрироваться')]"
    )

    LOGIN_LINK_REGISTER = (
        By.XPATH,
        "//a[contains(text(), 'Войти')]"
    )

    PASSWORD_ERROR = (
        By.XPATH,
        "//p[contains(text(), 'Некорректный пароль')]"
    )

    # Страница входа

    LOGIN_EMAIL_INPUT = (
        By.XPATH,
        "(//input[@type='text'])[1]"
    )

    LOGIN_PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти')]"
    )

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Восстановить пароль')]"
    )

    # Страница восстановления пароля

    LOGIN_LINK_FORGOT_PASSWORD = (
        By.XPATH,
        "//a[contains(text(), 'Войти')]"
    )

    # Личный кабинет

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )

# Конструктор

    BUNS_SECTION = (
        By.XPATH,
        "//span[contains(text(), 'Булки')]/parent::*"
    )

    SAUCES_SECTION = (
        By.XPATH,
        "//span[contains(text(), 'Соусы')]/parent::*"
    )

    FILLINGS_SECTION = (
        By.XPATH,
        "//span[contains(text(), 'Начинки')]/parent::*"
    )