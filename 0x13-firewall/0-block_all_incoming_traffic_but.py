from fabric.api import *

env.use_ssh_config = True
env.hosts = ['blaq1', 'blaq2', 'loadb']

def ufw():
    """
        Setup firewall
    """
    # sudo("apt-get -y update")
    # sudo("apt-get -y install ufw")
    sudo("ufw disable")
    sudo("ufw default deny incoming")
    sudo("ufw default allow outgoing")
    sudo("ufw disable")
    sudo("ufw allow 22/tcp")
    sudo("ufw allow 443/tcp")
    sudo("ufw allow 80/tcp")
    sudo("ufw allow 3306/tcp") #mysql to allow replication
    sudo("ufw enable")
    sudo("ufw reload")
    # Display ufw status
    sudo("ufw status")

