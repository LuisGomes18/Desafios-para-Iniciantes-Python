import random as rd

def pontopc():
    print('PC não certou o numero gerado')
    print('-' * 20)
def acertou():
    print('PC conseguiu acertar o numero')
    print('-' * 20)
def numeros():
    print(f'Numero gerado pelo codigo foi {numpc}')
    print(f'Numero gerado pelo PC foi {numpc2} \n')
def pontuacao():
    print(f'\n\033[42m' + '\033[1m' + '\033[33m' + '\nPontuação total' +'\033[0;0m')
    print(f'PC: {pontuacaopc} pontos\nA.I: {pontuacaopc2} pontos\n')        

n = 0
nwhl = 5
pontuacaopc = 0
pontuacaopc2 = 0

#* Gerador de numeros
while n < nwhl:
    n += 1
    numpc = int(rd.uniform(0, 10)) 
    numpc2 = int(rd.uniform(0, 10))

#* Parte da pontuação
    numeros()
    if numpc == numpc2:
        acertou()
        pontuacaopc2 += 1
    elif numpc != numpc2:
        pontopc()
        pontuacaopc += 1

pontuacao()
if pontuacaopc2 > pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'Código' +'\033[0;0m')
elif pontuacaopc2 < pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'PC' + '\033[0;0m')