import socket

host = "127.0.0.6"
port = 65432
data_payload = 1024

#matriz com associações nome-ip
dns = [['renan','10.0.84.183'],['gilvan','10.0.84.181'],['wesley','10.0.84.184'],['raquel','192.168.0.4'],['pedro','10.0.84.188']]

#criação socket tcp
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = (host,port)

print('Iniciando servidor no ip %s e porta %s ' % server_address)
sock.bind(server_address)

sock.listen(5)
client, address = sock.accept()

while True:
    print('esperando mensagem')
    data = client.recv(data_payload)
    message = data.decode()
    if message:
        for i in range(len(dns)):
            if message == dns[i][0]:
                message = dns[i][1]  
        print("Data: %s" % message)
        client.sendall(message.encode())
    else:
        break
print('fechando conexão,',sock)
sock.close()        
