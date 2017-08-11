'''fun with socket programming'''
import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_adddr=('localhost',5000)
print("starting up {} on port {}".format(*server_adddr))
s.bind(server_adddr)
s.listen(1)
while True:
	print("waiting for the connection......")
	connection,client_addr=s.accept()
	
	try:
		print("connection from",client_addr)
		while True:
			data=connection.recv(16)
			print("received {}".format(data.decode()))
			if data:
				print("sending data back to client.....")
				connection.sendall(data)
			else:
				print("no data from",client_addr)
				break
	finally:
		connection.close()
		