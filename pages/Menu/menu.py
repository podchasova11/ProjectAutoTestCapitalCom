import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MenuSection(BasePage):

    # Локаторы страницы
    SUB_MENU_DE_LEARN_TO_TRADE = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/de/learn-to-trade']")
    SUB_MENU_EN_LEARN_TO_TRADE = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/learn-to-trade']")
    SUB_MENU_ES_LEARN_TO_TRADE = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/es/learn-to-trade']")
    SUB_MENU_FR_LEARN_TO_TRADE = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/fr/learn-to-trade']")


    # Методы для страницы
    def check_signup_form(self, cur_language):
        print(f"{datetime.now()}   Start step Check that form [Sign up] opened")
        if self.element_is_visible(*self.SUB_MENU_EN_LEARN_TO_TRADE,  timeout=5):
            print(f"{datetime.now()}   'Sign up' form opened")

    @allure.step(f"{datetime.now()}.   Click 'Education' menu section.")
    def menu_education_move_focus(self, d, test_language):
        ed_menu_locator = None
        match test_language:
            case "":
                ed_menu_locator = SUB_MENU_EN_LEARN_TO_TRADE.
            case "ar":
                ed_menu_locator = MenuUS11Education.SUB_MENU_AR_LEARN_TO_TRADE
            case "de":
                ed_menu_locator = MenuUS11Education.SUB_MENU_DE_LEARN_TO_TRADE
            case "el":
                ed_menu_locator = MenuUS11Education.SUB_MENU_EL_LEARN_TO_TRADE
            case "es":
                ed_menu_locator = MenuUS11Education.SUB_MENU_ES_LEARN_TO_TRADE
            case "fr":
                ed_menu_locator = MenuUS11Education.SUB_MENU_FR_LEARN_TO_TRADE
            case "it":
                ed_menu_locator = MenuUS11Education.SUB_MENU_IT_LEARN_TO_TRADE
            case "hu":
                ed_menu_locator = MenuUS11Education.SUB_MENU_HU_LEARN_TO_TRADE
            case "nl":
                ed_menu_locator = MenuUS11Education.SUB_MENU_NL_LEARN_TO_TRADE
            case "pl":
                ed_menu_locator = MenuUS11Education.SUB_MENU_PL_LEARN_TO_TRADE
            case "ro":
                ed_menu_locator = MenuUS11Education.SUB_MENU_RO_LEARN_TO_TRADE
            case "ru":
                ed_menu_locator = MenuUS11Education.SUB_MENU_RU_LEARN_TO_TRADE
            case "zh":
                ed_menu_locator = MenuUS11Education.SUB_MENU_ZH_LEARN_TO_TRADE
            case "cn":
                ed_menu_locator = MenuUS11Education.SUB_MENU_CN_LEARN_TO_TRADE


    # Методы для страницы
    def check_signup_form(self, cur_language):
        print(f"{datetime.now()}   Start step Check that form [Sign up] opened")
        if self.element_is_visible(*self.SIGNUP_FIELD,  timeout=5):
            print(f"{datetime.now()}   'Sign up' form opened")