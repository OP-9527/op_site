#! coding:utf-8

import paramiko


def get_ssh(ip, user, pwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, user, pwd, timeout=8)
        return ssh
    except Exception, e:
        print e
        return "False"
