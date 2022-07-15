n = 0
pontuacaoplayer1 = 0
pontuacaoplayer2 = 0
def jogador1 ():
    print('Jogador 1 marca ponto \n')
def jogador2 ():
    print('Jogador 2 marca ponto \n')    

while n < 3:
    n += 1
    escolhaplayer1 = str(input('Jogador 1 suavez: '))
    escolhaplayer2 = str(input('Jogador 2 sua vez: '))

    if escolhaplayer1 == "pedra":
        if escolhaplayer2 == "tesoura":
            jogador1 ()
            pontuacaoplayer1 += 1

    if escolhaplayer1 == "tesoura":
        if escolhaplayer2 == "papel":
            jogador1 ()
            pontuacaoplayer1 +=1

    if escolhaplayer1 == "papel":
        if escolhaplayer2 == "pedra":
            jogador1 ()
            pontuacaoplayer1 += 1

    if escolhaplayer2 == "pedra":
        if escolhaplayer1 == "tesoura":
            jogador2 ()
            pontuacaoplayer2 += 1

    if escolhaplayer2 == "tesoura":
        if escolhaplayer1 == "papel":
            jogador2 ()
            pontuacaoplayer2 += 1

    if escolhaplayer2 == "papel":
        if escolhaplayer1 == "pedra":
            jogador2 ()        
            pontuacaoplayer2 += 1

print(f'\nPontuação total\nJogador 1- {pontuacaoplayer1} pontos\nJogador 2- {pontuacaoplayer2} pontos')
if pontuacaoplayer1 == pontuacaoplayer2:
    print('Empate')
elif pontuacaoplayer1 > pontuacaoplayer2:
    print('Quem ganhou foi o ' + '\u001b[33m' + 'Jogador 1')
elif pontuacaoplayer1 < pontuacaoplayer2:
    print('Quem ganhou foi o ' + '\u001b[33m' + 'Jogador 2')