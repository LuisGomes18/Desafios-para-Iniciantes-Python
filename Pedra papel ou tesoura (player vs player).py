n = 0
pontuacaoplayer1 = 0
pontuacaoplayer2 = 0
def jg1 ():
    print(f'{jogador1} marca ponto \n')
def jg2 ():
    print(f'{jogador2} marca ponto \n')    
jogador1 = str(input('Insira o nome do primeiro jogador: '))
jogador2 = str(input('Insira o nome do segundo jogador: '))

while n < 3:
    n += 1
    escolhaplayer1 = str(input(f'\n{jogador1} sua vez: '))
    escolhaplayer2 = str(input(f'{jogador2} sua vez: '))

    if escolhaplayer1 == "pedra":
        if escolhaplayer2 == "tesoura":
            jg1 ()
            pontuacaoplayer1 += 1

    if escolhaplayer1 == "tesoura":
        if escolhaplayer2 == "papel":
            jg1 ()
            pontuacaoplayer1 +=1

    if escolhaplayer1 == "papel":
        if escolhaplayer2 == "pedra":
            jg1 ()
            pontuacaoplayer1 += 1

    if escolhaplayer2 == "pedra":
        if escolhaplayer1 == "tesoura":
            jg2 ()
            pontuacaoplayer2 += 1

    if escolhaplayer2 == "tesoura":
        if escolhaplayer1 == "papel":
            jg2 ()
            pontuacaoplayer2 += 1

    if escolhaplayer2 == "papel":
        if escolhaplayer1 == "pedra":
            jg2 ()        
            pontuacaoplayer2 += 1

print(f'\033[42m'+'\033[1m'+'\033[33m'+'\nPontuação total'+ '\033[0;0m')
print(f'Jogador 1: {pontuacaoplayer1} pontos\nJogador 2: {pontuacaoplayer2} pontos\n')
if pontuacaoplayer1 == pontuacaoplayer2:
 print('Empate')
elif pontuacaoplayer1 > pontuacaoplayer2:
 print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m'  + f'{jogador1}' + '\033[0;0m')
elif pontuacaoplayer1 < pontuacaoplayer2:
 print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m'  + f'{jogador2}' + '\033[0;0m')