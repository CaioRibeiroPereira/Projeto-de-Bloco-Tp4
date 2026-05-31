import socket

HOST = "192.168.2.101"
PORT = 8081

servidor = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

servidor.bind((HOST, PORT))

print(f"Servidor UDP escutando na porta {PORT}...")

while True:

    dados, endereco = servidor.recvfrom(1024)

    mensagem = dados.decode()

    print(f"{endereco}: {mensagem}")

    servidor.sendto(
        f"Servidor recebeu: {mensagem}".encode(),
        endereco
    )