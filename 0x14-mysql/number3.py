# fabfile.py

from fabric.api import *

env.use_ssh_config = True
env.hosts = ['blaq1']

def create_replica_user():
    # MySQL user details
    replica_user = 'replica_user'
    replica_password = '518Oloko.'
    mysql_password = '518Oloko.'

    # MySQL commands to create replica_user and grant permissions
    mysql_commands = [
        f"CREATE USER '{replica_user}'@'%' IDENTIFIED BY '{replica_password}';",
        f"GRANT REPLICATION SLAVE ON *.* TO '{replica_user}'@'%';",
        f"GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';",
        f"FLUSH PRIVILEGES;"
    ]

    # Run MySQL commands on web-01
    for command in mysql_commands:
        sudo(f"mysql -u root -e '{command}'-p{mysql_password}")
        # run(f"mysql -u root -e '{command}'-p{mysql_password}")

def main():
    # Create replica_user and grant permissions on web-01
    create_replica_user()

if __name__ == '__main__':
    main()
