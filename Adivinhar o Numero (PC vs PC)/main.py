from random import randint

n = 0
pontos_AI_1 = 0
pontos_AI_2 = 0


def verificacao(numero_escolhido_AI_1, numero_escolhido_AI_2, pontos_AI_1, pontos_AI_2):
    if numero_escolhido_AI_1 == numero_escolhido_AI_2:
        print('Empate')
    elif numero_escolhido_AI_1 > numero_escolhido_AI_2:
        print('Ponto para AI 1')
        pontos_AI_1 += 1
    elif numero_escolhido_AI_1 < numero_escolhido_AI_2:
        print('Ponto para AI 2')
        pontos_AI_2 += 1

    return pontos_AI_1, pontos_AI_2


while n < 5:
    numero_escolhido_AI_1 = randint(0, 10)
    numero_escolhido_AI_2 = randint(0, 10)
    pontos_AI_1, pontos_AI_2 = verificacao(numero_escolhido_AI_1, numero_escolhido_AI_2, pontos_AI_1, pontos_AI_2)
    print('\033[32m' + f'Pontos do AI 1: {pontos_AI_1}')
    print(f'Pontos do AI 2: {pontos_AI_2}\n' + '\033[0m')
    n += 1

print('\033[1m' + '\nPontuacao Final' + '\033[0m')
print('\033[33m' + f'Pontos do AI 1: {pontos_AI_1}')
print(f'Pontos do AI 2: {pontos_AI_2}' + '\033[0m')
