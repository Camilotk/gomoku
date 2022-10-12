from typing import List

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

LINHAS = 8
COLUNAS = 8

altura_tabuleiro = LINHAS + 2
largura_tabuleiro = COLUNAS + 2

LINHA = 0
COLUNA = 0

TAMANHO_TABULEIRO = altura_tabuleiro * largura_tabuleiro
CONT_JOGADAS = 1


def jogadas_restantes(tab):
    for i in range(altura_tabuleiro):
        for j in range(largura_tabuleiro):
            if tab[j+largura_tabuleiro*i] == 0:
                return True
    return False


def imprime_tabuleiro(tab):
    print("\n")
    for i in range(altura_tabuleiro):
        for j in range(largura_tabuleiro):
            print(tab[j+largura_tabuleiro*i], end=" ")
        print("-")


def valida():
    for i in range(1, altura_tabuleiro):
        for j in range(1, largura_tabuleiro-1):
            if 0 < tabuleiro[j+(largura_tabuleiro*i)] < 9:
                if (tabuleiro[j+(largura_tabuleiro)*i] == tabuleiro[j+(largura_tabuleiro*i)+1] and tabuleiro[j+(largura_tabuleiro*i)+1] == tabuleiro[j+(largura_tabuleiro*i)+2]):
                    print(
                        f"\n\t !!! 3 seguidos em uma linha para o : jogador {tabuleiro[j+(largura_tabuleiro)*i]} na linha {i}!!!")
                    break
                elif (tabuleiro[j+(largura_tabuleiro)*i] == tabuleiro[j+(largura_tabuleiro*i)+1]):
                    print(f"\n\t !!! 2 seguidos na linha {i}!!!")


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


if __name__ == "__main__":

    while True:

        if jogadas_restantes(tabuleiro) is False:
            print("Sem jogadas restantes")
            break

        if CONT_JOGADAS % 2 != 0:
            JOGADOR = 1
        else:
            JOGADOR = 2
        CONT_JOGADAS += 1

        get_jogada(LINHA, COLUNA, JOGADOR, tabuleiro)
        imprime_tabuleiro(tabuleiro)
        valida()

# ------------ #
