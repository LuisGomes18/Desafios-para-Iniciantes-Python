from random import choice


movimentos = ['cara', 'coroa']

movimento_geral = choice(movimentos)
JOGADA_USUARIO = str(input('Escolha seu Movimento (cara ou coroa): '))
while JOGADA_USUARIO not in movimentos:
    JOGADA_USUARIO = str(input('Escolha seu Movimento (cara ou coroa): '))
JOGADA_USUARIO = JOGADA_USUARIO.lower()
movimentos.remove(JOGADA_USUARIO)
jogada_AI = choice(movimentos)

print(f'AI escolheu {jogada_AI}')
print(f'Usuario escolheu {JOGADA_USUARIO}')
print(f'\nCaiu {movimento_geral}')

if jogada_AI == movimento_geral:
    print('\nAI acertou')
    print('Usuario errou')
elif JOGADA_USUARIO == movimento_geral:
    print('\nUsuario acertou')
    print('AI errou')
