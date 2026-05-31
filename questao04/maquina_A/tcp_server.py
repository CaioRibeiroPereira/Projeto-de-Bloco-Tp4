import socket

HOST = "192.168.2.101"
PORT = 8080

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORT))

servidor.listen()

print(f"Servidor TCP escutando na porta {PORT}...")

while True:

    cliente, endereco = servidor.accept()

    print(f"Cliente conectado: {endereco}")

    try:

        while True:

            dados = cliente.recv(1024)

            if not dados:
                break

            mensagem = dados.decode()

            print(f"Recebido: {mensagem}")

            cliente.send(
                f"Servidor recebeu: {mensagem}".encode()
            )

    except Exception as erro:

        print("Erro:", erro)

    cliente.close()

    print("Cliente desconectado")