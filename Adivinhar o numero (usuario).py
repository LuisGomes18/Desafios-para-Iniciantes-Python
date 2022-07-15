import random
n = 0
def errou():
    print('Numeros estão errados')  
    print('-------------------------------------')
def acertou():
    print('Mumero do pc estão certos')
    print('-------------------------------------')
def num():    
    print(f'\nNumero escolhido foi {numusuario}')
    print(f'Numero gerado pelo pc foi {numpc} \n')

while n < 10:
    n +=1
    numusuario = int(input('Digite um numero entre 0 é 10: '))
    numpc = int(random.uniform(0, 10))
    num()
    if numusuario == numpc:
        acertou()
    elif numusuario != numpc:
        errou()