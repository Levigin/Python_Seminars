import subprocess

PATH_FROM = "/home/levigin/GB/HW2"
PATH_TO = "/home/levigin/GB/HW2/exclude"
CHECK_FOLDER = "include"


def checkout(command: str, text: str) -> bool:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if not result.returncode and text in result.stdout:
        return True
    return False


def test_step1():
    # test1
    assert checkout(f"cd {PATH_FROM}; 7z l archive.7z", "test.txt")


def test_step2():
    # test2
    archive = checkout(f'cd {PATH_FROM}; 7z x archive.7z -o{PATH_TO}', "Everything is Ok")
    check_folder = checkout(f'ls {PATH_TO}', CHECK_FOLDER)
    check_file = checkout(f'ls {PATH_FROM}/{CHECK_FOLDER}', "test2.txt")
    assert archive and check_folder and check_file
