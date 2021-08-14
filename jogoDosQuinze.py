import random

jogando = True
matriz = []
rodada = 1

def main():
    global jogando
    
    tutorial()
    geraMatriz(matriz)

    while jogando:
        imprimeJogo(matriz)    
    return

def geraMatriz(matriz):
    lista = list(range(0, 16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)
                                
def imprimeJogo(matriz):
    global rodada
    print('============= RODADA %d =============' % rodada)

    print('|%2.d %2.d %2.d %2.d|' % (matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], ))
    print('|%2.d %2.d %2.d %2.d|' % (matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], ))
    print('|%2.d %2.d %2.d %2.d|' % (matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], ))
    print('|%2.d %2.d %2.d %2.d|' % (matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], ))
    opcao = True
    verificaSeJogadorDesejaInserirUmaPosicao(opcao)
    
def verificaSeJogadorDesejaInserirUmaPosicao(opcao):
    if opcao:
        jogadaValida = recebeJogada()
        if not jogadaValida:
            print('\nJogada inválida')
            imprimeJogo(matriz)
    return

def fazerJogada(linhaPeca, colunaPeca, linhaVazia, colunaVazia):

    aux = matriz[linhaPeca][colunaPeca]
    matriz[linhaPeca][colunaPeca] = 0
    matriz[linhaVazia][colunaVazia] = aux

    verificaSeVenceu()
    return

def verificaSeVenceu():
    global jogando, rodada
    jogoVencedor = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    venceu = matriz == jogoVencedor
    if venceu:
        jogando = False
        print('Parabéns, Você venceu O Jogo em %d rodadas!!!' % rodada)
    return venceu

def recebeJogada():
    global rodada
    jogadaValida = False

    jogada = input('Qual peça voce deseja mover? ')
    if jogada == '':
        return False
    jogada = int(jogada)
    linhaPeca, colunaPeca, linhaVazia, colunaVazia, jogadaValida = achaPosicaoJogada(jogada)
    if jogadaValida:
        fazerJogada(linhaPeca, colunaPeca, linhaVazia, colunaVazia)
        rodada += 1
        return True
    return False
    
def achaPosicaoJogada(num):
    global matriz
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
    
    linhaVazia, colunaVazia, jogadaValida = verificaJogada(linhaPeca, colunaPeca)
    if jogadaValida:
        return linhaPeca, colunaPeca, linhaVazia, colunaVazia, jogadaValida
    return -1, -1, -1, -1, jogadaValida

def verificaJogada(linhaPeca, colunaPeca):
    global matriz
    
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
    print('Jogo dos Quinze')
    
main()
