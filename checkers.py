import subprocess
import datetime
import yaml

with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)

def check_out(command: str, text: str) -> bool:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if not result.returncode and text in result.stdout:
        return True
    return False


def get_out(command: str) -> str:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    return result.stdout


def writer():
    data_proc = get_out(f"cat {data['LOADAVG']}")
    time_now = datetime.datetime.now()
    with open(f"{data['PATH_FROM']}/stat.txt", 'a') as f:
        f.write(f"Time: {time_now}, Files: {data['FILE_QUANTITY']}, Size: {data['FILE_SIZE']}, Data proc: {data_proc}")


if __name__ == '__main__':
    writer()
