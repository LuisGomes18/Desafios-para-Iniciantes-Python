from random import randint


N = 0
NUMERO_SORTEADO_GERAL = 0
minimo = 1
maximo = 10


while N < 5:
    NUMERO_SORTEADO_GERAL = randint(minimo, maximo)
    numero_sorteado_1 = randint(minimo, maximo)
    numero_sorteado_2 = randint(minimo, maximo)

    print(f'\nNumero Sorteado: {NUMERO_SORTEADO_GERAL}')
    print(f'Número sorteado 1: {numero_sorteado_1}')
    print(f'Número sorteado 2: {numero_sorteado_2}')

    if numero_sorteado_1 == NUMERO_SORTEADO_GERAL and \
    numero_sorteado_2 == NUMERO_SORTEADO_GERAL:
        print('Empate')
    elif numero_sorteado_1 == NUMERO_SORTEADO_GERAL:
        print('Numero sorteado 1 vence a ronda')
    elif numero_sorteado_2 == NUMERO_SORTEADO_GERAL:
        print('Numero sorteado 2 vence a ronda')

    N += 1
