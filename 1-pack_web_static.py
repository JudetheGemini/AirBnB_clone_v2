#!/usr/bin/python3
"""
Python script that uses the fabric ;ocal api
to execute bash commands to create a folder and
create a tar file
"""
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['34.204.177.254', '18.207.112.39']


def do_pack():
    """
        Function that generates a .tgz archive of all static files
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}.tgz'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
