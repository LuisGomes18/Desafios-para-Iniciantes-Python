import random
import getpass


MOVIMENTOS = ['cara', 'coroa']
MOVIMENTO_GERAL = random.choice(MOVIMENTOS)

movimento_player_1 = getpass.getpass('\nQual o seu movimento player 1? ')
while movimento_player_1 not in MOVIMENTOS:
    movimento_player_1 = getpass.getpass('Qual o seu movimento player 1? ')

MOVIMENTOS.remove(movimento_player_1)

movimento_player_2 = getpass.getpass('Qual o seu movimento player 2? ')
while movimento_player_2 not in MOVIMENTOS:
    movimento_player_2 = getpass.getpass('Qual o seu movimento player 2? ')

print(f'\nO player 1 escolheu {movimento_player_1}')
print(f'O player 2 escolheu {movimento_player_2}')
print(f'Caiu: {MOVIMENTO_GERAL}\n')

if movimento_player_1 == MOVIMENTO_GERAL:
    print('Player 1 venceu')

if movimento_player_2 == MOVIMENTO_GERAL:
    print('Player 2 venveu')
