import random
n = 0
pontuacao = 0
def errou():
    print('Numeros estão errados')  
    print('-------------------------------------')
def acertou():
    print('Mumero do pc estão certos')
    print('-------------------------------------')  

#* Gerador de numeros
while n < 5:
    n +=1
    numimp = int(random.uniform(0, 10))
    numpc = int(random.uniform(0, 10))

    #* Parte da "A.I"
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
        acertou()
        pontuacao += 1
    elif numimp != numpc:
        errou()

print(f'De {n} o pc conseguiu acertar {pontuacao} ')        