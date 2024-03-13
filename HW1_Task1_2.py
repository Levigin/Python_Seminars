import re
import subprocess
import string


def checkout(command: str, text: str) -> bool:

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    for ch in string.punctuation:
        out.replace(ch, " ")
    out_list = re.split(r'\n|=| ', out)
    print(out_list)
    if not result.returncode and text in out_list:
        return True
    return False


if __name__ == '__main__':
    print(f'Result: {checkout("cat /etc/os-release", "22.04.1")}')
