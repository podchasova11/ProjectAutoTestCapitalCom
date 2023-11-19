from pages.Signup_login_page.signup_login_page_locators import SignupFormLocators
from pages.base_page import BasePage
from datetime import datetime


class SignupLogin(BasePage):
    # URL страницы
    PAGE_URL = "https://capital.com/"

    # Локаторы страницы
    SIGNUP_FIELD = ("xpath", "(//input[@class='field__control'])[5]")
    PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[2]")
    CONTINUE_BUTTON = ("xpath", "(//button[@type='submit'])[4]")

    def check_signup_form(self, cur_language):

        print(f"{datetime.now()}   Start step Check that form [Sign up] opened")
        if self.element_is_visible(*self.SIGNUP_FORM,  timeout=5):
            print(f"{datetime.now()}   'Sign up' form opened")


    # Методы для страницы
    def enter_login(self):
        self.driver.find_element(*self.LOGIN_FIELD).send_keys("example@mail.ru")

    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("123123123")

    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

