#Não foi utilizado nessa máquina está aqui somente para apresentar o código.
# Foi utilizado na máquina Física Windows, enquanto o Server TCP foi utilizado na máquina Virtual Linux.

import socket

HOST = "192.168.2.101"
PORT = 8081

cliente = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

mensagem = input("Digite uma mensagem: ")

cliente.sendto(
    mensagem.encode(),
    (HOST, PORT)
)

resposta, _ = cliente.recvfrom(1024)

print(resposta.decode())

cliente.close()