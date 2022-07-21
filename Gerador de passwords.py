import random

letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "@#$%&*/\?"
n = 0

while n < 5:
    n += 1
    juntar = letras_minusculas + letras_maiusculas + numeros + simbolos
    quantidade_de_caracteres = 10
    password = "".join(random.sample(juntar, quantidade_de_caracteres))
    print(f'Sua password nova é {password}')
    print("-" * 30)
