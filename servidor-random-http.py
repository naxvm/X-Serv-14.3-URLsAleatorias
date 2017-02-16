#! /usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)


try:
    while True:
        #print('--------------------')
        #print('Waiting a request...')
        (recvSocket, address) = mySocket.accept()
        nextNumber = random.randrange(0,9999999)
        recvSocket.send(bytes('HTTP/1.1 200 OK \r\n\r\n' +
                        '<html><title>Hola!</title>' +
                        '<body>Hola.' +
                        '<a href="http://localhost:1234/' + str(nextNumber) +
                        '">Dame otra</a>' +
                        '</body></html>', 'utf-8'))
        recvSocket.close()



except KeyboardInterrupt:
    print('Closing binded socket')
    mySocket.close()



# Hola. Dame otra (enlace a URL aleatoria bajo localhost:1234
# distinta cada vez)
