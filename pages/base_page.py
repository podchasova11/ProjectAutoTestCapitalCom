import pytest
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    LOGO_LOCATOR = ("xpath", "//a[@href='https://capital.com/']")
    MENU_LANGUAGE_AND_COUNTRY = ("xpath", "//div[@class='licLangSw js-licLangSw']")
    DROP_DOWN_LIST_COUNTRY = ("xpath", "//div[contains(@class,'Dropdown')]")
    COUNTRIES_SEARCH_INPUT = ("xpath", "(//a[contains(@class, 'switchCountry')])")
    COUNTRIES_LIST = ("xpath", "(//a[contains(@class, 'switchCountry')])")

    # Тут создаются необходимые объекты, которые будут доступны в pages
    def __int__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    # Данный метод будет вызываться для любой страницы, принимая ее PAGE_URL
    def open(self):
        self.driver.get(self.PAGE_URL)

    # Ниже описываются общие для всех страниц методы
    def click_on_logo(self):
        self.driver.find_element(*self.LOGO_LOCATOR).click()

    def element_is_visible(self, locator, timeout=1):
        return Wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

