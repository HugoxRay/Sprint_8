from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import BASE_URL, register_and_login_user
from locators import Locators

class TestNavigation:

    def test_personal_account_navigation(self, driver):
        register_and_login_user(driver)

        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_BUTTON
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )

        assert "account" in driver.current_url


    def test_navigation_to_constructor_by_constructor_button(self, driver):
        register_and_login_user(driver)

        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_BUTTON
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )

        driver.find_element(
            *Locators.CONSTRUCTOR_BUTTON
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL


    def test_navigation_to_constructor_by_logo(self, driver):
        register_and_login_user(driver)

        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_BUTTON
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )

        driver.find_element(
            *Locators.LOGO
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL


    def test_logout(self, driver):
        register_and_login_user(driver)

        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_BUTTON
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                Locators.LOGOUT_BUTTON
            )
        )

        logout_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        assert "login" in driver.current_url
