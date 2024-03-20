from checkers import check_out
from yaml import safe_load
from configtest import data_record

with open("config.yaml", "r") as file:
    data = safe_load(file)


def test_step1(data_record):
    # test1
    assert check_out(f"cd {data['PATH_FROM']}; {data['FORMAT_7Z']} l archive.{data['FORMAT_7Z']}", "test.txt")


def test_step2(data_record):
    assert check_out(f"rm -rf {data['PATH_TO']}", '')


def test_step3(data_record):
    # test2
    archive = check_out(f"cd {data['PATH_FROM']}; {data['FORMAT_7Z']} x archive.{data['FORMAT_7Z']} -o{data['PATH_TO']}", "Everything is Ok")
    check_folder = check_out(f"ls {data['PATH_TO']}", data['CHECK_FOLDER'])
    check_file = check_out(f"ls {data['PATH_FROM']}/{data['CHECK_FOLDER']}", "test2.txt")
    assert archive and check_folder and check_file


def test_step4(data_record):
    assert check_out(f"cd {data['PATH_TO']}; 7z a -t{data['FORMAT_ZIP']} archive.{data['FORMAT_ZIP']}", '')
