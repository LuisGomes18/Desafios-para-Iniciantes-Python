from random import randint

n = 0
pontos_AI_1 = 0
pontos_Utilizador = 0


def verificacao(numero_escolhido_AI_1, numero_Utilizador, pontos_AI_1, pontos_Utilizador):
    if numero_escolhido_AI_1 == numero_Utilizador:
        print('Empate')
    elif numero_escolhido_AI_1 > numero_Utilizador:
        print('Ponto para AI 2')
        pontos_Utilizador += 1
    elif numero_escolhido_AI_1 < numero_Utilizador:
        print('Ponto para AI 1')
        pontos_AI_1 += 1

    return pontos_AI_1, pontos_Utilizador


while n < 5:
    numero_escolhido_AI_1 = randint(0, 10)
    numero_Utilizador = int(input('Escreva o numero: '))
    pontos_AI_1, pontos_AI_2 = verificacao(numero_escolhido_AI_1, numero_Utilizador, pontos_AI_1, pontos_Utilizador)
    print('\033[32m' + f'Pontos do AI 1: {pontos_AI_1}')
    print(f'Pontos do Utilizador: {pontos_Utilizador}\n' + '\033[0m')
    n += 1

print('\033[1m' + '\nPontuacao Final' + '\033[0m')
print('\033[33m' + f'Pontos do AI 1: {pontos_AI_1}')
print(f'Pontos do Utilizador: {pontos_Utilizador}' + '\033[0m')
