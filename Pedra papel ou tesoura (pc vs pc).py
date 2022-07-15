import random

def acertou():
    print('Pc acertou \n')
def errou():
    print('Pc errou \n') 

jogos = ["pedra", "papel", "tesoura"]
n = 0
pontuacao = 0
while n < 3:
    n += 1
    resultadochoiche = random.choice(jogos)
    resultadopc = random.choice(jogos)
    print(f'O iten sorteado foi {resultadochoiche}')
    print(f'O resultado sorteado pelo pc foi {resultadopc}')

    if resultadochoiche == resultadopc:
        acertou()
        pontuacao +=1
    elif resultadochoiche != resultadopc:
        errou()

print(f'Pontuação final\n De {n} o pc acertou {pontuacao}')        