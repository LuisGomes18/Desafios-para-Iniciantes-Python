def jg1():
    print(f'{player1} marca ponto \n')
def jg2():
    print(f'{player2} marca ponto \n')

n = 0
pontuacaoplayer1 = 0
pontuacaoplayer2 = 0

player1 = str(input('Insira o nome do primeiro jogador: '))
player2 = str(input('Insira o nome do segundo jogador: '))

while n < 3:
    n += 1
    escolhaplayer1 = str(input(f'\n{player1} sua vez: '))
    escolhaplayer2 = str(input(f'{player2} sua vez: '))

    if escolhaplayer1 == "pedra":
        if escolhaplayer2 == "tesoura":
            jg1()
            pontuacaoplayer1 += 1

    if escolhaplayer1 == "tesoura":
        if escolhaplayer2 == "papel":
            jg1()
            pontuacaoplayer1 += 1

    if escolhaplayer1 == "papel":
        if escolhaplayer2 == "pedra":
            jg1()
            pontuacaoplayer1 += 1

    if escolhaplayer2 == "pedra":
        if escolhaplayer1 == "tesoura":
            jg2()
            pontuacaoplayer2 += 1

    if escolhaplayer2 == "tesoura":
        if escolhaplayer1 == "papel":
            jg2()
            pontuacaoplayer2 += 1

    if escolhaplayer2 == "papel":
        if escolhaplayer1 == "pedra":
            jg2()
            pontuacaoplayer2 += 1

print(f'\n\033[42m' + '\033[1m' + '\033[33m' + '\nPontuação total' +'\033[0;0m')
print(f'{player1}: {pontuacaoplayer1} pontos\n{player2}: {pontuacaoplayer2} pontos\n')
if pontuacaoplayer1 > pontuacaoplayer2:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + f'{player1}' +'\033[0;0m')
elif pontuacaoplayer1 < pontuacaoplayer2:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + f'{player2}' +'\033[0;0m')