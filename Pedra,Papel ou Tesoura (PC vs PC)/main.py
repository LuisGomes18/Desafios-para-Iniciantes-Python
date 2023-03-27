from random import choices

acoes_permitidas = ['pedra', 'papel', 'tesoura']
ponto_AI_1 = 0
ponto_AI_2 = 0
n = 0

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
original = '\033[0;0m'
negrito = '\033[1m'

def ponto_ai_1():
    global ponto_AI_1
    print(amarelo + 'Ponto da AI 1\n'+ original)
    ponto_AI_1 += 1

def ponto_ai_2():
    global ponto_AI_2
    print(amarelo + 'Ponto da AI 2\n'+ original)
    ponto_AI_2 += 1

while n < 5:
    movimento_AI_1 = str(choices(acoes_permitidas))
    movimento_AI_2 = str(choices(acoes_permitidas))
    movimento_AI_1 = movimento_AI_1.replace("[", "").replace("]", "").replace("'", "")
    movimento_AI_2 = movimento_AI_2.replace("[", "").replace("]", "").replace("'", "")
    print(f'AI 1 escolheu {movimento_AI_1}\nAI 2 escolheu {movimento_AI_2}')
    if movimento_AI_1 == movimento_AI_2:
        print(amarelo + 'Empatou\n' + original)

    elif movimento_AI_1 == 'pedra' and movimento_AI_2 == 'tesoura':
        ponto_ai_1()
    elif movimento_AI_1 == 'tesoura' and movimento_AI_2 == 'papel':
        ponto_ai_1()
    elif movimento_AI_1 == 'papel' and movimento_AI_2 == 'pedra':
        ponto_ai_1()
    
    elif movimento_AI_2 == 'pedra' and movimento_AI_1 == 'tesoura':
        ponto_ai_2()
    elif movimento_AI_2 == 'tesoura' and movimento_AI_1 == 'papel':
        ponto_ai_2()
    elif movimento_AI_2 == 'papel' and movimento_AI_1 == 'pedra':
        ponto_ai_2()
    n += 1

print(negrito + amarelo + 'Pontuacao final' + original)
print(f'AI 1 fez {ponto_AI_1}\nAI 2 fez {ponto_AI_2}')