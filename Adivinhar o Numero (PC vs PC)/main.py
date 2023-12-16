from random import randint


N = 0
PONTOS_AI_1 = 0
PONTOS_AI_2 = 0

while N < 5:
    numero_escolhido_AI_1 = randint(1, 10)
    numero_escolhido_AI_2 = randint(1, 10)

    print(f'Número escolhido por AI 1: {numero_escolhido_AI_1}')
    print(f'Número escolhido por AI 2: {numero_escolhido_AI_2}')

    if numero_escolhido_AI_1 == numero_escolhido_AI_2:
        print('Empate')
    elif numero_escolhido_AI_1 > numero_escolhido_AI_2:
        print('Ponto para AI 1')
        PONTOS_AI_1 += 1
    elif numero_escolhido_AI_1 < numero_escolhido_AI_2:
        print('Ponto para AI 2')
        PONTOS_AI_2 += 1

    print(f'Pontos do AI 1: {PONTOS_AI_1}')
    print(f'Pontos do AI 2: {PONTOS_AI_2}\n')
    N += 1


print('\nPontuação Final: ')
print(f'Pontos do AI 1: {PONTOS_AI_1}')
print(f'Pontos do AI 2: {PONTOS_AI_2}')
