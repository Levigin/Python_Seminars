# from conftets import post_data, get_posts
from requests import post, get
import yaml
import pytest

with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)


def post_data():
    data_ = {"username": data["USERNAME"], "password": data["PASSWORD"]}
    result = post(data['URL'], data=data_)
    return result.json()["token"]


def get_posts():
    token = post_data()
    print(f'token: {token}')
    return get(url=data["URL_POSTS"], headers={"X-Auth-Token": token}).json()


if __name__ == '__main__':
    print(get_posts())