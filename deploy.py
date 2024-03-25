from ssh_checkers import ssh_check_out, upload_files


def deploy():
    upload_files("127.0.0.1", "user2", "qwerty11", "p7zip-full.deb", "/home/user2/p7zip-full.deb")
    print(ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", "echo 'qwerty11' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                        "Настраивается пакет", 22))

    print(ssh_check_out("127.0.0.1", "user2",
                        "qwerty11", "echo 'qwerty11' | sudo -S dpkg -s p7zip-full",
                        "Status: install ok installed", 22))


if __name__ == '__main__':
    deploy()
