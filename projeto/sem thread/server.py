#import socket module
from socket import *
# In order to terminate the program
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare um sevidor socket
#início
host = '127.0.0.1'
port = 65432
data_payload = 1024

server_address = (host,port)
serverSocket.bind(server_address)
serverSocket.listen(5)
#fim

while True:
    #Estabeleça a conexão
    print('Pronto para servir...')
    connectionSocket, addr = serverSocket.accept()#início #fim
    try:
        data = connectionSocket.recv(data_payload)
        message = data.decode() #início #fim
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()     #início #fim
        #Send one HTTP header line into socket
        #início 
        httpHeader = 'HTTP/1.1 200 OK\n\n'
        connectionSocket.send(httpHeader.encode())
        #fim
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #início 
        messageError = 'HTTP/1.1\n\n 404 Not Found'
        connectionSocket.send(messageError.encode())
        #fim
        #Close client socket
        #início 
        connectionSocket.close()
        #fim
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data


