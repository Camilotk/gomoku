import socket, os, pickle
from _thread import *
from gomoku import *

tabuleiro = [9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             2, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             3, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             4, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             5, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             6, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             7, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             8, 0, 0, 0, 0, 0, 0, 0, 0, 9,
             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
             ]


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


# def threads_cliente(conexao):
#     print(conexao[0])
#     conexao.sendall(str.encode('Server is working:'))
#     while True:
#         conexao.sendall(str.encode('Server is working:'))
#         data = conexao.recv(2048)
#         response = pickle.loads(data)
#         if not data:
#             break
# 		#conexao.sendall(response)
#     conexao.close()

enderecos = []
while True:
    jogador1, endereco = servidor.accept()
    print('Conectado a:' + endereco[0] + ':' + str(endereco[1]))
    enderecos.append(endereco[0] + ':' + str(endereco[1]))
    jogador2, endereco = servidor.accept()
    print('Conectado a:' + endereco[0] + ':' + str(endereco[1]))
    enderecos.append(endereco[0] + ':' + str(endereco[1]))
    jogador1.sendall(pickle.dumps(tabuleiro))
    jogador2.sendall(b'teste2')


servidor.close()
