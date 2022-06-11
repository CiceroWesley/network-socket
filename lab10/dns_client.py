import socket

host = '127.0.0.6'
port = 65432

#criação socket tcp/ip
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#criaçã socket udp
sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#conecta o socket no servidor
client_address = (host,port)
print('conectando no host %s e porta %s' % client_address)
sock.connect(client_address)

#enviar data socket tcp
message = input('Insira o nome do destinatário:')
sock.sendall(message.encode())
#recebe ip do destinatário
data = sock.recv(1024)
ip = data.decode()

print(ip)

message = 'echo'
client_address2 = (ip,50001)
#envio de mensagem para o ip destino com socket udp
sock2.sendto(message.encode(),client_address2)
#recebe mensagem do destinatário
data2 = sock2.recvfrom(1024)
mensagem = data2[0].decode()
print(mensagem)

print('fechando conexão com o servidor')
sock.close()
sock2.close()



