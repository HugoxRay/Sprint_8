import uuid

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators


BASE_URL = "https://stellarburgers.education-services.ru/"


def generate_email():
    """Генерирует уникальный email для регистрации."""
    return f"test_{uuid.uuid4().hex[:10]}@yandex.ru"


def generate_password():
    """Генерирует пароль."""
    return "password123"


def register_user(driver, name="Тест"):
    """Регистрирует нового пользователя и возвращает email и password."""

    email = generate_email()
    password = generate_password()

    driver.get(BASE_URL + "register")

    driver.find_element(
        *Locators.REGISTER_NAME_INPUT
    ).send_keys(name)

    driver.find_element(
        *Locators.REGISTER_EMAIL_INPUT
    ).send_keys(email)

    driver.find_element(
        *Locators.REGISTER_PASSWORD_INPUT
    ).send_keys(password)

    driver.find_element(
        *Locators.REGISTER_BUTTON
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            Locators.LOGIN_BUTTON
        )
    )

    return email, password


def login_user(driver, email, password):
    """Выполняет вход пользователя."""

    driver.find_element(
        *Locators.LOGIN_EMAIL_INPUT
    ).send_keys(email)

    driver.find_element(
        *Locators.LOGIN_PASSWORD_INPUT
    ).send_keys(password)

    driver.find_element(
        *Locators.LOGIN_BUTTON
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )


def register_and_login_user(driver):
    """Регистрирует пользователя и выполняет вход."""

    email, password = register_user(driver)

    login_user(driver, email, password)

    return email, password