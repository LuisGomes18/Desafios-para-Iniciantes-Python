import random

n = 0
pontuacaopc = 0
pontuacaousuario = 0

def errou():
    print('Usuario errou')
    print('-' * 20)

def acertou():
    print('Usuario acertou')
    print('-' * 20)

def empatou():
    print('Ambos empataram')
    print('-' * 20)

while n < 5:
    n += 1
    numusuario = int(input('Digite um numero entre 0 é 10: '))
    numpc = int(random.uniform(0, 10))
    print(f'\nNumero escolhido foi {numusuario}')
    print(f'Numero gerado pelo pc foi {numpc} \n')

    if numusuario == numpc:
        empatou()
    elif numusuario > numpc:
        acertou()
        pontuacaousuario += 1
    elif numusuario < numpc:
        errou()
        pontuacaopc += 1

print(f'\n\033[42m' + '\033[1m' + '\033[33m' + '\nPontuação total' +'\033[0;0m')
print(f'Usuario: {pontuacaopc} pontos\nA.I: {pontuacaopc} pontos\n')
if pontuacaousuario == pontuacaopc:
    print('Ambos ' + '\u001b[33m' + '\033[1m' + 'empataram' + '\033[0;0m')
elif pontuacaousuario > pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'A.I' +'\033[0;0m')
elif pontuacaousuario < pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'Usario' + '\033[0;0m')