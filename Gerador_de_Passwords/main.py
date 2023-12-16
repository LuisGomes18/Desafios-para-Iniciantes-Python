from os import path
from os import makedirs
from string import ascii_letters
from string import digits
from random import sample
import qrcode


if not path.exists('Gerador_de_Passwords/passwords'):
    makedirs('Gerador_de_Passwords/passwords')

SIMBOLOS = '!#$%&()*+,-./:;<=>?@[\]^_{|}~'
QUANTCATR = 15
N = 0

while N < 5:
    N += 1
    JUNCAO = ascii_letters + digits + SIMBOLOS
    TEXTO = ''.join(sample(JUNCAO, QUANTCATR))

    NOME_FICHEIRO = "Password_" + str(N) + '.png'
    img = qrcode.make(TEXTO)
    img.save(f'Gerador_de_Passwords/passwords/{NOME_FICHEIRO}')
