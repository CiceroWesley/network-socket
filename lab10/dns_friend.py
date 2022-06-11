import random
from socket import *
# Cria o socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Define o endereço e a porta do socket
serverSocket.bind(('10.0.84.184', 50001))
while True:
    # Recebe o pacote e o endereço do cliente
    message, address = serverSocket.recvfrom(1024)
    message = message.decode()
    print(message)
    serverSocket.sendto(message.encode(), address)