import random as rd

def pontocodigo():
    print('Usuario falhou ponto para o PC')
    print('-' * 20)
def pontousuario():
    print('Usuario acertou')
    print('-' * 20)
def numeros():
    print(f'\nNumero gerado pelo código foi {numgr}')
    print(f'Numero escolhido pelo Usuario foi {numusuario}')
def pontuacao():
    print(f'\n\033[42m' + '\033[1m' + '\033[33m' + '\nPontuação total' + '\033[0;0m')
    print(f'Usuario: {pontuacaopc} pontos\nA.I: {pontuacaopc} pontos\n')

n = 0
nwhl = 5
pontuacaopc = 0
pontuacaousuario = 0

while n < nwhl:
    n += 1
    numusuario = int(input('Digite um numero entre 0 é 10: '))
    numgr = int(rd.uniform(0, 10))

    numeros()
    if numusuario == numgr:
        pontocodigo()
    elif numusuario != numgr:
        pontousuario()
        pontuacaousuario =+ 1

pontuacao()
if pontuacaousuario == pontuacaopc:
    print('Ambos ' + '\u001b[33m' + '\033[1m' + 'empataram' + '\033[0;0m')
elif pontuacaousuario > pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'Código' + '\033[0;0m')
elif pontuacaousuario < pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'Usario' + '\033[0;0m')
