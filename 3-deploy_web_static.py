#!/usr/bin/python3
"""
Fabric python file
"""
from fabric.api import put, run, env, local
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


def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except:
        return False


def deploy():
    """
        Function that creates and sistributes an archive to web servers
    """
    tar_file = do_pack()
    answer = do_deploy(tar_file)
    return answer
