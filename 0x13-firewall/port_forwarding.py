# fabfile.py

from fabric.api import env, run, sudo, put

env.use_ssh_config = True
env.hosts = ['blaq1', 'blaq2', 'loadb']

def update_ufw():
    """
    Update UFW configuration on multiple servers.
    """
    # Upload the modified before.rules file to each server
    put('before.rules', '/etc/ufw/before.rules', use_sudo=True)

    # Restart UFW to apply the changes
    sudo('ufw disable')
    sudo('ufw enable')

# Run the update_ufw task on all specified hosts
