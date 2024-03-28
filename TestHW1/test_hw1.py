import pytest
from checker import get_posts


def test1(title_post):
    assert title_post in get_posts()


if __name__ == '__main__':
    pytest.main(["-v"])
