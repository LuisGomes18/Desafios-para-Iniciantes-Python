from random import choice


MOVIMENTOS = ['pedra', 'papel', 'tesoura']
pontos_pc = 0
pontos_usuario = 0
N = 0
print('\n')

def aumentar_pontos_pc(pontos: int) -> int:
    print('Pontos para o PC')
    pontos += 1
    return pontos

def aumentar_pontos_usuario(pontos: int) -> int:
    print('Ponto para o Usuario')
    pontos += 1
    return pontos

while N < 3:
    movimento_pc = choice(MOVIMENTOS)

    movimento_usuario = input('\nEscolha qual opcao (pedra, papel, tesoura): ').lower()
    while movimento_usuario not in MOVIMENTOS:
        movimento_usuario = input('\nEscolha qual opcao (pedra, papel, tesoura): ').lower()

    print(f'PC escolheu {movimento_pc}\nUsuario escolheu {movimento_usuario}')

    if movimento_pc == movimento_usuario:
        print('Empatou')
    elif movimento_pc == 'pedra' and movimento_usuario == 'tesoura':
        pontos_pc = aumentar_pontos_pc(pontos_pc)
    elif movimento_pc == 'tesoura' and movimento_usuario == 'papel':
        pontos_pc = aumentar_pontos_pc(pontos_pc)
    elif movimento_pc == 'papel' and movimento_usuario == 'pedra':
        pontos_pc = aumentar_pontos_pc(pontos_pc)

    elif movimento_usuario == 'pedra' and movimento_pc == 'tesoura':
        pontos_usuario = aumentar_pontos_usuario(pontos_usuario)
    elif movimento_usuario == 'tesoura' and movimento_pc == 'papel':
        pontos_usuario = aumentar_pontos_usuario(pontos_usuario)
    elif movimento_usuario == 'papel' and movimento_pc == 'pedra':
        pontos_usuario = aumentar_pontos_usuario(pontos_usuario)

    N += 1


print('\nPontuacao final')
print(f'AI 1 fez {pontos_pc}\nUsuario fez {pontos_usuario}')
