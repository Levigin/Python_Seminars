from checkers import check_out, get_out
import yaml
from configtest import data_record

with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)


def test1(data_record):
    crc32_ = get_out(f"cd {data['PATH_FROM']}; crc32 {data['ARCHIVE']}").upper()[:-1]
    assert check_out(f"cd {data['PATH_FROM']}; 7z h {data['ARCHIVE']}", crc32_)


if __name__ == '__main__':
    crc32 = get_out(f"cd {data['PATH_FROM']}; crc32 {data['ARCHIVE']}").upper()
    z7 = get_out(f"cd {data['PATH_FROM']}; 7z h {data['ARCHIVE']}").split()
    if crc32[:-1] in z7:
        print("Equals!")
    else:
        print("Not equals!")
