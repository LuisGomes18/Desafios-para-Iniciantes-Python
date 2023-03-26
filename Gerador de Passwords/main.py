import os
from os import mkdir
from shutil import rmtree
from string import ascii_letters
from string import digits
from random import sample
import qrcode
from shutil import move

diretorio = 'Fotos'

if not os.path.exists(diretorio):
    os.makedirs(diretorio)

simbolos = '!#$%&()*+,-./:;<=>?@[\]^_{|}~'
n = 0
quantcatr = 12
nome_ficheiro = ""
caminho_final = '/home/luis/Desktop/Projetos_Python/Desafios-para-Iniciantes-Python/Gerador de Passwords/Fotos/'
rmtree('/home/luis/Desktop/Projetos_Python/Desafios-para-Iniciantes-Python/Gerador de Passwords/Fotos')
mkdir('Fotos')

while n < 5:
    n += 1
    juncao = ascii_letters + digits + simbolos
    texto = ''.join(sample(juncao, quantcatr))
    fromato_imagem = "png"
    nome_ficheiro = "Password_" + str(n) + '.' + fromato_imagem
    caminho_ficheiro = f'/home/luis/Desktop/Projetos_Python/Desafios-para-Iniciantes-Python/Gerador de Passwords/{nome_ficheiro}'
    img = qrcode.make(texto)
    img.save(nome_ficheiro)
    move(caminho_ficheiro, caminho_final)

print('Obrigado por usar o codigo ')
