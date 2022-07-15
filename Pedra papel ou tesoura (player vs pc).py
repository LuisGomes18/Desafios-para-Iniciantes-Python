import random

def acertou():
    print('Acertou')

def errou():
    print('Errou')

jogo = ["pedra", "papel", "tesoura"]
n = 0
while n < 3:
    n += 1
    resultadopc = random.choice(jogo)

    resultadousuario = str(input('Qual sua jogada: '))

    print(resultadopc)

    if resultadopc == resultadousuario:
        acertou()
    elif resultadopc != resultadousuario:
        errou()