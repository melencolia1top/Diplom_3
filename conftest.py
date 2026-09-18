import pytest
import requests
from selenium import webdriver

from data import Urls
from helpers import generate_user_data
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def user():
    user_data = generate_user_data()
    response = requests.post(Urls.REGISTER_USER, json=user_data)
    response_data = response.json()
    user_data['access_token'] = response_data['accessToken']

    yield user_data

    requests.delete(
        Urls.DELETE_USER,
        headers={'Authorization': user_data['access_token']},
    )


@pytest.fixture
def authorized_driver(driver, user):
    login_page = LoginPage(driver)
    login_page.open(Urls.LOGIN_PAGE)
    login_page.login(user['email'], user['password'])
    login_page.wait_for_url(Urls.BASE_URL)
    return driver
