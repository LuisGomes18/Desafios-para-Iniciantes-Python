from random import choice

movimentos = ['cara', 'coroa']
n = 0

while n == 0:
    movimento = choice(movimentos)
    jogada_ai = choice(movimentos)
    jogada_usuario = str(input('Insira o seu movimentos: '))
    jogada_usuario.lower()
    while jogada_usuario not in movimentos:
        jogada_usuario = str(input('Insira o seu movimentos'))
        jogada_usuario.lower()
    print(f'Caiu {movimento}')
    print(f'\nAI escolheu {jogada_ai} e Usuario escolheu {jogada_usuario}')
    if movimento == jogada_ai and movimento != jogada_usuario:
        print('AI acertou')
        print('Usuario perdeu')
    elif movimento == jogada_usuario and movimento != jogada_ai:
        print('Usuario acertou')
        print('AI perdeu')
    n = 1
