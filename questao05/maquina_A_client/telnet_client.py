#Não foi utilizado nessa máquina está aqui somente para apresentar o código.
# Foi utilizado na máquina Física Windows, enquanto o Server Telnet foi utilizado na máquina Virtual Linux.

import socket

HOST = "192.168.2.101"
PORT = 2323

cliente = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

cliente.connect((HOST, PORT))

print("Conectado ao servidor.")

while True:

    comando = input("Telnet> ")

    if comando.lower() == "sair":
        break

    cliente.send(comando.encode())

    resposta = cliente.recv(4096)

    print(resposta.decode())

cliente.close()