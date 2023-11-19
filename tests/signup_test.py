import allure
import pytest
from datetime import datetime
from pages.Signup_login_page.signup_login_page import SignupLogin

# @pytest.fixture()
# def cur_time():
#     return str(datetime.now())


@pytest.mark.usefixtures("driver")  # Фикстура драйвера
class TestSignupLogin:
    def setup(self):
        self.login_page = SignupLogin(self.driver)  # Создаем обьект страницы

    # Вызываем через объект страницы все нужные методы, это и есть шаги теста
    def test_login_in_account(self):
        self.login_page.open()  # open() подхватит PAGE_URL именно с LoginPage
        self.login_page.enter_login()
        self.login_page.enter_password()
        # self.login_page.click_on_login_button()
        print("Ctr_open")