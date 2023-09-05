# Cliente
import socket

def main():
    host = '127.3.2.1'
    porta = 8080

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    while True:
        comando = input("Digite 'd' para Data, 'h' para Hora, 'dh' para Data e Hora, ou 'sair' para sair: ")
        if comando == 'sair':
            break
        cliente.send(comando.encode('utf-8'))
        resposta = cliente.recv(1024).decode('utf-8')
        print("Resposta do servidor:", resposta)
        print("----------------")

    cliente.close()

if __name__ == '__main__':
    main()
