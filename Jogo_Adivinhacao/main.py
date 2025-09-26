from random import choice


CORES = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'rosa', 'roxo']
COMIDA = ['esparguete', 'macarrão', 'arroz', 'bife', 'fiambre', 'queijo']
categoria = []
N = 0

esc = int(input('''\nEscolhe qual categoria que:
1) Cores
2) Comida
--> '''))
if esc == 1:
    categoria = CORES[:]
elif esc == 2:
    categoria = COMIDA[:]


print('\nAs opcoes sao:')
for e in categoria:
    print(f'> {e}')

MOVIMENTO_GERAL = choice(categoria)

while N < 3:
    palpite = input('\nQual é o teu palpite? ').lower()
    while palpite not in categoria:
        palpite = input('Qual é o teu palpite? ').lower()
    if palpite == MOVIMENTO_GERAL:
        print('Acertaste!')
        break
    else:
        print('Erraste!')

    N += 1

print('\nO movimento geral é', MOVIMENTO_GERAL)
