import allure
import pytest
from datetime import datetime


@pytest.fixture()
def cur_time():
    return str(datetime.now())


class TestSignup:

    def test_button_signup(self, cur_login, cur_password, cur_time):


