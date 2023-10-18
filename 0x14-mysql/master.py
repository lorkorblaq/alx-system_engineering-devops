# fabfile.py
from fabric.api import *

env.use_ssh_config = True
env.hosts = ['blaq1']


def make_master():


