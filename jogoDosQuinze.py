import random

jogando = True
matriz = []
rodada = 1


def main():

    tutorial()
    geraMatriz(matriz)

    while jogando:
        imprimeJogo(matriz)


def geraMatriz(tabuleiro):
    lista = list(range(0, 16))
    for _ in range(4):
        linha = []
        for _ in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        tabuleiro.append(linha)


def imprimeJogo(tabuleiro):
    print('============= RODADA %d =============' % rodada)
    t = tabuleiro
    t0, t1, t2, t3 = t[0], t[1], t[2], t[3]
    print('|%2.d %2.d %2.d %2.d|' % (t0[0], t0[1], t0[2], t0[3], ))
    print('|%2.d %2.d %2.d %2.d|' % (t1[0], t1[1], t1[2], t1[3], ))
    print('|%2.d %2.d %2.d %2.d|' % (t2[0], t2[1], t2[2], t2[3], ))
    print('|%2.d %2.d %2.d %2.d|' % (t3[0], t3[1], t3[2], t3[3], ))
    opcao = True
    verificaSeJogadorDesejaInserirUmaPosicao(opcao)


def verificaSeJogadorDesejaInserirUmaPosicao(opcao):
    if opcao:
        jogadaValida = recebeJogada()
        if not jogadaValida:
            print("\nJogada inválida")
            imprimeJogo(matriz)


def fazerJogada(linhaPeca, colunaPeca, linhaVazia, colunaVazia):

    aux = matriz[linhaPeca][colunaPeca]
    matriz[linhaPeca][colunaPeca] = 0
    matriz[linhaVazia][colunaVazia] = aux

    verificaSeVenceu()


def verificaSeVenceu():
    global jogando
    jogoVencedor = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    venceu = matriz == jogoVencedor
    if venceu:
        jogando = False
        print("Parabéns, Você venceu O Jogo em %d rodadas!!!" % rodada)
    return venceu


def recebeJogada():
    global rodada

    jogadaValida = False

    jogada = input("Qual peça voce deseja mover? ")
    if jogada == "":
        return False
    jogada = int(jogada)
    linhaPeca, colunaPeca, linhaVazia, colunaVazia, jogadaValida = achaPosicaoJogada(
        jogada)
    if jogadaValida:
        fazerJogada(linhaPeca, colunaPeca, linhaVazia, colunaVazia)
        rodada += 1
        return True
    return False


def achaPosicaoJogada(num):
    linhaPeca = colunaPeca = linhaVazia = colunaVazia = 0
    linha1 = matriz[0]
    linha2 = matriz[1]
    linha3 = matriz[2]
    linha4 = matriz[3]

    if linha1.count(num) == 1:
        linhaPeca = 0
        colunaPeca = linha1.index(num)
    elif linha2.count(num) == 1:
        linhaPeca = 1
        colunaPeca = linha2.index(num)
    elif linha3.count(num) == 1:
        linhaPeca = 2
        colunaPeca = linha3.index(num)
    elif linha4.count(num) == 1:
        linhaPeca = 3
        colunaPeca = linha4.index(num)

    linhaVazia, colunaVazia, jogadaValida = verificaJogada(
        linhaPeca, colunaPeca)
    if jogadaValida:
        return linhaPeca, colunaPeca, linhaVazia, colunaVazia, jogadaValida
    return -1, -1, -1, -1, jogadaValida


def verificaJogada(linhaPeca, colunaPeca):
    linhaVazia = colunaVazia = 0
    numeroNorte = numeroSul = numeroLeste = numeroOeste = -1

    linhaNorte = linhaPeca - 1
    colunaNorte = colunaPeca
    linhaSul = linhaPeca + 1
    colunaSul = colunaPeca
    linhaLeste = linhaPeca
    colunaLeste = colunaPeca + 1
    linhaOeste = linhaPeca
    colunaOeste = colunaPeca - 1

    if 4 > linhaNorte >= 0 and 4 > colunaNorte >= 0:
        numeroNorte = matriz[linhaNorte][colunaNorte]
    if 4 > linhaSul >= 0 and 4 > colunaSul >= 0:
        numeroSul = matriz[linhaSul][colunaSul]
    if 4 > linhaLeste >= 0 and 4 > colunaLeste >= 0:
        numeroLeste = matriz[linhaLeste][colunaLeste]
    if 4 > linhaOeste >= 0 and 4 > colunaOeste >= 0:
        numeroOeste = matriz[linhaOeste][colunaOeste]
    jogadaValida = False

    if numeroNorte == 0:
        return linhaNorte, colunaNorte, True
    if numeroSul == 0:
        return linhaSul, colunaSul, True
    if numeroLeste == 0:
        return linhaLeste, colunaLeste, True
    if numeroOeste == 0:
        return linhaOeste, colunaOeste, True
    return linhaVazia, colunaVazia, jogadaValida


def tutorial():
    print("Jogo dos Quinze")


main()
