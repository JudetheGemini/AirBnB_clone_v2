#!/usr/bin/python3
"""
Fabric python file
"""
from fabric.api import put, run, env
import os

env.user = 'ubuntu'
env.hosts = ['34.204.177.254', '18.207.112.39']


def do_deploy(archive_path):
    """
        script that distributes an archive file to web server
    """
    if not archive_path:
        return False
    else:
        # make sure the directory is there
        put(archive_path, '/tmp/')
        path = os.path.basename(archive_path)
        file = path.split('.')
        folder = file[1]
        run('sudo mkdir -p /data/web_static/releases/{}'.format(folder))
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(archive_path, folder))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(folder, folder))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'.format(folder))
        run('sudo rm /tmp/{}'.format(archive_path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(folder))
