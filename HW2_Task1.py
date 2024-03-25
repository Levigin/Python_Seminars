from checkers import check_out
from yaml import safe_load
from configtest import data_record
from ssh_checkers import ssh_check_out

with open("config.yaml", "r") as file:
    data = safe_load(file)


def test_step1(data_record):
    # test1
    assert ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", f"cd {data['PATH_FROM_USER']}; {data['FORMAT_7Z']} l archive.{data['FORMAT_7Z']}", "test.txt")


def test_step2(data_record):
    assert ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", f"rm -rf {data['PATH_TO_USER']}", '')


def test_step3(data_record):
    # test2
    archive = ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", f"cd {data['PATH_FROM_USER']}; {data['FORMAT_7Z']} x archive.{data['FORMAT_7Z']} -o{data['PATH_TO_USER']}", "Everything is Ok")
    check_folder = ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", f"ls {data['PATH_TO_USER']}", data['CHECK_FOLDER'])
    check_file = ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", f"ls {data['PATH_FROM_USER']}/{data['CHECK_FOLDER']}", "test2.txt")
    assert archive and check_folder and check_file


def test_step4(data_record):
    assert ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", f"cd {data['PATH_TO_USER']}; 7z a -t{data['FORMAT_ZIP']} archive.{data['FORMAT_ZIP']}", '')
