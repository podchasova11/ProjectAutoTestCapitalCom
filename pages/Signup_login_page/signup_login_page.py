from pages.Signup_login_page.signup_login_page_locators import SignupFormLocators
from pages.base_page import BasePage
from datetime import datetime


class SignupLogin(BasePage):
    def check_signup_form(self, cur_language):

        print(f"{datetime.now()}   Start step Check that form [Sign up] opened")
        if self.element_is_visible(SignupFormLocators.SIGNUP_FORM, timeout=5):
            print(f"{datetime.now()}   'Sign up' form opened")




