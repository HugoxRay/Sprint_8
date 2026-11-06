from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import BASE_URL
from locators import Locators


class TestConstructor:

    def test_buns_section(self, driver):
        driver.get(BASE_URL)

        # Сначала переходим в другой раздел
        sauces = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )
        sauces.click()

        # Затем переходим в Булки
        buns = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUNS_SECTION)
        )
        buns.click()

        assert "current" in buns.get_attribute("class")


    def test_sauces_section(self, driver):
        driver.get(BASE_URL)

        sauces = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )

        sauces.click()

        assert "current" in sauces.get_attribute("class")


    def test_fillings_section(self, driver):
        driver.get(BASE_URL)

        fillings = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.FILLINGS_SECTION)
        )

        fillings.click()

        assert "current" in fillings.get_attribute("class")
        