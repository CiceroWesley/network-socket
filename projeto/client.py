from socket import *
import sys


host = sys.argv[1]
port =  sys.argv[2]
filename = sys.argv[3]

#cria sockt tcp/ip
sock = socket(AF_INET,SOCK_STREAM)
#conecta o socket no servidor
client_address = (host, int(port))
print('conectando no host %s e porta %s' % client_address)
sock.connect(client_address)

#enviar mensagem
message = "GET /" +filename + " HTTP/1.1\r\nHost:"+ host + ":" + port + "/" + "\r\n\r\n"
sock.sendall(message.encode())

resposta = ''
while True:
    data = sock.recv(4096)
    if not data:
        break
    resposta += data.decode()

#mostrando resposta
print(resposta)
sock.close()