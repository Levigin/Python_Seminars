import subprocess

PATH_FROM = "/home/levigin/GB/HW2"
PATH_TO = "/home/levigin/GB/HW2/exclude"
CHECK_FOLDER = "include"
FILE = "test.txt"  # Check hash file
ARCHIVE = "archive.7z"  # Check hash archive


def get_out(command: str) -> str:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    return result.stdout


if __name__ == '__main__':
    crc32 = get_out(f"cd {PATH_FROM}; crc32 {ARCHIVE}").upper()
    z7 = get_out(f"cd {PATH_FROM}; 7z h {ARCHIVE}").split()
    if crc32[:-1] in z7:
        print("Equals!")
    else:
        print("Not equals!")
