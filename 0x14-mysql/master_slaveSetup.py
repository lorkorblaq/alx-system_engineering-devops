from fabric.api import *

# Specify that Fabric should use the SSH config
env.use_ssh_config = True

# Specify the hosts using hostnames from your SSH config
env.hosts = ['blaq1', 'blaq2']

@task
def configure_antibinding():
    """
    Configure MySQL on the replica server (blaq2).
    """
    sudo("sed -i '/bind-address/s/^/#/' /etc/mysql/my.cnf")
    sudo("systemctl restart mysql")

@task
@hosts('blaq1')
def create_replication_user(replica_ip='blaq1', password='518Oloko.'):
    mysql_root_password='518Oloko.'
    """
    Create a MySQL user for replication on the master server (blaq1).

    """
    mysql_root_password = prompt("Enter MySQL root password for sudo: ", default='', validate=str)
    
    create_user_command = "sudo mysql -uroot -p'{}' -e \"CREATE USER 'replication_user'@'{}' IDENTIFIED BY '{}';\"".format(mysql_root_password, replica_ip, password)

    #CREATE USER 'replication_user'@'18.234.169.154' IDENTIFIED BY '518Oloko.';

    grant_replication_command = "sudo mysql -uroot -p'{}' -e \"GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'{}';\"".format(mysql_root_password, replica_ip)

    #GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'18.234.169.154;

    run(create_user_command)
    run(grant_replication_command)

@task
@hosts('blaq1')
def get_master_status():
    """
    Get the binary log position on the master server (blaq1).
    """
    result = run(f"mysql -uroot -p{'518Oloko.'} 'SHOW MASTER STATUS\\G'")
    print(result)
    

@task
@hosts('blaq2')
def configure_replication(master_host, master_log_file, master_log_pos, password):
    """
    Configure MySQL replication on the replica server (blaq2).
    """
    sudo("sed -i '/bind-address/s/^/#/' /etc/mysql/my.cnf")
    sudo("systemctl restart mysql")

    run("mysql -e \"CHANGE MASTER TO "
        "MASTER_HOST='{}', "
        "MASTER_USER='replication_user', "
        "MASTER_PASSWORD='{}', "
        "MASTER_LOG_FILE='{}', "
        "MASTER_LOG_POS={};\"".format(master_host, password, master_log_file, master_log_pos))
    run("mysql -e \"START SLAVE;\"")

# CHANGE MASTER TO MASTER_HOST='18.234.169.154', MASTER_USER='replication_user', MASTER_PASSWORD='518Oloko.', MASTER_LOG_FILE='mysql-bin.000002', MASTER_LOG_POS='154';"

@task
@hosts('blaq2')
def check_replication_status():
    """
    Check the replication status on the replica server (blaq2).
    """
    result = run("mysql -e 'SHOW SLAVE STATUS\\G'")
    print(result)
