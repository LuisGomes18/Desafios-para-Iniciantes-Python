import getpass
import random


NUMERO_GERAL = random.randint(1, 10)

numero_player_1 = int(getpass.getpass('\nPlayer 1 escolha um numero de 1 a 10: '))
while numero_player_1 not in range(1, 10):
    numero_player_1 = int(getpass.getpass('Player 1 escolha um numero de 1 a 10: '))

numero_player_2 = int(getpass.getpass('Player 2 escolha um numero de 1 a 10: '))
while numero_player_2 not in range(1, 10):
    numero_player_2 = int(getpass.getpass('Player 2 escolha um numero de 1 a 10: '))

print(f'\nPlayer 1 escolheu o numero: {numero_player_1}')
print(f'Player 2 escolheu o numero: {numero_player_2}')
print(f'O numero sorteado foi {NUMERO_GERAL}')


print('\n')
if numero_player_1 == NUMERO_GERAL and \
numero_player_2 == NUMERO_GERAL:
    print('Empate')
elif numero_player_1 == NUMERO_GERAL:
    print('Player 1 acertou')
elif numero_player_2 == NUMERO_GERAL:
    print('Player 2 acertou')
else:
    print('Ninguem acetou o numero :(')
