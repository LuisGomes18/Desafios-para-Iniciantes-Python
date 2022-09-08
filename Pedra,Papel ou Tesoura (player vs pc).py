import random as rd


escolha = ["pedra", "papel", "tesoura"]
n = 0
pontuacaousuario = 0
questoeserradas = 0
empates = 0

def empate():
    print(f'\nUsuário escolheu {resulusuario}\nCódigo escolheu {resulcodigo}')
    print('\033[94m' + 'Houve um empate\n' + '\033[0m')
    global empates
    empates += 1

def certo():
    print(f'\nUsuário escolheu {resulusuario}\nCódigo escolheu {resulcodigo}')
    print('\033[32m' + 'Ponto para Usuário\n' + '\033[0m')
    global pontuacaousuario
    pontuacaousuario += 1 

def errado():
    print(f'\nUsuário escolheu {resulusuario}\nCódigo escolheu {resulcodigo}')
    print('\033[31m' + 'Ponto para Código\n' + '\033[0m')
    global questoeserradas
    questoeserradas += 1

while n < 3:

    n += 1

    resulcodigo = rd.choice(escolha)
    resulusuario = str(input('Sua vez de jogar: '))

    #Verificar se e igual
    if resulusuario == resulcodigo:
        empate()

    #Teste ao var resulusuario
    if resulusuario == "pedra":
        if resulcodigo == "tesoura":
            certo()
    if resulusuario == "tesoura":
        if resulcodigo == "papel":
            certo() 
    if resulusuario == "papel":
        if resulcodigo == "pedra":
            certo()

    #Teste ao var resulcodigo
    if resulcodigo == "pedra":
        if resulusuario == "tesoura":
            errado()
    if resulcodigo == "tesoura":
        if resulusuario == "papel":
            errado()
    if resulcodigo == "papel":
        if resulusuario == "pedra":
            errado()                                                          

print('\033[93m' + '\nPontuação Final' + '\033[0m')
if empates >= 1:  
    if pontuacaousuario == 1:
        print('A Usuário acertou ' + '\033[32m' + f'{pontuacaousuario}' + '\033[0m' + ' vez')
    else:     
        print('A Usuário acertou ' + '\033[32m' + f'{pontuacaousuario}' + '\033[0m' + ' vezes')
    if questoeserradas == 1:
        print('Errou ' + '\033[31m' + f'{questoeserradas}' + '\033[0m' + ' vez')
    else:     
        print('Errou ' + '\033[31m' + f'{questoeserradas}' + '\033[0m' + ' vezes')  
    if empates == 1:
        print('E empatou ' + '\033[96m' + f'{empates}' + '\033[0m'+ ' vez')
    else:    
        print('E empatou ' + '\033[96m' + f'{empates}' + '\033[0m'+ ' vezes')
else:
    print('A Usuário acertou ' + '\033[32m' + f'{pontuacaousuario}' + '\033[0m' + ' vezes')
    print('Errou ' + '\033[31m' + f'{questoeserradas}' + '\033[0m' + ' vezes') 