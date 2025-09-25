from random import randint


N = 0
NUMERO_GERAL = 0
PONTOS_PC = 0
PONTOS_UTILIZADOR = 0
minimo = 0
maximo = 10

while N < 5:
    NUMERO_GERAL = randint(minimo, maximo)
    numero_escolhido_pc = randint(minimo, maximo)
    numero_escolhido_usuario = int(input(f'Insira um numero: ({minimo} a {maximo}): '))

    while numero_escolhido_usuario not in range(minimo, maximo):
        numero_escolhido_usuario = int(input(f'Insira um numero: ({minimo} a {maximo}): '))

    print(f'\nNúmero a adivinhar: {NUMERO_GERAL}')
    print(f'Número escolhido por PC: {numero_escolhido_pc}')
    print(f'Número escolhido por Usuario: {numero_escolhido_usuario}')

    if numero_escolhido_pc == NUMERO_GERAL or \
    numero_escolhido_usuario == NUMERO_GERAL:
        print('Empate')
    elif numero_escolhido_pc == NUMERO_GERAL:
        print('Ponto para PC')
        PONTOS_PC += 1
    elif numero_escolhido_usuario == NUMERO_GERAL:
        print('Ponto para Usuario')
        PONTOS_UTILIZADOR += 1

    print(f'\nPontos do AI 1: {PONTOS_PC}')
    print(f'Pontos do Utilizador: {PONTOS_UTILIZADOR}\n')
    N += 1


print('\nPontuação Final: ')
print(f'Pontos do AI 1: {PONTOS_PC}')
print(f'Pontos do Utilizador: {PONTOS_UTILIZADOR}')
