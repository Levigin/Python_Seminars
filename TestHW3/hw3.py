import time

import pytest
import yaml
from TestPage import OperationsHelper
from configtest import browser

with open('config.yaml') as f:
    data = yaml.safe_load(f)
    status_error = data['status_error']
    address = data['address']
    address_contact = data['address_contact']
    username = data['username']
    password = data['password']


def test_1(browser):
    test_page = OperationsHelper(browser, address)
    test_page.go_to_site()
    test_page.enter_login(username)
    test_page.enter_pass(password)
    test_page.click_login_button()
    assert test_page.get_username_label() == f'Hello, myname'


time.sleep(5)


def test_2(browser):
    test_page = OperationsHelper(browser, address_contact)
    test_page.click_contact_button()
    time.sleep(2)
    test_page.enter_name("Test")
    time.sleep(2)
    test_page.enter_content("Test content")
    time.sleep(2)
    test_page.click_button_send()
    time.sleep(2)
    alert = test_page.driver.switch_to.alert
    assert alert.text == "Form successfully submitted"


if __name__ == '__main__':
    pytest.main(['-vv'])
