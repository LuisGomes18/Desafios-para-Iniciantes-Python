import random

def errou():
    print('PC errou')
    print('-' * 20)
def acertou():
    print('PC acertou')
    print('-' * 20)
def empatou():
    print('Ambos empataram')
    print('-' * 20)

n = 0
pontuacaopc = 0
pontuacaoimp = 0

#* Gerador de numeros
while n < 5:
    n += 1
    numimp = int(random.uniform(0, 10))
    numpc = int(random.uniform(0, 10))

    #* Parte da "A.I" para ajudar no mumero gerado pelo PC
    number = int(random.uniform(0, 10))
    if number == 2:
        if numimp != numpc:
            print('A A.I desidiu dar uma ajuda no código')
            print(f'O primeiro numero era: {numpc}')
            numpc = int(random.uniform(0, 10))
            print(f'O novo munero passou a ser: {numpc} \n')

    #* Parte da pontuação
    print(f'Numero escolhido foi {numimp}')
    print(f'Numero gerado pelo pc foi {numpc} \n')
    if numimp == numpc:
        empatou()
    elif numimp > numpc:
        acertou()
        pontuacaopc += 1
    elif numimp < numpc:
        errou()
        pontuacaoimp += 1

print(f'\n\033[42m' + '\033[1m' + '\033[33m' + '\nPontuação total' +'\033[0;0m')
print(f'PC: {pontuacaopc} pontos\nA.I: {pontuacaoimp} pontos\n')
if pontuacaoimp > pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'A.I' +'\033[0;0m')
elif pontuacaoimp < pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'PC' + '\033[0;0m')