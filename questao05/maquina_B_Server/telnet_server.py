import socket
import subprocess

HOST = "192.168.2.101"
PORT = 2323

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Servidor Telnet iniciado...")

while True:

    cliente, endereco = server.accept()

    print(f"Conexão de {endereco}")

    while True:

        comando = cliente.recv(1024).decode()

        if not comando:
            break

        try:

            resultado = subprocess.check_output(
                comando,
                shell=True,
                stderr=subprocess.STDOUT
            )

            cliente.send(resultado)

        except Exception as erro:

            cliente.send(str(erro).encode())

    cliente.close()