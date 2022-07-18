import random

def acertou():
    print('Acertou')

def errou():
    print('Errou')
pontuacaojogador  =  0
pontuacaopc = 0 

jogo = ["pedra", "papel", "tesoura"]
n = 0
while n < 3:
    n += 1
    resultadopc = random.choice(jogo)

    resultadousuario = str(input('\n Qual sua jogada: '))
    print(f'Joga do pc foi: {resultadopc}')

    if resultadopc == resultadousuario:
        acertou()
        pontuacaojogador += 1
    elif resultadopc != resultadousuario:
        errou()
        pontuacaopc +=1

print(f'\n\033[42m'+'\033[1m'+'\033[33m'+'\nPontuação total'+ '\033[0;0m')
print(f'Jogador 1: {pontuacaojogador} pontos\nJogador 2: {pontuacaopc} pontos\n')
if pontuacaojogador == pontuacaopc:
 print('Empate')
elif pontuacaojogador > pontuacaopc:
 print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m'  + 'Jogador' + '\033[0;0m')
elif pontuacaojogador < pontuacaopc:
 print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m'  + 'PC' + '\033[0;0m')