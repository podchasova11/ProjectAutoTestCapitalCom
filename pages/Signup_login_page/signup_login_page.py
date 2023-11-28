from pages.base_page import BasePage
from datetime import datetime


class SignupLogin(BasePage):
    # URL страницы
    PAGE_URL = "https://capital.com/"

    # Локаторы страницы
    SIGNUP_FIELD = ("xpath", "(//input[@class='field__control'])[5]")
    PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[2]")
    CONTINUE_BUTTON = ("xpath", "(//button[@type='submit'])[4]")

    # Методы для страницы
    def check_signup_form(self, cur_language):
        print(f"{datetime.now()}   Start step Check that form [Sign up] opened")
        if self.element_is_visible(*self.SIGNUP_FIELD,  timeout=5):
            print(f"{datetime.now()}   'Sign up' form opened")

    def enter_login(self):
        self.driver.find_element(*self.SIGNUP_FIELD).send_keys("aqa.tomelo.an@gmail.com")

    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("iT9Vgqi6d$fiZ*Z")

    def click_button_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
