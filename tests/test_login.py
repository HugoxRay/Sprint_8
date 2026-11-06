from helpers import (
BASE_URL,
register_user,
login_user
)


from locators import Locators


class TestLogin:

    def test_login_from_main_page(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)

        driver.find_element(
            *Locators.LOGIN_ACCOUNT_BUTTON
        ).click()

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL


    def test_login_from_personal_account_button(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)

        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_BUTTON
        ).click()

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL


    def test_login_from_registration_page(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL + "register")

        driver.find_element(
            *Locators.LOGIN_LINK_REGISTER
        ).click()

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL


    def test_login_from_forgot_password_page(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL + "forgot-password")

        driver.find_element(
            *Locators.LOGIN_LINK_FORGOT_PASSWORD
        ).click()

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL
