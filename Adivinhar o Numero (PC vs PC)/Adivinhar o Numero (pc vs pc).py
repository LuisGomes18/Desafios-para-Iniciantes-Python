import random as rd


n = 0
questoescertas = 0
questoeserradas = 0

def certo():
    print(f'Numero do código --> {codigo}')
    print(f'Numero da A.I --> {ai}')
    print('\033[32m' + 'A.I conseguiu acertar o numero\n' + '\033[0m')
    global questoescertas
    questoescertas += 1

def errado():
    print(f'Numero do código --> {codigo}')
    print(f'Numero da A.I --> {ai}')
    print('\033[31m' + 'A.I não consegui acertar o numero\n' + '\033[0m')    

def pontuacao():
    print('\033[93m' + '\nPontuação Final' + '\033[0m')
    global questoeserradas
    questoeserradas = 5 - questoescertas
    print('A A.I acertou ' + '\033[32m' + f'{questoescertas}' + '\033[0m' + ' numeros')
    print('A A.I errou ' + '\033[31m' + f'{questoeserradas}' + '\033[0m' + ' numeros')

while n < 5:
    n += 1

    codigo = int(rd.uniform(0, 10))
    ai = int(rd.uniform(0, 10))

    if codigo == ai:
        certo()
    else:
        errado()

pontuacao()