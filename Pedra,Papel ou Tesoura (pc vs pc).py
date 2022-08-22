import random as rd

def acertou():
    print('Pc acertou \n')
def empataram():
    print('Ambos empataram \n')
def acertouai():
    print('A.I acertou \n')

jogos = ["pedra", "papel", "tesoura"]
n = 0
pontuacaopc = 0
pontuacaoai = 0

while n < 3:
    n += 1
    resultadoai = rd.choice(jogos)
    resultadopc = rd.choice(jogos)
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
            pontuacaoai += 1
    if resultadoai == "tesoura":
        if resultadopc == "papel":
            acertouai()
            pontuacaoai += 1
    if resultadoai == "papel":
        if resultadopc == "pedra":
            acertouai()
            pontuacaoai += 1

print(f'\033[42m' + '\033[1m' + '\033[33m' + '\nPontuação total' + '\033[0;0m')
print(f'PC: {pontuacaopc} pontos\nA.I: {pontuacaoai} pontos\n')
if pontuacaoai > pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'A.I' +'\033[0;0m')
elif pontuacaoai < pontuacaopc:
    print('Quem ganhou foi o ' + '\u001b[33m' + '\033[1m' + 'PC' + '\033[0;0m')