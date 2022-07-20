import random

def acertou():
    print('Pc acertou \n')
def empataram():
    print('Ambos empataram')
def acertouai():
    print('A.I acertou')      

jogos = ["pedra", "papel", "tesoura"]
n = 0
pontuacaopc = 0
pontuacaoai = 0
while n < 3:
    n += 1
    resultadoai = random.choice(jogos)
    resultadopc = random.choice(jogos)
    print(f'O iten sorteado foi {resultadoai}')
    print(f'O resultado sorteado pelo pc foi {resultadopc}')

    if resultadopc == resultadoai:
        empataram()
    if resultadopc == "pedra":
        if resultadoai == "tesoura":
            acertou()
            pontuacaopc += 1
    if resultadopc == "tesoura":
        if resultadoai == "papel":
            acertou()
            pontuacaopc += 1
    if resultadopc == "papel":
        if resultadoai == "pedra":
            acertou()
            pontuacaopc += 1

    if resultadoai == "pedra":
        if resultadopc == "tesoura":
            acertouai()
            pontuacaoai +=1
    if resultadoai == "tesoura":
        if resultadopc == "papel":
            acertouai()
            pontuacaoai +=1
    if resultadoai == "papel":
        if resultadopc == "pedra":
            acertouai()    
            pontuacaoai +=1            
