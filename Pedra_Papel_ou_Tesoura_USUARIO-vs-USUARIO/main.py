import getpass


MOVIMENTOS_PERMITIDOS = ['pedra', 'papel', 'tesoura']
pontos_player_1 = 0
pontos_player_2 = 0
n = 0

while n < 3:
    jogada_player_1 = getpass.getpass('\nSua vez de jogar player 1: ').lower()
    while jogada_player_1 not in MOVIMENTOS_PERMITIDOS:
        print('Jogada inválida! Tente novamente.')
        jogada_player_1 = getpass.getpass('Sua vez de jogar player 1: ').lower()

    jogada_player_2 = getpass.getpass('Sua vez de jogar player 2: ').lower()
    while jogada_player_2 not in MOVIMENTOS_PERMITIDOS:
        print('Jogada inválida! Tente novamente.')
        jogada_player_2 = getpass.getpass('Sua vez de jogar player 2: ').lower()

    print(f'\nPlayer 1 jogou: {jogada_player_1}')
    print(f'Player 2 jogou: {jogada_player_2}\n')

    if jogada_player_1 == jogada_player_2:
        print('Empate!')
    elif jogada_player_1 == 'pedra' and jogada_player_2 == 'tesoura':
        print('Player 1 venceu essa rodada!')
        pontos_player_1 += 1
    elif jogada_player_1 == 'papel' and jogada_player_2 == 'pedra':
        print('Player 1 venceu essa rodada!')
        pontos_player_1 += 1
    elif jogada_player_1 == 'tesoura' and jogada_player_2 == 'papel':
        print('Player 1 venceu essa rodada!')
        pontos_player_1 += 1
    else:
        print('Player 2 venceu essa rodada!')
        pontos_player_2 += 1
    n += 1


print('\nPontacao Final: ')
print(f'Placar final - Player 1: {pontos_player_1}, Player 2: {pontos_player_2}')
