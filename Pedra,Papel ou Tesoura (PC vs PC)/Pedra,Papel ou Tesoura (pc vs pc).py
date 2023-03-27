import random as rd


escolha = ["pedra", "papel", "tesoura"]
n = 0
pontuacaoai = 0
questoeserradas = 0
empates = 0

def empate():
    print(f'A.I escolheu {resulai}\nCódigo escolheu {resulcodigo}')
    print('\033[94m' + 'Houve um empate\n' + '\033[0m')
    global empates
    empates += 1

def certo():
    print(f'A.I escolheu {resulai}\nCódigo escolheu {resulcodigo}')
    print('\033[32m' + 'Ponto para A.I\n' + '\033[0m')
    global pontuacaoai
    pontuacaoai += 1 

def errado():
    print(f'A.I escolheu {resulai}\nCódigo escolheu {resulcodigo}')
    print('\033[31m' + 'Ponto para Código\n' + '\033[0m')
    global questoeserradas
    questoeserradas += 1

while n < 3:

    n += 1

    resulcodigo = rd.choice(escolha)
    resulai = rd.choice(escolha)

    #Verificar se e igual
    if resulai == resulcodigo:
        empate()

    #Teste ao var resulai
    if resulai == "pedra":
        if resulcodigo == "tesoura":
            certo()
    if resulai == "tesoura":
        if resulcodigo == "papel":
            certo() 
    if resulai == "papel":
        if resulcodigo == "pedra":
            certo()

    #Teste ao var resulcodigo
    if resulcodigo == "pedra":
        if resulai == "tesoura":
            errado()
    if resulcodigo == "tesoura":
        if resulai == "papel":
            errado()
    if resulcodigo == "papel":
        if resulai == "pedra":
            errado()                                                          

print('\033[93m' + '\nPontuação Final' + '\033[0m')
if empates >= 1:  
    if pontuacaoai == 1:
        print('A A.I acertou ' + '\033[32m' + f'{pontuacaoai}' + '\033[0m' + ' vez')
    else:     
        print('A A.I acertou ' + '\033[32m' + f'{pontuacaoai}' + '\033[0m' + ' vezes')
    if questoeserradas == 1:
        print('Errou ' + '\033[31m' + f'{questoeserradas}' + '\033[0m' + ' vez')
    else:     
        print('Errou ' + '\033[31m' + f'{questoeserradas}' + '\033[0m' + ' vezes')  
    if empates == 1:
        print('E empatou ' + '\033[96m' + f'{empates}' + '\033[0m'+ ' vez')
    else:    
        print('E empatou ' + '\033[96m' + f'{empates}' + '\033[0m'+ ' vezes')
else:
    print('A A.I acertou ' + '\033[32m' + f'{pontuacaoai}' + '\033[0m' + ' vezes')
    print('Errou ' + '\033[31m' + f'{questoeserradas}' + '\033[0m' + ' vezes') 