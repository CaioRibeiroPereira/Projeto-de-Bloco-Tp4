#Não foi utilizado nessa máquina está aqui somente para apresentar o código.
# Foi utilizado na máquina Física Windows, enquanto o Server TCP foi utilizado na máquina Virtual Linux.

import socket

HOST = "192.168.2.101"
PORT = 8080

cliente = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

cliente.connect((HOST, PORT))

mensagem = input("Digite uma mensagem: ")

cliente.send(mensagem.encode())

resposta = cliente.recv(1024)

print(resposta.decode())

cliente.close()