from checkers import check_out, get_out
import yaml
from configtest import data_record
from ssh_checkers import ssh_check_out, ssh_get_out

with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)


def test1(data_record):
    crc32_ = ssh_get_out("127.0.0.1", "user2",
                        "qwerty11", f"cd {data['PATH_FROM_USER']}; crc32 {data['ARCHIVE']}").upper()[:-1]
    assert ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", f"cd {data['PATH_FROM_USER']}; 7z h {data['ARCHIVE']}", crc32_)


if __name__ == '__main__':
    crc32 = get_out(f"cd {data['PATH_FROM']}; crc32 {data['ARCHIVE']}").upper()
    z7 = get_out(f"cd {data['PATH_FROM']}; 7z h {data['ARCHIVE']}").split()
    s = ssh_get_out("127.0.0.1", "user2",
                        "qwerty11", f"cd {data['PATH_FROM_USER']}; crc32 {data['ARCHIVE']}")
    if crc32[:-1] in z7:
        print("Equals!")
    else:
        print("Not equals!")
