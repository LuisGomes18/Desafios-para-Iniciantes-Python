import random

cores = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'rosa', 'roxo']
comida = ['esparguete', 'macarrão', 'arroz', 'bife', 'fiambre', 'queijo']
tentativa = 0
vermelho = '\033[31m'
amarelo = '\033[33m'
verde = '\033[32m'
normal = '\033[0;0m'

esc = int(input('''Escolhe qual categoria que:\n
1) Cores
2) Comida
--> '''))
if esc == 1:
    print('Estas são os itens do jogo')
    for e in cores:
        print(f'--> {e}')
    print('\n')
    escolha_ai = random.choice(cores)
    while tentativa < 3:
        escolha = str(input('Qual sua jogada: '))
        if escolha_ai == escolha:
            print(verde + 'Voce acertou\n' + normal)
            break
        elif escolha_ai != escolha and escolha in cores:
            print(vermelho + 'Voce errou')
            tentativa += 1
            print(f'Tentativa {tentativa}/3\n' + normal)
        elif escolha not in cores:
            print(amarelo + 'Resposta invalida\n' + normal)
elif esc == 2:
    print('Estas são os itens do jogo')
    for e in comida:
        print(f'--> {e}')
    print('\n')
    escolha_ai = random.choice(comida)
    while tentativa < 3:
        escolha = str(input('Qual sua jogada: '))
        if escolha_ai == escolha:
            print(verde + 'Voce acertou\n' + normal)
            break
        elif escolha_ai != escolha and escolha in comida:
            print(vermelho + 'Voce errou')
            tentativa += 1
            print(f'Tentativa {tentativa}/3\n' + normal)
        elif escolha not in comida:
            print(amarelo + 'Resposta invalida\n' + normal)
    
