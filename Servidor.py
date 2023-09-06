# Servidor
import socket
import threading
from datetime import datetime

def tratar_cliente(conexao, endereco):
    print(f"[NOVA CONEXÃO] {endereco} conectado.")
    conectado = True
    while conectado:
        msg = conexao.recv(1024).decode('utf-8')
        if msg == '/sair':
            conectado = False
        elif msg == 'd':
            agora = datetime.now()
            data = agora.strftime("%d/%m/%Y")
            conexao.send(data.encode('utf-8'))
        elif msg == 'h':
            agora = datetime.now()
            hora = agora.strftime("%H:%M:%S")
            conexao.send(hora.encode('utf-8'))
        elif msg == 'dh':
            agora = datetime.now()
            data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")
            conexao.send(data_hora.encode('utf-8'))
        else:
            resposta = "Opção inválida."
            conexao.send(resposta.encode('utf-8'))
    conexao.close()

def iniciar():
    host = '127.3.2.1'
    porta = 8080

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)
    print(f"[OUVINDO] Servidor ouvindo em {host}")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conexao, endereco))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.activeCount() - 1}")

if __name__ == '__main__':
    print("[INICIANDO] Servidor está iniciando")
    print("...")
    iniciar()
