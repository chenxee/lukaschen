from fabric.api import require, cd, run, env, local, hosts, put, settings
from fabric.operations import sudo

import hashlib
import os
import os.path as path
import pwd
import time

host_addr = '69.163.253.189'







@hosts(host_addr)
def pull():
    """docstring for def setup"""
    env.user = 'chenxee'
    env.repo_name = 'lukaschen'
    with cd('/home/%(user)s/%(repo_name)s' % env):
        run('git pull') 



 


