from random import choice

movimentos = ['cara', 'coroa']
n = 0

while n == 0:
    movimento = choice(movimentos)
    jogada_ai_1 = choice(movimentos)
    jogada_ai_2 = choice(movimentos)
    print(f'Caiu {movimento}')
    if movimento == jogada_ai_1 and movimento != jogada_ai_2:
        print(f'\nAI 1 escolheu {jogada_ai_1} e AI 2 escolheu {jogada_ai_2}')
        print('AI 1 acertou')
        print('AI 2 errou')
    elif movimento == jogada_ai_2 and movimento != jogada_ai_1:
        print(f'\nAI 1 escolheu {jogada_ai_1} e AI 2 escolheu {jogada_ai_2}')
        print('AI 2 acertou')
        print('AI 1 errou')
    n = 1
