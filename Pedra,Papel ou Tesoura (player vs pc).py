import random

def acertou():
    print('Usuario acertou \n')
def empataram():
    print('Ambos empataram \n')
def acertoupc():
    print('PC acertou \n')

pontuacaousuario = 0
pontuacaopc = 0
jogo = ["pedra", "papel", "tesoura"]
n = 0

while n < 3:
    n += 1
    resultadopc = random.choice(jogo)
    resultadousuario = str(input('\n Qual sua jogada: '))
    print(f'Joga do pc foi: {resultadopc}')

    if resultadopc == resultadousuario:
        empataram()
    if resultadousuario == "pedra":
        if resultadopc == "tesoura":
            acertou()
            pontuacaousuario += 1
    if resultadousuario == "tesoura":
        if resultadopc == "papel":
            acertou()
            pontuacaousuario += 1
    if resultadousuario == "papel":
        if resultadopc == "pedra":
            acertou()
            pontuacaousuario += 1

    if resultadopc == "pedra":
        if resultadousuario == "tesoura":
            acertoupc()
            pontuacaousuario += 1
    if resultadopc == "tesoura":
        if resultadousuario == "papel":
            acertoupc()
            pontuacaousuario += 1
    if resultadopc == "papel":
        if resultadousuario == "pedra":
            acertoupc()
            pontuacaousuario += 1

print(f'\033[42m' + '\033[1m' + '\033[33m' + '\nPontuação total' + '\033[0;0m')
print(f'PC: {pontuacaopc} pontos\nPlayer: {pontuacaousuario} pontos\n')
if pontuacaousuario > pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'Usuario' +'\033[0;0m')
elif pontuacaousuario < pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'PC' + '\033[0;0m')