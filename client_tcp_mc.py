import socket
import pickle
from gomoku import *


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


LINHA = 0
COLUNA = 0

cliente = socket.socket()
host = 'localhost'
porta = 8000
destino = (host, porta)


print('Esperando')
try:
    cliente.connect(destino)
except socket.error as e:
    print(str(e))

res = cliente.recv(1024)

while True:
	if CONT_JOGADAS % 2 != 0:
		JOGADOR = 1
	else:
		JOGADOR = 2
	CONT_JOGADAS += 1
	ln = 0
	cl = 0
	jogador = JOGADOR
	tab = tabuleiro
	#mensagem = cliente.recv(1024)
	#print(mensagem.decode(utf-8))
	imprime_tabuleiro(tabuleiro)
	jogada = get_jogada(ln, cl, jogador, tab)
	print(tabuleiro)
	cliente.sendall(pickle.dumps(jogada))
	valida()
	imprime_tabuleiro(jogada)
	res = cliente.recv(1024)
	print(res.decode('utf-8'))
	#jogada = get_jogada(LINHA, COLUNA, JOGADOR, tabuleiro)
	#cliente.send(pickle.dumps(jogada))
	#resposta = cliente.recv(1024)
	#imprime_tabuleiro(pickle.loads(resposta))
cliente.close()
