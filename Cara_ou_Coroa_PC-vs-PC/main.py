from random import choice


movimentos = ['cara', 'coroa']
movimento_geral = choice(movimentos)

movimento_escolhido_1 = choice(movimentos)
movimentos.remove(movimento_escolhido_1)
movimento_escolhido_2 = choice(movimentos)

print(f'\nMovimento escolhido 1 escolheu {movimento_escolhido_1}')
print(f'Movimento escolhido 2 escolheu {movimento_escolhido_2}')
print(f'Caiu {movimento_geral}')

if movimento_escolhido_1 == movimento_geral:
    print('\nMovimento escolhido 1 acertou')
    print('Movimento escolhido 2 errou')
elif movimento_escolhido_2 == movimento_geral:
    print('\nMovimento escolhido 2 acertou')
    print('Movimento escolhido 1 errou')
