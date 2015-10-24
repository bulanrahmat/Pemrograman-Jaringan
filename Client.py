# chat_client.py

import sys, socket, select
 
def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host


    print 'Please write login to login'
    test=raw_input()
    if test == "login" :
	    sys.stdout.write('Write your username '); sys.stdout.flush()
	    test =raw_input()
	    if test == '':
	    	sys.exit()
    	    try :
       	 	s.connect((host, port))
    	    except :
        	print 'Unable to connect'
        	sys.exit()
            print 'Write list to view user active'
            print 'Start chatting'
            sys.stdout.write(test+" says "); sys.stdout.flush()
            s.send(test+" says "+ test) 
            while 1:
        	socket_list = [sys.stdin, s] 
        	# Get the list sockets which are readable
        	read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        	for sock in read_sockets:            
            	    if sock == s:
                        data = sock.recv(4096)
                        if not data :
                            print '\nDisconnected from chat server'
                            sys.exit()
                        else :
                    #print data
                            sys.stdout.write(data)
		            if data =="\rUsername already in use\n":
		                sys.exit()
                            else :
		                sys.stdout.write(test+" says "); sys.stdout.flush()     
            
                    else :
               		# user entered a message
                 	msg = sys.stdin.readline()
		 	msg = test+" says "+msg
			s.send(msg)
		 	sys.stdout.write(test+" says "); sys.stdout.flush()
    else :
	sys.exit()

if __name__ == "__main__":

    sys.exit(chat_client())


