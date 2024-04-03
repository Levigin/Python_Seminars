import pytest
import yaml
from module import Site

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def set_locator3():
    return '''button'''


@pytest.fixture()
def username():
    return data['username']


@pytest.fixture()
def password():
    return data['password']


@pytest.fixture()
def create_post():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def save():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def check_post():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture(scope="session")
def site():
    site_instance = Site(data['address'])
    yield site_instance
    # site_instance.quit()
