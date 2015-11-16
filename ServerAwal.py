import threading
import socket
import time
import sys
import re

def get_file(nama):
	myfile = open(nama)
	return myfile.read()


class MemprosesClient(threading.Thread):
	def __init__(self,client_socket,client_address,nama):
		self.client_socket = client_socket
		self.client_address = client_address
		self.nama = nama
		threading.Thread.__init__(self)
	
	def run(self):
		message = ''
		while True:
			self.client_socket, self.my_socket = self.my_socket.accept()
    			print "Connection from: " + `caddr`
    			data = self.client_socket.recv(1024)
    			print data
    			match = re.match('GET /gambar\=(\d+)\sHTTP/1', data)
            		if match:
				angle = match.group(1)
        			print angle
        			if angle == "1":
            				f=open("history.jpg","r+")
           				gambar=f.read()
            				f.close()
            				self.client_socket("HTTP/1.1 200 OK \r\n\r\n%s"%gambar)
				elif angle == "2":
	    				f=open("gambar.jpg","r+")
            				gambar=f.read()
           				f.close()
            				self.client_socket.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%gambar)
            		else:
				print "Returning 404"
       				self.client_socket.sendall("HTTP/1.0 404 Not Found\r\n")
    				self.client_socket.close()
		


class Server(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = ('127.0.0.1',10002)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.listen(1)
		nomor=0
		while (True):
			self.client_socket, self.client_address = self.my_socket.accept()
    			nomor=nomor+1
			#---- menghandle message cari client (Memproses client)
			my_client = MemprosesClient(self.client_socket, self.client_address, 'PROSES NOMOR '+str(nomor))
			my_client.start()
			#----


serverku = Server()
serverku.start()


