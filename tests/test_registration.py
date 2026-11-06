from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import BASE_URL, generate_email, generate_password
from locators import Locators

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.REGISTER_NAME_INPUT
            )
        ).send_keys("Тест")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.REGISTER_EMAIL_INPUT
            )
        ).send_keys(generate_email())

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.REGISTER_PASSWORD_INPUT
            )
        ).send_keys(generate_password())

        driver.find_element(
            *Locators.REGISTER_BUTTON
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        assert "login" in driver.current_url

    def test_registration_with_incorrect_password(self, driver):
        driver.get(BASE_URL + "register")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.REGISTER_NAME_INPUT
            )
        ).send_keys("Тест")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.REGISTER_EMAIL_INPUT
            )
        ).send_keys(generate_email())

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.REGISTER_PASSWORD_INPUT
            )
        ).send_keys("12345")

        driver.find_element(
            *Locators.REGISTER_BUTTON
        ).click()

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.PASSWORD_ERROR
            )
        )

        assert error.is_displayed()
