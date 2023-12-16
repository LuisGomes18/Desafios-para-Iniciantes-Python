from random import choice


movimentos = ['cara', 'coroa']

movimento_geral = choice(movimentos)
jogada_AI_1 = choice(movimentos)
movimentos.remove(jogada_AI_1)
jogada_AI_2 = choice(movimentos)

print(f'AI 1 escolheu {jogada_AI_1}')
print(f'AI 2 escolheu {jogada_AI_2}')
print(f'\nCaiu {movimento_geral}')

if jogada_AI_1 == movimento_geral:
    print('\nAI 1 acertou')
    print('AI 2 errou')
elif jogada_AI_2 == movimento_geral:
    print('\nAI 2 acertou')
    print('AI 1 errou')
