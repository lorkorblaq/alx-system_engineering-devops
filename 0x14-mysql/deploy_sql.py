# fabfile.py
from fabric.api import *

env.use_ssh_config = True
env.hosts = [  'blaq2']


def install_mysql():
    """
    Install MySQL on a remote server if not already installed
    """

    #removes previous installed files
    sudo('rm -rf /etc/mysql /var/lib/mysql')

    sudo('apt-get remove --purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*')
    sudo('apt-get autoremove')
    sudo('apt-get autoclean')  
    sudo('apt-get -f install')

    put("signature.key", '/tmp/')
    #make sure you saved your signatue.key on same directory as fabfile.py
    sudo('apt-key add /tmp/signature.key')
    sudo("""sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'""")

    sudo('apt-get update')
    sudo("sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*")

    


