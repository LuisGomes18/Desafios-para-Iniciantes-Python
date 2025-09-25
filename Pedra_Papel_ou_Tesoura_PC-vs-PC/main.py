from random import choice


MOVIMENTOS = ['pedra', 'papel', 'tesoura']
ponto_pc_1 = 0
ponto_pc_2 = 0
N = 0


while N < 5:
    movimento_pc_1 = choice(MOVIMENTOS)
    movimento_pc_2 = choice(MOVIMENTOS)

    print(f'\nPC 1 escolheu {movimento_pc_1}')
    print(f'PC 2 escolheu {movimento_pc_2}')

    if movimento_pc_1 == movimento_pc_2:
        print('Empatou')
    elif movimento_pc_1 == 'pedra' and movimento_pc_2 == 'tesoura':
        print('Ponto para PC 1')
        ponto_pc_1 += 1
    elif movimento_pc_1 == 'papel' and movimento_pc_2 == 'pedra':
        print('Ponto para PC 1')
        ponto_pc_1 += 1
    elif movimento_pc_1 == 'tesoura' and movimento_pc_2 == 'papel':
        print('Ponto para PC 1')
        ponto_pc_1 += 1
    else:
        print('Ponto para PC 2')
        ponto_pc_2 += 1

    print('\n')
    N += 1


print('\nPontuacao Final')
print(f'PC 1 fez {ponto_pc_1}\nPC 2 fez {ponto_pc_2}')
