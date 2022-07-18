import socket
import _thread
import sys
#Função para lidar com cada conexão (cliente)
def clientthread(conn):
    #Sai do loop quando o cliente desconecta, pois a variável data não conterá nenhum conteúdo
    while True:
        #Receiving from client
        data = conn.recv(1024)
        #reply = 'OK...' + data.decode()
        if not data:
            break
        response = 'HTTP/1.1 200 OK\n\n Hello World'
        conn.sendall(response.encode())
        #conn.sendall(reply.encode())
        #destroi aquela conexão com o cliente e encerra thread ao sair do loop
        conn.close()
        break

host = '127.0.0.1'
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#garante que o socket será destruído (pode ser reusado) após uma interrupção da execução
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Bind socket to local host and port
try:
    s.bind((host, port))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

s.listen(1)
#Continua recebendo conexões
while True:
    #Aceita conexões
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    #Cria nova thread para uma nova conexão. O primeiro
    #argumento é o nome da função, e o segundo é uma tupla
    #com os parâmetros da função.
    _thread.start_new_thread(clientthread ,(conn,))