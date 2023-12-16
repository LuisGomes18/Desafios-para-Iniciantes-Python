from random import choice

movimentos = ['pedra', 'papel', 'tesoura']
ponto_AI_1 = 0
ponto_AI_2 = 0
n = 0

while n < 5:
    movimento_AI_1 = choice(movimentos)
    movimento_AI_2 = choice(movimentos)
    
    print(f'\nAI 1 escolheu {movimento_AI_1}')
    print(f'AI 2 escolheu {movimento_AI_2}\n')
    if movimento_AI_1 == movimento_AI_2:
        print('Empatou')
    elif movimento_AI_1 == 'pedra' and movimento_AI_2 == 'tesoura':
        print('Ponto para AI 1')
        ponto_AI_1 += 1
    elif movimento_AI_1 == 'papel' and movimento_AI_2 == 'pedra':
        print('Ponto para AI 1')
        ponto_AI_1 += 1
    elif movimento_AI_1 == 'tesoura' and movimento_AI_2 == 'papel':
        print('Ponto para AI 1')
        ponto_AI_1 += 1
    else:
        print('Ponto para AI 2')
        ponto_AI_2 += 1
    print('\n')
    n += 1

print('\nPontuacao Final')
print(f'AI 1 fez {ponto_AI_1}\nAI 2 fez {ponto_AI_2}')
