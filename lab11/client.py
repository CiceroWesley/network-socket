import socket

host = '127.0.0.1'
port = 1234

#cria sockt tcp/ip
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#conecta o socket no servidor
client_address = (host,port)
print('conectando no host %s e porta %s' % client_address)
sock.connect(client_address)

#enviar data
message = 'Hello, World'
sock.sendall(message.encode())
data = sock.recv(1024)
print('Recebido %s' % data.decode())

print('fechando conexão com o servidor')
sock.close()



