import socket
import pickle
from gomoku import *




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
	#imprime_tabuleiro(tabuleiro)
	#jogada = get_jogada(ln, cl, jogador, tab)
	#print(tabuleiro)
	#cliente.sendall(pickle.dumps(jogada))
	#valida()
	#imprime_tabuleiro(jogada)
	res = cliente.recv(1024)
	print(imprime_tabuleiro(res))
	#jogada = get_jogada(LINHA, COLUNA, JOGADOR, tabuleiro)
	#cliente.send(pickle.dumps(jogada))
	#resposta = cliente.recv(1024)
	#imprime_tabuleiro(pickle.loads(resposta))
cliente.close()
