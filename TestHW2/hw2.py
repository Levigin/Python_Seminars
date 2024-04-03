from telnetlib import EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from configtest import site, set_locator1, set_locator2, set_locator3, username, password, title, description, content, \
    save, check_post, create_post


def test_1(site, set_locator1, set_locator2, set_locator3, username, password):
    input1 = site.find_element('xpath', set_locator1)
    input1.send_keys(username)
    input2 = site.find_element('xpath', set_locator2)
    input2.send_keys(password)
    input3 = site.find_element('css', set_locator3)
    input3.click()
    selector4 = '''h1'''
    find1 = site.find_element('css', selector4)
    assert find1.text == 'Blog'


time.sleep(10)


def test_2(site, create_post,  title, description, content, save, check_post):
    time.sleep(5)
    post_created = site.find_element('xpath', create_post)
    post_created.click()
    time.sleep(3)
    post_title = site.find_element('xpath', title)
    post_title.send_keys("Test")
    time.sleep(1)
    description_post = site.find_element('xpath', description)
    description_post.send_keys("Test description")
    time.sleep(1)
    content_post = site.find_element('xpath', content)
    content_post.send_keys("Test content")
    time.sleep(1)
    save_post = site.find_element('xpath', save)
    save_post.click()
    time.sleep(2)
    check = site.find_element('xpath', check_post)
    assert check.text == "Test"


if __name__ == '__main__':
    pytest.main(["-vv"])
