# fabfile.py

from fabric.api import *

env.use_ssh_config = True
env.hosts = ['blaq2']


def create_mysql_database():
    # MySQL database and user details
    mysql_db = 'tyrell_corp'
    mysql_user = 'holberton_user'
    mysql_password = '518Oloko.'

    # MySQL commands to create database and table
    mysql_commands = [
        f"mysql -u root -p -e 'CREATE DATABASE {mysql_db};' -p{mysql_password}",
        f"mysql -u root -p -e 'USE {mysql_db}; CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, model VARCHAR(255) NOT NULL, manufacture_date DATE NOT NULL);' -p{mysql_password}",
        f"mysql -u root -p -e 'USE {mysql_db}; INSERT INTO nexus6 (model, manufacture_date) VALUES (\"Nexus 6\", \"2023-10-18\");' -p{mysql_password}",
        f"mysql -u root -p -e 'GRANT SELECT ON {mysql_db}.nexus6 TO \"{mysql_user}\"@\"localhost\"; FLUSH PRIVILEGES;' -p{mysql_password}"
    ]




    for command in mysql_commands:
        sudo(command)

def main():
    # Create MySQL database on both web-01 and web-02
    create_mysql_database()

if __name__ == '__main__':
    main()
