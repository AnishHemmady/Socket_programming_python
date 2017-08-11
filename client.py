import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_addr=('localhost',5000)
print("connecting to {} at port {}".format(*server_addr))
s.connect(server_addr)

try:
	msg="hello anish iam here"
	print('sending {}'.format(msg))
	s.sendall(msg.encode())
	amt_recvd=0
	amt_expectd=len(msg)
	
	while amt_recvd<amt_expectd:
		data=s.recv(16)
		amt_recvd+=len(data.decode())
		print("received {}".format(data.decode()))
		
finally:
	print("closing socket....")
	s.close()