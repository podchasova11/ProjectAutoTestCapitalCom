import pytest

import allure
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

import conf
from conf import CHROME_WINDOW_SIZES


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.fixture()
def set_driver_chrome(request):

    chrome_options = webdriver.ChromeOptions
    chrome_options.page_load_strategy = "eager"
    chrome_options.add_argument(conf.CHROME_WINDOW_SIZES)

    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        "Reg/NoAuth",
        "Auth",
    ],
)
def cur_role(request):
    print(f"\n\n\nCurrent test role - {request.param}")
    return request.param


# Language parameter
@pytest.fixture(
    scope="class",
    params=[
        # "en"
        # "de",
        # "es",
        # "fr",
        "it"
    ],
)
def cur_language(request):
    language = request.param
    print(f"Current test language - {language}")
    return language


# Country/License parameter
@pytest.fixture(
    scope="class",
    params=[
        # "gb",  # United Kingdom - "FCA"
        # "de",  # Germany - "CYSEC"
        # "es",  # Spain - "CYSEC"
        # "fr",  # France - "CYSEC"
        # "it",  # Italy - "CYSEC"

    ],
)
def cur_country(request):
    print(f"Current country of trading - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "aqa.tomelo.an@gmail.com",
    ],
)
def cur_login(request):
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "iT9Vgqi6d$fiZ*Z",
    ],
)
def cur_password(request):
    print(f"Current login - {request.param}")
    return request.param

