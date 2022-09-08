import os

n = 0
pontuacaojogador1 = 0
pontuacaojogador2 = 0

def empate():
    print(f'\nJogador 1 escolheu {jogadajogador1}\nJogador 2 escolheu {jogadajogador2}')
    print('\033[94m' + 'Houve um empate\n' + '\033[0m')

def jogador1():
    print(f'\nJogador 1 escolheu {jogadajogador1}\nJogador 2 escolheu {jogadajogador2}')
    print('\033[32m' + 'Ponto para Jogador 1\n' + '\033[0m')
    pontuacaojogador1 += 1  

def jogador2():
    print(f'\nJogador 1 escolheu {jogadajogador1}\nJogador 2 escolheu {jogadajogador2}')
    print('\033[32m' + 'Ponto para Jogador 2\n' + '\033[0m')
    pontuacaojogador2 += 1            

while n < 3:
    n += 1

    jogadajogador1 = str(input('Sua vez de jogar jogador 1: '))
    os.system('clear')
    jogadajogador2 = str(input('Sua vez de jogar jogador 2: '))
    os.system('clear')

    #Verificar se e igual
    if jogadajogador1 == jogadajogador2:
        empate()

    #Teste ao var jogadajogador1
    if jogadajogador1 == "pedra":
        if jogadajogador2 == "tesoura":
            jogador1()
    if jogadajogador1 == "tesoura":
        if jogadajogador2 == "papel":
            jogador1()
    if jogadajogador1 == "papel":
        if jogadajogador2 == "pedra":
            jogador1() 

    #Teste ao var jogadajogador2
    if jogadajogador2 == "pedra":
        if jogadajogador1 == "tesoura":
            jogador2()
    if jogadajogador2 == "tesoura":
        if jogadajogador1 == "papel":
            jogador2()
    if jogadajogador2 == "papel":
        if jogadajogador1 == "pedra":
            jogador2()

print('\033[93m' + '\nPontuação Final' + '\033[0m')
print(f'Jogador 1 marcou {pontuacaojogador1} pontos\nJogador 2 marcou {pontuacaojogador2} pontos')             