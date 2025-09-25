from random import choice


movimentos = ['cara', 'coroa']
movimento_geral = choice(movimentos)

jogada_usuario = str(input('Escolha seu Movimento (cara ou coroa): ')).lower()
while jogada_usuario not in movimentos:
    jogada_usuario = str(input('Escolha seu Movimento (cara ou coroa): ')).lower()
movimentos.remove(jogada_usuario)

movimento_pc = choice(movimentos)

print(f'\nPC escolheu {movimento_pc}')
print(f'Usuario escolheu {jogada_usuario}')
print(f'Caiu {movimento_geral}')

if movimento_pc == movimento_geral:
    print('\nPC acertou')
    print('Usuario errou')
elif jogada_usuario == movimento_geral:
    print('\nUsuario acertou')
    print('PC errou')
