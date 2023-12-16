from random import choice

cores = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'rosa', 'roxo']
comida = ['esparguete', 'macarrão', 'arroz', 'bife', 'fiambre', 'queijo']
TENTATIVA = 0

esc = int(input('''\nEscolhe qual categoria que:\n
1) Cores
2) Comida
--> '''))

if esc == 1:
    print('\nEstas são os itens do jogo')
    for e in cores:
        print(f'-> {e}')

    escolha_geral = choice(cores)

    while TENTATIVA < 3:
        ESCOLHA = str(input('Qual sua jogada: '))
        ESCOLHA = ESCOLHA.lower()
        if escolha_geral == ESCOLHA:
            print('Voce acertou')
            break
        elif escolha_geral != ESCOLHA and escolha_geral in cores:
            print('\nVoce errou')
            TENTATIVA += 1
            print(f'TENTATIVA {TENTATIVA}\n')
        else:
            print('Resposta invalida\n')

if esc == 2:
    print('Estas são os itens do jogo')
    for e in comida:
        print(f'-> {e}')

    escolha_geral = choice(comida)

    while TENTATIVA < 3:
        ESCOLHA = str(input('Qual sua jogada: '))
        ESCOLHA = ESCOLHA.lower()
        if escolha_geral == ESCOLHA:
            print('Voce acertou')
        elif escolha_geral != ESCOLHA and escolha_geral in comida:
            print('\nVoce errou')
            TENTATIVA += 1
            print(f'TENTATIVA {TENTATIVA}\n')
        else:
            print('Resposta invalida\n')
