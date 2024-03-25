import paramiko


def upload_files(host, username, password, local_path, remote_path, port=22):
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    sftp.close()
    transport.close()


def download_files(host, username, password, local_path, remote_path, port=22):
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remote_path, local_path)
    sftp.close()
    transport.close()


def ssh_get_out(host, username, password, cmd, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    out = (stdout.read() + stderr.read()).decode("utf8")
    client.close()
    return out


def ssh_check_out(host, username, password, cmd, text, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf8")
    client.close()

    if not exit_code and text in out:
        return True
    return False
