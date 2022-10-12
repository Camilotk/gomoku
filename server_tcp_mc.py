import socket, os, pickle
from _thread import *
from gomoku import *


host = 'localhost'
porta = 8000
origem = (host, porta)
servidor = socket.socket()
contador_thread = 0


try:
    servidor.bind(origem)

except socket.error as e:
    print(str(e))
print('Servidor ativo')
servidor.listen(5)


def threads_cliente(conexao):
	for i in enderecos:
		print(i)
	conexao.sendall(str.encode('Server is working:'))
	while True:
		conexao.sendall(str.encode('Server is working:'))
		data = conexao.recv(2048)
		response = pickle.loads(data)
		if not data:
			break
		#conexao.sendall(response)
	conexao.close()

enderecos = []
while True:
	cliente, endereco = servidor.accept()
	print('Connected to:' + endereco[0] + ':' + str(endereco[1]))
	enderecos.append(endereco[0] + ':' + str(endereco[1]))
	start_new_thread(threads_cliente, (cliente,))
	contador_thread += 1
	print('Threaded number:' + str(contador_thread))

servidor.close()

def get_jogada(ln: int, cl: int, jogador: int, tab: List) -> tabuleiro:
    escolha_jogador = 0
    print(f"\nJogador {jogador} insira sua escolha \n")

    while escolha_jogador < 1 or escolha_jogador > LINHAS:
        try:
            escolha_jogador = int(
                input(f"Por favor escolha uma linha entre 1 e {LINHAS} > "))
        except ValueError:
            print('Por favor insira um valor válido')
        ln = escolha_jogador

    escolha_jogador = 0
    while escolha_jogador < 1 or escolha_jogador > COLUNAS:
        try:
            escolha_jogador = int(
                input(f"Por favor escolha uma coluna entre 1 e {LINHAS} > "))
        except ValueError:
            print('Por favor insira um valor válido')
        cl = escolha_jogador

    posicao = ((int(ln)*largura_tabuleiro))+(int(cl))

    if jogador == 1:
        tab[posicao] = 1
    else:
        tab[posicao] = 2

    return tab