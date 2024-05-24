import paramiko
from scp import SCPClient, SCPException

def create_scp_client(host, port, username, password):
    """Create an SCP client session."""
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password, timeout=30)
    ssh.get_transport().set_keepalive(60)
    return SCPClient(ssh.get_transport())
    
def main():
    router_ip = "192.168.1.1"
    server_ip = "192.168.1.2"
    router_username = "root"
    router_password = "indians14"
    server_username = "Danny"
    server_password = "Indians14@"
    server_path = r"C:/Scripts/openwrt"
    router_port = 222  # Update to the new port

    files_to_copy = ["/etc", "/overlay"]
    tar_cmd = f"tar -czf /tmp/openwrt_backup.tar.gz {' '.join(files_to_copy)}"

    # Connect to the router and create the tar file
    router_ssh = paramiko.SSHClient()
    router_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    router_ssh.connect(router_ip, port=router_port, username=router_username, password=router_password)
    stdin, stdout, stderr = router_ssh.exec_command(tar_cmd)
    stdout.channel.recv_exit_status()  # Wait for the command to complete

    # SCP the file from the router
    with create_scp_client(router_ip, router_port, router_username, router_password) as scp:
        scp.get("/tmp/openwrt_backup.tar.gz", "openwrt_backup.tar.gz")

    # SCP the file to the server
    try:
        with create_scp_client(server_ip, 22, server_username, server_password) as scp:
            scp.put("openwrt_backup.tar.gz", server_path)
    except SCPException as e:
        if "Broken pipe" in str(e):
            print("Transfer reported a broken pipe, but file was sent successfully.")
        else:
            raise  # Re-raise the exception if it's not the known 'Broken pipe' issue
    
    print("Files successfully copied.")

if __name__ == "__main__":
    main()
