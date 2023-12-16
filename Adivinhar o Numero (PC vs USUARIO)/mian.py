from random import randint


N = 0
PONTOS_AI_1 = 0
PONTOS_UTILIZADOR = 0

while N < 5:
    numero_escolhido_AI_1 = randint(1, 10)
    numero_escolhido_Usuario = int(input('Insira um numero: (1 a 10): '))
    while numero_escolhido_Usuario not in range(1, 11):
        numero_escolhido_Usuario = int(input('Insira um numero: (1 a 10): '))

    print(f'\nNúmero escolhido por AI 1: {numero_escolhido_AI_1}')
    print(f'Número escolhido por AI 2: {numero_escolhido_Usuario}')
    if numero_escolhido_AI_1 == numero_escolhido_Usuario:
        print('Empate')
    elif numero_escolhido_AI_1 > numero_escolhido_Usuario:
        print('Ponto para AI 1')
        PONTOS_AI_1 += 1
    elif numero_escolhido_AI_1 < numero_escolhido_Usuario:
        print('Ponto para AI 2')
        PONTOS_UTILIZADOR += 1

    print(f'Pontos do AI 1: {PONTOS_AI_1}')
    print(f'Pontos do Utilizador: {PONTOS_UTILIZADOR}\n')
    N += 1


print('\nPontuação Final: ')
print(f'Pontos do AI 1: {PONTOS_AI_1}')
print(f'Pontos do Utilizador: {PONTOS_UTILIZADOR}')
