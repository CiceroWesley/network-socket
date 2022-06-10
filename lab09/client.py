from socket import *
import time
host = '127.0.0.1'
port = 50000

#cria sockt udp
sock = socket(AF_INET,SOCK_DGRAM)
#tempo de resposta
sock.settimeout(1)

client_address = (host,port)

Rtts = []
perda = 0
for i in range(10):
    number = i
    tempo = time.time()
    message = 'Ping:' + str(i) + '|' + str(tempo)
    
    rttb = time.time()
    sock.sendto(message.encode(),client_address)
    
    try:
        data = sock.recvfrom(1024)
        mensagem = data[0].decode()
        
        rtta = time.time()
        rtt = rtta - rttb
        Rtts.append(rtt)
        print('Mensagem:{}'.format(mensagem))
        print('RTT: {}'.format(rtt))

    except:
        print('Request time out')
        perda +=1
        continue    
    
print('RTT-mínimo: {}'.format(min(Rtts)))
print('RTT-máximo: {}'.format(max(Rtts)))
print('RTT-médio: {}'.format((sum(Rtts)/len(Rtts))))
print('Taxa de perda: {}%'.format((perda/10)*100))

#fechando socket
sock.close()



