# /usr/bin/python3

import socket

serverssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gets the ip of the host
host = socket.gethostname()
port = 444


# Binding to socket
serverssocket.bind(('', port))

#starting the TCP listener
serverssocket.listen(3)

#STARTING THE CONNECTION    
while True:
    clientsocket, address = serverssocket.accept()

    print("Connection Established from: %s " % str(address))
        
    message = 'Hello, thankyou for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    

    clientsocket.close()
    
    
