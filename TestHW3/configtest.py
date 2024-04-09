import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import yaml
from requests import post, get


with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)


def post_data():
    data_ = {"username": data["username"], "password": data["password"]}
    result = post(data['URL'], data=data_)
    return result.json()["token"]


@pytest.fixture(scope="session")
def browser():
    if data['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def get_posts():
    token = post_data()
    js = get(url=data["URL_POSTS"], headers={"X-Auth-Token": token}).json()
    return js['data'][0]['title']


@pytest.fixture
def title_post():
    return "Test"
