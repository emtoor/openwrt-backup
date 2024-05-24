OpenWRT Backup Script
This script automates the process of creating a backup of specific directories on an OpenWRT router and transferring the backup file to a specified server. It uses SSH and SCP for secure connections and file transfers.

Requirements
Python 3.x
paramiko library
scp library
You can install the required libraries using pip:

sh
Copy code
pip install paramiko scp
Usage
Clone the repository or download the script file.

Update the script with your router and server details:

router_ip: IP address of your OpenWRT router.
router_port: Port for SSH connection to the router (default is 222).
router_username: Username for SSH login to the router.
router_password: Password for SSH login to the router.
server_ip: IP address of your server.
server_username: Username for SSH login to the server.
server_password: Password for SSH login to the server.
server_path: Path on the server where the backup file will be stored.
Run the script:

sh
Copy code
python backup_script.py
Script Details
The script performs the following steps:

Connects to the OpenWRT router via SSH.
Creates a tar.gz archive of the specified directories (/etc and /overlay) on the router.
Transfers the backup file from the router to the local machine using SCP.
Transfers the backup file from the local machine to the specified server using SCP.
Configuration
The script includes a function create_scp_client to establish an SCP session, and a main function that orchestrates the backup process. Here are the key sections of the script:

create_scp_client: Establishes an SCP session using Paramiko.
main: Orchestrates the backup process, including SSH connections and file transfers.
Example
Here is an example configuration within the script:

python
Copy code
router_ip = "192.168.1.1"
router_port = 222
router_username = "root"
router_password = "your_router_password"
server_ip = "192.168.1.2"
server_username = "your_server_username"
server_password = "your_server_password"
server_path = r"/path/to/destination"
Troubleshooting
Broken pipe error: If you encounter a "Broken pipe" error during file transfer, the script includes a handler to recognize this issue and print a relevant message.
License
This project is licensed under the MIT License.
