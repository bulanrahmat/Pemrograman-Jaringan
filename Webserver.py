import socket
import re


host = '127.0.0.1'
port = 10012
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(1)


while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024)
    print req
    match = re.match('GET /gambar\=(\d+)\sHTTP/1', req)
    if match:
        angle = match.group(1)
        print angle
        if angle == "1":
            f=open("a.JPG","r+")
            gambar=f.read()
            f.close()
            csock.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%gambar)
            
	elif angle == "2":
	    f=open("b.JPG","r+")
            gambar=f.read()
            f.close()
            csock.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%gambar)

	elif angle == "3":
	    f=open("c.JPG","r+")
            gambar=f.read()
            f.close()
            csock.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%gambar)

    else:
        print "Returning 404"
        csock.sendall("HTTP/1.0 404 Not Found\r\n")
    csock.close()