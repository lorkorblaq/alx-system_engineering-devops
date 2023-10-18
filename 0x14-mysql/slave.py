# fabfile.py
from fabric.api import *

env.use_ssh_config = True
env.hosts = ['blaq2']


def install_mysql():
    """
    Install MySQL on a remote server if not already installed
    """
    # Check if MySQL is already installed
    # Update the package list and install MySQL server
    sudo('apt-get update')
    sudo('apt-get install -y mysql-server')
    #Start the MySQL service
    sudo('systemctl start mysql')
    #Enable MySQL to start on boot
    sudo('systemctl enable mysql')
    # Secure the MySQL installation (set rootpassword, remove anonymous users, etc.)
    sudo('mysql_secure_installation')
    print("MySQL installation complete!")
    sudo('systemctl status mysql')

