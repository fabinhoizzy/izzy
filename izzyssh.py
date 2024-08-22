#!/usr/bin/python
import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect('172.16.1.5', username='root', password='root')
stdin, stdout, stderr = ssh.exec_command('id')


for linha in stdout.readlines():
    
    print(linha.strip())

ssh.close()